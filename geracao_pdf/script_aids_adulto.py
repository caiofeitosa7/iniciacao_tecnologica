from .pdfWritter import PDFWriter


def gerar_pdf_hiv(notificatoriaCSV: dict, dict_especifico: dict, modelo_pdf: str, modelo_pdf_base: str,
                  path_pdf_gerado: str, nome_arquivo: str):
    document = PDFWriter(modelo_pdf)

    ##############################################
    #####            DADOS GERAIS             ####
    ##############################################
    document.write_text(dict_especifico["numero_ficha2"], (475, 44), 0)
    document.write_date(dict_especifico['dt_notificacao2'], (448, 162), 0, spacing=2)  #data-notificacao
    document.write_uf(dict_especifico['uf_notificacao2'], (55, 191), 0)  #uf-notificacao
    document.write_text(dict_especifico['municipio_notificacao2'], (90, 191),
                        0)  #municipio-notificacao --unid-saude 55,220
    document.write_code(dict_especifico['cod_ibge_notificacao2'], (477, 191), 0, 2)  #cod-ibge
    document.write_text(dict_especifico['unidade_saude2'], (70, 220), 0)  #cod-unid-saude
    document.write_code(dict_especifico['cod_unidade_saude2'], (340, 220), space=2)  #cod-unid-saude
    document.write_date(dict_especifico['dt_diagnostico'], (448, 218), spacing=2)  #data-diagnostico
    ##############################################
    #####          NOTIFICACAO INDIVIDUAL     ####
    ##############################################
    document.write_text(dict_especifico['nome_paciente2'], (55, 250), 0)  #nome
    document.write_date(dict_especifico['dt_nascimento2'], (450, 249), spacing=2)  #data-nascimento
    document.write_code(dict_especifico['idade2'], (65, 278), 0, 2)  #idade
    document.write_mini(dict_especifico['tipo_idade2'], (112, 271), 0)  #tipo-idade
    document.write_mini(dict_especifico['sexo2'], (234, 265), 0)  #sexo
    document.write_mini(dict_especifico['gestante2'], (430, 265), 0)  #gestante
    document.write_mini(dict_especifico['raca2'], (555, 265), 0)  #raça/cor
    document.write_mini(dict_especifico['escolaridade2'], (555, 294), 0)  #escolaridade
    document.write_code(dict_especifico['numero_sus2'], (53, 340), space=1, font_size=14)  #cartao-sus
    document.write_text(dict_especifico['nome_mae2'], (240, 338), 0)  #nome-mae
    ##############################################
    #####          DADOS DE RESIDENCIA        ####
    ##############################################

    document.write_uf(dict_especifico['uf_residencia2'], (56, 371), 0)  #uf-residencia
    document.write_text(dict_especifico['municipio_residencia2'], (95, 371), 0)  #municipio-residencia
    document.write_code(dict_especifico['cod_ibge_residencia2'], (327, 370), 0, 2)  #cod-ibge-residencia
    document.write_text(dict_especifico['distrito_residencia2'], (424, 370), 0)  #endereco
    document.write_text(dict_especifico['bairro_residencia2'], (64, 393), 0)  #bairro
    document.write_text(dict_especifico['logradouro_residencia2'], (210, 395), 0)  #logradouro
    document.write_code(dict_especifico['codigo_residencia2'], (480, 395), 0, 2)  #cod-logradouro
    document.write_text(dict_especifico['numero_residencia2'], (60, 420), 0)  #numero
    document.write_text(dict_especifico['complemento_residencia2'], (120, 420), 0)  #complemento
    document.write_text(dict_especifico['geo_campo1_2'], (418, 422), 0)  #geo-campo-1
    document.write_text(dict_especifico['geo_campo2_2'], (60, 445), 0)  #geo-campo-2
    document.write_text(dict_especifico['ponto_ref_residencia2'], (230, 445), 0)  #ponto-ref
    document.write_cep(dict_especifico['cep_residencia2'], (459, 449), space=2, font_size=12)  #cep
    document.write_telefone(dict_especifico['telefone_residencia2'], (59, 472), space=2)  #telefone
    document.write_mini(dict_especifico['zona_residencia2'], (335, 460))  #zona
    document.write_text(dict_especifico['pais_residencia2'], (380, 472))  #pais

    ##############################################
    #####          DADOS COMPLEMENTARES       ####
    ##############################################
    document.write_text(dict_especifico['ocupacao'], (70, 524))  #ocupacao
    document.write_mini(dict_especifico['trans_vertical'], (238, 552))  #transmissao
    document.write_mini(dict_especifico['trans_sexual'], (552, 548))  #orientacao-sexual
    document.write_mini(dict_especifico['trans_droga_injetavel'], (287, 594))  #uso-drogas
    document.write_mini(dict_especifico['trans_hemotransfusao'], (287, 613))  #tratamento-hemotransfusao
    document.write_mini(dict_especifico['trans_transfusao'], (486, 594))  #transfussao
    document.write_mini(dict_especifico['trans_mat_biologico'], (486, 612))  #acidente-biologico
    document.write_date(dict_especifico['dt_transfusao'], (68, 652), spacing=2)  #data-transfussao
    document.write_uf(dict_especifico['uf_transfusao'], (186, 652))  #uf-transfussao
    document.write_text(dict_especifico['municipio_transfusao'], (230, 652))  #municipio-transfussao
    document.write_code(dict_especifico['cod_ibge_transfusao'], (482, 652), space=2)  #ibge-transfussao
    document.write_text(dict_especifico['instituicao_transfusao'], (70, 680))  #instituicao-transfussao
    document.write_code(dict_especifico['cod_instit_transfusao'], (468, 680), space=2)  #cod-instituicao-transfussao
    document.write_mini(dict_especifico['causa_infeccao'], (545, 700))  #resultado-invest-aids
    ##############################################
    #####          DADOS COMPLEMENTARES LAB   ####
    ##############################################
    document.write_date(dict_especifico['dt_coleta_triagem'], (164, 770), spacing=2)  #data-coleta-1
    document.write_date(dict_especifico['dt_coleta_confirm'], (387, 770), spacing=2)  #data-coleta-2
    document.write_date(dict_especifico['dt_coleta_rapida'], (368, 805), spacing=2)  #data-coleta-3
    document.write_mini(dict_especifico['test_triagem_hiv'], (114, 761), 0)  #triagem
    document.write_mini(dict_especifico['test_confirmatorio'], (312, 763), 0)  #confirmatorio
    document.write_mini(dict_especifico['test_rapido1'], (157, 794), 0)  #rapido-1
    document.write_mini(dict_especifico['test_rapido2'], (237, 795), 0)  #rapido-2
    document.write_mini(dict_especifico['test_rapido3'], (315, 795), 0)  #rapido-3
    ##############################################
    #####        DOS COMPLEMENTARES DEF AIDS  ####
    ##############################################
    #COLUNA 1
    document.write_mini(dict_especifico['crit_kaposi'], (70, 50), 1)  #sarcoma-de-kaposi
    document.write_mini(dict_especifico['crit_tb_disseminada'], (70, 65), 1)  #tuberculose-ncavitaria
    document.write_mini(dict_especifico['crit_candidose'], (70, 79), 1)  #candidose-oral-ou-leucoplasia
    document.write_mini(dict_especifico['crit_tb_pulmonar'], (70, 94), 1)  #turbeculose-cavitaria
    document.write_mini(dict_especifico['crit_herpes_zoster'], (70, 108), 1)  #herpes-zoster-menor-60
    document.write_mini(dict_especifico['crit_disf_snc'], (70, 123), 1)  #disf-sist-nerv-central
    document.write_mini(dict_especifico['crit_diarreia'], (70, 137), 1)  #diarreia-cronica
    document.write_mini(dict_especifico['crit_febre'], (70, 151), 1)  #febre-maior-1-mes

    #COLUNA 2
    document.write_mini(dict_especifico['crit_caquexia'], (304, 50), 1)  #perda-10-peso-1-mes
    document.write_mini(dict_especifico['crit_astenia'], (304, 65), 1)  #astenia-maior-1-mes
    document.write_mini(dict_especifico['crit_dermatite'], (304, 79), 1)  #dermatite-persistente
    document.write_mini(dict_especifico['crit_anemia'], (304, 94), 1)  #anemia-linfopenia-trombocitopenia
    document.write_mini(dict_especifico['crit_tosse'], (304, 108), 1)  #tosse-cronica-ou-pneumonia
    document.write_mini(dict_especifico['crit_linfadeno'], (304, 123), 1)  #linfadenopatia->1-tempo->1-mes

    # CDC ADAPTADO
    #COLUNA 1
    document.write_mini(dict_especifico['crit_cdc_ca_cervical'], (69, 182), 1)  #cancer-cervical-inv
    document.write_mini(dict_especifico['crit_cdc_candidose_eso'], (69, 196), 1)  #candidose-esofago
    document.write_mini(dict_especifico['crit_cdc_candidose_traq'], (69, 211), 1)  #candidose-traqueia-pulmao
    document.write_mini(dict_especifico['crit_cdc_citomegalovirose'], (69, 225), 1)  #citomegalovirose
    document.write_mini(dict_especifico['crit_cdc_criptococose'], (69, 240), 1)  #criptococose-extrapulmonar
    document.write_mini(dict_especifico['crit_cdc_criptosporidiose'], (69, 254), 1)  #criptosporidiose-cronica
    document.write_mini(dict_especifico['crit_cdc_herpes'], (69, 269), 1)  #herpes-simples
    document.write_mini(dict_especifico['crit_cdc_histoplasmose'], (69, 285), 1)  #histoplasmose-disseminada
    document.write_mini(dict_especifico['crit_cdc_isosporidiose'], (69, 299), 1)  #isossporidiose

    #COLUNA 2
    document.write_mini(dict_especifico['crit_cdc_leucoencefalopatia'], (302, 181), 1)  #leucoencefalopatia
    document.write_mini(dict_especifico['crit_cdc_linf_nao_hodgkin'], (302, 198), 1)  #linfoma-n-hodgkin
    document.write_mini(dict_especifico['crit_cdc_linf_cerebro'], (302, 212), 1)  #linfoma-prim-cerebro
    document.write_mini(dict_especifico['crit_cdc_micobacteriose'], (302, 226), 1)  #micobacteriose-disseminada
    document.write_mini(dict_especifico['crit_cdc_pneumonia'], (302, 242), 1)  #pneumonia-pneumocystis
    document.write_mini(dict_especifico['crit_cdc_chagas'], (302, 256), 1)  #reativacao-chagas
    document.write_mini(dict_especifico['crit_cdc_salmonelose'], (302, 270), 1)  #salmonelose
    document.write_mini(dict_especifico['crit_cdc_toxoplasmose'], (302, 285), 1)  #toxoplasmose-cerebral
    document.write_mini(dict_especifico['crit_cdc_linfocito'], (302, 299), 1)  #cont-linfocito-T-baixa

    ##############################################
    #####          RESULTADO TRATAMENTO       ####
    ##############################################
    document.write_mini(dict_especifico['criterio_obito'], (507, 328), 1)  #obito
    document.write_uf(dict_especifico['uf_tratamento'], (56, 377), 1)  #uf-tratamento
    document.write_text(dict_especifico['municipio_tratamento'], (95, 377), 1)  #municipio-tratamento
    document.write_code(dict_especifico['cod_ibge_tratamento'], (252, 377), 1, 2)  #ibge-tratamento
    document.write_text(dict_especifico['us_tratamento'], (350, 377), 1)  #instituicao-tratamento
    document.write_code(dict_especifico['cod_ibge_us_tratamento'], (467, 377), 1, 2)  #cod-instituicao-tratamento
    document.write_mini(dict_especifico['evolucao_caso'], (428, 392), 1)  #evolucao
    document.write_date(dict_especifico['dt_obito'], (452, 410), pg=1, spacing=2)  #data-obito
    document.write_text(dict_especifico['nome_investigador'], (70, 440), 1)  #nome-investigador
    document.write_text(dict_especifico['funcao_investigador'], (380, 440), 1)  #func-investigador
    document.write_text(dict_especifico['assinatura_investigador'], (70, 470), 1)  #assign-investigador

    document.save(nome_arquivo, path_pdf_gerado, notificatoriaCSV, modelo_pdf_base)
