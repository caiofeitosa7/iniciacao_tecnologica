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


def listar_usuarios():
    nome_tabela = 'usuario'
    colunas = get_colunas_tabela(nome_tabela)
    conexao, cursor = abrir_conexao()
    cursor.execute(f"SELECT * FROM {nome_tabela}")
    resultados = cursor.fetchall()
    fechar_conexao(conexao)
    return [criar_dicionario(colunas, list(res)) for res in resultados]


def set_usuario(dados: dict):
    nome_tabela = 'usuario'
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


def get_usuario(codigo: int):
    nome_tabela = 'usuario'
    colunas = get_colunas_tabela(nome_tabela)
    conexao, cursor = abrir_conexao()
    cursor.execute(f"SELECT * FROM {nome_tabela} WHERE codigo = ?", (codigo,))
    resultado = cursor.fetchone()
    fechar_conexao(conexao)
    return criar_dicionario(colunas, list(resultado)) if resultado else {}


def alterar_usuario(dados: dict):
    alterar_registro_tabela('usuario', dados)


def apagar_usuario(codigo: int):
    nome_tabela = 'usuario'
    conexao, cursor = abrir_conexao()
    cursor.execute(f"DELETE FROM {nome_tabela} WHERE codigo = ?", (codigo,))
    fechar_conexao(conexao)





