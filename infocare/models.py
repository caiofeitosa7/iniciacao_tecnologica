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
        if 'dt' in coluna.lower() and valores[i]:
            data_obj = datetime.strptime(str(valores[i]), '%Y-%m-%d')
            valores[i] = data_obj.strftime('%d/%m/%Y')
        elif 'dataHora' in coluna.lower() and valores[i]:
            data_hora = datetime.strptime(str(valores[i]), '%Y-%m-%d %H:%M:%S')
            valores[i] = data_hora.strftime('%d/%m/%Y %H:%M')
        dados[coluna] = valores[i]
    return dados


# def formatar_datas_dicionario(dados: dict) -> dict:
#     """
#     Formata as datas do dicionário para o formato dd/mm/aaaa.
#     """
#     for key in dados:
#         if 'dt' in key.lower() and dados[key]:
#             data_obj = datetime.strptime(str(dados[key]), '%Y-%m-%d')
#             dados[key] = data_obj.strftime('%d/%m/%Y')
#         elif 'dataHora' in key.lower() and dados[key]:
#             data_hora = datetime.strptime(str(dados[key]), '%Y-%m-%d %H:%M:%S')
#             dados[key] = data_hora.strftime('%d/%m/%Y %H:%M')
#
#     return dados


def get_colunas_tabela(cursor, nome_tabela: str, indentificacao: bool = False) -> list:
    """
    Retorna uma lista com os nomes das colunas de uma tabela.

    :param cursor: Cursor da conexão com o banco de dados.
    :param nome_tabela: Nome da tabela.
    :param indentificacao: Se True, adiciona o nome da tabela ao final do nome da coluna. Exemplo: coluna_tabela.
    :return: Lista com os nomes das colunas.
    """

    cursor.execute(f"SHOW COLUMNS FROM {nome_tabela};")
    resultados = cursor.fetchall()

    if indentificacao:
        return [f'{resultado[0]}_{nome_tabela}' for resultado in resultados]
    else:
        return [resultado[0] for resultado in resultados]


def get_placeholders(colunas: list, usa_colunas: bool) -> str:
    if usa_colunas:
        return ', '.join(colunas)
    return ', '.join(['%s'] * len(colunas))


# def preparar_query(nome_tabela: str, lista_filtros: list) -> str:
#     clausura_where = ''
#     for filtro in lista_filtros:
#         if filtro:
#             if clausura_where:
#                 clausura_where += " AND "
#             clausura_where += filtro
#
#     query = f"SELECT * FROM {nome_tabela}"
#     query += f" WHERE {clausura_where}" if clausura_where else ""
#
#     return query


def inserir_registro_tabela(nome_tabela: str, dados: dict):
    conexao, cursor = abrir_conexao()
    colunas = get_colunas_tabela(cursor, nome_tabela)
    valores = tuple(dados.values())
    query = f"""
        INSERT INTO {nome_tabela} (
            {get_placeholders(colunas[1:], True)}
        ) VALUES (
            {get_placeholders(colunas[1:], False)}
        )
    """

    try:
        cursor.execute(query, valores)
        conexao.commit()
        cod_registro = cursor.lastrowid
        return cod_registro
    except Exception as e:
        conexao.rollback()
        print(e)
    finally:
        fechar_conexao(conexao)


def alterar_registro_tabela(nome_tabela: str, dados: dict):
    conexao, cursor = abrir_conexao()
    colunas = get_colunas_tabela(cursor, nome_tabela)
    codigo = dados.pop('codigo')
    placeholders = [f"{coluna} = %s" for coluna in colunas if coluna in dados]

    query = f"""
        UPDATE {nome_tabela}
        SET {', '.join(placeholders)}
        WHERE codigo = %s;
    """

    valores = list(dados.values())
    valores.append(codigo)

    try:
        cursor.execute(query, valores)
        conexao.commit()
    except Exception as e:
        conexao.rollback()
        print(e)
    finally:
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
    query = f"DELETE FROM {nome_tabela} WHERE codigo = %s"
    cursor.execute(query,  (codigo,))
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


