from .pdfWritter import PDFWriter


def gerar_pdf_intox_exog(notificatoriaCSV: dict, dict_especifico: dict, modelo_pdf: str, modelo_pdf_base: str, path_pdf_gerado: str, nome_arquivo: str):
    document = PDFWriter(modelo_pdf)

    ###################################################
    # Dados do paciente
    ###################################################
    document.write_text(dict_especifico['numero_ficha2'],(475, 49))
    document.write_date(dict_especifico['dt_notificacao2'], (448, 158), spacing=2) #data_notificacao
    document.write_uf(dict_especifico['uf_notificacao2'], (55, 187)) #uf_notificacao
    document.write_text(dict_especifico['municipio_notificacao2'], (90, 187)) #municipio_notificacao __unid_saude 55,space=220
    document.write_code(dict_especifico['cod_ibge_notificacao2'], (477, 187),space=2) #cod_ibge
    document.write_text(dict_especifico['unidade_saude2'], (70, 216)) #cod_unid_saude
    document.write_code(dict_especifico['cod_unidade_saude2'], (338, 216),space=2) #cod_unid_saude
    document.write_date(dict_especifico['dt_sintomas2'], (446, 215), spacing=2) #data_diagnostico
    ##############################################
    #####          NOTIFICACAO INDIVIDUAL     ####
    ##############################################
    document.write_text(dict_especifico['nome_paciente2'], (55, 247)) #nome
    document.write_date(dict_especifico['dt_nascimento2'], (448, 247), spacing=2) #data_nascimento
    document.write_code(dict_especifico['idade2'], (65, 276),space=2) #idade
    document.write_mini(dict_especifico['tipo_idade2'], (112, 269)) #tipo_idade
    document.write_mini(dict_especifico['sexo2'], (233, 261)) #sexo
    document.write_mini(dict_especifico['gestante2'], (429, 261)) #gestante
    document.write_mini(dict_especifico['raca2'], (555, 262)) #raça/cor
    document.write_mini(dict_especifico['escolaridade2'], (555, 291)) #escolaridade
    document.write_code(dict_especifico['numero_sus2'], (57, 337),space=2, font_size=10) #cartao_sus
    document.write_text(dict_especifico['nome_mae2'], (240, 337)) #nome_mae
    ##############################################
    #####          DADOS DE RESIDENCIA        ####
    ##############################################

    document.write_uf(dict_especifico['uf_residencia2'], (56, 366)) #uf_residencia
    document.write_text(dict_especifico['municipio_residencia2'], (95, 366)) #municipio_residencia
    document.write_code(dict_especifico['cod_ibge_residencia2'], (325, 366),space=2) #cod_ibge_residencia
    document.write_text(dict_especifico['distrito_residencia2'], (424, 366)) #endereco
    document.write_text(dict_especifico['bairro_residencia2'], (64, 390)) #bairro
    document.write_text(dict_especifico['logradouro_residencia2'], (210, 392)) #logradouro
    document.write_code(dict_especifico['codigo_residencia2'], (480, 392),space=2) #cod_logradouro
    document.write_text(dict_especifico['numero_residencia2'], (65, 415)) #numero
    document.write_text(dict_especifico['complemento_residencia2'], (120, 415)) #complemento
    document.write_text(dict_especifico['geo_campo1_2'], (415, 418)) #geo_campo_1
    document.write_text(dict_especifico['geo_campo2_2'], (55, 440)) #geo_campo_2
    document.write_text(dict_especifico['ponto_ref_residencia2'], (230, 442)) #ponto_ref
    document.write_code(dict_especifico['cep_residencia2'], (457, 444),space=2) #cep
    document.write_telefone(dict_especifico['telefone_residencia2'], (57, 468), space=2) #telefone
    document.write_mini(dict_especifico['zona_residencia2'], (335, 455)) #zona
    document.write_text(dict_especifico['pais_residencia2'], (380, 466)) #pais
    ##############################################
    #####        DADOS  COMPLEMENTARES        ####
    ##############################################
    document.write_date(dict_especifico['dt_investigacao'], (60, 523), spacing=2) #data_investigacao
    document.write_text(dict_especifico['ocupacao'], (200, 524)) #ocupacao
    document.write_code(dict_especifico['sit_merc_trabalho'], (533, 543),space=1) #sit_mercado_tr
    document.write_mini(dict_especifico['sit_merc_trabalho_outro'], (470, 574)) #sit_mercado_tr_outros
    document.write_mini(dict_especifico['loc_exposicao'], (542, 604)) #loc_exposicao
    document.write_mini(dict_especifico['loc_exposicao_outro'], (350, 620)) #loc_exposicao_outros
    ##############################################
    #####        DADOS  EXPOSICAO             ####
    ##############################################
    document.write_text(dict_especifico['nome_estab_ocorr'], (55, 650)) #local
    document.write_text(dict_especifico['atv_econ_estab_ocorr'], (410, 650)) #cnae
    document.write_uf(dict_especifico['uf_estab_ocorr'], (57, 677)) #uf
    document.write_text(dict_especifico['municipio_estab_ocorr'], (100, 676)) #municipio
    document.write_code(dict_especifico['cod_ibge_estab_ocorr'], (313, 676),space=2) #ibge
    document.write_text(dict_especifico['distrito_estab_ocorr'], (420, 676)) #distrito
    document.write_text(dict_especifico['bairro_estab_ocorr'], (55, 705)) #bairro
    document.write_text(dict_especifico['lograd_estab_ocorr'], (222, 705)) #logradouro
    document.write_text(dict_especifico['numero_estab_ocorr'], (62, 730)) #numero
    document.write_text(dict_especifico['complem_estab_ocorr'], (120, 730)) #complemento
    document.write_text(dict_especifico['pt_ref_estab_ocorr'], (283, 728)) #ponto_ref
    document.write_code(dict_especifico['cep_estab_ocorr'], (456, 729),space=2) #cep
    document.write_telefone(dict_especifico['telefone_estab_ocorr'], (57, 758), space=2) #telefone
    document.write_mini(dict_especifico['zona_estab_ocorr'], (330, 745)) #zona
    document.write_text(dict_especifico['pais_estab_ocorr'], (380, 758)) #pais
    document.write_code(dict_especifico['agente_toxico'], (532, 42),pg=1, space=1) #gp_agente_toxic
    document.write_mini(dict_especifico['agente_toxico_outro'], (240, 84),pg=1) #gp_agente_toxico_outros
    document.write_text(dict_especifico['nome_agente_tox1'], (83, 122),pg=1) #agente_toxico_1
    document.write_text(dict_especifico['nome_agente_tox2'], (83, 141),pg=1) #agente_toxico_2
    document.write_text(dict_especifico['nome_agente_tox3'], (83, 159),pg=1) #agente_toxico_3
    document.write_text(dict_especifico['princ_agente_tox1'], (350, 124),pg=1) #principio_ativo_1
    document.write_text(dict_especifico['princ_agente_tox2'], (350, 142),pg=1) #principio_ativo_2
    document.write_text(dict_especifico['princ_agente_tox3'], (350, 160),pg=1) #principio_ativo_3
    document.write_mini(dict_especifico['finalid_agrotox'], (535, 179),pg=1) #agrotoxico_fin
    document.write_mini(dict_especifico['finalid_agrotox_outro'], (235, 196),pg=1) #agrotoxico_fin_outros
    document.write_code(dict_especifico['atv_agrotox1'], (486, 219),pg=1, space=1) #agrotoxico_ativ_1
    document.write_code(dict_especifico['atv_agrotox2'], (486, 234),pg=1, space=1) #agrotoxico_ativ_2
    document.write_code(dict_especifico['atv_agrotox3'], (486, 249),pg=1, space=1) #agrotoxico_ativ_3
    document.write_text(dict_especifico['lavoura'], (80, 285),pg=1) #agrotoxico_cult
    document.write_mini(dict_especifico['via_exp1'], (488, 306),pg=1) #via_exposicao_1
    document.write_mini(dict_especifico['via_exp2'], (488, 320),pg=1) #via_exposicao_2
    document.write_mini(dict_especifico['via_exp3'], (488, 336),pg=1) #via_exposicao_3
    document.write_code(dict_especifico['circ_exp'], (233, 360),pg=1,space=1) #circunstancia_cont
    document.write_mini(dict_especifico['circ_exp_outro'], (295, 390),pg=1) #circunstancia_outros
    document.write_mini(dict_especifico['exp_decor_trab'], (285, 420),pg=1) #decorrente_trab
    document.write_mini(dict_especifico['tipo_exposicao'], (538, 422),pg=1) #tipo_exposicao
    ##############################################
    #####        DADOS  ATENDIMENTO           ####
    ##############################################

    document.write_code(dict_especifico['tempo_exp_atend'], (170, 465),pg=1,space=1) #tempo_expo_atend
    document.write_mini(dict_especifico['tipo_tempo_exp_atend'], (228, 462),pg=1) #tempo_expo_atend_un
    document.write_mini(dict_especifico['tipo_atendimento'], (247, 487),pg=1) #tipo_atendimento
    document.write_mini(dict_especifico['hospitalizacao2'], (390, 488),pg=1) #hospitalizacao
    document.write_date(dict_especifico['dt_internacao'], (418, 511),pg=1, spacing=2) #dt_internacao
    document.write_uf(dict_especifico['uf_hospital2'], (537, 510),pg=1) #uf_internacao
    document.write_text(dict_especifico['municipio_hospital2'], (65, 542),pg=1) #municipio_internacao
    document.write_code(dict_especifico['cod_ibge_hospital2'], (225, 542),pg=1,space=2) #ibge_internacao
    document.write_text(dict_especifico['nome_hospital2'], (330, 542),pg=1) #instituicao_internacao
    document.write_code(dict_especifico['cod_hospital2'], (465, 542),pg=1,space=2) #cod_instituicao_internacao
    ##############################################
    #####        CONCLUSAO                    ####
    ##############################################
    document.write_mini(dict_especifico['classif_final'], (545, 568),pg=1) #class_final
    document.write_text(dict_especifico['diag_intox_conf'], (70, 600),pg=1) #diagnostico
    document.write_code(dict_especifico['cid_intox_conf'], (490, 602),pg=1,space=2) #cid_10
    document.write_mini(dict_especifico['criterio_confirm'], (205, 617),pg=1) #crit_confirmacao
    document.write_mini(dict_especifico['evolucao_caso'], (544, 617),pg=1) #evolucao
    document.write_date(dict_especifico['dt_obito'], (63, 665),pg=1, spacing=2) #dt_obito
    document.write_mini(dict_especifico['comun_acid_trab'], (428, 653),pg=1) #cat
    document.write_date(dict_especifico['dt_encerramento'], (458, 665),pg=1, spacing=2) #dt_encerramento
    document.write_box(dict_especifico['obs_adicionais'], pg=1, rect=(35,705, 565, 750)) #obs
    document.write_text(dict_especifico['municipio_us_investigador'], (65, 778),pg=1) #municipio_unid_saude
    document.write_code(dict_especifico['cod_us_investigador'], (468, 780),pg=1, space=2) #cod_unidade_saude
    document.write_text(dict_especifico['nome_investigador'], (70, 810),pg=1) #nome_investigador
    document.write_text(dict_especifico['funcao_investigador'], (280, 810),pg=1) #func_investigador
    document.write_text(dict_especifico['assinatura_investigador'], (470, 810),pg=1) #assign_investigador

    document.save(nome_arquivo, path_pdf_gerado, notificatoriaCSV, modelo_pdf_base)