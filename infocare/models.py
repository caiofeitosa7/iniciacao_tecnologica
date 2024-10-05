from django.db import connections, transaction
from datetime import datetime, date
from . import settings
import pandas as pd
import pymysql
import re
import os

# imports locais
from geracao_pdf.pdfWritter import PDFWriter
from geracao_pdf.script_ficha_base import generateFicha
from geracao_pdf.script_aids_adulto import gerar_pdf_hiv
from geracao_pdf.script_meningite import gerar_pdf_meningite
from geracao_pdf.script_coqueluche import gerar_pdf_coqueluche
from geracao_pdf.script_intox_exog import gerar_pdf_intox_exog
from geracao_pdf.script_anti_rabica import gerar_pdf_anti_rabica
from geracao_pdf.script_leptospirose import gerar_pdf_leptospirose
from geracao_pdf.script_acid_mat_bio import gerar_pdf_acid_mat_bio
from geracao_pdf.script_obito_fetal_inf import gerar_pdf_obt_fetal_inf
from geracao_pdf.script_leish_visceral import gerar_pdf_leish_visceral
from geracao_pdf.script_dengue_chikungunya import gerar_pdf_dengue_chik
from geracao_pdf.script_doenca_chagas_aguda import gerar_pdf_chagas_aguda
from geracao_pdf.script_obito_tuberculose import gerar_pdf_obt_tuberculose
from geracao_pdf.script_hepatites_virais import gerar_pdf_hepatites_virais
from geracao_pdf.script_sifilis_adquirida import gerar_pdf_sifilis_adquirida
from geracao_pdf.script_paralisia_flacida import gerar_pdf_paralisia_flacida
from geracao_pdf.script_acidente_trabalho_grave import gerar_acid_trab_grave
from geracao_pdf.script_violencia_autoprovocada import gerar_pdf_vio_autoprov
from geracao_pdf.script_obt_mulher_id_fer import gerar_pdf_obt_mulher_id_fertil
from geracao_pdf.script_sindrome_neuroinvasiva import gerar_pdf_sind_neuroinvasiva
from geracao_pdf.script_evento_adv_pos_vacina import gerar_pdf_evento_adv_pos_vacina
from geracao_pdf.script_acid_animal_peconhento import gerar_pdf_acid_animal_peconhento


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
        if 'dataHora' in coluna.lower() and valores[i]:
            data_hora = datetime.strptime(str(valores[i]), '%Y-%m-%d %H:%M:%S')
            valores[i] = data_hora.strftime('%d/%m/%Y %H:%M')
        dados[coluna] = valores[i]
    return dados


def separar_dicionario_ficha(dicionario: dict) -> tuple:
    """
        Separa um dicionário em duas partes: uma parte para a ficha de notificação e outra para a ficha específica.
        return: tuple (ficha_notificacao, ficha_especifica)
    """

    campo_separacao = "bairro_infeccao"
    chaves = list(dicionario.keys())
    indice_separacao = chaves.index(campo_separacao) + 1

    ficha_notificacao = {chave: dicionario[chave] for chave in chaves[:indice_separacao]}
    ficha_especifica = {chave: dicionario[chave] for chave in chaves[indice_separacao:]}

    return ficha_notificacao, ficha_especifica


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
    placeholders = [f"{coluna} = %s" for coluna in colunas]
    dados = dicionario.copy()
    codigo = dados.pop('codigo')

    query = f"""
        UPDATE {nome_tabela}
        SET {', '.join(placeholders)}
        WHERE codigo = {codigo};
    """

    try:
        cursor.execute(query, tuple(dados.values()))
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
    cursor.execute(query, (codigo,))
    fechar_conexao(conexao)


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
    cursor.execute(f"SELECT arquivoHTML FROM tipo_ficha WHERE codigo = %s", (codigo,))
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


