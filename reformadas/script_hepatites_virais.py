from pdfWritter import PDFWriter
pdf = 'fichas/prioridades/Hepatites1.pdf'
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
    "unidade_saude2": "25",
    "cod_unidade_saude2": "123456",
    "dt_sintomas2": "15/02/2022",
    "nome_paciente2": "observacao",
    "dt_nascimento2": "15/02/2022",
    "idade2": "25",
    "tipo_idade2": "9",
    "sexo2": "9",
    "gestante2": "9",
    "raca2": "9",
    "escolaridade2": "9",
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
    "suspeita": "3",
    "vacina_hepa": "9",
    "vacina_hepb": "9",
    "institucionalizado": "9",
    "agrav_assoc_hiv": "9",
    "agrav_assoc_dst": "9",
    "contat_pac_sex": "9",
    "contat_pec_dom": "9",
    "contat_pac_ocu": "9",
    "exp_med_inj": "9",
    "exp_crack": "9",
    "exp_drog_inj": "9",
    "exp_agua": "9",
    "exp_sex": "9",
    "exp_transplante": "9",
    "exp_tatu": "9",
    "exp_acupuntura": "9",
    "exp_trat_cirurg": "9",
    "exp_trat_dent": "9",
    "exp_hemodialise": "9",
    "exp_outras": "9",
    "exp_acid_mat_bio": "9",
    "exp_transf_sang": "9",
    "dt_acid_transf": "15/02/2022",
    "uf_exp1": "PI",
    "municipio_exp1": "observacao",
    "local_exp1": "observacao",
    "fone_exp1": "observacao",
    "uf_exp2": "PI",
    "municipio_exp2": "observacao",
    "local_exp2": "observacao",
    "fone_exp2": "observacao",
    "uf_exp3": "PI",
    "municipio_exp3": "observacao",
    "local_exp3": "observacao",
    "fone_exp3": "observacao",
    "comun_nome1": "observacao",
    "comun_idade1": "25",
    "comun_tp_cont1": "9",
    "comun_hbsag1": "9",
    "comun_anti_hbc1": "9",
    "comun_anti_hcv1": "9",
    "comun_vac_hepb1": "9",
    "comun_imuno_hepb1": "9",
    "comun_nome2": "observacao",
    "comun_idade2": "25",
    "comun_tp_cont2": "9",
    "comun_hbsag2": "9",
    "comun_anti_hbc2": "9",
    "comun_anti_hcv2": "9",
    "comun_vac_hepb2": "9",
    "comun_imuno_hepb2": "9",
    "comun_nome3": "observacao",
    "comun_idade3": "25",
    "comun_tp_cont3": "9",
    "comun_hbsag3": "9",
    "comun_anti_hbc3": "9",
    "comun_anti_hcv3": "9",
    "comun_vac_hepb3": "9",
    "comun_imuno_hepb3": "9",
    "comun_nome4": "observacao",
    "comun_idade4": "25",
    "comun_tp_cont4": "9",
    "comun_hbsag4": "9",
    "comun_anti_hbc4": "9",
    "comun_anti_hcv4": "9",
    "comun_vac_hepb4": "9",
    "comun_imuno_hepb4": "9",
    "comun_nome5": "observacao",
    "comun_idade5": "25",
    "comun_tp_cont5": "9",
    "comun_hbsag5": "9",
    "comun_anti_hbc5": "9",
    "comun_anti_hcv5": "9",
    "comun_vac_hepb5": "9",
    "comun_imuno_hepb5": "9",
    "pac_encamin": "9",
    "dt_amostra_cta": "15/02/2022",
    "res_soro_hbsag": "9",
    "res_soro_anti_hbc": "9",
    "res_soro_anti_hcv": "9",
    "dt_sorologia": "15/02/2022",
    "genotipo_hcv": "9",
    "res_vir_hav_igm": "9",
    "res_vir_hbsag": "9",
    "res_vir_hbc_igm": "9",
    "res_vir_hbc_total": "9",
    "res_vir_hbs": "9",
    "res_vir_hbeag": "9",
    "res_vir_hbe": "9",
    "res_vir_hdv_total": "9",
    "res_vir_hdv_igm": "9",
    "res_vir_hev_igm": "9",
    "res_vir_hcv": "9",
    "res_vir_hcv_rna": "9",
    "classif_final": "9",
    "forma_clinica": "9",
    "classif_etiologica": "99",
    "mecan_infeccao": "99",
    "mecan_infeccao_outros": "observacao",
    "dt_encerramento": "15/02/2022",
    "obs_adicionais": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc.",
    "municipio_us_investigador": "observacao",
    "cod_us_investigador": "123456",
    "nome_investigador": "observacao",
    "funcao_investigador": "observacao",
    "assinatura_investigador": "observacao"
}

