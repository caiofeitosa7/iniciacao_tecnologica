from pdfWritter import PDFWriter
pdf = 'fichas/prioridades/Doença de Chagas Aguda1.pdf'
doc = PDFWriter(pdf)

notificatoria = {
    "numero_ficha": "15485",
    "tipo_notificacao": "9",
    "agravoDoenca": "observacao",
    "dt_notificacao": "15/02/2022",
    "uf_notificacao": "PI",
    "municipio_notificacao": "observacao",
    "cod_ibge_notificacao": "123456",
    "unidade_saude": "25",
    "cod_unidade_saude": "123456",
    "dt_sintomas": "15/02/2022",
    "nome_paciente": "observacao",
    "dt_nascimento": "15/02/2022",
    "idade": "25",
    "tipo_idade": "25",
    "sexo": "observacao",
    "gestante": "9",
    "raca": "9",
    "escolaridade": "25",
    "numero_sus": "123456789012345",
    "nome_mae": "observacao",
    "dt_primeiro_sintoma": "15/02/2022",
    "numero_casos_suspeitos": "123456789012345",
    "local_inicial_ocorrencia": "9",
    "local_inicial_ocorrencia_outro": "observacao",
    "uf_residencia": "PI",
    "municipio_residencia": "observacao",
    "cod_ibge_residencia": "123456",
    "distrito_residencia": "observacao",
    "bairro_residencia": "observacao",
    "logradouro_residencia": "observacao",
    "codigo_residencia": "123456",
    "numero_residencia": "15485",
    "complemento_residencia": "observacao",
    "geo_campo1": "observacao",
    "geo_campo2": "observacao",
    "ponto_ref_residencia": "observacao",
    "cep_residencia": "64000000",
    "telefone_residencia": "86999999999",
    "zona_residencia": "9",
    "pais_residencia": "observacao",
    "municipio_us_notificante": "observacao",
    "nome_notificante": "observacao",
    "funcao_notificante": "observacao",
    "assinatura_notificante": "observacao",
    "dt_amostra_sorologia": "15/02/2022",
    "dt_outra_amostra": "15/02/2022",
    "tipo_exame": "observacao",
    "obito": "9",
    "caso_semelhante": "9",
    "exantema": "9",
    "dt_inicio_exantema": "15/02/2022",
    "petequiaSufusao": "PI",
    "liquor": "9",
    "bacterioscopia": "observacao",
    "tomou_vacina": "9",
    "dt_ultima_dose_tomada": "15/02/2022",
    "hospitalizacao": "9",
    "dt_hospitalizacao": "15/02/2022",
    "uf_hospital": "PI",
    "municipio_hospital": "observacao",
    "cod_ibge_hospital": "123456",
    "nome_hospital": "observacao",
    "cod_hospital": "123456",
    "hipotese_diagnostica1": "observacao",
    "hipotese_diagnostica2": "observacao",
    "pais_infeccao": "observacao",
    "distrito_infeccao": "observacao",
    "uf_infeccao": "PI",
    "municipio_infeccao": "observacao",
    "bairro_infeccao": "observacao"
}
especifico = {
    "numero_ficha2": "15485",
    "dt_notificacao2": "15/02/2022",
    "uf_notificacao2": "PI",
    "municipio_notificacao2": "observacao",
    "cod_ibge_notificacao2": "123456",
    "unidade_saude2": "observacao",
    "cod_unidade_saude2": "123456",
    "dt_sintomas2": "15/02/2022",
    "nome_paciente2": "observacao",
    "dt_nascimento2": "15/02/2022",
    "idade2": "25",
    "tipo_idade2": "4",
    "sexo2": "9",
    "gestante2": "9",
    "raca2": "9",
    "escolaridade2": "25",
    "numero_sus2": "123456789012345",
    "nome_mae2": "observacao",
    "uf_residencia2": "PI",
    "municipio_residencia2": "observacao",
    "cod_ibge_residencia2": "123456",
    "distrito_residencia2": "observacao",
    "bairro_residencia2": "observacao",
    "logradouro_residencia2": "observacao",
    "codigo_residencia2": "123456",
    "numero_residencia2": "15485",
    "complemento_residencia2": "observacao",
    "geo_campo1_2": "observacao",
    "geo_campo2_2": "observacao",
    "ponto_ref_residencia2": "observacao",
    "cep_residencia2": "64000000",
    "telefone_residencia2": "86999999999",
    "zona_residencia2": "9",
    "pais_residencia2": "observacao",
    "dt_investigacao": "15/02/2022",
    "ocupacao": "observacao",
    "uf_desloc1": "PI",
    "municipio_desloc1": "observacao",
    "uf_desloc2": "PI",
    "municipio_desloc2": "observacao",
    "uf_desloc3": "PI",
    "municipio_desloc3": "observacao",
    "pres_triat_intra_dom": "9",
    "dt_encontro_vestigio": "15/02/2022",
    "hist_uso_sangue": "9",
    "contr_soro_un_hemo": "9",
    "manip_t_cruzi": "9",
    "mae_infec_chag": "9",
    "possiv_trans_oral": "9",
    "sint_assint": "9",
    "sint_febre": "9",
    "sint_astenia": "9",
    "sint_edema": "9",
    "sint_hepato": "9",
    "sint_espleno": "9",
    "sint_mening": "9",
    "sint_icc": "9",
    "sint_chagoma": "9",
    "sint_poliade": "9",
    "sint_taquicardia": "9",
    "sint_outro": "9",
    "sint_outro_descricao": "observacao",
    "dt_paras_direto": "15/02/2022",
    "paras_dir_ex_fresc": "9",
    "paras_dir_strout": "9",
    "paras_dir_outro": "9",
    "dt_paras_indireto": "15/02/2022",
    "paras_indir_xeno": "9",
    "paras_indir_hemo": "9",
    "dt_coleta_s1": "15/02/2022",
    "dt_coleta_s2": "15/02/2022",
    "elisa_igm_s1": "9",
    "elisa_igm_s2": "9",
    "elisa_igg_s1": "9",
    "elisa_igg_s2": "9",
    "hemo_igm_s1": "9",
    "hemo_igm_s2": "9",
    "hemo_igg_s1": "9",
    "hemo_igg_s2": "9",
    "ifi_igm_s1": "9",
    "ifi_igm_s1_titulo": "12345",
    "ifi_igm_s2": "9",
    "ifi_igm_s2_titulo": "12345",
    "ifi_igg_s1": "9",
    "ifi_igg_s1_titulo": "12345",
    "ifi_igg_s2": "9",
    "ifi_igg_s2_titulo": "12345",
    "dt_coleta_histopat": "15/02/2022",
    "resultado_histopat": "9",
    "tp_trat_especifico": "9",
    "tp_trat_sintomatico": "9",
    "droga_trat": "9",
    "tempo_trat": "999",
    "medida_triato": "9",
    "medida_fiscal": "9",
    "medida_implant": "9",
    "medida_outro": "9",
    "medida_outro_descricao": "observacao",
    "classif_final": "9",
    "criterio_confirm": "9",
    "evolucao_caso": "9",
    "dt_obito": "15/02/2022",
    "modo_infeccao": "9",
    "modo_infeccao_outro": "observacao",
    "local_infeccao": "9",
    "caso_autoctone": "9",
    "uf_infeccao2": "PI",
    "pais_infeccao2": "observacao",
    "municipio_infeccao2": "observacao",
    "cod_ibge_infeccao2": "123456",
    "distrito_infeccao2": "observacao",
    "bairro_infeccao2": "observacao",
    "doenca_rel_trab": "9",
    "dt_encerramento": "15/02/2022",
    "obs_adicionais": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc.",
    "municipio_us_investigador": "observacao",
    "cod_us_investigador": "123456",
    "nome_investigador": "observacao",
    "funcao_investigador": "observacao",
    "assinatura_investigador": "observacao"
}

