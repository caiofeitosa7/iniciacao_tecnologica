from .pdfWritter import PDFWriter


def gerar_pdf_chagas_aguda(notificatoriaCSV: dict, dict_especifico: dict, modelo_pdf: str, modelo_pdf_base: str, path_pdf_gerado: str, nome_arquivo: str):
    document = PDFWriter(modelo_pdf)

    ###################################################
    # Dados do paciente
    ###################################################
    document.write_text(dict_especifico['numero_ficha2'],(470, 48))
    document.write_date(dict_especifico['dt_notificacao2'], (448, 178), spacing=2) #data_notificacao
    document.write_uf(dict_especifico['uf_notificacao2'], (56, 208)) #uf_notificacao
    document.write_text(dict_especifico['municipio_notificacao2'], (88, 208)) #municipio_notificacao __unid_saude 55,space=220
    document.write_code(dict_especifico['cod_ibge_notificacao2'], (478, 208),space=2) #cod_ibge
    document.write_text(dict_especifico['unidade_saude2'], (65, 235)) #cod_unid_saude
    document.write_code(dict_especifico['cod_unidade_saude2'], (339, 235),space=2) #cod_unid_saude
    document.write_date(dict_especifico['dt_sintomas2'], (446, 235), spacing=2) #data_diagnostico
    ##############################################
    #####          NOTIFICACAO INDIVIDUAL     ####
    ##############################################
    document.write_text(dict_especifico['nome_paciente2'], (62, 267)) #nome
    document.write_date(dict_especifico['dt_nascimento2'], (449, 266), spacing=2) #data_nascimento
    document.write_code(dict_especifico['idade2'], (65, 296),space=2) #idade
    document.write_mini(dict_especifico['tipo_idade2'], (112, 288)) #tipo_idade
    document.write_mini(dict_especifico['sexo2'], (235, 281)) #sexo
    document.write_mini(dict_especifico['gestante2'], (429, 281)) #gestante
    document.write_mini(dict_especifico['raca2'], (554, 282)) #raça/cor
    document.write_mini(dict_especifico['escolaridade2'], (555, 311)) #escolaridade
    document.write_code(dict_especifico['numero_sus2'], (58, 356),space=2, font_size=10) #cartao_sus
    document.write_text(dict_especifico['nome_mae2'], (240, 356)) #nome_mae
    ##############################################
    #####          DADOS DE RESIDENCIA        ####
    ##############################################

    document.write_uf(dict_especifico['uf_residencia2'], (58, 387)) #uf_residencia
    document.write_text(dict_especifico['municipio_residencia2'], (92, 386)) #municipio_residencia
    document.write_code(dict_especifico['cod_ibge_residencia2'], (328, 386),space=2) #cod_ibge_residencia
    document.write_text(dict_especifico['distrito_residencia2'], (422, 386)) #endereco
    document.write_text(dict_especifico['bairro_residencia2'], (64, 410)) #bairro
    document.write_text(dict_especifico['logradouro_residencia2'], (207, 412)) #logradouro
    document.write_code(dict_especifico['codigo_residencia2'], (481, 412),space=2) #cod_logradouro
    document.write_text(dict_especifico['numero_residencia2'], (65, 435)) #numero
    document.write_text(dict_especifico['complemento_residencia2'], (120, 436)) #complemento
    document.write_text(dict_especifico['geo_campo1_2'], (415, 438)) #geo_campo_1
    document.write_text(dict_especifico['geo_campo2_2'], (60, 460)) #geo_campo_2
    document.write_text(dict_especifico['ponto_ref_residencia2'], (230, 462)) #ponto_ref
    document.write_code(dict_especifico['cep_residencia2'], (456, 463),space=2) #cep
    document.write_telefone(dict_especifico['telefone_residencia2'], (57, 488), space=2) #telefone
    document.write_mini(dict_especifico['zona_residencia2'], (336, 476)) #zona
    document.write_text(dict_especifico['pais_residencia2'], (365, 488)) #pais
    ####################################################
    # Dados Complementares
    ####################################################
    document.write_date(dict_especifico['dt_investigacao'], (66, 538), spacing=2) #data_investigacao
    document.write_text(dict_especifico['ocupacao'], (190, 538)) #ocupacao
    document.write_uf(dict_especifico['uf_desloc1'], (95, 585)) #uf_desloc1
    document.write_text(dict_especifico['municipio_desloc1'], (170, 585)) #municipio_desloc1
    document.write_uf(dict_especifico['uf_desloc2'], (95, 600)) #uf_desloc2
    document.write_text(dict_especifico['municipio_desloc2'], (170, 600)) #municipio_desloc2
    document.write_uf(dict_especifico['uf_desloc3'], (95, 615)) #uf_desloc3
    document.write_text(dict_especifico['municipio_desloc3'], (170, 615)) #municipio_desloc3
    document.write_mini(dict_especifico['pres_triat_intra_dom'], (259, 639)) #pres_triat_intra_dom
    document.write_date(dict_especifico['dt_encontro_vestigio'], (278, 646), spacing=2) #data_encontro_vestigio
    document.write_mini(dict_especifico['hist_uso_sangue'], (549, 632)) #hist_uso_sangue
    document.write_mini(dict_especifico['contr_soro_un_hemo'], (313, 662)) #contr_soro_un_hemo
    document.write_mini(dict_especifico['manip_t_cruzi'], (555, 658)) #manip_t_cruzi
    document.write_mini(dict_especifico['mae_infec_chag'], (312, 701)) #mae_infec_chag
    document.write_mini(dict_especifico['possiv_trans_oral'],(555, 700)) #poss_transmissao_oral
    document.write_mini(dict_especifico['sint_assint'], (79, 740)) #sint_assint
    document.write_mini(dict_especifico['sint_febre'], (79, 755)) #sint_febre
    document.write_mini(dict_especifico['sint_astenia'], (79, 772)) #sint_astenia
    document.write_mini(dict_especifico['sint_edema'], (162, 740)) #sint_edema
    document.write_mini(dict_especifico['sint_hepato'], (162, 756)) #sint_hepato
    document.write_mini(dict_especifico['sint_espleno'], (162, 772)) #sint_espleno
    document.write_mini(dict_especifico['sint_mening'], (264, 739)) #sint_mening
    document.write_mini(dict_especifico['sint_icc'], (264, 752)) #sint_icc
    document.write_mini(dict_especifico['sint_chagoma'], (264, 769)) #sint_chagoma
    document.write_mini(dict_especifico['sint_poliade'], (430, 735)) #sint_poliade
    document.write_mini(dict_especifico['sint_taquicardia'], (430, 749)) #sint_taquicardia
    document.write_mini(dict_especifico['sint_outro'], (430, 764)) #sint_outro
    document.write_mini(dict_especifico['sint_outro_descricao'], (468, 763)) #sint_outro_descricao
    #################################################### fim da pagina 1

    document.write_date(dict_especifico['dt_paras_direto'], (64, 75), spacing=2, pg=1) #data_paras_direto
    document.write_mini(dict_especifico['paras_dir_ex_fresc'], (357,59), pg=1) #paras_dir_ex_fresc
    document.write_mini(dict_especifico['paras_dir_strout'], (357, 73), pg=1) #paras_dir_strout
    document.write_mini(dict_especifico['paras_dir_outro'], (531, 58), pg=1) #paras_dir_outro
    document.write_date(dict_especifico['dt_paras_indireto'], (64, 115), spacing=2, pg=1) #data_paras_indireto
    document.write_mini(dict_especifico['paras_indir_xeno'], (391, 106), pg=1) #paras_indir_xeno
    document.write_mini(dict_especifico['paras_indir_hemo'], (506, 107), pg=1) #paras_indir_hemo
    document.write_date(dict_especifico['dt_coleta_s1'], (64, 156), spacing=2, pg=1) #data_coleta_s1
    document.write_date(dict_especifico['dt_coleta_s2'], (64, 190), spacing=2, pg=1) #data_coleta_s2
    document.write_mini(dict_especifico['elisa_igm_s1'], (293, 163), pg=1) #elisa_igm_s1
    document.write_mini(dict_especifico['elisa_igm_s2'], (293, 175), pg=1) #elisa_igm_s2
    document.write_mini(dict_especifico['elisa_igg_s1'], (327, 161), pg=1) #elisa_igg_s1
    document.write_mini(dict_especifico['elisa_igg_s2'], (327, 174), pg=1) #elisa_igg_s2
    document.write_mini(dict_especifico['hemo_igm_s1'], (486, 165), pg=1) #hemo_igm_s1
    document.write_mini(dict_especifico['hemo_igm_s2'], (486, 178), pg=1) #hemo_igm_s2
    document.write_mini(dict_especifico['hemo_igg_s1'], (520, 163), pg=1) #hemo_igg_s1
    document.write_mini(dict_especifico['hemo_igg_s2'], (520, 176), pg=1) #hemo_igg_s2
    document.write_mini(dict_especifico['ifi_igm_s1'], (211, 232), pg=1) #ifi_igm_s1
    document.write_code(dict_especifico['ifi_igm_s1_titulo'], (255, 236),space=2, pg=1) #ifi_igm_s1_titulo
    document.write_mini(dict_especifico['ifi_igm_s2'], (211, 260), pg=1) #ifi_igm_s2
    document.write_code(dict_especifico['ifi_igm_s2_titulo'], (255, 260),space=2, pg=1) #ifi_igm_s2_titulo
    document.write_mini(dict_especifico['ifi_igg_s1'], (410, 232), pg=1) #ifi_igg_s1
    document.write_code(dict_especifico['ifi_igg_s1_titulo'], (454, 236),space=2, pg=1) #ifi_igg_s1_titulo
    document.write_mini(dict_especifico['ifi_igg_s2'], (410, 260), pg=1) #ifi_igg_s2
    document.write_code(dict_especifico['ifi_igg_s2_titulo'], (454, 260),space=2, pg=1) #ifi_igg_s2_titulo
    document.write_date(dict_especifico['dt_coleta_histopat'], (67, 299), spacing=2, pg=1) #data_coleta_histopat
    document.write_mini(dict_especifico['resultado_histopat'], (550, 283), pg=1) #resultado_histopat
    document.write_mini(dict_especifico['tp_trat_especifico'], (185, 316), pg=1) #tp_trat_especifico
    document.write_mini(dict_especifico['tp_trat_sintomatico'], (185, 330), pg=1) #tp_trat_sintomatico
    document.write_mini(dict_especifico['droga_trat'], (414, 325), pg=1) #droga_trat
    document.write_code(dict_especifico['tempo_trat'], (486, 333),space=3, pg=1) #tempo_trat
    document.write_mini(dict_especifico['medida_triato'], (152, 371), pg=1) #medida_triato
    document.write_mini(dict_especifico['medida_fiscal'], (152, 387), pg=1) #medida_fiscal
    document.write_mini(dict_especifico['medida_implant'], (350, 371), pg=1) #medida_implant
    document.write_mini(dict_especifico['medida_outro'], (350, 387), pg=1) #medida_outro
    document.write_mini(dict_especifico['medida_outro_descricao'], (390, 386), pg=1) #medida_outro_descricao
    document.write_mini(dict_especifico['classif_final'], (152, 410), pg=1) #classif_final
    document.write_mini(dict_especifico['criterio_confirm'], (280, 418), pg=1) #criterio_confirm
    document.write_mini(dict_especifico['evolucao_caso'], (432, 409), pg=1) #evolucao_caso
    document.write_date(dict_especifico['dt_obito'], (458, 430), spacing=2, pg=1) #data_obito
    document.write_mini(dict_especifico['modo_infeccao'], (302, 459), pg=1) #modo_infeccao
    document.write_mini(dict_especifico['modo_infeccao_outro'], (195, 473), pg=1) #modo_infeccao_outro
    document.write_mini(dict_especifico['local_infeccao'], (557, 458), pg=1) #local_infeccao
    document.write_mini(dict_especifico['caso_autoctone'], (308, 495), pg=1) #caso_autoctone
    document.write_uf(dict_especifico['uf_infeccao2'], (349, 506), pg=1) #uf_infeccao
    document.write_text(dict_especifico['pais_infeccao2'], (383, 506), pg=1) #pais_infeccao
    document.write_text(dict_especifico['municipio_infeccao2'], (63, 535), pg=1) #municipio_infeccao
    document.write_code(dict_especifico['cod_ibge_infeccao2'], (211, 536),space=2, pg=1) #cod_ibge_infeccao
    document.write_text(dict_especifico['distrito_infeccao2'], (308, 536), pg=1) #distrito_infeccao
    document.write_text(dict_especifico['bairro_infeccao2'], (450, 536), pg=1) #bairro_infeccao
    document.write_mini(dict_especifico['doenca_rel_trab'], (431, 553), pg=1) #doenca_rel_trab
    document.write_date(dict_especifico['dt_encerramento'], (457, 565), spacing=2, pg=1) #data_encerramento
    document.write_box(dict_especifico['obs_adicionais'],rect=(32, 588 ,569, 724), pg=1) #obs_adicionais
    document.write_text(dict_especifico['municipio_us_investigador'], (60, 766), pg=1) #municipio_us_investigador
    document.write_code(dict_especifico['cod_us_investigador'], (468, 766),space=2, pg=1) #cod_us_investigador
    document.write_text(dict_especifico['nome_investigador'], (58, 795), pg=1) #nome_investigador
    document.write_text(dict_especifico['funcao_investigador'], (265, 795), pg=1) #funcao_investigador
    document.write_text(dict_especifico['assinatura_investigador'], (470, 795), pg=1) #assinatura_investigador

    document.save(nome_arquivo, path_pdf_gerado, notificatoriaCSV, modelo_pdf_base)