def get_tipos_ficha_ativos():
    """
    Retorna uma lista com os códigos e nomes de todos os tipos de fichas ativos.

    :return: list - Lista com os códigos e nomes de todos os tipos de fichas ativos.
    :rtype: list

    :Example:

    >>> get_tipos_ficha_ativos()
    [{'codigo': 1, 'nome': 'Ficha de Notificação'}, {'codigo': 2, 'nome': 'Ficha Acidente de Trabalho Grave'},
    {'codigo': 3, 'nome': 'Ficha Violência Interpessoal/Autoprovocada'}]
    """

    nome_tabela = 'tipo_ficha'
    conexao, cursor = abrir_conexao()
    cursor.execute(f"""
        SELECT codigo, nome
        FROM {nome_tabela}
        WHERE ativo = 1
        ORDER BY nome
    """)
    resultado = cursor.fetchall()
    colunas = get_colunas_tabela(cursor, nome_tabela)[:2]

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
    cursor.execute("SELECT tabela FROM formulario WHERE codigo = %s",  (cod_formulario, ))
    tabela = cursor.fetchone()[0]
    fechar_conexao(conexao, False)
    return tabela


def get_html_tipo_ficha(codigo: int):
    """
    Retorna o template HTML do tipo de ficha de acordo com o código do tipo de ficha.

    :param codigo: int - Código do tipo de ficha.
    :type codigo: int

    :return: str - HTML do tipo de ficha.
    :rtype: str

    :Example:

    >>> get_html_tipo_ficha(1)
    'fichaNotificacaoGeral.html'
    """

    conexao, cursor = abrir_conexao()
    cursor.execute(f"SELECT arquivoHTML FROM tipo_ficha WHERE codigo = %s",  (codigo,))
    html = cursor.fetchone()[0]
    fechar_conexao(conexao, False)
    return html


def alterar_estado_ficha(codigo: int, status: int):
    conexao, cursor = abrir_conexao()
    cursor.execute(f"""
        UPDATE ficha
        SET cod_estado = %s
        WHERE codigo = %s
    """, (status, codigo))

    fechar_conexao(conexao)


def set_ficha_notificacao(campos: dict, tabela: str = ""):
    cod_ficha = proximo_codigo_ficha()
    conexao, cursor = abrir_conexao()

    print('codigo da ficha: ', cod_ficha)

    estado_ficha = {
        'cod_ficha': cod_ficha,
        'tabela': get_tabela_formulario(campos['cod_formulario']),
        'status': 'preliminar'
    }

    inserir_registro_tabela('estado', estado_ficha)

    tabela_ficha_notificacao = get_tabela_formulario(1)
    nome_tabela = tabela_ficha_notificacao if tabela == "" else tabela

    colunas = get_colunas_tabela(cursor, nome_tabela)
    query = f"""
        INSERT INTO {nome_tabela} (
            {get_placeholders(colunas, True)}
        ) VALUES (
            {get_placeholders(colunas, False)}
        )
    """

    conexao, cursor = abrir_conexao()
    try:
        valores = (cod_ficha,) + tuple(campos.values())
        cursor.execute(query, valores)
        conexao.commit()
    except Exception as e:
        conexao.rollback()
        print(e)
    finally:
        fechar_conexao(conexao)

    print('é pra ter salvo a ficha')

    return cod_ficha


