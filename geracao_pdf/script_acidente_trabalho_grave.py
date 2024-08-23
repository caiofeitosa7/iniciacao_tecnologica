from .pdfWritter import PDFWriter


def gerar_acid_trab_grave(notificatoriaCSV: dict, dict_especifico: dict, modelo_pdf: str, modelo_pdf_base: str, path_pdf_gerado: str, nome_arquivo: str):
    document = PDFWriter(modelo_pdf)

    ###################################################
    # Dados do paciente
    ###################################################
    document.write_text(dict_especifico['numero_ficha2'],(470, 45))
    document.write_date(dict_especifico['dt_notificacao2'], (448, 205), spacing=2) #data_notificacao
    document.write_uf(dict_especifico['uf_notificacao2'], (55, 234)) #uf_notificacao
    document.write_text(dict_especifico['municipio_notificacao2'], (88, 235)) #municipio_notificacao __unid_saude 55,space=220
    document.write_code(dict_especifico['cod_ibge_notificacao2'], (478, 235),space=2) #cod_ibge
    document.write_text(dict_especifico['unidade_saude2'], (65, 262)) #cod_unid_saude
    document.write_code(dict_especifico['cod_unidade_saude2'], (338, 262),space=2) #cod_unid_saude
    document.write_date(dict_especifico['dt_acidente'], (444, 262), spacing=2) #data_diagnostico
    ##############################################
    #####          NOTIFICACAO INDIVIDUAL     ####
    ##############################################
    document.write_text(dict_especifico['nome_paciente2'], (62, 294)) #nome
    document.write_date(dict_especifico['dt_nascimento2'], (449, 293), spacing=2) #data_nascimento
    document.write_code(dict_especifico['idade2'], (63, 323),space=2) #idade
    document.write_mini(dict_especifico['tipo_idade2'], (110, 315)) #tipo_idade
    document.write_mini(dict_especifico['sexo2'], (233, 308)) #sexo
    document.write_mini(dict_especifico['gestante2'], (428, 308)) #gestante
    document.write_mini(dict_especifico['raca2'], (553, 309)) #raça/cor
    document.write_mini(dict_especifico['escolaridade2'], (553, 338)) #escolaridade
    document.write_code(dict_especifico['numero_sus2'], (56, 384),space=2, font_size=10) #cartao_sus
    document.write_text(dict_especifico['nome_mae2'], (240, 384)) #nome_mae
    ##############################################
    #####          DADOS DE RESIDENCIA        ####
    ##############################################

    document.write_uf(dict_especifico['uf_residencia2'], (57, 412)) #uf_residencia
    document.write_text(dict_especifico['municipio_residencia2'], (95, 410)) #municipio_residencia
    document.write_code(dict_especifico['cod_ibge_residencia2'], (325, 410),space=2) #cod_ibge_residencia
    document.write_text(dict_especifico['distrito_residencia2'], (422, 410)) #endereco
    document.write_text(dict_especifico['bairro_residencia2'], (64, 435)) #bairro
    document.write_text(dict_especifico['logradouro_residencia2'], (207, 438)) #logradouro
    document.write_code(dict_especifico['codigo_residencia2'], (478, 438),space=2) #cod_logradouro
    document.write_text(dict_especifico['numero_residencia2'], (65, 460)) #numero
    document.write_text(dict_especifico['complemento_residencia2'], (120, 460)) #complemento
    document.write_text(dict_especifico['geo_campo1_2'], (415, 462)) #geo_campo_1
    document.write_text(dict_especifico['geo_campo2_2'], (55, 485)) #geo_campo_2
    document.write_text(dict_especifico['ponto_ref_residencia2'], (230, 487)) #ponto_ref
    document.write_code(dict_especifico['cep_residencia2'], (456, 489),space=2) #cep
    document.write_telefone(dict_especifico['telefone_residencia2'], (57, 513), space=2) #telefone
    document.write_mini(dict_especifico['zona_residencia2'], (334, 501)) #zona
    document.write_text(dict_especifico['pais_residencia2'], (380, 512)) #pais
    ####################################################
    # Dados Complementares
    ####################################################
    document.write_text(dict_especifico['ocupacao'], (60, 567)) #ocupacao
    document.write_mini(dict_especifico['sit_merc_trabalho'], (535, 582), spacing=3) #sit_merc_trabalho
    document.write_code(dict_especifico['tempo_trabalho'], (68, 664), space=2) #tempo_trabalho
    document.trab_tempo_ocupacao(dict_especifico['tipo_tempo_trabalho']) #tipo_tempo_trabalho
    document.write_mini(dict_especifico['local_acidente'], (554, 645)) #local_acidente
    document.write_code(dict_especifico['cnpj_contratante'], (60, 705), space=2, font_size=12) #cnpj_contratante
    document.write_text(dict_especifico['nome_contratante'], (260, 705)) #nome_contratante
    document.write_text(dict_especifico['ativ_contratante'], (62, 736)) #ativ_contratante
    document.write_uf(dict_especifico['uf_contratante'], (221, 736)) #uf_contratante
    document.write_text(dict_especifico['municipio_contratante'], (260, 734)) #municipio_contratante
    document.write_code(dict_especifico['cod_ibge_contratante'], (484, 734), space=2) #cod_ibge_contratante
    document.write_text(dict_especifico['distrito_contratante'], (62, 761)) #distrito_contratante
    document.write_text(dict_especifico['bairro_contratante'], (223, 761)) #bairro_contratante
    document.write_text(dict_especifico['endereco_contratante'], (388, 761)) #endereco_contratante
    document.write_text(dict_especifico['numero_contratante'], (66, 784)) #numero_contratante
    document.write_text(dict_especifico['ponto_ref_contratante'], (120, 784)) #ponto_ref_contratante
    document.write_telefone(dict_especifico['telefone_contratante'], (430, 785), space=2) #telefone_contratante
    document.write_mini(dict_especifico['empresa_terceirizada'], (480, 800)) #empresa_terceirizada
    #################################################### fim da pagina 1

    document.write_code(dict_especifico['cnae_emp_principal'], (190, 52),space=2, pg=1) #cnae_emp_principal
    document.write_code(dict_especifico['cnpj_emp_principal'], (368, 54),space=2, pg=1) #cnpj_emp_principal
    document.write_text(dict_especifico['rz_social_emp_principal'], (60, 80), pg=1) #rz_social_emp_principal
    document.write_code(dict_especifico['hr_acidente'], (95, 118),space=2, pg=1) #hr_acidente
    document.write_code(dict_especifico['min_acidente'], (198, 117),space=2, pg=1) #min_acidente
    document.write_code(dict_especifico['hr_apos_inicio_jornada'], (407, 117),space=2, pg=1) #hr_apos_inicio_jornada
    document.write_code(dict_especifico['min_apos_inicio_jornada'], (474, 117),space=2, pg=1) #min_apos_inicio_jornada
    document.write_uf(dict_especifico['uf_acidente'], (62, 146), pg=1) #uf_acidente
    document.write_text(dict_especifico['municipio_acidente'], (95, 146), pg=1) #municipio_acidente
    document.write_code(dict_especifico['cod_ibge_acidente'], (240, 146),space=2, pg=1) #cod_ibge_acidente
    document.write_code(dict_especifico['cod_causa_acidente'], (494, 147),space=2, pg=1) #cod_causa_acidente
    document.write_mini(dict_especifico['tipo_acidente'], (222, 162), pg=1) #tipo_acidente
    document.write_mini(dict_especifico['outros_atingidos'], (435, 162), pg=1) #outros_atingidos
    document.write_code(dict_especifico['quant_trab_atingidos'], (494, 175),space=2, pg=1) #quant_trab_atingidos
    document.write_mini(dict_especifico['ocorreu_atendimento'], (368, 196), pg=1) #ocorreu_atendimento
    document.write_date(dict_especifico['dt_atendimento'], (412, 206), spacing=2, pg=1) #dt_atendimento
    document.write_uf(dict_especifico['uf_atendimento'], (539, 206), pg=1) #uf_atendimento
    document.write_text(dict_especifico['municipio_atendimento'], (60, 234), pg=1) #municipio_atendimento
    document.write_code(dict_especifico['cod_ibge_atendimento'], (196, 235),space=2, pg=1) #cod_ibge_atendimento
    document.write_text(dict_especifico['nome_hosp_atendimento'], (310, 235), pg=1) #nome_hosp_atendimento
    document.write_code(dict_especifico['cod_us_atendimento'], (465, 235),space=2, pg=1) #cod_us_atendimento
    document.write_mini(dict_especifico['parte_corpo_atend1'], (312, 263),spacing=2, pg=1) #parte_corpo_atend1
    document.write_mini(dict_especifico['parte_corpo_atend2'], (312, 278),spacing=2, pg=1) #parte_corpo_atend2
    document.write_mini(dict_especifico['parte_corpo_atend3'], (312, 291),spacing=2, pg=1) #parte_corpo_atend3
    document.write_code(dict_especifico['diag_lesao'], (360, 293),space=2, pg=1) #diag_lesao
    document.write_mini(dict_especifico['regime_tratamento'], (550, 268), pg=1) #regime_tratamento
    document.write_mini(dict_especifico['evolucao_caso'], (545, 317), pg=1) #evolucao_caso
    document.write_date(dict_especifico['dt_obito'], (65, 380), spacing=2, pg=1) #dt_obito
    document.write_mini(dict_especifico['comun_acid_trab'], (547, 373), pg=1) #comun_acid_trab
    document.write_box(dict_especifico['obs_adicionais'], rect=(34, 440, 565, 532), pg=1) #obs_adicionais
    document.write_box(dict_especifico['outras_informacoes'], rect=(36, 553, 566, 650), pg=1) #outras_informacoes
    document.write_text(dict_especifico['municipio_us_investigador'], (60, 680), pg=1) #municipio_us_investigador
    document.write_code(dict_especifico['cod_us_investigador'], (468, 681),space=2, pg=1) #cod_us_investigador
    document.write_text(dict_especifico['nome_investigador'], (60, 710), pg=1) #nome_investigador
    document.write_text(dict_especifico['funcao_investigador'], (265, 710), pg=1) #funcao_investigador
    document.write_text(dict_especifico['assinatura_investigador'], (470, 709), pg=1) #assinatura_investigador

    document.save(nome_arquivo, path_pdf_gerado, notificatoriaCSV, modelo_pdf_base)