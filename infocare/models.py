from django.db import connections
from datetime import date, datetime, timedelta


def abrir_conexao():
    conexao = connections['default']
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
        if 'dt' in coluna.lower() and valores[i] is not None:
            data_obj = datetime.strptime(str(valores[i]), '%Y-%m-%d')
            valores[i] = data_obj.strftime('%d/%m/%Y')
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
    # cursor.execute("SELECT tabela FROM formulario ")
    cursor.execute("SELECT tabela FROM formulario WHERE codigo = 1")
    tabelas = cursor.fetchall()

    for tabela in tabelas:
        cursor.execute(f"SELECT COUNT(codigo) FROM {tabela[0]}")
        quant_registros_tabela = cursor.fetchone()[0]

        if quant_registros_tabela == 0:
            continue

        cursor.execute(f"SELECT MAX(codigo) FROM {tabela[0]}")
        maior_codigo_tabela = cursor.fetchone()[0]

        print('maior codigo da tabela', tabela[0], '=', maior_codigo_tabela)

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
    Retorna a tabela do formulário de acordo com o código de formulário.

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


def registrar_ficha_preliminar(cursor, cod_ficha, cod_formulario):
    nome_tabela = 'preliminar'
    colunas = get_colunas_tabela(nome_tabela)[1:]
    cursor.execute(f"""
        INSERT INTO {nome_tabela} (
            {get_placeholders(colunas, True)}
        ) VALUES (
            {get_placeholders(colunas, False)}
        )
    """,  (cod_ficha, cod_formulario))


def registrar_ficha_notificacao(campos: dict, tabela: str = ""):
    cod_ficha = proximo_codigo_ficha()
    conexao, cursor = abrir_conexao()

    print('codigo da ficha', cod_ficha)

    if not tabela:
        registrar_ficha_preliminar(cursor, cod_ficha, campos['cod_formulario'])

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





































