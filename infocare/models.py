from django.db import connections
from datetime import date, datetime, timedelta

import sqlite3


def abrir_conexao():
    conexao = connections['default']
    # conexao = sqlite3.connect('..\db.sqlite3')
    cursor = conexao.cursor()
    return conexao, cursor


def fechar_conexao(conexao, commit: bool = True):
    if commit:
        conexao.commit()
    conexao.close()


def criar_dicionario(colunas: list, valores: list) -> dict:
    """
    # Cria um dicionário com as chaves iguais aos nomes das colunas e os valores iguais aos valores das colunas.

    # :param colunas: Lista de strings com os nomes das colunas
    # :param valores: Lista de valores correspondentes às colunas
    # :return: Dicionário com as chaves iguais aos nomes das colunas e os valores iguais aos valores das colunas

    # Exemplo de uso:
    # colunas = ['nome', 'idade', 'cidade']
    # valores = ['João', 30, 'São Paulo']
    # dicionario = criar_dicionario(colunas, valores)
    # print(dicionario)
    # {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}

    # Verifica se o valor da coluna é um objeto datetime.
    """

    dados = dict()
    for i, coluna in enumerate(colunas):
        if 'dt' in coluna.lower() and valores[i]:
            data_obj = datetime.strptime(str(valores[i]), '%Y-%m-%d')
            valores[i] = data_obj.strftime('%d/%m/%Y')
        elif 'dataHora' in coluna.lower() and valores[i]:
            data_hora = datetime.strptime(str(valores[i]), '%Y-%m-%d %H:%M:%S')
            valores[i] = data_hora.strftime('%d/%m/%Y %H:%M')
        dados[coluna] = valores[i]
    return dados


def get_colunas_tabela(nome_tabela: str, indentificacao: bool = False) -> list:
    """
    Retorna uma lista com os nomes das colunas de uma tabela.

    :param nome_tabela: Nome da tabela.
    :param indentificacao: Se True, adiciona uma identificação ao nome da coluna.
    :return: Lista com os nomes das colunas.
    """

    conexao, cursor = abrir_conexao()
    cursor.execute(f"PRAGMA table_info({nome_tabela});")
    resultados = cursor.fetchall()
    fechar_conexao(conexao)

    if indentificacao:
        return [f'{resultado[1]}_{nome_tabela}' for resultado in resultados]
    else:
        return [resultado[1] for resultado in resultados]


def get_placeholders(colunas: list, usa_colunas: bool) -> str:
    if usa_colunas:
        return ', '.join(colunas)
    return ', '.join(['?' for _ in range(len(colunas))])


def preparar_query(nome_tabela: str, lista_filtros: list) -> str:
    clausura_where = ''
    for filtro in lista_filtros:
        if filtro:
            if clausura_where:
                clausura_where += " AND "
            clausura_where += filtro

    query = f"SELECT * FROM {nome_tabela}"
    query += f" WHERE {clausura_where}" if clausura_where else ""

    return query


def inserir_registro_tabela(nome_tabela: str, dados: dict):
    colunas = get_colunas_tabela(nome_tabela)
    conexao, cursor = abrir_conexao()
    valores = tuple(dados.values())
    query = f"""INSERT INTO {nome_tabela} (
                    {get_placeholders(colunas[1:], True)}
                ) VALUES (
                    {get_placeholders(colunas[1:], False)}
                )
            """

    try:
        cursor.execute(query, valores)
    except Exception as e:
        print(e)

    fechar_conexao(conexao)


def alterar_registro_tabela(nome_tabela: str, dados: dict):
    colunas = get_colunas_tabela(nome_tabela)
    conexao, cursor = abrir_conexao()
    valores = tuple(dados.values())[1:]

    lista = list()
    for i, coluna in enumerate(colunas[1:]):
        lista.append(f"{coluna} = ?")

    query = f"""
            UPDATE {nome_tabela}
            SET 
                {get_placeholders(lista, True)}
            WHERE codigo = {dados['codigo']};
        """

    try:
        cursor.execute(query, valores)
    except Exception as e:
        print(e)

    fechar_conexao(conexao)


def apagar_registro_tabela(nome_tabela: str, codigo: int):
    """
    Apaga um registro da tabela.

    :param nome_tabela: Nome da tabela.
    :param codigo: Código do registro a ser apagado.
    :return: None.

    :Example:

    >>> apagar_registro_tabela('ficha', 1)
    None

    :Note:

    - O código do registro a ser apagado deve ser um inteiro.
    - O código do registro deve existir na tabela.
    - Não é possível apagar um registro que tenha sido utilizado em uma ficha.
    """
    conexao, cursor = abrir_conexao()
    query = f"DELETE FROM {nome_tabela} WHERE codigo = {codigo}"
    cursor.execute(query)
    fechar_conexao(conexao)


