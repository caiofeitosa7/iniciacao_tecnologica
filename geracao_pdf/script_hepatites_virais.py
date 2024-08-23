from .pdfWritter import PDFWriter


def gerar_pdf_hepatites_virais(notificatoriaCSV: dict, dict_especifico: dict, modelo_pdf: str, modelo_pdf_base: str, path_pdf_gerado: str, nome_arquivo: str):
    document = PDFWriter(modelo_pdf)

    ###################################################
    # Dados do paciente
    ###################################################
    document.write_text(dict_especifico['numero_ficha2'],(470, 46))
    document.write_date(dict_especifico['dt_notificacao2'], (446, 287), spacing=2) #data_notificacao
    document.write_uf(dict_especifico['uf_notificacao2'], (56, 318)) #uf_notificacao
    document.write_text(dict_especifico['municipio_notificacao2'], (95, 318)) #municipio_notificacao __unid_saude 55,space=220
    document.write_code(dict_especifico['cod_ibge_notificacao2'], (480, 318),space=2) #cod_ibge
    document.write_text(dict_especifico['unidade_saude2'], (62, 346)) #unid_saude
    document.write_code(dict_especifico['cod_unidade_saude2'], (339, 346),space=2) #cod_unid_saude
    document.write_date(dict_especifico['dt_sintomas2'], (446, 345), spacing=2) #data_diagnostico
    ##############################################
    #####          NOTIFICACAO INDIVIDUAL     ####
    ##############################################
    document.write_text(dict_especifico['nome_paciente2'], (65, 376)) #nome
    document.write_date(dict_especifico['dt_nascimento2'], (450, 376),spacing=2) #data_nascimento
    document.write_code(dict_especifico['idade2'], (64, 406),space=2) #idade
    document.write_mini(dict_especifico['tipo_idade2'], (111, 399)) #tipo_idade
    document.write_mini(dict_especifico['sexo2'], (233, 392)) #sexo
    document.write_mini(dict_especifico['gestante2'], (427, 392)) #gestante
    document.write_mini(dict_especifico['raca2'], (552, 393)) #raça/cor
    document.write_mini(dict_especifico['escolaridade2'], (553, 422)) #escolaridade
    document.write_code(dict_especifico['numero_sus2'], (56, 466),space=2, font_size=10) #cartao_sus
    document.write_text(dict_especifico['nome_mae2'], (240, 466)) #nome_mae
    ##############################################
    #####          DADOS DE RESIDENCIA        ####
    ##############################################

    document.write_uf(dict_especifico['uf_residencia2'], (58, 497)) #uf_residencia
    document.write_text(dict_especifico['municipio_residencia2'], (90, 496)) #municipio_residencia
    document.write_code(dict_especifico['cod_ibge_residencia2'], (328, 496),space=2) #cod_ibge_residencia
    document.write_text(dict_especifico['distrito_residencia2'], (420, 496)) #endereco
    document.write_text(dict_especifico['bairro_residencia2'], (60, 520)) #bairro
    document.write_text(dict_especifico['logradouro_residencia2'], (205, 522)) #logradouro
    document.write_code(dict_especifico['codigo_residencia2'], (480, 522),space=2) #cod_logradouro
    document.write_text(dict_especifico['numero_residencia2'], (62, 545)) #numero
    document.write_text(dict_especifico['complemento_residencia2'], (120, 545)) #complemento
    document.write_text(dict_especifico['geo_campo1_2'], (420, 547)) #geo_campo_1
    document.write_text(dict_especifico['geo_campo2_2'], (65, 570)) #geo_campo_2
    document.write_text(dict_especifico['ponto_ref_residencia2'], (230, 571)) #ponto_ref
    document.write_code(dict_especifico['cep_residencia2'], (455, 573),space=2) #cep
    document.write_telefone(dict_especifico['telefone_residencia2'], (56, 598), space=2) #telefone
    document.write_mini(dict_especifico['zona_residencia2'], (333, 586)) #zona
    document.write_text(dict_especifico['pais_residencia2'], (365, 598)) #pais
    ###################################################
    # Dados complementares                            #
    ###################################################
    document.write_date(dict_especifico['dt_investigacao'], (62, 650), spacing=2) #data_investigacao
    document.write_text(dict_especifico['ocupacao'], (190, 650)) #ocupacao
    document.write_code(dict_especifico['suspeita'], (135, 668)) #suspeita
    document.write_mini(dict_especifico['vacina_hepa'], (460, 669)) #vacina_hepa
    document.write_mini(dict_especifico['vacina_hepb'], (459, 686)) #vacina_hepb
    document.write_mini(dict_especifico['institucionalizado'], (504, 708)) #institucionalizado
    document.write_mini(dict_especifico['agrav_assoc_hiv'], (183, 752)) #agrav_assoc_hiv
    document.write_mini(dict_especifico['agrav_assoc_dst'], (183, 766)) #agrav_assoc_dst
    document.write_mini(dict_especifico['contat_pac_sex'], (463,743)) #contat_pac_sex
    document.write_mini(dict_especifico['contat_pec_dom'], (464, 756)) #contat_pec_dom
    document.write_mini(dict_especifico['contat_pac_ocu'], (464, 769)) #contat_pac_ocu
    ################################################### fim da pagina 1
    document.write_mini(dict_especifico['exp_med_inj'], (66, 62), pg=1) #exp_med_inj
    document.write_mini(dict_especifico['exp_crack'], (66, 79), pg=1) #exp_crack
    document.write_mini(dict_especifico['exp_drog_inj'], (66, 95), pg=1) #exp_drog_inj
    document.write_mini(dict_especifico['exp_agua'], (66, 112), pg=1) #exp_agua
    document.write_mini(dict_especifico['exp_sex'], (66, 127),pg=1) #exposicao sexual
    document.write_mini(dict_especifico['exp_transplante'], (66,141), pg=1) #exp_transplante
    document.write_mini(dict_especifico['exp_tatu'], (267, 62), pg=1) #exp_tatu
    document.write_mini(dict_especifico['exp_acupuntura'], (267, 79), pg=1) #exp_acupuntura
    document.write_mini(dict_especifico['exp_trat_cirurg'], (267, 94), pg=1) #exp_trat_cirurg
    document.write_mini(dict_especifico['exp_trat_dent'], (267, 112), pg=1) #exp_trat_dent
    document.write_mini(dict_especifico['exp_hemodialise'], (266, 127), pg=1) #exp_hemodialise
    document.write_mini(dict_especifico['exp_outras'], (266, 139), pg=1) #exp_outras
    document.write_mini(dict_especifico['exp_acid_mat_bio'], (405, 61), pg=1) #exp_acid_mat_bio
    document.write_mini(dict_especifico['exp_transf_sang'], (405, 78), pg=1) #exp_transf_sang
    document.write_date(dict_especifico['dt_acid_transf'], (393, 135), pg=1, spacing=2) #dt_acid_transf
    document.write_uf(dict_especifico['uf_exp1'], (57, 189), pg=1) #uf_exp1
    document.write_text(dict_especifico['municipio_exp1'], (80, 189), pg=1) #municipio_exp1
    document.write_text(dict_especifico['local_exp1'], (250, 189), pg=1) #local_exp1
    document.write_telefone(dict_especifico['fone_exp1'], (485, 189), pg=1) #fone_exp1
    document.write_uf(dict_especifico['uf_exp2'], (57, 202), pg=1) #uf_exp2
    document.write_text(dict_especifico['municipio_exp2'], (80, 202), pg=1) #municipio_exp2
    document.write_text(dict_especifico['local_exp2'], (250, 202), pg=1) #local_exp2
    document.write_telefone(dict_especifico['fone_exp2'], (485, 202), pg=1) #fone_exp2
    document.write_uf(dict_especifico['uf_exp3'], (57, 215), pg=1) #uf_exp3
    document.write_text(dict_especifico['municipio_exp3'], (80, 215), pg=1) #municipio_exp3
    document.write_text(dict_especifico['local_exp3'], (250, 215), pg=1) #local_exp3
    document.write_telefone(dict_especifico['fone_exp3'], (485, 215), pg=1) #fone_exp3
    ################ quadro comunicantes
    document.write_text(dict_especifico['comun_nome1'], (57, 302), pg=1) #comun_nome1
    document.write_code(dict_especifico['comun_idade1'], (135, 302), pg=1) #comun_idade1
    document.write_text(dict_especifico['comun_tp_cont1'], (195, 302), pg=1) #comun_tp_cont1
    document.write_text(dict_especifico['comun_hbsag1'], (262, 302), pg=1) #comun_hbsag1
    document.write_text(dict_especifico['comun_anti_hbc1'], (315, 302), pg=1) #comun_anti_hbc1
    document.write_text(dict_especifico['comun_anti_hcv1'], (380, 302), pg=1) #comun_anti_hcv1
    document.write_text(dict_especifico['comun_vac_hepb1'], (445, 302), pg=1) #comun_vac_hepb1
    document.write_text(dict_especifico['comun_imuno_hepb1'], (520, 302), pg=1) #comun_imuno_hepb1
    document.write_text(dict_especifico['comun_nome2'], (57, 315), pg=1) #comun_nome2
    document.write_code(dict_especifico['comun_idade2'], (135, 315), pg=1) #comun_idade2
    document.write_text(dict_especifico['comun_tp_cont2'], (195, 315), pg=1) #comun_tp_cont2
    document.write_text(dict_especifico['comun_hbsag2'], (262, 315), pg=1) #comun_hbsag2
    document.write_text(dict_especifico['comun_anti_hbc2'], (315, 315), pg=1) #comun_anti_hbc2
    document.write_text(dict_especifico['comun_anti_hcv2'], (380, 315), pg=1) #comun_anti_hcv2
    document.write_text(dict_especifico['comun_vac_hepb2'], (445, 315), pg=1) #comun_vac_hepb2
    document.write_text(dict_especifico['comun_imuno_hepb2'], (520, 315), pg=1) #comun_imuno_hepb2
    document.write_text(dict_especifico['comun_nome3'], (57, 327), pg=1) #comun_nome3
    document.write_code(dict_especifico['comun_idade3'], (135, 327), pg=1) #comun_idade3
    document.write_text(dict_especifico['comun_tp_cont3'], (195, 327), pg=1) #comun_tp_cont3
    document.write_text(dict_especifico['comun_hbsag3'], (262, 327), pg=1) #comun_hbsag3
    document.write_text(dict_especifico['comun_anti_hbc3'], (315, 327), pg=1) #comun_anti_hbc3
    document.write_text(dict_especifico['comun_anti_hcv3'], (380, 327), pg=1) #comun_anti_hcv3
    document.write_text(dict_especifico['comun_vac_hepb3'], (445, 327), pg=1) #comun_vac_hepb3
    document.write_text(dict_especifico['comun_imuno_hepb3'], (520, 327), pg=1) #comun_imuno_hepb3
    document.write_text(dict_especifico['comun_nome4'], (57, 340), pg=1) #comun_nome4
    document.write_code(dict_especifico['comun_idade4'], (135, 340), pg=1) #comun_idade4
    document.write_text(dict_especifico['comun_tp_cont4'], (195, 340), pg=1) #comun_tp_cont4
    document.write_text(dict_especifico['comun_hbsag4'], (262, 340), pg=1) #comun_hbsag4
    document.write_text(dict_especifico['comun_anti_hbc4'], (315, 340), pg=1) #comun_anti_hbc4
    document.write_text(dict_especifico['comun_anti_hcv4'], (380, 340), pg=1) #comun_anti_hcv4
    document.write_text(dict_especifico['comun_vac_hepb4'], (445, 340), pg=1) #comun_vac_hepb4
    document.write_text(dict_especifico['comun_imuno_hepb4'], (520, 340), pg=1) #comun_imuno_hepb4
    document.write_text(dict_especifico['comun_nome5'], (57, 353), pg=1) #comun_nome5
    document.write_code(dict_especifico['comun_idade5'], (135, 353), pg=1) #comun_idade5
    document.write_text(dict_especifico['comun_tp_cont5'], (195, 353), pg=1) #comun_tp_cont5
    document.write_text(dict_especifico['comun_hbsag5'], (262, 353), pg=1) #comun_hbsag5
    document.write_text(dict_especifico['comun_anti_hbc5'], (315, 353), pg=1) #comun_anti_hbc5
    document.write_text(dict_especifico['comun_anti_hcv5'], (380, 353), pg=1) #comun_anti_hcv5
    document.write_text(dict_especifico['comun_vac_hepb5'], (445, 353), pg=1) #comun_vac_hepb5
    document.write_text(dict_especifico['comun_imuno_hepb5'], (520, 353), pg=1) #comun_imuno_hepb5
    ############ Dados laboratoriais
    document.write_mini(dict_especifico['pac_encamin'], (208, 368), pg=1) #pac_encamin
    document.write_date(dict_especifico['dt_amostra_cta'], (236, 401), pg=1, spacing=2) #data_amostra
    document.write_mini(dict_especifico['res_soro_hbsag'], (499, 379), pg=1) #res_soro_hbsag
    document.write_mini(dict_especifico['res_soro_anti_hbc'], (499, 392), pg=1) #res_soro_anti_hbc
    document.write_mini(dict_especifico['res_soro_anti_hcv'], (499, 406), pg=1) #res_soro_anti_hcv
    document.write_date(dict_especifico['dt_sorologia'], (118, 438), pg=1, spacing=2) #data_sorologia
    document.write_mini(dict_especifico['genotipo_hcv'], (222, 451), pg=1) #genotipo_hcv
    document.write_mini(dict_especifico['res_vir_hav_igm'], (347, 433), pg=1) #res_vir_hav_igm
    document.write_mini(dict_especifico['res_vir_hbsag'], (347, 446), pg=1) #res_vir_hbsag
    document.write_mini(dict_especifico['res_vir_hbc_igm'], (347, 459), pg=1) #res_vir_hbc_igm
    document.write_mini(dict_especifico['res_vir_hbc_total'], (347, 472), pg=1) #res_vir_hbc_total
    document.write_mini(dict_especifico['res_vir_hbs'], (425, 433), pg=1) #res_vir_hbs
    document.write_mini(dict_especifico['res_vir_hbeag'], (425, 446), pg=1) #res_vir_hbeag
    document.write_mini(dict_especifico['res_vir_hbe'], (425, 459), pg=1) #res_vir_hbe
    document.write_mini(dict_especifico['res_vir_hdv_total'], (425, 472), pg=1) #res_vir_hdv_total
    document.write_mini(dict_especifico['res_vir_hdv_igm'], (496, 430), pg=1) #res_vir_hdv_igm
    document.write_mini(dict_especifico['res_vir_hev_igm'], (496, 444), pg=1) #res_vir_hev_igm
    document.write_mini(dict_especifico['res_vir_hcv'], (496, 459), pg=1) #res_vir_hcv
    document.write_mini(dict_especifico['res_vir_hcv_rna'], (496, 473), pg=1) #res_vir_hcv_rna
    ############# Conclusao
    document.write_mini(dict_especifico['classif_final'], (230, 496), pg=1) #classif_final
    document.write_mini(dict_especifico['forma_clinica'], (355, 494), pg=1) #forma_clinica
    document.write_code(dict_especifico['classif_etiologica'], (545, 494), pg=1, space=1) #classif_etiologica
    document.write_code(dict_especifico['mecan_infeccao'], (510, 557), pg=1, space=1) #mecan_infeccao
    document.write_mini(dict_especifico['mecan_infeccao_outros'], (476, 582), pg=1) #mecan_infeccao_outros
    document.write_date(dict_especifico['dt_encerramento'], (57, 629), pg=1, spacing=2) #data_encerramento
    document.write_box(dict_especifico['obs_adicionais'], rect=(30, 650,566,735), pg=1) #obs_adicionais
    document.write_text(dict_especifico['municipio_us_investigador'], (62, 770), pg=1) #municipio_us_investigador
    document.write_code(dict_especifico['cod_us_investigador'], (464, 772), pg=1, space=2) #cod_us_investigador
    document.write_text(dict_especifico['nome_investigador'], (62, 805), pg=1) #nome_investigador
    document.write_text(dict_especifico['funcao_investigador'], (264, 805), pg=1) #funcao_investigador
    document.write_text(dict_especifico['assinatura_investigador'], (465, 804), pg=1) #assinatura_investigador

    document.save(nome_arquivo, path_pdf_gerado, notificatoriaCSV, modelo_pdf_base)