def inserir_valores_ficha(cursor, cod_ficha: int, tipo_ficha: int, valores: list, ids: list):
    """
        Insere os valores das colunas do tipo de ficha na tabela valorcampo.
        :param cursor: Cursor da conexão com o banco de dados.
        :param cod_ficha: Código da ficha.
        :param tipo_ficha: Código do tipo de ficha.
        :param valores: Lista com os valores das colunas do tipo de ficha.
        :param ids: Lista com os nomes das colunas do tipo de ficha.
        :return: None.
    """

    cursor.execute("""
        SELECT
            C.codigo,
            C.cod_tipo_campo,
            C.nome
        FROM campo AS C
            INNER JOIN campo_tipo_ficha AS CTF
                ON CTF.cod_campo = C.codigo
        WHERE CTF.cod_tipo_ficha = %s
    """, (tipo_ficha,))
    resultados = cursor.fetchall()

    novos_registros = []
    for i, res in enumerate(resultados):
        registro = []
        cod_campo = res[0]
        tipo_campo = res[1]
        # nome_campo = res[2]
        #
        # if type(valores[i]) in (int, float):
        #     tp_input = 2
        # elif type(valores[i]) == str:
        #     tp_input = 1
        # else:
        #     tp_input = 3
        #
        # print('\ncod_campo:', cod_campo,
        #       '; nome_banco:', nome_campo,
        #       '; nome_input:', ids[i],
        #       '; tp_banco:', tipo_campo,
        #       '; tp_input:', tp_input,
        #       '; tipo_diferente:', 0 if tipo_campo == tp_input else 1,
        #       '; valor_input:', valores[i],
        #       )

        if tipo_campo == 1:  # Se for do tipo string
            registro.append(str(valores[i]))
            registro.append(None)
            registro.append(None)
        elif tipo_campo == 2:  # Se for do tipo numérico
            registro.append(None)
            registro.append(int(valores[i]))
            registro.append(None)
        else:  # Campo do tipo data
            registro.append(None)
            registro.append(None)
            registro.append(valores[i])

        registro.append(cod_ficha)
        registro.append(cod_campo)
        novos_registros.append(tuple(registro))

    cursor.executemany("""
        INSERT INTO valorcampo (valor_string, valor_numerico, valor_data, cod_ficha, cod_campo)
        VALUES (%s, %s, %s, %s, %s)
    """, novos_registros)


def averiguar_campos(cursor, tipo_ficha: int, campos: dict):
    sql = """
        SELECT
            C.codigo        AS cod_campo,
            C.nome          AS nome_campo,
            C.descricao     AS descricao_campo,
            TC.nome         AS nome_tipo_campo,
            TF.nome         AS tipo_ficha
        FROM campo_tipo_ficha AS CTF
            INNER JOIN campo AS C
                ON C.codigo = cod_campo
            INNER JOIN tipo_campo AS TC
                ON TC.codigo = C.cod_tipo_campo
            INNER JOIN tipo_ficha AS TF
                ON TF.codigo = CTF.cod_tipo_ficha
        WHERE CTF.cod_tipo_ficha = %s
    """

    cursor.execute(sql, (tipo_ficha,))
    results = cursor.fetchall()

    registros = []
    keys = list(campos.keys())
    for i, row in enumerate(results):
        valor_campo = campos.get(keys[i])

        if type(valor_campo) in (int, float):
            tp_campo = 'INT'
        elif type(valor_campo) == str:
            tp_campo = 'STRING'
        else:
            tp_campo = 'DATE'

        registro = {
            'cod_campo': row[0],
            'nome_campo': row[1],
            'id_campo_input': keys[i],
            'valor_campo_input': valor_campo,
            'tipo_campo_bd': row[3],
            'tipo_campo_input': type(valor_campo),
            'tipo_diferente': 0 if tp_campo == row[3] else 1,
            'descricao_campo': row[2],
            'tipo_ficha': row[4]
        }

        registros.append(registro)

    df = pd.DataFrame(registros)
    df.to_excel('output.xlsx', index=False)
    print('\nArquivo salvo.\n')


