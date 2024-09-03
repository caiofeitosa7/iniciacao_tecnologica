from .pdfWritter import PDFWriter


def gerar_pdf_paralisia_flacida(notificatoriaCSV: dict, dict_especifico: dict, modelo_pdf: str, modelo_pdf_base: str, path_pdf_gerado: str, nome_arquivo: str):
    document = PDFWriter(modelo_pdf)

    ###################################################
    # Dados do paciente
    ###################################################

    document.write_text(dict_especifico['numero_ficha2'], (467, 45))
    document.write_date(dict_especifico['dt_notificacao2'], (446, 158), spacing=2)  # data_notificacao
    document.write_uf(dict_especifico['uf_notificacao2'], (55, 189))  # uf_notificacao
    document.write_text(dict_especifico['municipio_notificacao2'], (90, 188))  # municipio_notificacao __unid_saude 55,220
    document.write_code(dict_especifico['cod_ibge_notificacao2'], (479, 189), space=2)  # cod_ibge
    document.write_text(dict_especifico['unidade_saude2'], (65, 217))  # cod_unid_saude
    document.write_code(dict_especifico['cod_unidade_saude2'], (339, 218), space=2)  # cod_unid_saude
    document.write_date(dict_especifico['dt_sintomas2'], (446, 217), spacing=2)  # data_diagnostico
    ##############################################
    #####          NOTIFICACAO INDIVIDUAL     ####
    ##############################################
    document.write_text(dict_especifico['nome_paciente2'], (55, 248))  # nome
    document.write_date(dict_especifico['dt_nascimento2'], (449, 248), spacing=2)  # data_nascimento
    document.write_code(dict_especifico['idade2'], (65, 277), space=2)  # idade
    document.write_mini(dict_especifico['tipo_idade2'], (111, 270))  # tipo_idade
    document.write_mini(dict_especifico['sexo2'], (234, 263))  # sexo
    document.write_mini(dict_especifico['gestante2'], (429, 263))  # gestante
    document.write_mini(dict_especifico['raca2'], (554, 264))  # raça/cor
    document.write_mini(dict_especifico['escolaridade2'], (554, 293))  # escolaridade
    document.write_code(dict_especifico['numero_sus2'], (57, 338), space=2, font_size=10)  # cartao_sus
    document.write_text(dict_especifico['nome_mae2'], (240, 338), font_size=9)  # nome_mae
    ##############################################
    #####          DADOS DE RESIDENCIA        ####
    ##############################################

    document.write_uf(dict_especifico['uf_residencia2'], (57, 368))  # uf_residencia
    document.write_text(dict_especifico['municipio_residencia2'], (90, 368), font_size=9)  # municipio_residencia
    document.write_code(dict_especifico['cod_ibge_residencia2'], (325, 368), space=2)  # cod_ibge_residencia
    document.write_text(dict_especifico['distrito_residencia2'], (420, 368), font_size=9)  # endereco
    document.write_text(dict_especifico['bairro_residencia2'], (62, 392), font_size=9)  # bairro
    document.write_text(dict_especifico['logradouro_residencia2'], (208, 393), font_size=9)  # logradouro
    document.write_code(dict_especifico['codigo_residencia2'], (480, 394), space=2)  # cod_logradouro
    document.write_text(dict_especifico['numero_residencia2'], (62, 417))  # numero
    document.write_text(dict_especifico['complemento_residencia2'], (120, 417), font_size=9)  # complemento
    document.write_text(dict_especifico['geo_campo1_2'], (415, 420))  # geo_campo_1
    document.write_text(dict_especifico['geo_campo2_2'], (55, 443))  # geo_campo_2
    document.write_text(dict_especifico['ponto_ref_residencia2'], (230, 443), font_size=9)  # ponto_ref
    document.write_code(dict_especifico['cep_residencia2'], (456, 446), space=2)  # cep
    document.write_telefone(dict_especifico['telefone_residencia2'], (55, 470), space=2)  # telefone
    document.write_mini(dict_especifico['zona_residencia2'], (333, 458))  # zona
    document.write_text(dict_especifico['pais_residencia2'], (360, 469), font_size=9)  # pais
    ##############################################
    #####        DADOS  COMPLEMENTARES        ####
    ##############################################
    document.write_date(dict_especifico['dt_1_consulta'], (63, 525), spacing=2)  # data_primeira_consulta
    document.write_date(dict_especifico['dt_investigacao'], (182, 525), spacing=2)  # data_investigacao
    document.write_mini(dict_especifico['vac_polio'], (439, 520))  # vacina_polio
    document.write_code(dict_especifico['num_dose_polio'] + '9', (500, 524), space=2)  # num_doses_polio
    document.write_date(dict_especifico['dt_ult_dose_polio'], (63, 572), spacing=2)  # data_ultima_dose_polio
    document.write_mini(dict_especifico['viajou_30_dias'], (421, 547))  # viajou_30_dias
    document.write_text(dict_especifico['pais_viagem_polio'], (440, 555))  # pais_viagem

    # !campo 38
    document.write_mini(dict_especifico['sint_febre'], (77, 606))  # sint_febre
    document.write_mini(dict_especifico['sint_vomito'], (77, 625))  # sint_vomito
    document.write_mini(dict_especifico['sint_diarreia'], (142, 606))  # sint_diarreia
    document.write_mini(dict_especifico['sint_obstipacao'], (142, 625))  # sint_obstipacao
    document.write_mini(dict_especifico['sint_dor_muscular'], (221, 606))  # sint_dor_muscular
    document.write_mini(dict_especifico['sint_cefaleia'], (221, 625))  # sint_cefaleia
    document.write_mini(dict_especifico['sint_alter_resp'], (315, 606))  # sint_alter_resp
    document.write_mini(dict_especifico['sint_outro'], (315, 625))  # sint_outro
    document.write_text(dict_especifico['sint_outro_descricao'], (353, 623), font_size=9)  # sint_outro_descricao

    # ! campo 39
    document.write_date(dict_especifico['dt_def_motora'], (452, 630), spacing=2)  # data_def_motora

    # ! campo 40 deficiencia motora
    document.write_mini(dict_especifico['def_aguda'], (92, 660))  # aguda
    document.write_mini(dict_especifico['def_flacida'], (157, 660))  # flacida
    document.write_mini(dict_especifico['def_assim'], (223, 660))  # assimetrica
    document.write_mini(dict_especifico['def_progess'], (302, 660))  # progressiva
    document.write_mini(dict_especifico['def_ascend'], (415, 660))  # ascendente
    document.write_mini(dict_especifico['def_descend'], (503, 660))  # descendente

    # ! campo 41 força muscular
    document.write_mini(dict_especifico['forca_mie'], (103, 694))  # membro_inferior_esquerdo
    document.write_mini(dict_especifico['forca_mse'], (154, 694))  # membro_superior_esquerdo
    document.write_mini(dict_especifico['forca_mid'], (206, 694))  # membro_inferior_direito
    document.write_mini(dict_especifico['forca_msd'], (257, 694))  # membro_superior_direito

    # ! campo 42 localização da deficiencia
    document.write_mini(dict_especifico['loc_mie'], (356, 694))  # membro_inferior_esquerdo
    document.write_mini(dict_especifico['loc_mse'], (407, 694))  # membro_superior_esquerdo
    document.write_mini(dict_especifico['loc_mid'], (458, 694))  # membro_inferior_direito
    document.write_mini(dict_especifico['loc_msd'], (509, 694))  # membro_superior_direito

    # ! campo 43 comprometimento de
    document.write_mini(dict_especifico['compr_resp'], (68, 735))  # respiracao
    document.write_mini(dict_especifico['compr_cerv'], (173, 734))  # cervical
    document.write_mini(dict_especifico['compr_face'], (268, 735))  # facial

    # ! campo 44 exame fisico na fase aguda
    document.write_date(dict_especifico['dt_exam_aguda'], (312, 737), spacing=2)  # data_exame_fisico_agudo

    # ! campo 45 força muscular
    document.write_mini(dict_especifico['forca_mie_aguda'], (446, 721))  # membro_inferior_esquerdo
    document.write_mini(dict_especifico['forca_mse_aguda'], (486, 721))  # membro_superior_esquerdo
    document.write_mini(dict_especifico['forca_mid_aguda'], (446, 734))  # membro_inferior_direito
    document.write_mini(dict_especifico['forca_msd_aguda'], (486, 734))  # membro_superior_direito

    # ! campo 46 tonus muscular
    document.write_mini(dict_especifico['tonus_mie'], (68, 768))  # membro_inferior_esquerdo
    document.write_mini(dict_especifico['tonus_cerv'], (68, 782))  # cervical
    document.write_mini(dict_especifico['tonus_mse'], (106, 768))  # membro_superior_esquerdo
    document.write_mini(dict_especifico['tonus_mid'], (140, 768))  # membro_inferior_direito
    document.write_mini(dict_especifico['tonus_face'], (140, 782))  # facial
    document.write_mini(dict_especifico['tonus_msd'], (174, 767))  # membro_superior_direito

    # ! campo 47 sensibilidade
    document.write_mini(dict_especifico['sensi_mie'], (285, 778))  # membro_inferior_esquerdo
    document.write_mini(dict_especifico['sensi_mse'], (325, 778))  # membro_superior_esquerdo
    document.write_mini(dict_especifico['sensi_mid'], (365, 778))  # membro_inferior_direito
    document.write_mini(dict_especifico['sensi_msd'], (415, 778))  # membro_superior_direito
    document.write_mini(dict_especifico['sensi_face'], (471, 778))  # facial

    # ! campo 48 reflexos
    document.write_mini(dict_especifico['reflex_aquE'], (88, 818))  # aquileu_esquerdo
    document.write_mini(dict_especifico['reflex_aquD'], (146, 818))  # aquileu_direito
    document.write_mini(dict_especifico['reflex_patE'], (208, 818))  # patelar_esquerdo
    document.write_mini(dict_especifico['reflex_patD'], (266, 818))  # patelar_direito
    document.write_mini(dict_especifico['reflex_bicE'], (328, 818))  # bicipital_esquerdo
    document.write_mini(dict_especifico['reflex_bicD'], (389, 818))  # bicipital_direito
    document.write_mini(dict_especifico['reflex_triE'], (448, 818))  # tricipital_esquerdo
    document.write_mini(dict_especifico['reflex_triD'], (508, 818))  # tricipital_direito

    # *====================== fim da pagina 1 ===============================*#

    # ! campo 49 reflexos cutaneos
    document.write_mini(dict_especifico['reflex_cut_flexE'], (75, 59), pg=1)  # cutaneo_flexor_esquerdo
    document.write_mini(dict_especifico['reflex_cut_flexD'], (75, 76), pg=1)  # cutaneo_flexor_direito
    document.write_mini(dict_especifico['reflex_cut_extE'], (181, 59), pg=1)  # cutaneo_extensor_esquerdo
    document.write_mini(dict_especifico['reflex_cut_extD'], (181, 75), pg=1)  # cutaneo_extensor_direito

    # ! campo 50 sinais meningeos
    document.write_mini(dict_especifico['meningea_kernig'], (328, 72), pg=1)  # kernig
    document.write_mini(dict_especifico['meningea_nuca'], (382, 72), pg=1)  # nuca
    document.write_mini(dict_especifico['meningea_brud'], (461, 72), pg=1)  # brudzinski

    # ! campo 51 ingestao toxica
    document.write_mini(dict_especifico['ingest_toxica'], (265, 92), pg=1)  # ingestao_toxica

    # ! campo 52 especificacao da ingestao toxica
    document.write_text(dict_especifico['esp_ingest_toxica'], (290, 110), pg=1, font_size=9)  # especificacao_ingestao_toxica

    # ! campo 53 injecao intramuscular
    document.write_mini(dict_especifico['inj_intramusc'], (199, 126), pg=1)  # injecao_intramuscular

    # ! campo 54 local da injecao intramuscular
    document.write_mini(dict_especifico['loc_inj_intramusc'], (492, 128), pg=1)  # local_injecao_intramuscular

    # ! campo 55 hipotese diagnostica
    document.write_code(dict_especifico['hipotese_diag'], (200, 173), pg=1, space=2)  # hipotese_diagnostica

    # ! campo 56 hospitalizacao
    document.write_mini(dict_especifico['hospitalizacao2'], (426, 164), pg=1)  # hospitalizacao

    # ! campo 57 data de internacao
    document.write_date(dict_especifico['dt_internacao'], (454, 175), pg=1, spacing=2)  # data_internacao

    # ! campo 58 local de internacao
    document.write_uf(dict_especifico['uf_hospital2'], (57, 202), pg=1)  # uf_hospital

    # ! campo 59 municipio de internacao
    document.write_text(dict_especifico['municipio_hospital2'], (90, 202), pg=1)  # municipio_hospital
    document.write_code(dict_especifico['cod_ibge_hospital2'], (485, 202), pg=1, space=2)  # cod_ibge_hospital

    # ! campo 60 data da coleta de amostra
    document.write_date(dict_especifico['dt_col_lab'], (62, 235), pg=1, spacing=2)  # data_coleta_amostra

    # ! campo 61 data do envio ao estado
    document.write_date(dict_especifico['dt_env_estado'], (190, 236), pg=1, spacing=2)  # data_env

    # ! campo 62 data do envio ao LRR
    document.write_date(dict_especifico['dt_env_lrr'], (314, 236), pg=1, spacing=2)  # data_env_lrr

    # ! campo 63 data do recebimento no LRR
    document.write_date(dict_especifico['dt_receb_lrr'], (61, 267), pg=1, spacing=2)  # data

    # ! campo 64 quantidade de amostras coletadas
    document.write_mini(dict_especifico['quant_fez_col'], (287, 252), pg=1)  # quant

    # ! campo 65 condicoes da amostra
    document.write_mini(dict_especifico['cond_fez_col'], (433, 249), pg=1)  # condicoes

    # ! campo 66 data do resultado laboratorial
    document.write_date(dict_especifico['dt_res_lab'], (455, 268), pg=1, spacing=2)  # data

    # ! campo 67 resultado laboratorial 1
    document.write_code(dict_especifico['res_laboratorial1'], (535, 285), pg=1, font_size=11, space=2)  # resultado
    document.write_code(dict_especifico['res_laboratorial2'], (535, 297), pg=1, font_size=11, space=2)  # resultado2
    document.write_code(dict_especifico['res_laboratorial3'], (535, 309), pg=1, font_size=11, space=2)  # resultado3

    # ! campo 68 exames complementares

    if dict_especifico['liq_dt1']:
        document.write_code(dict_especifico['liq_dt1'][:2], (75, 385), pg=1)  # data
        document.write_code(dict_especifico['liq_dt1'][3:5], (112, 385), pg=1)  # data
        document.write_code(dict_especifico['liq_dt1'][6:], (149, 385), pg=1)  # data

    document.write_text(dict_especifico['liq_cel1'], (190, 385), pg=1)  # celulas
    document.write_text(dict_especifico['liq_linf1'], (282, 385), pg=1)  # linfocitos
    document.write_text(dict_especifico['liq_prot1'], (358, 385), pg=1)  # proteinas
    document.write_text(dict_especifico['liq_gli1'], (432, 385), pg=1)  # glicose
    document.write_text(dict_especifico['liq_clo1'], (501, 385), pg=1)  # cloreto

    if dict_especifico['liq_dt2']:
        document.write_code(dict_especifico['liq_dt2'][:2], (75, 407), pg=1)  # data
        document.write_code(dict_especifico['liq_dt2'][3:5], (112, 407), pg=1)  # data
        document.write_code(dict_especifico['liq_dt2'][6:], (149, 407), pg=1)  # data

    document.write_text(dict_especifico['liq_cel2'], (190, 407), pg=1)  # celulas
    document.write_text(dict_especifico['liq_linf2'], (282, 407), pg=1)  # linfocitos
    document.write_text(dict_especifico['liq_prot2'], (358, 407), pg=1)  # proteinas
    document.write_text(dict_especifico['liq_gli2'], (432, 407), pg=1)  # glicose
    document.write_text(dict_especifico['liq_clo2'], (501, 407), pg=1)  # cloreto

    # ! campo 69 data do exame eletroneuromiografico
    document.write_date(dict_especifico['dt_eletrone'], (61, 442), pg=1, spacing=2)  # data
    # ! campo 70 diagnostico sugestivo
    document.write_text(dict_especifico['diag_sugestivo'], (200, 442), pg=1)  # diagnostico_sug
    # ! campo 71 anatomopatologico
    document.write_mini(dict_especifico['anatomo_cereb'], (89, 476), pg=1)  # cerebro
    document.write_mini(dict_especifico['anatomo_medula'], (134, 476), pg=1)  # medula
    document.write_mini(dict_especifico['anatomo_intest'], (179, 475), pg=1)  # intestino

    # ! campo 72 data do exame anatomopatologico
    document.write_date(dict_especifico['dt_anatomo'], (280, 485), pg=1, spacing=2)  # data da coleta

    # ! campo 73 resultado
    document.write_mini(dict_especifico['res_anatomo'], (556, 472), pg=1)  # resultado

    # ! campo 74 data da revisita
    document.write_date(dict_especifico['dt_revisita'], (61, 534), pg=1, spacing=2)  # data da revisita

    # ! campo 75 força muscular
    document.write_mini(dict_especifico['forca_mie2'], (194, 520), pg=1)  # membro_inferior_esquerdo
    document.write_mini(dict_especifico['forca_mse2'], (233, 520), pg=1)  # membro_superior_esquerdo
    document.write_mini(dict_especifico['forca_mid2'], (194, 533), pg=1)  # membro_inferior_direito
    document.write_mini(dict_especifico['forca_msd2'], (233, 533), pg=1)  # membro_superior_direito

    # ! campo 76 tonus muscular
    document.write_mini(dict_especifico['tonus_mie2'], (330, 516), pg=1)  # membro_inferior_esquerdo
    document.write_mini(dict_especifico['tonus_cerv2'], (332, 530), pg=1)  # cervical
    document.write_mini(dict_especifico['tonus_mse2'], (369, 516), pg=1)  # membro_superior_esquerdo
    document.write_mini(dict_especifico['tonus_mid2'], (404, 516), pg=1)  # membro_inferior_direito
    document.write_mini(dict_especifico['tonus_face2'], (404, 530), pg=1)  # facial
    document.write_mini(dict_especifico['tonus_msd2'], (438, 515), pg=1)  # membro_superior_direito

    # ! campo 77 reflexos
    document.write_mini(dict_especifico['reflex_aquE2'], (80, 565), pg=1)  # aquileu_esquerdo
    document.write_mini(dict_especifico['reflex_aquD2'], (138, 565), pg=1)  # aquileu_direito
    document.write_mini(dict_especifico['reflex_patE2'], (200, 565), pg=1)  # patelar_esquerdo
    document.write_mini(dict_especifico['reflex_patD2'], (258, 565), pg=1)  # patelar_direito
    document.write_mini(dict_especifico['reflex_bicE2'], (326, 565), pg=1)  # bicipital_esquerdo
    document.write_mini(dict_especifico['reflex_bicD2'], (388, 565), pg=1)  # bicipital_direito
    document.write_mini(dict_especifico['reflex_triE2'], (447, 565), pg=1)  # tricipital_esquerdo
    document.write_mini(dict_especifico['reflex_triD2'], (510, 565), pg=1)  # tricipital_direito

    # ! campo 78 reflexos cutaneos
    document.write_mini(dict_especifico['reflex_cut_flexE2'], (70, 596), pg=1)  # cutaneo_flexor_esquerdo
    document.write_mini(dict_especifico['reflex_cut_flexD2'], (125, 596), pg=1)  # cutaneo_flexor_direito
    document.write_mini(dict_especifico['reflex_cut_extE2'], (190, 596), pg=1)  # cutaneo_extensor_esquerdo
    document.write_mini(dict_especifico['reflex_cut_extD2'], (265, 596), pg=1)  # cutaneo_extensor_direito

    # ! campo 79 atrofia muscular
    document.write_mini(dict_especifico['atrofia_mie'], (366, 596), pg=1)  # membro_inferior_esquerdo
    document.write_mini(dict_especifico['atrofia_mse'], (418, 596), pg=1)  # membro_superior_esquerdo
    document.write_mini(dict_especifico['atrofia_mid'], (470, 596), pg=1)  # membro_inferior_direito
    document.write_mini(dict_especifico['atrofia_msd'], (522, 596), pg=1)  # membro_superior_direito

    # ! campo 80 sensibilidade
    document.write_mini(dict_especifico['sensi_mie2'], (136, 625), pg=1)  # membro_inferior_esquerdo
    document.write_mini(dict_especifico['sensi_mse2'], (200, 625), pg=1)  # membro_superior_esquerdo
    document.write_mini(dict_especifico['sensi_mid2'], (272, 625), pg=1)  # membro_inferior_direito
    document.write_mini(dict_especifico['sensi_msd2'], (348, 625), pg=1)  # membro_superior_direito
    document.write_mini(dict_especifico['sensi_face2'], (429, 624), pg=1)  # facial

    # ! campo 81 data da revisao
    document.write_date(dict_especifico['dt_revisao'], (60, 672), pg=1, spacing=2)  # data_revisao

    # ! campo 82 classificacao final
    document.write_mini(dict_especifico['classif_final'], (372, 648), pg=1)  # classificacao_final

    # ! campo 83 criterio de classificacao
    document.write_mini(dict_especifico['criterio_classif'], (555, 647), pg=1)  # criterio_classificacao

    # ! campo 84 diagnostico descartado
    document.write_code(dict_especifico['diag_descartado'], (105, 707), pg=1, space=2)  # diagnostico_descartado

    # ! campo 85 evolucao do caso
    document.write_mini(dict_especifico['evolucao_caso'], (553, 690), pg=1)  # evolucao

    # ! campo 86 data do obito
    document.write_date(dict_especifico['dt_obito'], (60, 736), pg=1, spacing=2)  # data_obito

    # ! campo 87 data do encerramento
    document.write_date(dict_especifico['dt_encerramento'], (180, 735), pg=1, spacing=2)  # data_encerramento

    document.write_text(dict_especifico['municipio_us_investigador'], (60, 769), pg=1, font_size=9)  # municipio_investigador
    document.write_code(dict_especifico['cod_us_investigador'], (469, 769), pg=1, space=2)  # cod_unidade_investigador
    document.write_text(dict_especifico['nome_investigador'], (55, 797), pg=1, font_size=9)  # nome_investigador
    document.write_text(dict_especifico['funcao_investigador'], (260, 797), pg=1, font_size=9)  # funcao_investigador
    document.write_text(dict_especifico['assinatura_investigador'], (470, 797), pg=1, font_size=9)  # assinatura_investigador
    
    document.save(nome_arquivo, path_pdf_gerado, notificatoriaCSV, modelo_pdf_base)