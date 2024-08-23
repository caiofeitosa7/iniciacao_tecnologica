from .pdfWritter import PDFWriter


def gerar_pdf_dengue_chik(notificatoriaCSV: dict, dict_especifico: dict, modelo_pdf: str, modelo_pdf_base: str, path_pdf_gerado: str, nome_arquivo: str):
    document = PDFWriter(modelo_pdf)

    ###################################################
    # Dados do paciente
    ###################################################
    document.write_text(dict_especifico['numero_ficha2'],(470, 48))
    document.write_date(dict_especifico['dt_notificacao2'], (449, 191), spacing=2) #data_notificacao
    document.write_uf(dict_especifico['uf_notificacao2'], (59, 220)) #uf_notificacao
    document.write_text(dict_especifico['municipio_notificacao2'], (90, 220)) #municipio_notificacao __unid_saude 55,space=220
    document.write_code(dict_especifico['cod_ibge_notificacao2'], (480, 220),space=2) #cod_ibge
    document.write_text(dict_especifico['unidade_saude2'], (65, 248)) #cod_unid_saude
    document.write_code(dict_especifico['cod_unidade_saude2'], (340, 248),space=2) #cod_unid_saude
    document.write_date(dict_especifico['dt_sintomas2'], (447, 248), spacing=2) #data_diagnostico
    ##############################################
    #####          NOTIFICACAO INDIVIDUAL     ####
    ##############################################
    document.write_text(dict_especifico['nome_paciente2'], (60, 279)) #nome
    document.write_date(dict_especifico['dt_nascimento2'], (446, 279), spacing=2) #data_nascimento
    document.write_code(dict_especifico['idade2'], (63, 308),space=2) #idade
    document.write_mini(dict_especifico['tipo_idade2'], (109, 301)) #tipo_idade
    document.write_mini(dict_especifico['sexo2'], (230, 294)) #sexo
    document.write_mini(dict_especifico['gestante2'], (426, 294)) #gestante
    document.write_mini(dict_especifico['raca2'], (551, 294)) #raça/cor
    document.write_mini(dict_especifico['escolaridade2'], (552, 324)) #escolaridade
    document.write_code(dict_especifico['numero_sus2'], (57, 369),space=2, font_size=10) #cartao_sus
    document.write_text(dict_especifico['nome_mae2'], (240, 368)) #nome_mae
    ##############################################
    #####          DADOS DE RESIDENCIA        ####
    ##############################################

    document.write_uf(dict_especifico['uf_residencia2'], (56, 398)) #uf_residencia
    document.write_text(dict_especifico['municipio_residencia2'], (95, 398)) #municipio_residencia
    document.write_code(dict_especifico['cod_ibge_residencia2'], (325, 398),space=2) #cod_ibge_residencia
    document.write_text(dict_especifico['distrito_residencia2'], (422, 398)) #endereco
    document.write_text(dict_especifico['bairro_residencia2'], (64, 423)) #bairro
    document.write_text(dict_especifico['logradouro_residencia2'], (207, 424)) #logradouro
    document.write_code(dict_especifico['codigo_residencia2'], (478, 424),space=2) #cod_logradouro
    document.write_text(dict_especifico['numero_residencia2'], (65, 447)) #numero
    document.write_text(dict_especifico['complemento_residencia2'], (120, 447)) #complemento
    document.write_text(dict_especifico['geo_campo1_2'], (415, 450)) #geo_campo_1
    document.write_text(dict_especifico['geo_campo2_2'], (55, 473)) #geo_campo_2
    document.write_text(dict_especifico['ponto_ref_residencia2'], (230, 474)) #ponto_ref
    document.write_code(dict_especifico['cep_residencia2'], (454, 477),space=2) #cep
    document.write_telefone(dict_especifico['telefone_residencia2'], (57, 500), space=2) #telefone
    document.write_mini(dict_especifico['zona_residencia2'], (335, 488)) #zona
    document.write_text(dict_especifico['pais_residencia2'], (380, 499)) #pais
    ####################################################
    # Dados Complementares
    ####################################################
    document.write_date(dict_especifico['dt_investigacao'], (63, 548), spacing=2) #data_investigacao
    document.write_text(dict_especifico['ocupacao'], (195, 548)) #ocupacao
    document.write_mini(dict_especifico['sinal_febre'], (58, 580)) #sinal_febre
    document.write_mini(dict_especifico['sinal_mialgia'], (58, 595)) #sinal_mialgia
    document.write_mini(dict_especifico['sinal_cefaleia'], (105, 580)) #sinal_cefaleia
    document.write_mini(dict_especifico['sinal_exantema'], (105, 595)) #sinal_exantema
    document.write_mini(dict_especifico['sinal_vomito'], (162, 580)) #sinal_vomito
    document.write_mini(dict_especifico['sinal_nausea'], (162, 595)) #sinal_nausea
    document.write_mini(dict_especifico['sinal_dor_costas'], (219, 581)) #sinal_dor_costas
    document.write_mini(dict_especifico['sinal_conjuntivite'], (219, 596)) #sinal_conjuntivite
    document.write_mini(dict_especifico['sinal_artrite'], (302, 579)) #sinal_artrite
    document.write_mini(dict_especifico['sinal_artralgia'], (302, 594)) #sinal_artralgia
    document.write_mini(dict_especifico['sinal_petequias'], (390, 577)) #sinal_petequias
    document.write_mini(dict_especifico['sinal_leucopenia'], (390, 592)) #sinal_leucopenia
    document.write_mini(dict_especifico['sinal_prova_laco'], (474, 577)) #sinal_prova_laco
    document.write_mini(dict_especifico['sinal_dor_retroorbital'], (474, 595)) #sinal_dor_retroorbital
    document.write_mini(dict_especifico['doenca_diabete'], (58, 632)) #doenca_diabete
    document.write_mini(dict_especifico['doenca_hemato'], (58, 648)) #doenca_hemato
    document.write_mini(dict_especifico['doenca_hepato'], (193, 630)) #doenca_hepato
    document.write_mini(dict_especifico['doenca_renal'], (193, 645)) #doenca_renal
    document.write_mini(dict_especifico['doenca_hipertensao'], (314, 630)) #doenca_hipertensao
    document.write_mini(dict_especifico['doenca_peptica'], (314, 645)) #doenca_peptica
    document.write_mini(dict_especifico['doenca_auto_imune'], (428, 629)) #doenca_auto_imune
    document.write_date(dict_especifico['dt_coleta_s1_ck'], (58, 697), spacing=2) #data_coleta_ck
    document.write_date(dict_especifico['dt_coleta_s2_ck'], (184, 697), spacing=2) #data_coleta_ck
    document.write_date(dict_especifico['dt_coleta_prnt'], (310, 697), spacing=2) #data_coleta_prnt
    document.write_mini(dict_especifico['resultado_s1_ck'], (464, 676)) #resultado_ck
    document.write_mini(dict_especifico['resultado_s2_ck'], (498, 676)) #resultado_ck
    document.write_mini(dict_especifico['resultado_prnt'], (538, 677)) #resultado_prnt
    document.write_date(dict_especifico['dt_coleta_dengue'], (65, 742), spacing=2) #data_coleta_dengue
    document.write_mini(dict_especifico['resultado_dengue'], (296, 722)) #resultado_dengue
    document.write_date(dict_especifico['dt_coleta_ns1'], (326, 742), spacing=2) #data_coleta_ns1
    document.write_mini(dict_especifico['resultado_ns1'], (550, 720)) #resultado_ns1
    document.write_date(dict_especifico['dt_isol_dengue'], (57, 776), spacing=2) #data_isolamento
    document.write_mini(dict_especifico['resultado_isol_dengue'], (285, 758)) #resultado_isolamento
    document.write_date(dict_especifico['dt_coleta_pcr'], (328, 777), spacing=2) #data_coleta_pcr
    document.write_mini(dict_especifico['resultado_pcr'], (551, 755)) #resultado_pcr
    document.write_mini(dict_especifico['sorotipo'], (150, 790)) #sorotipo
    document.write_mini(dict_especifico['histopatologia'], (285, 792)) #histopatologia
    document.write_mini(dict_especifico['imunohistoq'], (431, 791)) #imunohistoq

    #################################################### fim page

    document.write_mini(dict_especifico['hospitalizacao2'], (167, 57), pg=1) #hospitalizacao
    document.write_date(dict_especifico['dt_internacao'], (193, 59), pg=1, spacing=2) #data_internacao
    document.write_uf(dict_especifico['uf_hospital2'], (315, 59), pg=1) #uf_hospital
    document.write_text(dict_especifico['municipio_hospital2'], (354, 59), pg=1) #municipio_hospital
    document.write_code(dict_especifico['cod_ibge_hospital2'], (483, 59), pg=1,space=2) #cod_ibge_hospital
    document.write_text(dict_especifico['nome_hospital2'], (66, 93), pg=1) #nome_hospital
    document.write_code(dict_especifico['cod_hospital2'], (332, 93), pg=1,space=2) #cod_hospital
    document.write_telefone(dict_especifico['telefone_hospital2'], (436, 93), pg=1, space=2, font_size=12) #telefone_hospital
    document.write_mini(dict_especifico['caso_autoctone'], (301, 130), pg=1) #caso_autoctone
    document.write_uf(dict_especifico['uf_infeccao2'], (343, 135), pg=1) #uf_infeccao
    document.write_text(dict_especifico['pais_infeccao2'], (385, 135), pg=1) #pais_infeccao
    document.write_text(dict_especifico['municipio_infeccao2'], (66, 162), pg=1) #municipio_infeccao
    document.write_code(dict_especifico['cod_ibge_infeccao2'], (204, 162), pg=1,space=2) #cod_ibge_infeccao
    document.write_text(dict_especifico['distrito_infeccao2'], (303, 162), pg=1) #distrito_infeccao
    document.write_text(dict_especifico['bairro_infeccao2'], (440, 162), pg=1) #bairro_infeccao
    document.write_mini(dict_especifico['classif_caso'], (278, 182), pg=1) #classif_caso
    document.write_mini(dict_especifico['criterio_confirm'], (428, 184), pg=1) #criterio_confirm
    document.write_mini(dict_especifico['apresentacao_clinica'], (472, 194), pg=1) #apresentacao_clinica
    document.write_mini(dict_especifico['evolucao_caso'], (166, 221), pg=1) #evolucao_caso
    document.write_date(dict_especifico['dt_obito'], (313, 243), pg=1, spacing=2) #data_obito
    document.write_date(dict_especifico['dt_encerramento'], (448, 244), pg=1, spacing=2) #data_encerramento
    document.write_mini(dict_especifico['alarme_hipotensao'], (58, 304), pg=1) #alarme_hipotensao
    document.write_mini(dict_especifico['alarme_plaqueta'], (58, 319), pg=1) #alarme_plaqueta
    document.write_mini(dict_especifico['alarme_vomito'], (215, 275), pg=1) #alarme_vomito
    document.write_mini(dict_especifico['alarme_abdomem'], (214, 290), pg=1) #alarme_abdomem
    document.write_mini(dict_especifico['alarme_letargia'], (213, 307), pg=1) #alarme_letargia
    document.write_mini(dict_especifico['alarme_sangramento'], (213, 322), pg=1) #alarme_sangramento
    document.write_mini(dict_especifico['alarme_hematocito'], (346, 276), pg=1) #alarme_hematocito
    document.write_mini(dict_especifico['alarme_hepatomeglagia'], (346, 294), pg=1) #alarme_hepatomeglagia
    document.write_mini(dict_especifico['alarme_liquido'], (346, 310), pg=1) #alarme_liquido
    document.write_date(dict_especifico['dt_sinal_alarme'], (458, 323), pg=1, spacing=2) #data_sinal_alarme
    document.write_mini(dict_especifico['deng_grav_pulso'], (60, 372), pg=1) #deng_grav_pulso
    document.write_mini(dict_especifico['deng_grav_pa_conv'], (60, 389), pg=1) #deng_grav_pa_conv
    document.write_mini(dict_especifico['deng_grav_capilar'], (60, 405), pg=1) #deng_grav_capilar
    document.write_mini(dict_especifico['deng_grav_liquido'], (60, 420), pg=1) #deng_grav_liquido
    document.write_mini(dict_especifico['deng_grav_taqui'], (204, 374), pg=1) #deng_grav_taqui
    document.write_mini(dict_especifico['deng_grav_extrem'], (204, 389), pg=1) #deng_grav_extrem
    document.write_mini(dict_especifico['deng_grav_hipo'], (204, 405), pg=1) #deng_grav_hipo
    document.write_mini(dict_especifico['deng_grav_hemat'], (335, 358), pg=1) #deng_grav_hemat
    document.write_mini(dict_especifico['deng_grav_melena'], (335, 374), pg=1) #deng_grav_melena
    document.write_mini(dict_especifico['deng_grav_metror'], (429, 356), pg=1) #deng_grav_metror
    document.write_mini(dict_especifico['deng_grav_snc'], (429, 374), pg=1) #deng_grav_snc
    document.write_mini(dict_especifico['deng_grav_ast'], (333, 408), pg=1) #deng_grav_ast
    document.write_mini(dict_especifico['deng_grave_miocardite'], (428, 406), pg=1) #deng_grave_miocardite
    document.write_mini(dict_especifico['deng_grav_consc'], (488, 406), pg=1) #deng_grav_consc
    document.write_mini(dict_especifico['deng_grav_outro'], (334, 426), pg=1) #deng_grav_outro
    document.write_mini(dict_especifico['deng_grav_outro_descricao'], (458, 426), pg=1) #deng_grav_outro_descricao
    document.write_date(dict_especifico['dt_sinal_gravidade'], (58, 469), pg=1, spacing=2) #data_sinal_gravidade
    document.write_box(dict_especifico['obs_adicionais'],pg=1, rect=(30,520,566,750)) #obs_adicionais
    document.write_text(dict_especifico['municipio_us_investigador'], (60, 759), pg=1) #municipio_us_investigador
    document.write_code(dict_especifico['cod_us_investigador'], (463, 758), pg=1,space=2) #cod_us_investigador
    document.write_text(dict_especifico['nome_investigador'], (60, 789), pg=1) #nome_investigador
    document.write_text(dict_especifico['funcao_investigador'], (257, 789), pg=1) #funcao_investigador
    document.write_text(dict_especifico['assinatura_investigador'], (468, 789), pg=1) #assinatura_investigador

    document.save(nome_arquivo, path_pdf_gerado, notificatoriaCSV, modelo_pdf_base)