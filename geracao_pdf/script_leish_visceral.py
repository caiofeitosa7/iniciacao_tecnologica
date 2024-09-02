from .pdfWritter import PDFWriter


def gerar_pdf_leish_visceral(notificatoriaCSV: dict, dict_especifico: dict, modelo_pdf: str, modelo_pdf_base: str, path_pdf_gerado: str, nome_arquivo: str):
    document = PDFWriter(modelo_pdf)

    ###################################################
    # Dados do paciente
    ###################################################
    document.write_text(dict_especifico['numero_ficha2'],(470, 44))
    document.write_date(dict_especifico['dt_notificacao2'], (453, 155), spacing=2) #data_notificacao
    document.write_uf(dict_especifico['uf_notificacao2'], (60, 185)) #uf_notificacao
    document.write_text(dict_especifico['municipio_notificacao2'], (100, 185)) #municipio_notificacao __unid_saude 55,space=220
    document.write_code(dict_especifico['cod_ibge_notificacao2'], (484, 186),space=2) #cod_ibge
    document.write_text(dict_especifico['unidade_saude2'], (70, 214)) #cod_unid_saude
    document.write_code(dict_especifico['cod_unidade_saude2'], (344, 214),space=2) #cod_unid_saude
    document.write_date(dict_especifico['dt_sintomas2'], (452, 213), spacing=2) #data_diagnostico
    ##############################################
    #####          NOTIFICACAO INDIVIDUAL     ####
    ##############################################
    document.write_text(dict_especifico['nome_paciente2'], (65, 245)) #nome
    document.write_date(dict_especifico['dt_nascimento2'], (455, 244), spacing=2) #data_nascimento
    document.write_code(dict_especifico['idade2'], (70, 274),space=2) #idade
    document.write_mini(dict_especifico['tipo_idade2'], (117, 267)) #tipo_idade
    document.write_mini(dict_especifico['sexo2'], (239, 260)) #sexo
    document.write_mini(dict_especifico['gestante2'], (434, 260)) #gestante
    document.write_mini(dict_especifico['raca2'], (560, 261)) #raça/cor
    document.write_mini(dict_especifico['escolaridade2'], (560, 290)) #escolaridade
    document.write_code(dict_especifico['numero_sus2'], (64, 334),space=2, font_size=10) #cartao_sus
    document.write_text(dict_especifico['nome_mae2'], (250, 334)) #nome_mae
    ##############################################
    #####          DADOS DE RESIDENCIA        ####
    ##############################################

    document.write_uf(dict_especifico['uf_residencia2'], (62, 365)) #uf_residencia
    document.write_text(dict_especifico['municipio_residencia2'], (100, 365)) #municipio_residencia
    document.write_code(dict_especifico['cod_ibge_residencia2'], (333, 366),space=2) #cod_ibge_residencia
    document.write_text(dict_especifico['distrito_residencia2'], (430, 365)) #endereco
    document.write_text(dict_especifico['bairro_residencia2'], (70, 390)) #bairro
    document.write_text(dict_especifico['logradouro_residencia2'], (210, 392)) #logradouro
    document.write_code(dict_especifico['codigo_residencia2'], (487, 392),space=2) #cod_logradouro
    document.write_text(dict_especifico['numero_residencia2'], (68, 415)) #numero
    document.write_text(dict_especifico['complemento_residencia2'], (120, 415)) #complemento
    document.write_text(dict_especifico['geo_campo1_2'], (420, 417)) #geo_campo_1
    document.write_text(dict_especifico['geo_campo2_2'], (63, 440)) #geo_campo_2
    document.write_text(dict_especifico['ponto_ref_residencia2'], (235, 440)) #ponto_ref
    document.write_code(dict_especifico['cep_residencia2'], (462, 443),space=2) #cep
    document.write_telefone(dict_especifico['telefone_residencia2'], (62, 467), space=2) #telefone
    document.write_mini(dict_especifico['zona_residencia2'], (340, 455)) #zona
    document.write_text(dict_especifico['pais_residencia2'], (380, 466)) #pais
    ###################################################
    # Dados Complementares _ Ficha de Investigação    #
    ###################################################

    document.write_date(dict_especifico['dt_investigacao'], (68, 520), spacing=2) #data_investigacao
    document.write_text(dict_especifico['ocupacao'], (190, 520)) #ocupacao
    document.write_mini(dict_especifico['sintoma_febre'], (98, 552)) #febre
    document.write_mini(dict_especifico['sintoma_fraqueza'], (98, 565)) #fraqueza
    document.write_mini(dict_especifico['sintoma_edema'], (98, 579)) #edema
    document.write_mini(dict_especifico['sintoma_emagrecimento'], (180, 553)) #emagrecimento
    document.write_mini(dict_especifico['sintoma_tosse'], (180, 566)) #tosse_diarreia
    document.write_mini(dict_especifico['sintoma_palidez'], (181, 579)) #palidez
    document.write_mini(dict_especifico['sintoma_baco'], (278, 553)) #baco
    document.write_mini(dict_especifico['sintoma_quadro_infec'], (278, 567)) #infeccioso
    document.write_mini(dict_especifico['sintoma_hemorragia'], (278, 580)) #fen_hemorragico
    document.write_mini(dict_especifico['sintoma_figado'], (416, 553)) #aumento_figado
    document.write_mini(dict_especifico['sintoma_icteria'], (417, 566)) #ictericia
    document.write_text(dict_especifico['sintoma_outro'], (416, 581)) #outros
    document.write_mini(dict_especifico['sintoma_outro_descricao'], (454, 577)) #outros_text
    document.write_mini(dict_especifico['co_infec_hiv'], (536, 608)) #co_infec_hiv
    document.write_mini(dict_especifico['diag_parasitologica'], (217, 653)) #diag_parasitologico
    document.write_mini(dict_especifico['diag_imuno_ifi'], (362, 661)) #diag_imunologico
    document.write_mini(dict_especifico['diag_imuno_outro'], (362, 678)) #diag_imuno_outro
    document.write_mini(dict_especifico['tipo_entrada'], (548, 649)) #tipo_entrada
    document.write_date(dict_especifico['dt_inicio_trat'], (68, 717), spacing=2) #data_tratamento
    document.write_mini(dict_especifico['droga_inicial_adm'], (554, 698)) #drug_administrada
    document.write_code(dict_especifico['peso'], (98, 749),space=1) #peso
    document.write_mini(dict_especifico['dose_prescrita'], (398, 733)) #dose_presc
    document.write_code(dict_especifico['quant_ampolas'], (452, 758),space=1) #total_ampola
    document.write_mini(dict_especifico['droga_falencia_trat'], (542, 777)) #outra_droga

    ################################################### fim page

    document.write_mini(dict_especifico['classif_final'], (299, 50),pg=1) #class_final
    document.write_mini(dict_especifico['criterio_confirm'], (545, 46),pg=1) #crit_confirmacao
    document.write_mini(dict_especifico['caso_autoctone'], (306, 103),pg=1) #autoctone
    document.write_uf(dict_especifico['uf_conclusao'], (350, 113),pg=1) #uf
    document.write_text(dict_especifico['pais_conclusao'], (400, 113),pg=1) #pais
    document.write_text(dict_especifico['municipio_conclusao'], (70, 144),pg=1) #municipio
    document.write_code(dict_especifico['cod_ibge_conclusao'], (211, 144),pg=1,space=2) #ibge
    document.write_text(dict_especifico['distrito_conclusao'], (310, 143),pg=1) #distrito
    document.write_text(dict_especifico['bairro_conclusao'], (450, 143),pg=1) #bairro
    document.write_mini(dict_especifico['doenca_rel_trab'], (283, 160),pg=1) #doenca_rel_trabalho
    document.write_mini(dict_especifico['evolucao_caso'], (550, 160),pg=1) #evolucao_caso
    document.write_date(dict_especifico['dt_obito'], (62, 210),pg=1, spacing=2) #data_obito
    document.write_date(dict_especifico['dt_encerramento'], (188, 210),pg=1, spacing=2) #data_encerramento
    document.write_text(dict_especifico['dt_desloc1'], (36, 281),pg=1) #data_1_obs
    document.write_text(dict_especifico['dt_desloc2'], (36, 294),pg=1) #data_2_obs
    document.write_text(dict_especifico['dt_desloc3'], (36, 306),pg=1) #data_3_obs
    document.write_uf(dict_especifico['uf_desloc1'], (120, 281),pg=1) #uf_1_obs
    document.write_uf(dict_especifico['uf_desloc2'], (120, 294),pg=1) #uf_2_obs
    document.write_uf(dict_especifico['uf_desloc3'], (120, 306),pg=1) #uf_3_obs
    document.write_text(dict_especifico['municipio_desloc1'], (160, 281),pg=1) #municipio_1_obs
    document.write_text(dict_especifico['municipio_desloc2'], (160, 294),pg=1) #municipio_2_obs
    document.write_text(dict_especifico['municipio_desloc3'], (160, 306),pg=1) #municipio_3_obs
    document.write_text(dict_especifico['pais_desloc1'], (340, 281),pg=1) #pais_1_obs
    document.write_text(dict_especifico['pais_desloc2'], (340, 294),pg=1) #pais_2_obs
    document.write_text(dict_especifico['pais_desloc3'], (340, 306),pg=1) #pais_3_obs
    document.write_text(dict_especifico['transporte_desloc1'], (460, 281),pg=1) #meio_1_transporte
    document.write_text(dict_especifico['transporte_desloc2'], (460, 294),pg=1) #meio_2_transporte
    document.write_text(dict_especifico['transporte_desloc3'], (460, 306),pg=1) #meio_3_transporte
    document.write_box(dict_especifico['obs_adicionais'], pg=1, rect=(35,349, 570, 660)) #text_obs
    document.write_text(dict_especifico['municipio_us_investigador'], (65, 695),pg=1) #municipio_unid_saude
    document.write_code(dict_especifico['cod_us_investigador'], (466, 695),pg=1,space=2) #cod_municipio_un
    document.write_text(dict_especifico['nome_investigador'], (65, 723),pg=1) #investigador
    document.write_text(dict_especifico['funcao_investigador'], (265, 723),pg=1) #funcao
    document.write_text(dict_especifico['assinatura_investigador'], (470, 723),pg=1) #assinatura_investigador

    document.save(nome_arquivo, path_pdf_gerado, notificatoriaCSV, modelo_pdf_base)