###################################################
# Dados do paciente
###################################################
doc.write_text(especifico['numero_ficha2'],(470, 48))
doc.write_date(especifico['dt_notificacao2'], (448, 178), spacing=2) #data_notificacao
doc.write_uf(especifico['uf_notificacao2'], (56, 208)) #uf_notificacao
doc.write_text(especifico['municipio_notificacao2'], (88, 208)) #municipio_notificacao __unid_saude 55,space=220
doc.write_code(especifico['cod_ibge_notificacao2'], (478, 208),space=2) #cod_ibge
doc.write_text(especifico['unidade_saude2'], (65, 235)) #cod_unid_saude
doc.write_code(especifico['cod_unidade_saude2'], (339, 235),space=2) #cod_unid_saude
doc.write_date(especifico['dt_sintomas2'], (446, 235), spacing=2) #data_diagnostico
##############################################
#####          NOTIFICACAO INDIVIDUAL     ####
##############################################
doc.write_text(especifico['nome_paciente2'], (62, 267)) #nome
doc.write_date(especifico['dt_nascimento2'], (449, 266), spacing=2) #data_nascimento
doc.write_code(especifico['idade2'], (65, 296),space=2) #idade
doc.write_mini(especifico['tipo_idade2'], (112, 288)) #tipo_idade
doc.write_mini(especifico['sexo2'], (235, 281)) #sexo
doc.write_mini(especifico['gestante2'], (429, 281)) #gestante
doc.write_mini(especifico['raca2'], (554, 282)) #raça/cor
doc.write_mini(especifico['escolaridade2'], (555, 311)) #escolaridade
doc.write_code(especifico['numero_sus2'], (58, 356),space=2, font_size=10) #cartao_sus
doc.write_text(especifico['nome_mae2'], (240, 356)) #nome_mae
##############################################
#####          DADOS DE RESIDENCIA        ####
##############################################