def get_maior_codigo_ficha_registrado():
    """
    Retorna o maior código de ficha registrado no banco de dados.

    :return: int - Maior código de ficha registrado.
    :rtype: int

    :Example:

    >>> get_maior_codigo_ficha_registrado()
    1
    """

    maior_codigo_geral = 0
    conexao, cursor = abrir_conexao()
    # cursor.execute("SELECT tabela FROM formulario")
    cursor.execute("SELECT tabela FROM formulario WHERE codigo = 1")
    tabelas = cursor.fetchall()

    for tabela in tabelas:
        cursor.execute(f"SELECT COUNT(codigo) FROM {tabela[0]}")
        quant_registros_tabela = cursor.fetchone()[0]

        if quant_registros_tabela == 0:
            continue

        cursor.execute(f"SELECT MAX(codigo) FROM {tabela[0]}")
        maior_codigo_tabela = cursor.fetchone()[0]

        if maior_codigo_tabela > maior_codigo_geral:
            maior_codigo_geral = maior_codigo_tabela

    fechar_conexao(conexao, False)
    return maior_codigo_geral


def proximo_codigo_ficha():
    """
    Retorna o próximo código de ficha a ser registrado.

    :return: int - Próximo código de ficha a ser registrado.
    :rtype: int

    :Example:

    >>> proximo_codigo_ficha()
    2
    """

    global MAIOR_CODIGO_FICHA_REGISTRADA
    MAIOR_CODIGO_FICHA_REGISTRADA += 1

    return MAIOR_CODIGO_FICHA_REGISTRADA


MAIOR_CODIGO_FICHA_REGISTRADA = get_maior_codigo_ficha_registrado()


def get_formularios_ativos():
    """
    Retorna uma lista com os códigos e nomes de todos os formulario ativos.

    :return: list - Lista com os códigos e nomes de todos os formulario ativos.
    :rtype: list

    :Example:

    >>> get_formularios_ativos()
    [{'codigo': 1, 'nome': 'Ficha Notificação'}, {'codigo': 2, 'nome': 'Ficha Acidente de Trabalho Grave'},
    {'codigo': 3, 'nome': 'Ficha Violência Interpessoal/Autoprovocada'}]
    """

    nome_tabela = 'formulario'
    conexao, cursor = abrir_conexao()
    cursor.execute(f"SELECT codigo, nome FROM {nome_tabela} WHERE ativo = 1")
    resultado = cursor.fetchall()
    colunas = get_colunas_tabela(nome_tabela)[:2]
    formularios = list()

    for res in resultado:
        formularios.append(criar_dicionario(colunas, list(res)))

    fechar_conexao(conexao, False)
    return formularios


def get_tabela_formulario(cod_formulario: int) -> str:
    """
    Retorna a tabela do formulário de acordo com o código do formulário.

    :param cod_formulario: int - Código do formulário.
    :type cod_formulario: int

    :return: str - Nome da tabela.
    :rtype: str

    :Example:

    >>> get_tabela_formulario(1)
    'ficha_1'
    """

    conexao, cursor = abrir_conexao()
    cursor.execute(f"SELECT tabela FROM formulario WHERE codigo = {cod_formulario}")
    tabela = cursor.fetchone()[0]
    fechar_conexao(conexao, False)
    return tabela


def alterar_estado_ficha(cod_ficha: int, status: str):
    nome_tabela = 'estado'
    conexao, cursor = abrir_conexao()
    cursor.execute(f"""
        UPDATE {nome_tabela}
        SET status = '{status}'
        WHERE cod_ficha = {cod_ficha}
    """)


def set_ficha_notificacao(campos: dict, tabela: str = ""):
    cod_ficha = proximo_codigo_ficha()
    conexao, cursor = abrir_conexao()

    print('codigo da ficha', cod_ficha)

    estado_ficha = {
        'cod_ficha': cod_ficha,
        'tabela': get_tabela_formulario(campos['cod_formulario']),
        'status': 'preliminar'
    }

    inserir_registro_tabela('estado', estado_ficha)

    tabela_ficha_notificacao = get_tabela_formulario(1)
    nome_tabela = tabela_ficha_notificacao if tabela == "" else tabela

    print(nome_tabela)

    colunas = get_colunas_tabela(nome_tabela)
    query = f"""
        INSERT INTO {nome_tabela} (
            {get_placeholders(colunas, True)}
        ) VALUES (
            {get_placeholders(colunas, False)}
        )
    """

    try:
        cursor = conexao.cursor()
        valores = (cod_ficha,) + tuple(campos.values())
        cursor.execute(query, valores)
    except Exception as e:
        print(e)

    fechar_conexao(conexao)


def get_ficha(cod_ficha: int, cod_formulario: int):
    tabela = get_tabela_formulario(cod_formulario)
    conexao, cursor = abrir_conexao()
    cursor.execute(f"SELECT * FROM {tabela} WHERE codigo = {cod_ficha}")
    resultado = cursor.fetchone()
    colunas = get_colunas_tabela(tabela)
    ficha = criar_dicionario(colunas, list(resultado))
    fechar_conexao(conexao, False)
    return ficha


def alterar_ficha(campos: dict):
    tabela = get_tabela_formulario(campos['cod_formulario'])
    alterar_registro_tabela(tabela, campos)