def get_ficha(cod_ficha: int):
    conexao, cursor = abrir_conexao()
    query = f"""
        SELECT F.codigo     AS COD_FICHA,
               F.prontuario AS PRONTUARIO,
               TF.nome      AS TIPO_FICHA,
               TF.codigo    AS COD_TIPO_FICHA,
               F.setor      AS SETOR,
               C.nome       AS CAMPO,
               MAX(CASE
                       WHEN (C.cod_tipo_campo = 1) THEN VC.valor_string
                       WHEN (C.cod_tipo_campo = 2) THEN VC.valor_numerico
                       WHEN (C.cod_tipo_campo = 3) THEN VC.valor_data
                   END)     AS VALOR_CAMPO,
               OBS.quant    AS QUANT_OBS
        FROM ficha AS F
                 INNER JOIN campo_tipo_ficha AS CTF
                            ON CTF.cod_tipo_ficha = F.cod_tipo_ficha
                 LEFT JOIN valorcampo AS VC
                           ON VC.cod_ficha = F.codigo
                 INNER JOIN tipo_ficha AS TF
                            ON TF.codigo = F.cod_tipo_ficha
                 INNER JOIN campo AS C
                            ON C.codigo = VC.cod_campo
                 LEFT JOIN (SELECT cod_ficha,
                                   COUNT(codigo) AS quant
                            FROM observacao
                            GROUP BY cod_ficha) AS OBS ON OBS.cod_ficha = F.codigo
        WHERE
            F.codigo = %s
        GROUP BY F.codigo,
                 F.prontuario,
                 TF.nome,
                 TF.codigo,
                 F.setor,
                 C.nome,
                 OBS.quant
        ORDER BY F.setor;
    """

    cursor.execute(query, (cod_ficha,))
    resultados = cursor.fetchall()
    fechar_conexao(conexao, False)

    fichas = []
    for resultado in resultados:
        ficha_id = resultado[0]
        ficha_existente = next((ficha for ficha in fichas if ficha.get('codigo', None) == ficha_id), None)

        if ficha_existente:
            nome_campo = resultado[5]
            valor_campo = resultado[6]
            ficha_existente[nome_campo] = valor_campo
        else:
            ficha = {
                'codigo': ficha_id,
                'prontuario': resultado[1],
                'nome_tipo_ficha': resultado[2],
                'cod_tipo_ficha': resultado[3],
                'setor': resultado[4],
                'quant_obs': resultado[7],
                resultado[5]: resultado[6]
            }

            fichas.append(ficha)

    print(fichas)

    return fichas[0]


def alterar_ficha(campos: dict):
    tabela = get_tabela_formulario(campos['cod_formulario'])
    alterar_registro_tabela(tabela, campos)


def get_quantidade_fichas(status: int):
    conexao, cursor = abrir_conexao()
    cursor.execute(f"SELECT COUNT(*) FROM ficha WHERE cod_estado = %s", (status,))
    quant_fichas = cursor.fetchone()[0]
    fechar_conexao(conexao, False)
    return quant_fichas


def listar_fichas(status: int, numero_ficha: int = 0, setor: str = ''):
    conexao, cursor = abrir_conexao()
    query = f"""
        SELECT F.codigo     AS COD_FICHA,
               F.prontuario AS PRONTUARIO,
               TF.nome      AS TIPO_FICHA,
               TF.codigo    AS COD_TIPO_FICHA,
               F.setor      AS SETOR,
               C.nome       AS CAMPO,
               MAX(CASE
                       WHEN (C.cod_tipo_campo = 1) THEN VC.valor_string
                       WHEN (C.cod_tipo_campo = 2) THEN VC.valor_numerico
                       WHEN (C.cod_tipo_campo = 3) THEN DATE_FORMAT(VC.valor_data, '%d/%m/%Y')
                   END)     AS VALOR_CAMPO,
               OBS.quant    AS QUANT_OBS
        FROM ficha AS F
                 INNER JOIN campo_tipo_ficha AS CTF
                            ON CTF.cod_tipo_ficha = F.cod_tipo_ficha
                 LEFT JOIN valorcampo AS VC
                           ON VC.cod_ficha = F.codigo
                 INNER JOIN tipo_ficha AS TF
                            ON TF.codigo = F.cod_tipo_ficha
                 INNER JOIN campo AS C
                            ON C.codigo = VC.cod_campo
                 LEFT JOIN (SELECT cod_ficha,
                                   COUNT(codigo) AS quant
                            FROM observacao
                            GROUP BY cod_ficha) AS OBS ON OBS.cod_ficha = F.codigo
        WHERE
            F.cod_estado = {status}
        GROUP BY F.codigo,
                 F.prontuario,
                 TF.nome,
                 TF.codigo,
                 F.setor,
                 C.nome,
                 OBS.quant
        ORDER BY F.setor;
    """

    cursor.execute(query)
    resultados = cursor.fetchall()
    fechar_conexao(conexao, False)

    fichas = []
    for resultado in resultados:
        ficha_id = resultado[0]
        ficha_existente = next((ficha for ficha in fichas if ficha.get('cod_ficha', None) == ficha_id), None)

        if ficha_existente:
            nome_campo = resultado[5]
            valor_campo = resultado[6]
            ficha_existente[nome_campo] = valor_campo
        else:
            ficha = {
                'cod_ficha': ficha_id,
                'prontuario': resultado[1],
                'nome_tipo_ficha': resultado[2],
                'cod_tipo_ficha': resultado[3],
                'setor': resultado[4],
                'quant_obs': resultado[7],
                resultado[5]: resultado[6]
            }

            fichas.append(ficha)

    return fichas