doc.write_uf(especifico['uf_residencia2'], (58, 387)) #uf_residencia
doc.write_text(especifico['municipio_residencia2'], (92, 386)) #municipio_residencia
doc.write_code(especifico['cod_ibge_residencia2'], (328, 386),space=2) #cod_ibge_residencia
doc.write_text(especifico['distrito_residencia2'], (422, 386)) #endereco
doc.write_text(especifico['bairro_residencia2'], (64, 410)) #bairro
doc.write_text(especifico['logradouro_residencia2'], (207, 412)) #logradouro
doc.write_code(especifico['codigo_residencia2'], (481, 412),space=2) #cod_logradouro
doc.write_text(especifico['numero_residencia2'], (65, 435)) #numero
doc.write_text(especifico['complemento_residencia2'], (120, 436)) #complemento
doc.write_text(especifico['geo_campo1_2'], (415, 438)) #geo_campo_1
doc.write_text(especifico['geo_campo2_2'], (60, 460)) #geo_campo_2
doc.write_text(especifico['ponto_ref_residencia2'], (230, 462)) #ponto_ref
doc.write_code(especifico['cep_residencia2'], (456, 463),space=2) #cep
doc.write_telefone(especifico['telefone_residencia2'], (57, 488), space=2) #telefone
doc.write_mini(especifico['zona_residencia2'], (336, 476)) #zona
doc.write_text(especifico['pais_residencia2'], (365, 488)) #pais
####################################################
# Dados Complementares
####################################################
doc.write_date(especifico['dt_investigacao'], (66, 538), spacing=2) #data_investigacao
doc.write_text(especifico['ocupacao'], (190, 538)) #ocupacao
doc.write_uf(especifico['uf_desloc1'], (95, 585)) #uf_desloc1
doc.write_text(especifico['municipio_desloc1'], (170, 585)) #municipio_desloc1
doc.write_uf(especifico['uf_desloc2'], (95, 600)) #uf_desloc2
doc.write_text(especifico['municipio_desloc2'], (170, 600)) #municipio_desloc2
doc.write_uf(especifico['uf_desloc3'], (95, 615)) #uf_desloc3
doc.write_text(especifico['municipio_desloc3'], (170, 615)) #municipio_desloc3
doc.write_mini(especifico['pres_triat_intra_dom'], (259, 639)) #pres_triat_intra_dom
doc.write_date(especifico['dt_encontro_vestigio'], (278, 646), spacing=2) #data_encontro_vestigio
doc.write_mini(especifico['hist_uso_sangue'], (549, 632)) #hist_uso_sangue
doc.write_mini(especifico['contr_soro_un_hemo'], (313, 662)) #contr_soro_un_hemo
doc.write_mini(especifico['manip_t_cruzi'], (555, 658)) #manip_t_cruzi
doc.write_mini(especifico['mae_infec_chag'], (312, 701)) #mae_infec_chag
doc.write_mini(especifico['possiv_trans_oral'],(555, 700)) #poss_transmissao_oral
doc.write_mini(especifico['sint_assint'], (79, 740)) #sint_assint
doc.write_mini(especifico['sint_febre'], (79, 755)) #sint_febre
doc.write_mini(especifico['sint_astenia'], (79, 772)) #sint_astenia
doc.write_mini(especifico['sint_edema'], (162, 740)) #sint_edema
doc.write_mini(especifico['sint_hepato'], (162, 756)) #sint_hepato
doc.write_mini(especifico['sint_espleno'], (162, 772)) #sint_espleno
doc.write_mini(especifico['sint_mening'], (264, 739)) #sint_mening
doc.write_mini(especifico['sint_icc'], (264, 752)) #sint_icc
doc.write_mini(especifico['sint_chagoma'], (264, 769)) #sint_chagoma
doc.write_mini(especifico['sint_poliade'], (430, 735)) #sint_poliade
doc.write_mini(especifico['sint_taquicardia'], (430, 749)) #sint_taquicardia
doc.write_mini(especifico['sint_outro'], (430, 764)) #sint_outro
doc.write_mini(especifico['sint_outro_descricao'], (468, 763)) #sint_outro_descricao
#################################################### fim da pagina 1