def set_ficha(campos: dict, cod_usuario):
    conexao, cursor = abrir_conexao()
    tipo_ficha = campos.pop('cod_tipo_ficha')
    data_ficha = date.today() if not campos.get('campo-dt-notificacao') \
        else campos.get('campo-dt-notificacao')

    # averiguar_campos(cursor, tipo_ficha, campos)

    try:
        with transaction.atomic():
            cursor.execute(f"""
                INSERT INTO ficha (setor, prontuario, cod_estado, cod_tipo_ficha, cod_usuario, data)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                campos.pop('setor'),
                campos.pop('prontuario'),
                1,
                tipo_ficha,
                cod_usuario,
                data_ficha
            ))

            cursor.execute("SELECT LAST_INSERT_ID()")
            cod_ficha = int(cursor.fetchone()[0])

            # inserir_valores_ficha(cursor, cod_ficha, tipo_ficha, list(campos.values()))
            inserir_valores_ficha(cursor, cod_ficha, tipo_ficha, list(campos.values()), list(campos.keys()))

            print('Passou na insercao dos dados!')

        if cod_ficha:
            preencher_pdf(cod_ficha, tipo_ficha)

        return cod_ficha

    except Exception as e:
        conexao.rollback()
        print(e)
        return None

    finally:
        fechar_conexao(conexao)


def alterar_ficha(campos: dict):
    conexao, cursor = abrir_conexao()
    tipo_ficha = campos.pop('cod_tipo_ficha')
    cod_ficha = campos.pop('codigo')

    # try:
    with transaction.atomic():
        cursor.execute(f"""
            UPDATE ficha
            SET setor = %s,
                prontuario = %s
            WHERE codigo = %s
        """, (
            campos.pop('setor'),
            campos.pop('prontuario'),
            cod_ficha
        ))

        cursor.execute("""
            DELETE FROM valorcampo
            WHERE cod_ficha = %s
        """, (cod_ficha,))

        inserir_valores_ficha(cursor, cod_ficha, tipo_ficha, list(campos.values()), list(campos.keys()))

    if cod_ficha:
        preencher_pdf(cod_ficha, tipo_ficha, True)

    return cod_ficha

    # except Exception as e:
    #     conexao.rollback()
    #     print(e)
    #     return None
    #
    # finally:
    #     fechar_conexao(conexao)


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
               PEND.quant    AS QUANT_PEND_ABERTAS
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
                            FROM pendencia
                            WHERE concluida = 0
                            GROUP BY cod_ficha) AS PEND ON PEND.cod_ficha = F.codigo
        WHERE
            F.codigo = %s
        GROUP BY F.codigo,
                 F.prontuario,
                 TF.nome,
                 TF.codigo,
                 F.setor,
                 C.nome,
                 PEND.quant
        ORDER BY F.setor;
    """

    cursor.execute(query, (cod_ficha,))
    resultados = cursor.fetchall()
    fechar_conexao(conexao, False)

    fichas = []
    for resultado in resultados:
        ficha_id = resultado[0]
        nome_campo = resultado[5]
        valor_campo = resultado[6]

        ficha_existente = next((ficha for ficha in fichas if ficha.get('codigo', None) == ficha_id), None)

        if ficha_existente:
            ficha_existente[nome_campo] = valor_campo
        else:
            ficha = {
                'codigo': ficha_id,
                'prontuario': resultado[1],
                'nome_tipo_ficha': resultado[2],
                'cod_tipo_ficha': resultado[3],
                'setor': resultado[4],
                'quant_pendencias': resultado[7],
                nome_campo: valor_campo
            }

            fichas.append(ficha)

    ficha = fichas[0]
    ficha['arquivos'] = listar_arquivos_ficha(cod_ficha)

    return ficha


def get_quantidade_fichas(status: int):
    conexao, cursor = abrir_conexao()
    cursor.execute(f"SELECT COUNT(*) FROM ficha WHERE cod_estado = %s", (status,))
    quant_fichas = cursor.fetchone()[0]
    fechar_conexao(conexao, False)
    return quant_fichas


def listar_fichas(status: int, numero_ficha: int = 0, setor: str = ''):
    conexao, cursor = abrir_conexao()
    query = f"""
        SELECT F.codigo                                     AS COD_FICHA,
               F.prontuario                                 AS PRONTUARIO,
               TF.nome                                      AS TIPO_FICHA,
               TF.codigo                                    AS COD_TIPO_FICHA,
               F.setor                                      AS SETOR,
               C.nome                                       AS CAMPO,
               MAX(CASE
                       WHEN (C.cod_tipo_campo = 1) THEN VC.valor_string
                       WHEN (C.cod_tipo_campo = 2) THEN VC.valor_numerico
                       WHEN (C.cod_tipo_campo = 3) THEN DATE_FORMAT(VC.valor_data, '%d/%m/%Y')
                   END)                                     AS VALOR_CAMPO,
               PEND.quant                                   AS QUANT_PEND,
               DATE_FORMAT(F.data, '%d/%m/%Y')              AS DATA,
               SUBSTRING_INDEX(U.nome, ' ', 2)              AS NOTIFICANTE
        FROM ficha AS F
             INNER JOIN usuario AS U
                    ON U.codigo = F.cod_usuario
             INNER JOIN campo_tipo_ficha AS CTF
                    ON CTF.cod_tipo_ficha = F.cod_tipo_ficha
                    AND CTF.cod_campo IN (1, 11)
             LEFT JOIN valorcampo AS VC
                    ON VC.cod_ficha = F.codigo
             INNER JOIN tipo_ficha AS TF
                    ON TF.codigo = F.cod_tipo_ficha
             INNER JOIN campo AS C
                    ON C.codigo = VC.cod_campo
                    AND C.codigo IN (1, 11)
             LEFT JOIN (
                SELECT
                    cod_ficha,
                    COUNT(codigo) AS quant
                FROM pendencia
                GROUP BY cod_ficha
             ) AS PEND ON PEND.cod_ficha = F.codigo
        WHERE
            F.cod_estado = {status}
        GROUP BY F.codigo,
                 F.prontuario,
                 TF.nome,
                 TF.codigo,
                 F.setor,
                 C.nome,
                 PEND.quant,
                 F.data
        ORDER BY F.data DESC;
    """

    cursor.execute(query)
    resultados = cursor.fetchall()
    fechar_conexao(conexao, False)

    fichas = []
    for resultado in resultados:
        ficha_id = resultado[0]
        nome_campo = resultado[5]
        valor_campo = resultado[6]

        ficha_existente = next((ficha for ficha in fichas if ficha.get('cod_ficha', None) == ficha_id), None)

        if ficha_existente:
            ficha_existente[nome_campo] = valor_campo
        else:
            ficha = {
                'cod_ficha': ficha_id,
                'prontuario': resultado[1],
                'nome_tipo_ficha': resultado[2],
                'cod_tipo_ficha': resultado[3],
                'setor': resultado[4],
                'quant_pendencias': resultado[7],
                'data': resultado[8],
                'nome_notificante': resultado[9],
                nome_campo: valor_campo
            }

            fichas.append(ficha)

    return fichas


def listar_pendencias(cod_ficha: int):
    nome_tabela = 'pendencia'
    conexao, cursor = abrir_conexao()
    cursor.execute(f"""
        SELECT
            PEND.codigo,
            PEND.descricao,
            PEND.concluida,
            PEND.cod_ficha,
            PEND.cod_usuario_autor,
            PEND.cod_usuario_concluinte,
            PEND.dataHora_cadastro,
            PEND.dataHora_concluida,
            AUTOR.codigo,
            AUTOR.nome,
            CONCLUINTE.codigo,
            CONCLUINTE.nome
        FROM {nome_tabela} AS PEND
            INNER JOIN usuario AS AUTOR
                ON cod_usuario_autor = AUTOR.codigo
            INNER JOIN usuario AS CONCLUINTE
                ON cod_usuario_concluinte = CONCLUINTE.codigo
        WHERE cod_ficha = %s
    """, (cod_ficha,))

    resultados = cursor.fetchall()
    colunas = get_colunas_tabela(cursor, nome_tabela) + ['cod_autor', 'nome_autor', 'cod_concluinte', 'nome_concluinte']
    pendencias = [criar_dicionario(colunas, list(resultado)) for resultado in resultados] if resultados else []

    for pendencia in pendencias:
        pendencia['nome_concluinte'] = pendencia['nome_concluinte'].split(' ')[0]
        pendencia['nome_autor'] = pendencia['nome_autor'].split(' ')[0]
        pendencia['inicial_autor'] = pendencia['nome_autor'][0].upper()

    fechar_conexao(conexao, False)
    return pendencias


def set_pendencia(dados: dict):
    inserir_registro_tabela('pendencia', dados)
    alterar_estado_ficha(dados['cod_ficha'], 4)


def alterar_pendencia(dados: dict):
    alterar_registro_tabela('pendencia', dados)


def deletar_pendencia(cod_pendencia: int):
    apagar_registro_tabela('pendencia', cod_pendencia)


def fechar_pendencia(dados: dict):
    valores = (
        dados['dataHora_concluida'],
        dados['cod_usuario_concluinte'],
        dados['cod_pendencia']
    )

    try:
        conexao, cursor = abrir_conexao()
        cursor.execute(f"""
            UPDATE
                pendencia
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
    alterar_estado_ficha(cod_ficha, 3)


def set_arquivos_ficha(registros: list, cod_ficha: int, salvar_anexo: bool = True):
    # try:
    conexao, cursor = abrir_conexao()
    cursor.executemany("""
        INSERT INTO arquivo (
            nome_original,
            nome_armazenado,
            extensao,
            url,
            data_cadastro,
            data_deletado,
            deletado,
            cod_ficha,
            arq_principal
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, registros)

    if salvar_anexo:
        # anexos = list()
        # for registro in registros:
        #     nome_arquivo = registro[1]
        #     extensao = registro[2]
        #     anexos.append(os.path.join(settings.DIRETORIO_PDF, nome_arquivo + extensao))

        juntar_anexos_com_ficha_principal(cursor, cod_ficha)

    fechar_conexao(conexao)

    # except Exception as e:
    #     print(e)


def listar_arquivos_ficha(cod_ficha: int):
    conexao, cursor = abrir_conexao()
    colunas = ['codigo', 'nome', 'url']
    cursor.execute("""
        SELECT
            codigo,
            CONCAT(nome_original, extensao),
            url
        FROM arquivo
        WHERE cod_ficha = %s
            AND deletado = 0
        ORDER BY nome_original;
    """, (cod_ficha,))

    resultados = cursor.fetchall()
    fechar_conexao(conexao, False)

    return [criar_dicionario(colunas, list(resultado)) for resultado in resultados] \
        if resultados \
        else []


def numero_ficha_existe(numero_ficha: int) -> int:
    conexao, cursor = abrir_conexao()
    query = f"""
        SELECT COUNT(*)
        FROM valorcampo AS VC
        WHERE cod_campo = 1
            AND valor_numerico = %s
    """

    cursor.execute(query, (numero_ficha,))
    quant = cursor.fetchone()[0]
    fechar_conexao(conexao, False)
    return quant > 0


def formatar_dados_esperados(dados: dict) -> dict:
    """
        Formata as datas do dicionário para o formato dd/mm/aaaa.
        return: Dicionário com as datas formatadas.
    """
    for key in dados:
        if 'dt' in key.lower() and dados[key]:
            data_obj = datetime.strptime(str(dados[key]), '%Y-%m-%d')
            dados[key] = data_obj.strftime('%d/%m/%Y')
        elif 'dataHora' in key.lower() and dados[key]:
            data_hora = datetime.strptime(str(dados[key]), '%Y-%m-%d %H:%M:%S')
            dados[key] = data_hora.strftime('%d/%m/%Y %H:%M')

    return dados


def get_arquivo_principal_ficha(cursor, cod_ficha: int):
    cursor.execute("""
            SELECT nome_armazenado, extensao
            FROM arquivo
            WHERE cod_ficha = %s
                AND arq_principal = 1
        """, (cod_ficha,))

    nome_arquivo, extensao = cursor.fetchone()
    return nome_arquivo, extensao


def get_arquivos_anexos_ficha(cursor, cod_ficha: int):
    cursor.execute("""
            SELECT nome_armazenado, extensao
            FROM arquivo
            WHERE cod_ficha = %s
                AND arq_principal = 0
        """, (cod_ficha,))

    registros = cursor.fetchall()
    return [os.path.join(settings.DIRETORIO_PDF, res[0] + res[1])
            for res in registros] \
        if registros else []


def apagar_arquivo_ficha(cursor, cod_ficha: int):
    nome_arquivo, extensao = get_arquivo_principal_ficha(cursor, cod_ficha)
    os.remove(os.path.join(settings.DIRETORIO_PDF, nome_arquivo + extensao))

    cursor.execute("""
            DELETE FROM arquivo
            WHERE cod_ficha = %s
                AND arq_principal = 1;
        """, (cod_ficha,))

    return nome_arquivo


def juntar_anexos_com_ficha_principal(cursor, cod_ficha: int):
    nome_arquivo, extensao = get_arquivo_principal_ficha(cursor, cod_ficha)
    anexos = get_arquivos_anexos_ficha(cursor, cod_ficha)

    arquivo = nome_arquivo + extensao
    diretorio = settings.DIRETORIO_PDF
    path_pdf_principal = os.path.join(diretorio, arquivo)
    anexos = [PDFWriter(anexo) for anexo in anexos]
    pdf_principal = PDFWriter(path_pdf_principal)
    pdf_principal.addAnexos(anexos, diretorio, arquivo)


def preencher_pdf(cod_ficha, tipo_ficha, arq_existe=False):
    conexao, cursor = abrir_conexao()

    if arq_existe:
        nome_arq_anterior = apagar_arquivo_ficha(cursor, cod_ficha)
        # print(nome_arq_anterior)

    cursor.execute("""
        SELECT modelo_pdf, obito
        FROM tipo_ficha
        WHERE codigo = %s
    """, (tipo_ficha,))

    modelo_pdf, ficha_de_obito = cursor.fetchone()
    ficha_completa = get_ficha(cod_ficha)
    ficha_completa = formatar_dados_esperados(ficha_completa)
    nome_original = ficha_completa['nome_paciente']

    # if arq_existe:
    #     nome_armazenado = nome_arq_anterior
    # else:
    nome_armazenado = '_'.join(nome_original.split(' ')[:2]) \
                      + datetime.now().strftime('_%f')
    # + datetime.now().strftime('%Y%m%d_%H%M%S_%f')

    data_cadastro = datetime.now().strftime('%Y-%m-%d')
    data_deletado = None
    extensao = '.pdf'
    deletado = 0

    nome_arquivo = nome_armazenado + extensao
    url_arquivo = settings.MEDIA_URL + 'arquivos/' + nome_arquivo
    path_pdf_modelo = os.path.join('geracao_pdf', 'modelos_pdf', modelo_pdf)
    path_pdf_ficha_base = os.path.join('geracao_pdf', 'modelos_pdf', 'FichaNotificacao.pdf')
    path_pdf_gerado = settings.DIRETORIO_PDF

    print('indo gerar o pdf')

    if not ficha_de_obito and tipo_ficha != 1:  # Exclui ficha de notificacao geral e as fichas de obito
        ficha_notificacao, ficha_especifica = separar_dicionario_ficha(ficha_completa)

        if tipo_ficha == 2:
            gerar_acid_trab_grave(ficha_notificacao, ficha_especifica, path_pdf_modelo, path_pdf_ficha_base,
                                  path_pdf_gerado, nome_arquivo)
        elif tipo_ficha == 3:
            gerar_pdf_vio_autoprov(ficha_notificacao, ficha_especifica, path_pdf_modelo, path_pdf_ficha_base,
                                   path_pdf_gerado, nome_arquivo)
        elif tipo_ficha == 4:
            gerar_pdf_anti_rabica(ficha_notificacao, ficha_especifica, path_pdf_modelo, path_pdf_ficha_base,
                                  path_pdf_gerado, nome_arquivo)
        elif tipo_ficha == 6:
            gerar_pdf_leptospirose(ficha_notificacao, ficha_especifica, path_pdf_modelo, path_pdf_ficha_base,
                                   path_pdf_gerado, nome_arquivo)
        elif tipo_ficha == 8:
            gerar_pdf_sifilis_adquirida(ficha_notificacao, ficha_especifica, path_pdf_modelo, path_pdf_ficha_base,
                                        path_pdf_gerado, nome_arquivo)
        elif tipo_ficha == 9:
            gerar_pdf_meningite(ficha_notificacao, ficha_especifica, path_pdf_modelo, path_pdf_ficha_base,
                                path_pdf_gerado, nome_arquivo)
        elif tipo_ficha == 11:
            gerar_pdf_hiv(ficha_notificacao, ficha_especifica, path_pdf_modelo, path_pdf_ficha_base,
                          path_pdf_gerado,
                          nome_arquivo)
        elif tipo_ficha == 12:
            gerar_pdf_acid_mat_bio(ficha_notificacao, ficha_especifica, path_pdf_modelo, path_pdf_ficha_base,
                                   path_pdf_gerado, nome_arquivo)
        elif tipo_ficha == 13:
            gerar_pdf_coqueluche(ficha_notificacao, ficha_especifica, path_pdf_modelo, path_pdf_ficha_base,
                                 path_pdf_gerado, nome_arquivo)
        elif tipo_ficha == 14:
            gerar_pdf_acid_animal_peconhento(ficha_notificacao, ficha_especifica, path_pdf_modelo,
                                             path_pdf_ficha_base,
                                             path_pdf_gerado, nome_arquivo)
        elif tipo_ficha == 15:
            gerar_pdf_dengue_chik(ficha_notificacao, ficha_especifica, path_pdf_modelo, path_pdf_ficha_base,
                                  path_pdf_gerado, nome_arquivo)
        elif tipo_ficha == 16:
            gerar_pdf_chagas_aguda(ficha_notificacao, ficha_especifica, path_pdf_modelo, path_pdf_ficha_base,
                                   path_pdf_gerado, nome_arquivo)
        elif tipo_ficha == 17:
            gerar_pdf_intox_exog(ficha_notificacao, ficha_especifica, path_pdf_modelo, path_pdf_ficha_base,
                                 path_pdf_gerado, nome_arquivo)
        elif tipo_ficha == 18:
            gerar_pdf_hepatites_virais(ficha_notificacao, ficha_especifica, path_pdf_modelo, path_pdf_ficha_base,
                                       path_pdf_gerado, nome_arquivo)
        elif tipo_ficha == 19:
            gerar_pdf_paralisia_flacida(ficha_notificacao, ficha_especifica, path_pdf_modelo, path_pdf_ficha_base,
                                        path_pdf_gerado, nome_arquivo)
        elif tipo_ficha == 20:
            gerar_pdf_sind_neuroinvasiva(ficha_notificacao, ficha_especifica, path_pdf_modelo, path_pdf_ficha_base,
                                         path_pdf_gerado, nome_arquivo)
        elif tipo_ficha == 21:
            gerar_pdf_leish_visceral(ficha_notificacao, ficha_especifica, path_pdf_modelo, path_pdf_ficha_base,
                                     path_pdf_gerado, nome_arquivo)
        elif tipo_ficha == 22:
            gerar_pdf_evento_adv_pos_vacina(ficha_notificacao, ficha_especifica, path_pdf_modelo,
                                            path_pdf_ficha_base,
                                            path_pdf_gerado, nome_arquivo)

    elif tipo_ficha == 1:
        generateFicha(ficha_completa, path_pdf_modelo, path_pdf_gerado, nome_arquivo)

    # Fichas de Obito #
    elif tipo_ficha == 5:
        gerar_pdf_obt_mulher_id_fertil(ficha_completa, path_pdf_modelo, path_pdf_gerado, nome_arquivo)
    elif tipo_ficha == 7:
        gerar_pdf_obt_tuberculose(ficha_completa, path_pdf_modelo, path_pdf_gerado, nome_arquivo)
    elif tipo_ficha == 10:
        gerar_pdf_obt_fetal_inf(ficha_completa, path_pdf_modelo, path_pdf_gerado, nome_arquivo)

    print('passando para registro no banco')

    info_arquivo = (
        nome_original,
        nome_armazenado,
        extensao,
        url_arquivo,
        data_cadastro,
        data_deletado,
        deletado,
        cod_ficha,
        1
    )

    set_arquivos_ficha([info_arquivo], cod_ficha, False)


def get_info_comum_paciente(prontuario: int):
    bd_hut05 = settings.DATABASES.get('hutsaude05')
    resultado = None

    try:
        connection = pymysql.connect(
            host=bd_hut05['HOST'],
            user=bd_hut05['USER'],
            password=bd_hut05['PASSWORD'],
            database=bd_hut05['NAME'],
            cursorclass=pymysql.cursors.DictCursor  # Opcional, retorna resultados como dicionários
        )

        with connection.cursor() as cursor:
            cursor.execute("""
                    SELECT *
                    FROM infocare
                    WHERE prontuario = %s
                        OR prontuario_unico = %s
                """, (prontuario, prontuario))
            resultado = cursor.fetchone()

            if resultado:
                endereco_numero = resultado['endereco_numero'] \
                    .replace('NÂº', '&&') \
                    .split('&&')

                numero = endereco_numero[1].strip()
                numero = re.findall(r'\d+', numero) if numero else None
                resultado['endereco_numero'] = int(numero[0]) if numero else None
                resultado['endereco_logradouro'] = endereco_numero[0].strip(', ')
                resultado['endereco_completo'] = ' - '.join(endereco_numero)
                telefones = resultado['telefones'].replace(' ', '').split('/')
                resultado['telefones'] = telefones[0]

    except pymysql.MySQLError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

    finally:
        if connection:
            connection.close()
            print("Conexão fechada.")

        return resultado


def listar_fichas_download(dados):
    """
        Retorna uma lista contendo os códigos das fichas para download.
        :param dados: Dicionário contendo os filtros de data e tipo de ficha.
    """

    tipo_ficha = int(dados['tipo-ficha'])
    dt_inicio = dados['dt-inicio'] \
        if dados['dt-inicio'] \
        else datetime.now().strftime('%Y-%m-%d')
    dt_fim = dados['dt-fim'] \
        if dados['dt-fim'] \
        else datetime.now().strftime('%Y-%m-%d')
    query = """
        SELECT codigo
        FROM ficha
        WHERE data BETWEEN %s AND %s
    """

    if tipo_ficha:
        query += f' AND cod_tipo_ficha = {tipo_ficha};'

    conexao, cursor = abrir_conexao()
    cursor.execute(query, (dt_inicio, dt_fim))

    resultados = cursor.fetchall()
    fechar_conexao(conexao, False)
    return [res[0] for res in resultados] if resultados else list()
