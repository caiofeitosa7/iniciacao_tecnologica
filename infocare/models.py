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

        print('maior codigo da tabela', tabela[0], '=', maior_codigo_tabela)

        if maior_codigo_tabela > maior_codigo_geral:
            maior_codigo_geral = maior_codigo_tabela

    fechar_conexao_banco(conexao, False)
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


def registrar_ficha_preliminar(conexao, cod_ficha, cod_formulario):
    cursor = conexao.cursor()
    cursor.execute(f"INSERT INTO preliminar (cod_ficha, cod_formulario) VALUES ({cod_ficha}, {cod_formulario})")


def registrar_ficha_notificacao(campos: dict, tabela: str = ""):
    cod_ficha = proximo_codigo_ficha()
    conexao = abrir_conexao_banco()

    print('codigo da ficha', cod_ficha)

    # if not tabela:
    #     registrar_ficha_preliminar(conexao, cod_ficha, campos['cod_formulario'])

    placeholders = ', '.join(['?' for _ in range(74)])
    tabela_ficha_notificacao = get_tabela_formulario(1)
    tabela = tabela_ficha_notificacao if tabela == "" else tabela

    cursor = conexao.cursor()

    print(tabela)

    try:
        cursor.execute(f"""
            INSERT INTO {tabela} (
                codigo,
                numero_ficha,
                tipo_notificacao,
                agravoDoenca,
                dt_notificacao,
                uf_notificacao,
                municipio_notificacao,
                cod_ibge_notificacao,
                unidade_saude,
                cod_unidade_saude,
                dt_sintomas,
                nome_paciente,
                dt_nascimento,
                idade,
                tipo_idade,
                sexo,
                gestante,
                raca,
                escolaridade,
                numero_sus,
                nome_mae,
                dt_primeiro_sintoma,
                numero_casos_suspeitos,
                local_inicial_ocorrencia,
                local_inicial_ocorrencia_outro,
                uf_residencia,
                municipio_residencia,
                cod_ibge_residencia,
                distrito_residencia,
                bairro_residencia,
                logradouro_residencia,
                codigo_residencia,
                numero_residencia,
                complemento_residencia,
                geo_campo1,
                geo_campo2,
                ponto_ref_residencia,
                cep_residencia,
                telefone_residencia,
                zona_residencia,
                pais_residencia,
                municipio_us_notificante,
                nome_notificante,
                funcao_notificante,
                assinatura_notificante,
                dt_amostra_sorologia,
                dt_outra_amostra,
                tipo_exame,
                obito,
                caso_semelhante,
                exantema,
                dt_inicio_exantema,
                petequiaSufusao,
                liquor,
                bacterioscopia,
                tomou_vacina,
                dt_ultima_dose_tomada,
                hospitalizacao,
                dt_hospitalizacao,
                uf_hospital,
                municipio_hospital,
                cod_ibge_hospital,
                nome_hospital,
                cod_hospital,
                
                hipotese_diagnostica1,
                hipotese_diagnostica2,
                pais_infeccao,
                uf_infeccao,
                municipio_infeccao,
                distrito_infeccao,
                bairro_infeccao,
                setor,
                prontuario,
                cod_formulario
                
                
                
            ) VALUES ({placeholders})
            """, (
                cod_ficha,
                int(campos['numero_ficha']),
                int(campos['tipo_notificacao']),
                campos['agravoDoenca'],
                campos['dt_notificacao'],
                campos['uf_notificacao'],
                campos['municipio_notificacao'],
                int(campos['cod_ibge_notificacao']),
                campos['unidade_saude'],
                int(campos['cod_unidade_saude']),
                campos['dt_sintomas'],
                campos['nome_paciente'],
                campos['dt_nascimento'],
                int(campos['idade']),
                int(campos['tipo_idade']),
                str(campos['sexo']).upper(),
                int(campos['gestante']),
                int(campos['raca']),
                int(campos['escolaridade']),
                int(campos['numero_sus']),
                campos['nome_mae'],
                campos['dt_primeiro_sintoma'],
                int(campos['numero_casos_suspeitos']),
                int(campos['local_inicial_ocorrencia']),
                campos['local_inicial_ocorrencia_outro'],
                campos['uf_residencia'],
                campos['municipio_residencia'],
                int(campos['cod_ibge_residencia']),
                campos['distrito_residencia'],
                campos['bairro_residencia'],
                campos['logradouro_residencia'],
                int(campos['codigo_residencia']),
                int(campos['numero_residencia']),
                campos['complemento_residencia'],
                campos['geo_campo1'],
                campos['geo_campo2'],
                campos['ponto_ref_residencia'],
                campos['cep_residencia'],
                campos['telefone_residencia'],
                int(campos['zona_residencia']),
                campos['pais_residencia'],
                campos['municipio_us_notificante'],
                campos['nome_notificante'],
                campos['funcao_notificante'],
                campos['assinatura_notificante'],
                campos['dt_amostra_sorologia'],
                campos['dt_outra_amostra'],
                campos['tipo_exame'],
                int(campos['obito']),
                int(campos['caso_semelhante']),
                int(campos['exantema']),
                campos['dt_inicio_exantema'],
                int(campos['petequiaSufusao']),
                int(campos['liquor']),
                campos['bacterioscopia'],
                int(campos['tomou_vacina']),
                campos['dt_ultima_dose_tomada'],
                int(campos['hospitalizacao']),
                campos['dt_hospitalizacao'],

                campos['uf_hospital'],
                campos['municipio_hospital'],
                int(campos['cod_ibge_hospital']),
                campos['nome_hospital'],
                int(campos['cod_hospital']),
                campos['hipotese_diagnostica1'],
                campos['hipotese_diagnostica2'],
                campos['pais_infeccao'],
                campos['uf_infeccao'],
                campos['municipio_infeccao'],
                campos['distrito_infeccao'],
                campos['bairro_infeccao'],
                campos['setor'],
                int(campos['prontuario']),
                int(campos['cod_formulario'])



            ))
    except Exception as e:
        print(e)

    fechar_conexao_banco(conexao)




















