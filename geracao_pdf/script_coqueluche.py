from .pdfWritter import PDFWriter


def gerar_pdf_coqueluche(notificatoriaCSV: dict, dict_especifico: dict, modelo_pdf: str, modelo_pdf_base: str, path_pdf_gerado: str, nome_arquivo: str):
    document = PDFWriter(modelo_pdf)

    ###################################################
    # Dados do paciente
    ###################################################
    document.write_text(dict_especifico['numero_ficha2'],(467, 49))
    document.write_date(dict_especifico['dt_notificacao2'], (449, 183),spacing=2) #dict_especifico-notificacao
    document.write_uf(dict_especifico['uf_notificacao2'], (55, 212)) #uf-notificacao
    document.write_text(dict_especifico['municipio_notificacao2'], (90, 212)) #municipio-notificacao --unid-saude 55,220
    document.write_code(dict_especifico['cod_ibge_notificacao2'], (477, 212),space=2) #cod-ibge
    document.write_text(dict_especifico['unidade_saude2'], (65, 240)) #cod-unid-saude
    document.write_code(dict_especifico['cod_unidade_saude2'], (340, 240),space=2) #cod-unid-saude
    document.write_date(dict_especifico['dt_sintomas2'], (446, 240), spacing=2) #dict_especifico-diagnostico
    ##############################################
    #####          NOTIFICACAO INDIVIDUAL     ####
    ##############################################
    document.write_text(dict_especifico['nome_paciente2'], (60, 271)) #nome
    document.write_date(dict_especifico['dt_nascimento2'], (449, 270), spacing=2) #dict_especifico-nascimento
    document.write_code(dict_especifico['idade2'], (65, 300),space=2) #idade
    document.write_mini(dict_especifico['tipo_idade2'], (112, 292)) #tipo-idade
    document.write_mini(dict_especifico['sexo2'], (233, 286)) #sexo
    document.write_mini(dict_especifico['gestante2'], (429, 286)) #gestante
    document.write_mini(dict_especifico['raca2'], (554, 286)) #raça/cor
    document.write_mini(dict_especifico['escolaridade2'], (554, 316)) #escolaridade
    document.write_code(dict_especifico['numero_sus2'], (58, 361),space=2, font_size=10) #cartao-sus
    document.write_text(dict_especifico['nome_mae2'], (240, 360)) #nome-mae
    ##############################################
    #####          DADOS DE RESIDENCIA        ####
    ##############################################

    document.write_uf(dict_especifico['uf_residencia2'], (56, 390)) #uf-residencia
    document.write_text(dict_especifico['municipio_residencia2'], (95, 390)) #municipio-residencia
    document.write_code(dict_especifico['cod_ibge_residencia2'], (327, 391),space=2) #cod-ibge-residencia
    document.write_text(dict_especifico['distrito_residencia2'], (422, 390)) #endereco
    document.write_text(dict_especifico['bairro_residencia2'], (64, 415)) #bairro
    document.write_text(dict_especifico['logradouro_residencia2'], (210, 416)) #logradouro
    document.write_code(dict_especifico['codigo_residencia2'], (481, 417),space=2) #cod-logradouro
    document.write_text(dict_especifico['numero_residencia2'], (65, 439)) #numero
    document.write_text(dict_especifico['complemento_residencia2'], (120, 439)) #complemento
    document.write_text(dict_especifico['geo_campo1_2'], (415, 442)) #geo-campo-1
    document.write_text(dict_especifico['geo_campo2_2'], (55, 465)) #geo-campo-2
    document.write_text(dict_especifico['ponto_ref_residencia2'], (230, 466)) #ponto-ref
    document.write_code(dict_especifico['cep_residencia2'], (457, 467),space=2) #cep
    document.write_telefone(dict_especifico['telefone_residencia2'], (59, 491), space=2) #telefone
    document.write_mini(dict_especifico['zona_residencia2'], (335, 480)) #zona
    document.write_text(dict_especifico['pais_residencia2'], (380, 491)) #pais
    ####################################################
    # Dados Complementares
    ####################################################
    document.write_date(dict_especifico['dt_investigacao'], (64, 542), spacing=2) #dict_especifico-investigacao
    document.write_text(dict_especifico['ocupacao'], (190, 542)) #ocupacao
    document.write_mini(dict_especifico['notif_sentinela'], (555, 531)) #unidade-sentinela
    document.write_mini(dict_especifico['contat_caso_susp'], (555, 555)) #contato-coqueluche
    document.write_text(dict_especifico['contat_caso_susp_outro'], (242, 577)) #contato-outros
    document.write_text(dict_especifico['nome_contato'], (65, 607)) #nome-contato
    document.write_text(dict_especifico['endereco_contato'], (75, 631)) #endereco
    document.write_mini(dict_especifico['doses_tri_treta'], (432, 661)) #n-doses-dtp
    document.write_date(dict_especifico['dt_ult_dose_tri_treta'], (461, 672), spacing=2) #dt-ultima-dose
    document.write_date(dict_especifico['dt_tosse'], (67, 703), spacing=2) #dt-inicio-tosse
    document.write_mini(dict_especifico['sint_tosse'], (168, 724)) #tosse
    document.write_mini(dict_especifico['sint_tosse_parox'], (168, 739)) #tosse-paroxistica
    document.write_mini(dict_especifico['sint_resp_ruidosa'], (168, 754)) #respiracao-ruidosa
    document.write_mini(dict_especifico['sint_cianose'], (345, 724)) #cianose
    document.write_mini(dict_especifico['sint_vomito'], (345, 741)) #vomito
    document.write_mini(dict_especifico['sint_apneia'], (345, 757)) #apneia
    document.write_mini(dict_especifico['sint_temp_inferior38'], (459, 723)) #temperatura<38
    document.write_mini(dict_especifico['sint_temp_superior38'], (459, 739)) #temperatura>38
    document.write_mini(dict_especifico['sint_outro'], (459, 756)) #outros
    document.write_mini(dict_especifico['sint_outro_descricao'], (498, 755)) #sintomas-text
    document.write_mini(dict_especifico['comp_pneumonia'], (226, 778)) #pneumonia
    document.write_mini(dict_especifico['comp_encefalopatia'], (226, 794)) #encefalopatia
    document.write_mini(dict_especifico['comp_desidratacao'], (366, 778)) #desidratacao
    document.write_mini(dict_especifico['comp_otite'], (366, 794)) #otite
    document.write_mini(dict_especifico['comp_desnutricao'], (441, 778)) #desnutricao
    document.write_mini(dict_especifico['comp_outro'], (441, 794)) #outros
    document.write_mini(dict_especifico['comp_outro_descricao'], (480, 792)) #complica-text
    #############FIM PG 1#############

    document.write_mini(dict_especifico['hospitalizacao2'], (165, 38),pg=1) #hospitalizacao
    document.write_date(dict_especifico['dt_internacao'], (185, 53),pg=1, spacing=2) #dt-internacao
    document.write_uf(dict_especifico['uf_atendimento'], (305, 53),pg=1) #uf-internacao
    document.write_text(dict_especifico['municipio_atendimento'], (338, 53),pg=1) #municipio-internacao
    document.write_code(dict_especifico['cod_ibge_atendimento'], (484, 53),pg=1,space=2) #ibge-internacao
    document.write_text(dict_especifico['nome_hosp_atendimento'], (65, 84),pg=1) #hospital-internacao
    document.write_code(dict_especifico['cod_ibge_hosp_atendimento'], (472, 85),pg=1,space=2) #cod-hosp-internacao
    document.write_mini(dict_especifico['utilizou_antibiotico'], (432, 106),pg=1) #antibiotico
    document.write_date(dict_especifico['dt_adm_antibiotico'], (454, 122),pg=1, spacing=2) #dt-antibiotico
    document.write_mini(dict_especifico['nasofaringe'], (208, 141),pg=1) #coleta-nasofaringe
    document.write_date(dict_especifico['dt_nasofaringe'], (238, 160),pg=1, spacing=2) #dt-coleta-naso
    document.write_mini(dict_especifico['resultado_cultura'], (551, 139),pg=1) #res-cultura
    document.write_mini(dict_especifico['identif_comun'], (184, 190),pg=1) #comunicante-intimo
    document.write_code(dict_especifico['quant_comunicantes'], (250, 200),pg=1, space=2) #qtd-comunicante
    document.write_mini(dict_especifico['caso_secundario'], (552, 183),pg=1) #qtd-caso-secundarios
    document.write_mini(dict_especifico['coleta_naso'], (188, 235),pg=1) #coleta-naso-comunicante
    document.write_code(dict_especifico['quant_coleta_naso'], (253, 247),pg=1, space=2) #qtd-coleta
    document.write_code(dict_especifico['quant_coleta_posit'], (377, 247),pg=1, space=2) #qtd-res-positivo
    document.write_mini(dict_especifico['medida_controle'], (562, 223),pg=1) #medida-preventiva
    document.write_mini(dict_especifico['classif_final'], (200, 270),pg=1) #class-final
    document.write_mini(dict_especifico['crit_confimacao'], (548, 271),pg=1) #crit-confirmacao
    document.write_mini(dict_especifico['doenca_rel_trab'], (246, 307),pg=1) #doenca-trabalho
    document.write_mini(dict_especifico['evolucao_caso'], (555, 303),pg=1) #evolucao
    document.write_date(dict_especifico['dt_obito'], (63, 350),pg=1, spacing=2) #dt-obito
    document.write_date(dict_especifico['dt_encerramento'], (182, 349),pg=1, spacing=2) #dt-encerramento
    document.write_box(dict_especifico['obs_adicionais'], 1,(33, 413,570,660)) #obs
    document.write_text(dict_especifico['municipio_us_investigador'], (60, 690),pg=1) #municipio-investigador
    document.write_code(dict_especifico['cod_us_investigador'], (477, 692),pg=1, space=1) #cod-unid-saud
    document.write_text(dict_especifico['nome_investigador'], (60, 720),pg=1) #nome-investigador
    document.write_text(dict_especifico['funcao_investigador'], (268, 720),pg=1) #funcao-investigador
    document.write_text(dict_especifico['assinatura_investigador'], (470, 720),pg=1) #asign-investigador

    document.save(nome_arquivo, path_pdf_gerado, notificatoriaCSV, modelo_pdf_base)