def listar_observacoes(cod_ficha: int):
    nome_tabela = 'observacao'
    conexao, cursor = abrir_conexao()
    cursor.execute(f"""
        SELECT
            OBS.codigo,
            OBS.descricao,
            OBS.concluida,
            OBS.cod_ficha,
            OBS.cod_usuario_autor,
            OBS.cod_usuario_concluinte,
            OBS.dataHora_cadastro,
            OBS.dataHora_concluida,
            AUTOR.codigo,
            AUTOR.nome,
            CONCLUINTE.codigo,
            CONCLUINTE.nome
        FROM {nome_tabela} AS OBS
            INNER JOIN usuario AS AUTOR
                ON cod_usuario_autor = AUTOR.codigo
            INNER JOIN usuario AS CONCLUINTE
                ON cod_usuario_concluinte = CONCLUINTE.codigo
        WHERE cod_ficha = %s
    """,  (cod_ficha,))

    resultados = cursor.fetchall()
    colunas = get_colunas_tabela(cursor, nome_tabela) + ['cod_autor', 'nome_autor', 'cod_concluinte', 'nome_concluinte']
    observacoes = [criar_dicionario(colunas, list(resultado)) for resultado in resultados] if resultados else []

    for observacao in observacoes:
        observacao['nome_concluinte'] = observacao['nome_concluinte'].split(' ')[0]
        observacao['nome_autor'] = observacao['nome_autor'].split(' ')[0]
        observacao['inicial_autor'] = observacao['nome_autor'][0].upper()

    fechar_conexao(conexao, False)
    return observacoes


def set_observacao(dados: dict):
    inserir_registro_tabela('observacao', dados)
    alterar_estado_ficha(dados['cod_ficha'], 4)


def alterar_observacao(dados: dict):
    alterar_registro_tabela('observacao', dados)


def deletar_observacao(cod_observacao: int):
    apagar_registro_tabela('observacao', cod_observacao)


def get_quant_obs_abertas(cod_ficha: int):
    conexao, cursor = abrir_conexao()
    cursor.execute(f"""
        SELECT COUNT(codigo)
        FROM observacao
        WHERE cod_ficha = %s
            AND concluida <> 1
    """,  (cod_ficha, ))
    quant_obs = cursor.fetchone()[0]
    fechar_conexao(conexao, False)

    return quant_obs


def fechar_observacao(dados: dict):
    valores = (
        dados['dataHora_concluida'],
        dados['cod_usuario_concluinte'],
        dados['cod_observacao']
    )

    try:
        conexao, cursor = abrir_conexao()
        cursor.execute(f"""
            UPDATE
                observacao
            SET concluida = 1,
                dataHora_concluida = %s,
                cod_usuario_concluinte = %s
            WHERE 
                codigo = %s
        """, valores)
        fechar_conexao(conexao)
    except Exception as e:
        print(e)


def set_ficha_concluida(cod_ficha: int):
    alterar_estado_ficha(cod_ficha, 2)


def set_ficha_preliminar(cod_ficha: int):
    alterar_estado_ficha(cod_ficha, 1)


def set_ficha_descartada(cod_ficha: int):
    alterar_registro_tabela(cod_ficha, 3)

















