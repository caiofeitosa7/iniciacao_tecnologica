from django.db import models
from django.db import connections
from datetime import date, datetime, timedelta


def abrir_conexao_banco():
    return connections['default']


def fechar_conexao_banco(conexao, commit: bool = True):
    if commit:
        conexao.commit()
    conexao.close()


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

    conexao = abrir_conexao_banco()
    cursor = conexao.cursor()
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

        print(maior_codigo_tabela)

        if maior_codigo_tabela[0] > maior_codigo_geral:
            maior_codigo_geral = maior_codigo_tabela[0]

    fechar_conexao_banco(conexao, False)
    return maior_codigo_geral


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

    conexao = abrir_conexao_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT codigo, nome FROM formulario WHERE ativo = 1")
    dados = cursor.fetchall()
    fechar_conexao_banco(conexao, False)

    formularios = list()
    for dado in dados:
        formularios.append({
            'codigo': dado[0],
            'nome': dado[1]
        })

    return formularios


def get_tabela_formulario(cod_formulario):
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
    conexao = abrir_conexao_banco()
    cursor = conexao.cursor()
    cursor.execute(f"SELECT tabela FROM formulario WHERE codigo = {cod_formulario}")
    tabela = cursor.fetchone()[0]
    fechar_conexao_banco(conexao, False)

    return tabela


# def registrar_ficha_notificacao(campos: dict, tabela: str = ""):
#     conexao = abrir_conexao_banco()
#     cursor = conexao.cursor()
#
#     tabela_ficha_notificacao = get_tabela_formulario(1)
#     quant_campos_ficha_notificacao = cursor.execute(f"SELECT count(*) FROM pragma_table_info('{tabela_ficha_notificacao}')")
#     placeholders = ', '.join(['?' for _ in range(quant_campos_ficha_notificacao)])
#     tabela = tabela_ficha_notificacao if tabela == "" else tabela
#
#     cursor.execute(f"""
#         INSERT INTO {tabela} (
#             codigo,
#             prontuario,
#             setor,
#             numero_ficha,
#             tipo_notificacao,
#             agravoDoenca,
#             dt_notificacao,
#             uf_notificacao,
#             municipio_notificacao,
#             cod_ibge_notificacao,
#             unidade_saude,
#             codigo_unidade_saude,
#             dt_sintomas,
#             nome_paciente,
#             dt_nascimento,
#             idade,
#             tipo_idade,
#             sexo,
#             gestante,
#             raca,
#             escolaridade,
#             numero_sus,
#             nome_mae,
#             dt_primeiro_sintoma,
#             numero_casos_suspeitos,
#             local_inicial_ocorrencia,
#             local_especificar_ocorrencia,
#             uf_residencia,
#             codigo_unidade_saude,
#             dt_sintomas,
#             nome_paciente,
#             dt_nascimento,
#             idade,
#             tipo_idade,
#             sexo,
#             gestante,
#             raca,
#             escolaridade,
#             numero_sus,
#             nome_mae,
#             dt_primeiro_sintoma,
#             numero_casos_suspeitos,
#             local_inicial_ocorrencia,
#             local_especificar_ocorrencia,
#             uf_residencia,
#             municipio_residencia,
#             cod_ibge_residencia,
#             distrito_residencia,
#             bairro_residencia,
#             logradouro_residencia,
#             codigo_residencia,
#             numero_residencia,
#             complemento_residencia,
#             geo_campo1,
#             geo_campo2,
#             ponto_ref_residencia,
#             cep_residencia,
#             telefone_residencia,
#             zona_residencia,
#             pais_residencia,
#             municipio_us_notificante,
#             nome_notificante,
#             funcao_notificante,
#             assinatura_notificante,
#             dt_amostra_sorologia,
#             dt_outra_amostra,
#             tipo_exame,
#             obito,
#             caso_semelhante,
#             exantema,
#             dt_inicio_exatema,
#             petequiaSufusao,
#             liquor,
#             bacterioscopia,
#             tomou_vacina,
#             dt_ultima_dose_tomada,
#             hospitalizacao,
#             dt_hospitalizacao,
#             uf_hospital,
#             municipio_hospital,
#             cod_ibge_hospital,
#             nome_hospital,
#             cod_hospital,
#             hipotese_diagnostica1,
#             hipotese_diagnostica2,
#             pais_infeccao,
#             distrito_infeccao,
#             uf_infeccao,
#             municipio_infeccao,
#             bairro_infeccao,
#             cod_formulario
#         )
#         VALUES ({placeholders})
#     """, (
#         MAIOR_CODIGO_FICHA_REGISTRADA + 1,
#         prontuario,
#         setor,
#         numero_ficha,
#         tipo_notificacao,
#         agravoDoenca,
#         dt_notificacao,
#         uf_notificacao,
#         municipio_notificacao,
#         cod_ibge_notificacao,
#         unidade_saude
#     ))
#     fechar_conexao_banco(conexao)

