def get_quantidade_fichas(status: str):
    conexao, cursor = abrir_conexao()
    cursor.execute(f"SELECT COUNT(*) FROM estado WHERE status = '{status}'")
    quant_fichas = cursor.fetchone()[0]
    fechar_conexao(conexao, False)
    return quant_fichas


def listar_fichas(status: str, numero_ficha: int = 0, setor: str = ''):
    conexao, cursor = abrir_conexao()
    cursor.execute(f"SELECT cod_ficha, tabela FROM estado WHERE status = '{status}'")
    resultados = cursor.fetchall()

    colunas = [
        'cod_ficha',
        'numero_ficha',
        'nome_paciente',
        'nome_formulario',
        'cod_formulario',
        'setor',
        'nome_notificante',
        'dt_notificacao',
        'quant_obs'
    ]

    dados = list()
    for resultado in resultados:
        cod_ficha = int(resultado[0])
        tabela = resultado[1]
        query = f"""
            SELECT
                {tabela}.codigo,
                numero_ficha,
                nome_paciente,
                formulario.nome,
                formulario.codigo,
                setor,
                nome_notificante,
                dt_notificacao,
                COUNT(observacao.codigo)
            FROM {tabela}
                INNER JOIN formulario ON formulario.codigo = {tabela}.cod_formulario
                LEFT JOIN observacao ON observacao.cod_ficha = {cod_ficha}
            WHERE {tabela}.codigo = {cod_ficha}
            ORDER BY setor
        """

        cursor.execute(query)
        valores = list(cursor.fetchone())
        # quant_observacoes = cursor.execute(f"SELECT COUNT(*) FROM observacao WHERE cod_ficha = {cod_ficha}")
        # valores.append(int(quant_observacoes.fetchone()[0]))
        dados.append(criar_dicionario(colunas, valores))

    fechar_conexao(conexao, False)
    return dados


def listar_observacoes(cod_ficha: int):
    nome_tabela = 'observacao'
    conexao, cursor = abrir_conexao()
    cursor.execute(f"""
        SELECT
            {nome_tabela}.codigo,
            {nome_tabela}.descricao,
            {nome_tabela}.concluida,
            {nome_tabela}.cod_ficha,
            {nome_tabela}.cod_usuario_autor,
            {nome_tabela}.cod_usuario_concluinte,
            {nome_tabela}.dataHora_cadastro,
            {nome_tabela}.dataHora_concluida,
            AUTOR.codigo,
            AUTOR.nome,
            CONCLUINTE.codigo,
            CONCLUINTE.nome
        FROM observacao
            INNER JOIN usuario AS AUTOR
                ON cod_usuario_autor = AUTOR.codigo
            INNER JOIN usuario AS CONCLUINTE
                ON cod_usuario_concluinte == CONCLUINTE.codigo
        WHERE cod_ficha = {cod_ficha}
    """)

    resultados = cursor.fetchall()
    fechar_conexao(conexao, False)
    colunas = get_colunas_tabela(nome_tabela) + ['cod_autor', 'nome_autor', 'cod_concluinte', 'nome_concluinte']
    observacoes = [criar_dicionario(colunas, list(resultado)) for resultado in resultados] if resultados else []

    for observacao in observacoes:
        observacao['nome_concluinte'] = observacao['nome_concluinte'].split(' ')[0]
        observacao['nome_autor'] = observacao['nome_autor'].split(' ')[0]
        observacao['inicial_autor'] = observacao['nome_autor'][0].upper()

    return observacoes


def set_observacao(dados: dict):
    inserir_registro_tabela('observacao', dados)
    alterar_estado_ficha(dados['cod_ficha'], 'pendente')


def alterar_observacao(dados: dict):
    alterar_registro_tabela('observacao', dados)


def deletar_observacao(cod_observacao: int):
    apagar_registro_tabela('observacao', cod_observacao)


def get_quantidade_observacoes(cod_ficha: int):
    conexao, cursor = abrir_conexao()
    cursor.execute(f"""
        SELECT COUNT(codigo)
        FROM observacao
        WHERE cod_ficha = {cod_ficha}
            AND concluida = 0
    """)
    quant_obs = cursor.fetchone()[0]
    fechar_conexao(conexao, False)
    return quant_obs


def fechar_observacao(dados: dict):
    try:
        conexao, cursor = abrir_conexao()
        cursor.execute(f"""
            UPDATE
                observacao
            SET concluida = 1,
                dataHora_concluida = '{dados['dataHora_concluida']}',
                cod_usuario_concluinte = '{dados['cod_usuario_concluinte']}'
            WHERE 
                codigo = {dados['cod_observacao']}
        """)
        fechar_conexao(conexao)
    except Exception as e:
        print(e)


def set_ficha_concluida(cod_ficha: int):
    alterar_estado_ficha(cod_ficha, 'concluida')


def set_ficha_preliminar(cod_ficha: int):
    alterar_estado_ficha(cod_ficha, 'preliminar')

















