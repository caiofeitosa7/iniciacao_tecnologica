from .pdfWritter import PDFWriter


def gerar_pdf_acid_mat_bio(notificatoriaCSV: dict, dict_especifico: dict, modelo_pdf: str, modelo_pdf_base: str, path_pdf_gerado: str, nome_arquivo: str):
    document = PDFWriter(modelo_pdf)

    ###################################################
    # Dados do paciente
    ###################################################
    document.write_text(dict_especifico['numero_ficha2'],(470, 46))
    document.write_date(dict_especifico['dt_notificacao2'], (455, 195), spacing=2) #data_notificacao
    document.write_uf(dict_especifico['uf_notificacao2'], (62, 222)) #uf_notificacao
    document.write_text(dict_especifico['municipio_notificacao2'], (100, 222)) #municipio_notificacao __unid_saude 55,space=220
    document.write_code(dict_especifico['cod_ibge_notificacao2'], (485, 222),space=2) #cod_ibge
    document.write_text(dict_especifico['unidade_saude2'], (70, 251)) #cod_unid_saude
    document.write_code(dict_especifico['cod_unidade_saude2'], (345, 251),space=2) #cod_unid_saude
    document.write_date(dict_especifico['dt_acidente'], (453, 250), spacing=2) #data_diagnostico
    ##############################################
    #####          NOTIFICACAO INDIVIDUAL     ####
    ##############################################
    document.write_text(dict_especifico['nome_paciente2'], (65, 282)) #nome
    document.write_date(dict_especifico['dt_nascimento2'], (455, 281),spacing=2) #data_nascimento
    document.write_code(dict_especifico['idade2'], (70, 311),space=2) #idade
    document.write_mini(dict_especifico['tipo_idade2'], (117, 303)) #tipo_idade
    document.write_mini(dict_especifico['sexo2'], (238, 297)) #sexo
    document.write_mini(dict_especifico['gestante2'], (433, 297)) #gestante
    document.write_mini(dict_especifico['raca2'], (559, 297)) #raça/cor
    document.write_mini(dict_especifico['escolaridade2'], (559, 326)) #escolaridade
    document.write_code(dict_especifico['numero_sus2'], (63, 371),space=2, font_size=10) #cartao_sus
    document.write_text(dict_especifico['nome_mae2'], (250, 371)) #nome_mae
    ##############################################
    #####          DADOS DE RESIDENCIA        ####
    ##############################################

    document.write_uf(dict_especifico['uf_residencia2'], (62, 400)) #uf_residencia
    document.write_text(dict_especifico['municipio_residencia2'], (100, 400)) #municipio_residencia
    document.write_code(dict_especifico['cod_ibge_residencia2'], (333, 400),space=2) #cod_ibge_residencia
    document.write_text(dict_especifico['distrito_residencia2'], (430, 400)) #endereco
    document.write_text(dict_especifico['bairro_residencia2'], (70, 425)) #bairro
    document.write_text(dict_especifico['logradouro_residencia2'], (210, 425)) #logradouro
    document.write_code(dict_especifico['codigo_residencia2'], (485, 426),space=2) #cod_logradouro
    document.write_text(dict_especifico['numero_residencia2'], (68, 449)) #numero
    document.write_text(dict_especifico['complemento_residencia2'], (120, 449)) #complemento
    document.write_text(dict_especifico['geo_campo1_2'], (420, 452)) #geo_campo_1
    document.write_text(dict_especifico['geo_campo2_2'], (65, 475)) #geo_campo_2
    document.write_text(dict_especifico['ponto_ref_residencia2'], (235, 476)) #ponto_ref
    document.write_code(dict_especifico['cep_residencia2'], (462, 478),space=2) #cep
    document.write_telefone(dict_especifico['telefone_residencia2'], (63, 502), space=2) #telefone
    document.write_mini(dict_especifico['zona_residencia2'], (340, 490)) #zona
    document.write_text(dict_especifico['pais_residencia2'], (380, 502)) #pais
    ###################################################
    # Dados complementares                            #
    ###################################################
    document.write_text(dict_especifico['ocupacao'], (70, 553)) #ocupacao
    document.write_code(dict_especifico['sit_merc_trabalho'], (241, 569),space=1) #merc_trabalho
    document.write_code(dict_especifico['tempo_trabalho'], (460, 605),space=1) #tempo_trabalho
    document.write_mini(dict_especifico['tipo_tempo_trabalho'], (507, 604)) #tempo_tipo
    document.write_code(dict_especifico['cnpj_contratante'], (62, 654),space=2, font_size=12) #cnpj_cpf
    document.write_text(dict_especifico['nome_contratante'], (255, 654)) #nome_empresa_dono
    document.write_text(dict_especifico['ativ_contratante'], (70, 680)) #CNAE
    document.write_uf(dict_especifico['uf_contratante'], (284, 682)) #uf_empresa
    document.write_text(dict_especifico['municipio_contratante'], (320, 682)) #municipio_empresa
    document.write_code(dict_especifico['cod_ibge_contratante'], (485, 682),space=2) #ibge_empresa
    document.write_text(dict_especifico['distrito_contratante'], (70, 707)) #distrito_empresa
    document.write_text(dict_especifico['bairro_contratante'], (230, 707)) #bairro_empresa
    document.write_text(dict_especifico['endereco_contratante'], (390, 707)) #endereco
    document.write_text(dict_especifico['numero_contratante'], (70, 730)) #numero
    document.write_text(dict_especifico['ponto_ref_contratante'], (130, 730)) #ponto_referencia
    document.write_telefone(dict_especifico['telefone_contratante'], (431, 732), space=2) #telefone_empresa
    document.write_mini(dict_especifico['empresa_terceirizada'], (482, 748)) #tercerizado
    ###################################################
    document.write_mini(dict_especifico['tp_exp_percutanea'], (196, 50),pg=1) #exposicao_percutanea
    document.write_mini(dict_especifico['tp_exp_mucosa'], (196, 62),pg=1) #exposicao_mucosa
    document.write_mini(dict_especifico['tp_exp_pele_integra'], (304, 49),pg=1) #exposicao_pele_integra
    document.write_mini(dict_especifico['tp_exp_pele_nao_integra'], (304, 62),pg=1) #exposicao_pele_n_integra
    document.write_mini(dict_especifico['tp_exp_outro'], (421, 48),pg=1) #exposicao_outros
    document.write_mini(dict_especifico['tp_exp_outro_descricao'], (459, 45),pg=1) #text_outras
    document.write_mini(dict_especifico['mat_organico'], (547, 85),pg=1) #mat_organico
    document.write_mini(dict_especifico['mat_organico_outro'], (380, 100),pg=1) #mat_organico_outros
    document.write_code(dict_especifico['circunst_acidente'], (539, 121),pg=1,space=1) #cirscunstancia_acid
    document.write_mini(dict_especifico['agente'], (546, 250),pg=1) #agente
    document.write_mini(dict_especifico['epi_luva'], (71, 307),pg=1) #epi_luva
    document.write_mini(dict_especifico['epi_avental'], (130, 306),pg=1) #epi_avental
    document.write_mini(dict_especifico['epi_oculos'], (198, 307),pg=1) #epi_oculos
    document.write_mini(dict_especifico['epi_mascara'], (270, 306),pg=1) #epi_mascara
    document.write_mini(dict_especifico['epi_prot_facial'], (356, 306),pg=1) #epi_protecao_facial
    document.write_mini(dict_especifico['epi_bota'], (470, 308),pg=1) #epi_bota
    document.write_mini(dict_especifico['sit_vacinal_hepB'], (271, 334),pg=1) #situacao_vacinal
    document.write_mini(dict_especifico['res_exam_anti_hiv'], (295, 356),pg=1) #res_anti_hiv
    document.write_mini(dict_especifico['res_exam_hbsag'], (354, 356),pg=1) #res_anti_hbsag
    document.write_mini(dict_especifico['res_exam_anti_hbs'], (426, 357),pg=1) #res_anti_hbs
    document.write_mini(dict_especifico['res_exam_anti_hcv'], (493, 356),pg=1) #res_anti_hcv
    document.write_mini(dict_especifico['paciente_ft_conhecida'], (284, 377),pg=1) #paciente_fonte_conhecida
    document.write_mini(dict_especifico['teste_hbsag'], (329, 397),pg=1) #res_soro_hbsag
    document.write_mini(dict_especifico['teste_anti_hiv'], (329, 413),pg=1) #res_soro_anti_hiv
    document.write_mini(dict_especifico['teste_anti_hbs'], (450, 397),pg=1) #res_soro_anti_hbc trocou o c por s
    document.write_mini(dict_especifico['teste_anti_hcv'], (451, 412),pg=1) #res_soro_anti_hcv
    document.write_mini(dict_especifico['cond_sem_indicacao'], (65, 446),pg=1) #conduta_quimioprofilaxia
    document.write_mini(dict_especifico['cond_rec_quimio'], (65, 461),pg=1) #conduta_neg_quimioprofilaxia
    document.write_mini(dict_especifico['cond_azt_3tc'], (65, 478),pg=1) #conduta_azt_3tc
    document.write_mini(dict_especifico['cond_azt_indinavir'], (241, 445),pg=1) #conduta_azt_3tc_indinavir
    document.write_mini(dict_especifico['cond_azt_nelfinavir'], (241, 466),pg=1) #conduta_azt_3tc_nelfivanir
    document.write_mini(dict_especifico['cond_imuno_hepb'], (241, 486),pg=1) #conduta_hbig
    document.write_mini(dict_especifico['cond_vac_hepb'], (394, 445),pg=1) #conduta_vacina_hep_b
    document.write_mini(dict_especifico['cond_outro_arv'], (393, 468),pg=1) #conduta_outros
    document.write_mini(dict_especifico['cond_outro_arv_descricao'], (449, 470),pg=1) #conduta_text
    document.write_mini(dict_especifico['evolucao_caso'], (552, 505),pg=1) #evolucao_caso
    document.write_mini(dict_especifico['conversao_sorologica'], (248, 519),pg=1) #virus_espec
    document.write_date(dict_especifico['dt_obito'], (66, 573),pg=1, spacing=2) #dt_obito
    document.write_mini(dict_especifico['comun_acid_trab'], (548, 560),pg=1) #emitido_comun_trab
    document.write_box(dict_especifico['outras_informacoes'],pg=1, rect=(30, 600, 560, 740)) #obs
    document.write_text(dict_especifico['municipio_us_investigador'], (59, 765),pg=1) #municipio_investigador
    document.write_code(dict_especifico['cod_us_investigador'], (464, 764),pg=1,space=2) #cod_unid_saude
    document.write_text(dict_especifico['nome_investigador'], (59, 792),pg=1) #nome_investigador
    document.write_text(dict_especifico['funcao_investigador'], (260, 792),pg=1) #funcao_investigador
    document.write_text(dict_especifico['assinatura_investigador'], (470, 792),pg=1) #asign_investigador

    document.save(nome_arquivo, path_pdf_gerado, notificatoriaCSV, modelo_pdf_base)