###################################################
# Dados do paciente
###################################################
doc.write_text(especifico['numero_ficha2'],(470, 46))
doc.write_date(especifico['dt_notificacao2'], (446, 287), spacing=2) #data_notificacao
doc.write_uf(especifico['uf_notificacao2'], (56, 318)) #uf_notificacao
doc.write_text(especifico['municipio_notificacao2'], (95, 318)) #municipio_notificacao __unid_saude 55,space=220
doc.write_code(especifico['cod_ibge_notificacao2'], (480, 318),space=2) #cod_ibge
doc.write_text(especifico['unidade_saude2'], (62, 346)) #unid_saude
doc.write_code(especifico['cod_unidade_saude2'], (339, 346),space=2) #cod_unid_saude
doc.write_date(especifico['dt_sintomas2'], (446, 345), spacing=2) #data_diagnostico
##############################################
#####          NOTIFICACAO INDIVIDUAL     ####
##############################################
doc.write_text(especifico['nome_paciente2'], (65, 376)) #nome
doc.write_date(especifico['dt_nascimento2'], (450, 376),spacing=2) #data_nascimento
doc.write_code(especifico['idade2'], (64, 406),space=2) #idade
doc.write_mini(especifico['tipo_idade2'], (111, 399)) #tipo_idade
doc.write_mini(especifico['sexo2'], (233, 392)) #sexo
doc.write_mini(especifico['gestante2'], (427, 392)) #gestante
doc.write_mini(especifico['raca2'], (552, 393)) #raça/cor
doc.write_mini(especifico['escolaridade2'], (553, 422)) #escolaridade
doc.write_code(especifico['numero_sus2'], (56, 466),space=2, font_size=10) #cartao_sus
doc.write_text(especifico['nome_mae2'], (240, 466)) #nome_mae
##############################################
#####          DADOS DE RESIDENCIA        ####
##############################################

