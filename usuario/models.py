from django.db import connections
from datetime import date, datetime, timedelta
import sqlite3


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
            valores[i] = str(valores[i])
        dados[coluna] = valores[i]

    return dados


def get_colunas_tabela(cursor, nome_tabela: str, indentificacao: bool = False) -> list:
    """
    Retorna uma lista com os nomes das colunas de uma tabela.

    :param cursor: Cursor do banco de dados.
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


def alterar_registro_tabela(nome_tabela: str, dicionario: dict):
    conexao, cursor = abrir_conexao()
    colunas = get_colunas_tabela(cursor, nome_tabela)
    placeholders = [f"{coluna} = %s" for coluna in colunas][1:]
    dados = dicionario.copy()
    codigo = dados.pop('codigo')

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


def listar_acessos():
    nome_tabela = 'acesso'
    conexao, cursor = abrir_conexao()
    colunas = get_colunas_tabela(cursor, nome_tabela)
    cursor.execute("SELECT * FROM acesso")
    resultados = cursor.fetchall()
    fechar_conexao(conexao)

    return [criar_dicionario(colunas, list(res)) for res in resultados]


def listar_usuarios():
    nome_tabela = 'usuario'
    conexao, cursor = abrir_conexao()
    colunas = get_colunas_tabela(cursor, nome_tabela)
    cursor.execute(f"SELECT * FROM {nome_tabela}")
    resultados = cursor.fetchall()
    fechar_conexao(conexao)

    return [criar_dicionario(colunas, list(res)) for res in resultados]


def set_usuario(dados: dict):
    return inserir_registro_tabela('usuario', dados)


def atualizar_usuario(dados: dict):
    alterar_registro_tabela('usuario', dados)


def get_usuario(codigo: int):
    nome_tabela = 'usuario'
    conexao, cursor = abrir_conexao()
    colunas = get_colunas_tabela(cursor, nome_tabela)
    cursor.execute(f"SELECT * FROM {nome_tabela} WHERE codigo = %s", (codigo,))
    resultado = cursor.fetchone()
    fechar_conexao(conexao)

    return criar_dicionario(colunas, list(resultado)) if resultado else {}


def apagar_usuario(codigo: int):
    conexao, cursor = abrir_conexao()
    cursor.execute("DELETE FROM usuario WHERE codigo = %s", (codigo,))
    fechar_conexao(conexao)