doc.write_date(especifico['dt_paras_direto'], (64, 75), spacing=2, pg=1) #data_paras_direto
doc.write_mini(especifico['paras_dir_ex_fresc'], (357,59), pg=1) #paras_dir_ex_fresc
doc.write_mini(especifico['paras_dir_strout'], (357, 73), pg=1) #paras_dir_strout
doc.write_mini(especifico['paras_dir_outro'], (531, 58), pg=1) #paras_dir_outro
doc.write_date(especifico['dt_paras_indireto'], (64, 115), spacing=2, pg=1) #data_paras_indireto
doc.write_mini(especifico['paras_indir_xeno'], (391, 106), pg=1) #paras_indir_xeno
doc.write_mini(especifico['paras_indir_hemo'], (506, 107), pg=1) #paras_indir_hemo
doc.write_date(especifico['dt_coleta_s1'], (64, 156), spacing=2, pg=1) #data_coleta_s1
doc.write_date(especifico['dt_coleta_s2'], (64, 190), spacing=2, pg=1) #data_coleta_s2
doc.write_mini(especifico['elisa_igm_s1'], (293, 163), pg=1) #elisa_igm_s1
doc.write_mini(especifico['elisa_igm_s2'], (293, 175), pg=1) #elisa_igm_s2
doc.write_mini(especifico['elisa_igg_s1'], (327, 161), pg=1) #elisa_igg_s1
doc.write_mini(especifico['elisa_igg_s2'], (327, 174), pg=1) #elisa_igg_s2
doc.write_mini(especifico['hemo_igm_s1'], (486, 165), pg=1) #hemo_igm_s1
doc.write_mini(especifico['hemo_igm_s2'], (486, 178), pg=1) #hemo_igm_s2
doc.write_mini(especifico['hemo_igg_s1'], (520, 163), pg=1) #hemo_igg_s1
doc.write_mini(especifico['hemo_igg_s2'], (520, 176), pg=1) #hemo_igg_s2
doc.write_mini(especifico['ifi_igm_s1'], (211, 232), pg=1) #ifi_igm_s1
doc.write_code(especifico['ifi_igm_s1_titulo'], (255, 236),space=2, pg=1) #ifi_igm_s1_titulo
doc.write_mini(especifico['ifi_igm_s2'], (211, 260), pg=1) #ifi_igm_s2
doc.write_code(especifico['ifi_igm_s2_titulo'], (255, 260),space=2, pg=1) #ifi_igm_s2_titulo
doc.write_mini(especifico['ifi_igg_s1'], (410, 232), pg=1) #ifi_igg_s1
doc.write_code(especifico['ifi_igg_s1_titulo'], (454, 236),space=2, pg=1) #ifi_igg_s1_titulo
doc.write_mini(especifico['ifi_igg_s2'], (410, 260), pg=1) #ifi_igg_s2
doc.write_code(especifico['ifi_igg_s2_titulo'], (454, 260),space=2, pg=1) #ifi_igg_s2_titulo
doc.write_date(especifico['dt_coleta_histopat'], (67, 299), spacing=2, pg=1) #data_coleta_histopat
doc.write_mini(especifico['resultado_histopat'], (550, 283), pg=1) #resultado_histopat
doc.write_mini(especifico['tp_trat_especifico'], (185, 316), pg=1) #tp_trat_especifico
doc.write_mini(especifico['tp_trat_sintomatico'], (185, 330), pg=1) #tp_trat_sintomatico
doc.write_mini(especifico['droga_trat'], (414, 325), pg=1) #droga_trat
doc.write_code(especifico['tempo_trat'], (486, 333),space=3, pg=1) #tempo_trat
doc.write_mini(especifico['medida_triato'], (152, 371), pg=1) #medida_triato
doc.write_mini(especifico['medida_fiscal'], (152, 387), pg=1) #medida_fiscal
doc.write_mini(especifico['medida_implant'], (350, 371), pg=1) #medida_implant
doc.write_mini(especifico['medida_outro'], (350, 387), pg=1) #medida_outro
doc.write_mini(especifico['medida_outro_descricao'], (390, 386), pg=1) #medida_outro_descricao
doc.write_mini(especifico['classif_final'], (152, 410), pg=1) #classif_final
doc.write_mini(especifico['criterio_confirm'], (280, 418), pg=1) #criterio_confirm
doc.write_mini(especifico['evolucao_caso'], (432, 409), pg=1) #evolucao_caso
doc.write_date(especifico['dt_obito'], (458, 430), spacing=2, pg=1) #data_obito
doc.write_mini(especifico['modo_infeccao'], (302, 459), pg=1) #modo_infeccao
doc.write_mini(especifico['modo_infeccao_outro'], (195, 473), pg=1) #modo_infeccao_outro
doc.write_mini(especifico['local_infeccao'], (557, 458), pg=1) #local_infeccao
doc.write_mini(especifico['caso_autoctone'], (308, 495), pg=1) #caso_autoctone
doc.write_uf(especifico['uf_infeccao2'], (349, 506), pg=1) #uf_infeccao
doc.write_text(especifico['pais_infeccao2'], (383, 506), pg=1) #pais_infeccao
doc.write_text(especifico['municipio_infeccao2'], (63, 535), pg=1) #municipio_infeccao
doc.write_code(especifico['cod_ibge_infeccao2'], (211, 536),space=2, pg=1) #cod_ibge_infeccao
doc.write_text(especifico['distrito_infeccao2'], (308, 536), pg=1) #distrito_infeccao
doc.write_text(especifico['bairro_infeccao2'], (450, 536), pg=1) #bairro_infeccao
doc.write_mini(especifico['doenca_rel_trab'], (431, 553), pg=1) #doenca_rel_trab
doc.write_date(especifico['dt_encerramento'], (457, 565), spacing=2, pg=1) #data_encerramento
doc.write_box(especifico['obs_adicionais'],rect=(32, 588 ,569, 724), pg=1) #obs_adicionais
doc.write_text(especifico['municipio_us_investigador'], (60, 766), pg=1) #municipio_us_investigador
doc.write_code(especifico['cod_us_investigador'], (468, 766),space=2, pg=1) #cod_us_investigador
doc.write_text(especifico['nome_investigador'], (58, 795), pg=1) #nome_investigador
doc.write_text(especifico['funcao_investigador'], (265, 795), pg=1) #funcao_investigador
doc.write_text(especifico['assinatura_investigador'], (470, 795), pg=1) #assinatura_investigador

doc.save('doenca_chagas_aguda.pdf', notificatoria)