doc.write_uf(especifico['uf_residencia2'], (58, 497)) #uf_residencia
doc.write_text(especifico['municipio_residencia2'], (90, 496)) #municipio_residencia
doc.write_code(especifico['cod_ibge_residencia2'], (328, 496),space=2) #cod_ibge_residencia
doc.write_text(especifico['distrito_residencia2'], (420, 496)) #endereco
doc.write_text(especifico['bairro_residencia2'], (60, 520)) #bairro
doc.write_text(especifico['logradouro_residencia2'], (205, 522)) #logradouro
doc.write_code(especifico['codigo_residencia2'], (480, 522),space=2) #cod_logradouro
doc.write_text(especifico['numero_residencia2'], (62, 545)) #numero
doc.write_text(especifico['complemento_residencia2'], (120, 545)) #complemento
doc.write_text(especifico['geo_campo1_2'], (420, 547)) #geo_campo_1
doc.write_text(especifico['geo_campo2_2'], (65, 570)) #geo_campo_2
doc.write_text(especifico['ponto_ref_residencia2'], (230, 571)) #ponto_ref
doc.write_code(especifico['cep_residencia2'], (455, 573),space=2) #cep
doc.write_telefone(especifico['telefone_residencia2'], (56, 598), space=2) #telefone
doc.write_mini(especifico['zona_residencia2'], (333, 586)) #zona
doc.write_text(especifico['pais_residencia2'], (365, 598)) #pais
###################################################
# Dados complementares                            #
###################################################
doc.write_date(especifico['dt_investigacao'], (62, 650), spacing=2) #data_investigacao
doc.write_text(especifico['ocupacao'], (190, 650)) #ocupacao
doc.write_code(especifico['suspeita'], (135, 668)) #suspeita
doc.write_mini(especifico['vacina_hepa'], (460, 669)) #vacina_hepa
doc.write_mini(especifico['vacina_hepb'], (459, 686)) #vacina_hepb
doc.write_mini(especifico['institucionalizado'], (504, 708)) #institucionalizado
doc.write_mini(especifico['agrav_assoc_hiv'], (183, 752)) #agrav_assoc_hiv
doc.write_mini(especifico['agrav_assoc_dst'], (183, 766)) #agrav_assoc_dst
doc.write_mini(especifico['contat_pac_sex'], (463,743)) #contat_pac_sex
doc.write_mini(especifico['contat_pec_dom'], (464, 756)) #contat_pec_dom
doc.write_mini(especifico['contat_pac_ocu'], (464, 769)) #contat_pac_ocu
################################################### fim da pagina 1
doc.write_mini(especifico['exp_med_inj'], (66, 62), pg=1) #exp_med_inj
doc.write_mini(especifico['exp_crack'], (66, 79), pg=1) #exp_crack
doc.write_mini(especifico['exp_drog_inj'], (66, 95), pg=1) #exp_drog_inj
doc.write_mini(especifico['exp_agua'], (66, 112), pg=1) #exp_agua
doc.write_mini(especifico['exp_sex'], (66, 127),pg=1) #exposicao sexual
doc.write_mini(especifico['exp_transplante'], (66,141), pg=1) #exp_transplante
doc.write_mini(especifico['exp_tatu'], (267, 62), pg=1) #exp_tatu
doc.write_mini(especifico['exp_acupuntura'], (267, 79), pg=1) #exp_acupuntura
doc.write_mini(especifico['exp_trat_cirurg'], (267, 94), pg=1) #exp_trat_cirurg
doc.write_mini(especifico['exp_trat_dent'], (267, 112), pg=1) #exp_trat_dent
doc.write_mini(especifico['exp_hemodialise'], (266, 127), pg=1) #exp_hemodialise
doc.write_mini(especifico['exp_outras'], (266, 139), pg=1) #exp_outras
doc.write_mini(especifico['exp_acid_mat_bio'], (405, 61), pg=1) #exp_acid_mat_bio
doc.write_mini(especifico['exp_transf_sang'], (405, 78), pg=1) #exp_transf_sang
doc.write_date(especifico['dt_acid_transf'], (393, 135), pg=1, spacing=2) #dt_acid_transf
doc.write_uf(especifico['uf_exp1'], (57, 189), pg=1) #uf_exp1
doc.write_text(especifico['municipio_exp1'], (80, 189), pg=1) #municipio_exp1
doc.write_text(especifico['local_exp1'], (250, 189), pg=1) #local_exp1
doc.write_telefone(especifico['fone_exp1'], (485, 189), pg=1) #fone_exp1
doc.write_uf(especifico['uf_exp2'], (57, 202), pg=1) #uf_exp2
doc.write_text(especifico['municipio_exp2'], (80, 202), pg=1) #municipio_exp2
doc.write_text(especifico['local_exp2'], (250, 202), pg=1) #local_exp2
doc.write_telefone(especifico['fone_exp2'], (485, 202), pg=1) #fone_exp2
doc.write_uf(especifico['uf_exp3'], (57, 215), pg=1) #uf_exp3
doc.write_text(especifico['municipio_exp3'], (80, 215), pg=1) #municipio_exp3
doc.write_text(especifico['local_exp3'], (250, 215), pg=1) #local_exp3
doc.write_telefone(especifico['fone_exp3'], (485, 215), pg=1) #fone_exp3
################ quadro comunicantes
doc.write_text(especifico['comun_nome1'], (57, 302), pg=1) #comun_nome1
doc.write_code(especifico['comun_idade1'], (135, 302), pg=1) #comun_idade1
doc.write_text(especifico['comun_tp_cont1'], (195, 302), pg=1) #comun_tp_cont1
doc.write_text(especifico['comun_hbsag1'], (262, 302), pg=1) #comun_hbsag1
doc.write_text(especifico['comun_anti_hbc1'], (315, 302), pg=1) #comun_anti_hbc1
doc.write_text(especifico['comun_anti_hcv1'], (380, 302), pg=1) #comun_anti_hcv1
doc.write_text(especifico['comun_vac_hepb1'], (445, 302), pg=1) #comun_vac_hepb1
doc.write_text(especifico['comun_imuno_hepb1'], (520, 302), pg=1) #comun_imuno_hepb1
doc.write_text(especifico['comun_nome2'], (57, 315), pg=1) #comun_nome2
doc.write_code(especifico['comun_idade2'], (135, 315), pg=1) #comun_idade2
doc.write_text(especifico['comun_tp_cont2'], (195, 315), pg=1) #comun_tp_cont2
doc.write_text(especifico['comun_hbsag2'], (262, 315), pg=1) #comun_hbsag2
doc.write_text(especifico['comun_anti_hbc2'], (315, 315), pg=1) #comun_anti_hbc2
doc.write_text(especifico['comun_anti_hcv2'], (380, 315), pg=1) #comun_anti_hcv2
doc.write_text(especifico['comun_vac_hepb2'], (445, 315), pg=1) #comun_vac_hepb2
doc.write_text(especifico['comun_imuno_hepb2'], (520, 315), pg=1) #comun_imuno_hepb2
doc.write_text(especifico['comun_nome3'], (57, 327), pg=1) #comun_nome3
doc.write_code(especifico['comun_idade3'], (135, 327), pg=1) #comun_idade3
doc.write_text(especifico['comun_tp_cont3'], (195, 327), pg=1) #comun_tp_cont3
doc.write_text(especifico['comun_hbsag3'], (262, 327), pg=1) #comun_hbsag3
doc.write_text(especifico['comun_anti_hbc3'], (315, 327), pg=1) #comun_anti_hbc3
doc.write_text(especifico['comun_anti_hcv3'], (380, 327), pg=1) #comun_anti_hcv3
doc.write_text(especifico['comun_vac_hepb3'], (445, 327), pg=1) #comun_vac_hepb3
doc.write_text(especifico['comun_imuno_hepb3'], (520, 327), pg=1) #comun_imuno_hepb3
doc.write_text(especifico['comun_nome4'], (57, 340), pg=1) #comun_nome4
doc.write_code(especifico['comun_idade4'], (135, 340), pg=1) #comun_idade4
doc.write_text(especifico['comun_tp_cont4'], (195, 340), pg=1) #comun_tp_cont4
doc.write_text(especifico['comun_hbsag4'], (262, 340), pg=1) #comun_hbsag4
doc.write_text(especifico['comun_anti_hbc4'], (315, 340), pg=1) #comun_anti_hbc4
doc.write_text(especifico['comun_anti_hcv4'], (380, 340), pg=1) #comun_anti_hcv4
doc.write_text(especifico['comun_vac_hepb4'], (445, 340), pg=1) #comun_vac_hepb4
doc.write_text(especifico['comun_imuno_hepb4'], (520, 340), pg=1) #comun_imuno_hepb4
doc.write_text(especifico['comun_nome5'], (57, 353), pg=1) #comun_nome5
doc.write_code(especifico['comun_idade5'], (135, 353), pg=1) #comun_idade5
doc.write_text(especifico['comun_tp_cont5'], (195, 353), pg=1) #comun_tp_cont5
doc.write_text(especifico['comun_hbsag5'], (262, 353), pg=1) #comun_hbsag5
doc.write_text(especifico['comun_anti_hbc5'], (315, 353), pg=1) #comun_anti_hbc5
doc.write_text(especifico['comun_anti_hcv5'], (380, 353), pg=1) #comun_anti_hcv5
doc.write_text(especifico['comun_vac_hepb5'], (445, 353), pg=1) #comun_vac_hepb5
doc.write_text(especifico['comun_imuno_hepb5'], (520, 353), pg=1) #comun_imuno_hepb5
############ Dados laboratoriais
doc.write_mini(especifico['pac_encamin'], (208, 368), pg=1) #pac_encamin
doc.write_date(especifico['dt_amostra_cta'], (236, 401), pg=1, spacing=2) #data_amostra
doc.write_mini(especifico['res_soro_hbsag'], (499, 379), pg=1) #res_soro_hbsag
doc.write_mini(especifico['res_soro_anti_hbc'], (499, 392), pg=1) #res_soro_anti_hbc
doc.write_mini(especifico['res_soro_anti_hcv'], (499, 406), pg=1) #res_soro_anti_hcv
doc.write_date(especifico['dt_sorologia'], (118, 438), pg=1, spacing=2) #data_sorologia
doc.write_mini(especifico['genotipo_hcv'], (222, 451), pg=1) #genotipo_hcv
doc.write_mini(especifico['res_vir_hav_igm'], (347, 433), pg=1) #res_vir_hav_igm
doc.write_mini(especifico['res_vir_hbsag'], (347, 446), pg=1) #res_vir_hbsag
doc.write_mini(especifico['res_vir_hbc_igm'], (347, 459), pg=1) #res_vir_hbc_igm
doc.write_mini(especifico['res_vir_hbc_total'], (347, 472), pg=1) #res_vir_hbc_total
doc.write_mini(especifico['res_vir_hbs'], (425, 433), pg=1) #res_vir_hbs
doc.write_mini(especifico['res_vir_hbeag'], (425, 446), pg=1) #res_vir_hbeag
doc.write_mini(especifico['res_vir_hbe'], (425, 459), pg=1) #res_vir_hbe
doc.write_mini(especifico['res_vir_hdv_total'], (425, 472), pg=1) #res_vir_hdv_total
doc.write_mini(especifico['res_vir_hdv_igm'], (496, 430), pg=1) #res_vir_hdv_igm
doc.write_mini(especifico['res_vir_hev_igm'], (496, 444), pg=1) #res_vir_hev_igm
doc.write_mini(especifico['res_vir_hcv'], (496, 459), pg=1) #res_vir_hcv
doc.write_mini(especifico['res_vir_hcv_rna'], (496, 473), pg=1) #res_vir_hcv_rna
############# Conclusao
doc.write_mini(especifico['classif_final'], (230, 496), pg=1) #classif_final
doc.write_mini(especifico['forma_clinica'], (355, 494), pg=1) #forma_clinica
doc.write_code(especifico['classif_etiologica'], (545, 494), pg=1, space=1) #classif_etiologica
doc.write_code(especifico['mecan_infeccao'], (510, 557), pg=1, space=1) #mecan_infeccao
doc.write_mini(especifico['mecan_infeccao_outros'], (476, 582), pg=1) #mecan_infeccao_outros
doc.write_date(especifico['dt_encerramento'], (57, 629), pg=1, spacing=2) #data_encerramento
doc.write_box(especifico['obs_adicionais'], rect=(30, 650,566,735), pg=1) #obs_adicionais
doc.write_text(especifico['municipio_us_investigador'], (62, 770), pg=1) #municipio_us_investigador
doc.write_code(especifico['cod_us_investigador'], (464, 772), pg=1, space=2) #cod_us_investigador
doc.write_text(especifico['nome_investigador'], (62, 805), pg=1) #nome_investigador
doc.write_text(especifico['funcao_investigador'], (264, 805), pg=1) #funcao_investigador
doc.write_text(especifico['assinatura_investigador'], (465, 804), pg=1) #assinatura_investigador










doc.save("hepatitesVirais.pdf", notificatoria)
