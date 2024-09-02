from pdfWritter import PDFWriter

pdf = 'Even Adver Pós-Vacinal1.pdf'
doc = PDFWriter(pdf, default_font_size=8)

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
    "dt_investigacao": "15/02/2022",
    "numero_sus2": "123456789012345",
    "pais_notificacao": "observacao",
    "uf_notificacao2": "PI",
    "municipio_notificacao2": "observacao",
    "us_notificacao": "observacao",
    "nome_paciente2": "observacao",
    "iniciais_paciente": "observacao",
    "dt_nascimento2": "15/02/2022",
    "idade2": "25",
    "tipo_idade2": "25",
    "sexo_num": "9",
    "raca2": "9",
    "ocupacao": "observacao",
    "nome_mae2": "observacao",
    "gestante2": "9",
    "mes_vacina_gest": "observacao",
    "amamentando": "9",
    "aleitamento": "9",
    "logradouro_residencia2": "observacao",
    "numero_residencia2": "15485",
    "complemento_residencia2": "observacao",
    "bairro_residencia2": "observacao",
    "ponto_ref_residencia2": "observacao",
    "zona_residencia2": "9",
    "cep_residencia2": "64000000",
    "telefone_residencia2": "86999999999",
    "telefone2_residencia2": "86999999999",
    "pais_residencia2": "observacao",
    "uf_residencia2": "PI",
    "municipio_residencia2": "observacao",
    "vacinacao_dt1": "15/02/2022",
    "vacinacao_nome1": "observacao",
    "vacinacao_dose1": "2",
    "vacinacao_via_adm1": "observacao",
    "vacinacao_local_aplic1": "observacao",
    "vacinacao_fabri1": "observacao",
    "vacinacao_num_lote1": "9",
    "vacinacao_dt_valid1": "15/02/2022",
    "vacinacao_dt2": "15/02/2022",
    "vacinacao_nome2": "observacao",
    "vacinacao_dose2": "2",
    "vacinacao_via_adm2": "observacao",
    "vacinacao_local_aplic2": "observacao",
    "vacinacao_fabri2": "observacao",
    "vacinacao_num_lote2": "9",
    "vacinacao_dt_valid2": "15/02/2022",
    "vacinacao_dt3": "15/02/2022",
    "vacinacao_nome3": "observacao",
    "vacinacao_dose3": "2",
    "vacinacao_via_adm3": "observacao",
    "vacinacao_local_aplic3": "observacao",
    "vacinacao_fabri3": "observacao",
    "vacinacao_num_lote3": "9",
    "vacinacao_dt_valid3": "15/02/2022",
    "vacinacao_dt4": "15/02/2022",
    "vacinacao_nome4": "observacao",
    "vacinacao_dose4": "2",
    "vacinacao_via_adm4": "observacao",
    "vacinacao_local_aplic4": "observacao",
    "vacinacao_fabri4": "observacao",
    "vacinacao_num_lote4": "9",
    "vacinacao_dt_valid4": "15/02/2022",
    "vacinacao_dt5": "15/02/2022",
    "vacinacao_dose5": "2",
    "vacinacao_via_adm5": "observacao",
    "vacinacao_local_aplic5": "observacao",
    "vacinacao_fabri5": "observacao",
    "vacinacao_num_lote5": "9",
    "vacinacao_dt_valid5": "15/02/2022",
    "vacinacao_dt6": "15/02/2022",
    "vacinacao_nome6": "observacao",
    "vacinacao_dose6": "2",
    "vacinacao_via_adm6": "observacao",
    "vacinacao_local_aplic6": "observacao",
    "vacinacao_fabri6": "observacao",
    "vacinacao_num_lote6": "9",
    "vacinacao_dt_valid6": "15/02/2022",
    "vacinacao_dt7": "15/02/2022",
    "vacinacao_nome7": "observacao",
    "vacinacao_dose7": "2",
    "vacinacao_via_adm7": "observacao",
    "vacinacao_local_aplic7": "observacao",
    "vacinacao_fabri7": "observacao",
    "vacinacao_num_lote7": "9",
    "vacinacao_dt_valid7": "15/02/2022",
    "vacinacao_dt8": "15/02/2022",
    "vacinacao_nome8": "observacao",
    "vacinacao_dose8": "2",
    "vacinacao_via_adm8": "observacao",
    "vacinacao_local_aplic8": "observacao",
    "vacinacao_fabri8": "observacao",
    "vacinacao_num_lote8": "9",
    "vacinacao_dt_valid8": "15/02/2022",
    "vacinacao_dt9": "15/02/2022",
    "vacinacao_nome9": "observacao",
    "vacinacao_dose9": "2",
    "vacinacao_via_adm9": "observacao",
    "vacinacao_local_aplic9": "observacao",
    "vacinacao_fabri9": "observacao",
    "vacinacao_num_lote9": "9",
    "vacinacao_dt_valid9": "15/02/2022",
    "pais_aplicacao": "observacao",
    "uf_aplicacao": "PI",
    "municipio_aplicacao": "observacao",
    "us_aplicacao": "observacao",
    "motivo_aplicacao": "9",
    "local_aplicacao": "9",
    "doenca_preexist": "9",
    "op_doenca_aids_hiv": "9",
    "op_doenca_cardiaca": "9",
    "op_doenca_cardiaca_espec": "observacao",
    "op_doenca_alerg_alim": "9",
    "op_doenca_alerg_alim_espec": "observacao",
    "op_doenca_hepatica": "9",
    "op_doenca_hepatica_espec": "observacao",
    "op_doenca_alerg_med": "9",
    "op_doenca_alerg_med_espc": "observacao",
    "op_doenca_neuro": "9",
    "op_doenca_neuro_espc": "observacao",
    "op_doenca_diabete": "9",
    "op_doenca_pulmonar": "9",
    "op_doenca_pulmonar_espec": "observacao",
    "op_doenca_imune": "9",
    "op_doenca_imune_espec": "observacao",
    "op_doenca_outra": "9",
    "op_doenca_outra_espec": "observacao",
    "med_anter_vacina": "9",
    "op_med_anticonv": "9",
    "op_med_homeo": "9",
    "op_med_antiterm": "9",
    "op_med_quimio": "9",
    "op_med_cort": "9",
    "op_med_cort_via": "observacao",
    "med_tempo_uso": "observacao",
    "op_med_outro": "9",
    "op_med_outro_espec": "observacao",
    "op_med_imunog": "9",
    "transfusao": "9",
    "dt_transfusao": "15/02/2022",
    "hist_convulsoes": "9",
    "tipo_convulsao": "9",
    "eapv_anterior": "9",
    "qual_eapv": "observacao",
    "vac_adm_eapv": "observacao",
    "dt_eapv_anterior": "15/02/2022",
    "conduta_eapv": "observacao",
    "medicacao_eapv": "9",
    "qual_medicacao_eapv": "observacao",
    "viajou_15dias": "9",
    "tipo_viagem": "9",
    "pais_viagem": "observacao",
    "dt_ida_viagem": "15/02/2022",
    "dt_volta_viagem": "15/02/2022",
    "uf_viagem": "PI",
    "municipio_viagem": "observacao",
    "vac_antes_viagem": "9",
    "vac_durante_viagem": "9",
    "dt_vac_durante_viagem": "15/02/2022",
    "qual_vac_tomou": "observacao",
    "mani_loc_abs_frio": "1",
    "mani_loc_edema": "1",
    "mani_loc_linfa3cm": "9",
    "mani_loc_abs_dren": "9",
    "mani_loc_enduracao": "1",
    "mani_loc_linfa_nao_sup": "9",
    "mani_loc_abs_quente": "9",
    "mani_loc_eritema": "1",
    "mani_loc_rubor": "9",
    "mani_loc_atrofia": "1",
    "mani_loc_exan_local": "9",
    "mani_loc_ulcera": "1",
    "mani_loc_calor": "9",
    "mani_loc_exan_gene": "9",
    "mani_loc_outras": "1",
    "mani_loc_celulite": "9",
    "mani_loc_linfadenite_nao_sup": "9",
    "mani_loc_dor": "1",
    "mani_loc_linfadenite_sup": "9",
    "dt_sint_locais": "15/02/2022",
    "dia_vac_manif_loc": "9",
    "hr_vac_manif_loc": "9",
    "min_vac_manif_loc": "9",
    "dias_evento_loc": "9",
    "horas_evento_loc": "9",
    "min_evento_loc": "9",
    "mani_sis_angi_labios": "9",
    "mani_sis_cianose": "9",
    "mani_sis_purpura": "9",
    "mani_sis_angi_laringe": "9",
    "mani_sis_hiper": "9",
    "mani_sis_urti_gener": "9",
    "mani_sis_angi_lingua": "9",
    "mani_sis_ictericia": "1",
    "mani_sis_urti_local": "9",
    "mani_sis_angi_membro": "9",
    "mani_sis_palidez": "1",
    "mani_sis_outro_evento": "9",
    "mani_sis_angi_olho": "9",
    "mani_sis_petequia": "1",
    "mani_sis_angi_gener": "9",
    "mani_sis_prurido": "1",
    "mani_sis_hipotensao": "9",
    "mani_sis_taquicardia": "1",
    "mani_sis_bradicardia": "9",
    "mani_sis_apneia": "1",
    "mani_sis_garganta": "9",
    "mani_sis_fech_garg": "1",
    "mani_sis_bronco": "1",
    "mani_sis_espirro": "9",
    "mani_sis_taquipneia": "9",
    "mani_sis_dif_resp": "1",
    "mani_sis_rinorreia": "9",
    "mani_sis_intercost": "1",
    "mani_sis_dispineia": "9",
    "mani_sis_rouquidao": "1",
    "mani_sis_tosse_seca": "9",
    "mani_sis_ataxia": "1",
    "mani_sis_conv_toni": "9",
    "mani_sis_paresia": "1",
    "mani_sis_nivel_consc": "9",
    "mani_sis_desmaio": "1",
    "mani_sis_parestesia": "1",
    "mani_sis_conv_afeb": "9",
    "mani_sis_hipotonia": "1",
    "mani_sis_resposta": "9",
    "mani_sis_conv_feb": "1",
    "mani_sis_letargia": "1",
    "mani_sis_sin_neuro": "9",
    "mani_sis_conv_focal": "9",
    "mani_sis_nao_resposta": "1",
    "mani_sis_neuro_grave": "9",
    "mani_sis_conv_gener": "1",
    "mani_sis_memb_infer": "9",
    "mani_sis_outra_paral": "9",
    "mani_sis_diarreia": "1",
    "mani_sis_fezes_sang": "9",
    "mani_sis_nausea": "9",
    "mani_sis_abdomen": "1",
    "mani_sis_inva_intest": "9",
    "mani_sis_vomito": "9",
    "mani_sis_enterro": "1",
    "mani_sis_melena": "9",
    "dt_sint_sistem": "15/02/2022",
    "dia_vac_manif_sistem": "9",
    "hr_vac_manif_sistem": "9",
    "min_vac_manif_sistem": "9",
    "dias_evento_sistem": "9",
    "horas_evento_sistem": "1",
    "min_evento_sistem": "9",
    "otr_mani_artralgia": "9",
    "otr_mani_evi_sang": "9",
    "otr_mani_mialgia": "1",
    "otr_mani_artrite": "1",
    "otr_mani_fadiga": "9",
    "otr_mani_pancrea": "1",
    "otr_mani_cefaleia": "1",
    "otr_mani_feb_mais39": "9",
    "otr_mani_parotidite": "1",
    "otr_mani_cefa_vomito": "9",
    "otr_mani_feb_menos39": "1",
    "otr_mani_sonolencia": "1",
    "otr_mani_choro": "1",
    "otr_mani_hiper_bila": "9",
    "otr_mani_outra": "1",
    "otr_mani_dif_deamb": "9",
    "otr_mani_hiper_art": "1",
    "otr_mani_edem_art": "1",
    "otr_mani_lesao_bcg": "9",
    "dt_sint_otr_mani": "15/02/2022",
    "dia_vac_manif_otr_mani": "9",
    "hr_vac_manif_otr_mani": "9",
    "min_vac_manif_otr_mani": "9",
    "dias_evento_otr_mani": "9",
    "horas_evento_otr_mani": "9",
    "min_evento_otr_mani": "9",
    "atend_medico": "9",
    "dt_atendimento": "15/02/2022",
    "tipo_atendimento": "9",
    "ficou_obs": "9",
    "horas_obs": "9",
    "ficou_enfermaria": "9",
    "dias_enfermaria": "9",
    "ficou_uti": "9",
    "dias_uti": "9",
    "dt_alta": "15/02/2022",
    "nome_hosp_atendimento": "observacao",
    "tipo_loc_atendimento": "9",
    "municipio_atendimento": "observacao",
    "uf_atendimento": "PI",
    "dt_col_hemograma": "15/02/2022",
    "hemacias_hemo": "99",
    "hemoglobina_hemo": "99",
    "hematocrito_hemo": "99",
    "plaquetas_hemo": "99",
    "leucocitos_hemo": "99",
    "monocitos_hemo": "99",
    "linfocitos_hemo": "99",
    "neutrofilos_hemo": "99",
    "eosinofilos_hemo": "99",
    "dt_col_bioquimica": "15/02/2022",
    "bili_total_bioq": "99",
    "creatina_bioq": "99",
    "bili_dir_bioq": "99",
    "ast_bioq": "99",
    "inr_bioq": "99",
    "alt_bioq": "99",
    "pt_bioq": "99",
    "ureia_bioq": "99",
    "ptt_bioq": "99",
    "puncao_lombar": "9",
    "dt_puncao": "15/02/2022",
    "leucocitos_cito": "99",
    "glicose_cito": "99",
    "neutrofilos_cito": "99",
    "proteinas_cito": "99",
    "linfocitos_cito": "99",
    "cult_liquor": "9",
    "cult_liquor_espec": "99",
    "bacterioscopia": "9",
    "bacterio_espec": "observacao",
    "deteccao_viral": "9",
    "dt_detec_viral": "15/02/2022",
    "detec_viral_coleta": "9",
    "detec_viral_pcr": "9",
    "detec_viral_outro": "observacao",
    "autopsia": "9",
    "dt_autopsia": "15/02/2022",
    "autop_anatomo": "9",
    "autop_dt_anatomo": "15/02/2022",
    "autop_histo": "9",
    "autop_dt_histo": "15/02/2022",
    "autop_imuno": "9",
    "autop_dt_imuno": "15/02/2022",
    "dt_ecg": "15/02/2022",
    "dt_rm": "15/02/2022",
    "dt_eeg": "15/02/2022",
    "dt_enmg": "15/02/2022",
    "dt_rx": "15/02/2022",
    "dt_usg": "15/02/2022",
    "dt_tc": "15/02/2022",
    "outras_informacoes": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc.",
    "diag_descricao1": "observacao",
    "diag_cid1": "observacao",
    "diag_descricao2": "observacao",
    "diag_cid2": "observacao",
    "diag_descricao3": "observacao",
    "diag_cid3": "observacao",
    "diag_descricao4": "observacao",
    "diag_cid4": "observacao",
    "erro_programa": "9",
    "erro_programa_espec": "observacao",
    "evolucao_caso": "9",
    "dt_obito": "15/02/2022",
    "declara_obito": "observacao",
    "declara_vivo": "observacao",
    "conduta_vacinal": "9",
    "dt_encerramento": "15/02/2022",
    "nome_investigador": "observacao",
    "funcao_investigador": "observacao",
    "telefone_investigador": "86999999999",
    "municipio_us_investigador": "observacao",
    "unid_saude_investigador": "observacao",
    "telefone_us_investigador": "86999999999",
    "assinatura_investigador": "observacao",
    "data_preenchimento": "15/02/2022"
}

###################################################
# Cabeçalho Ficha
###################################################
doc.write_text(especifico['numero_ficha2'], (438,68)) # Número da ficha
doc.write_date(especifico['dt_notificacao2'], (439, 79),spacing=2,font_size=10) # Data da notificação
doc.write_date(especifico['dt_investigacao'], (438, 92), spacing=2, font_size=10) # Data da investigação
doc.write_text(especifico['numero_sus2'], (438, 114), font_size=11) # Número do SUS
doc.write_text(especifico['pais_notificacao'], (60, 197)) # País da notificação
doc.write_text(especifico['uf_notificacao2'], (180, 197)) # UF da notificação
doc.write_text(especifico['municipio_notificacao2'], (210, 197)) # Município da notificação
doc.write_text(especifico['us_notificacao'], (60, 218)) # Unidade de saúde da notificação
###################################################
# Dados do paciente
###################################################
doc.write_text(especifico['nome_paciente2'], (60, 252)) # Nome do paciente
doc.write_text(especifico['iniciais_paciente'], (380, 252)) # Iniciais do paciente
doc.write_date(especifico['dt_nascimento2'], (452, 250), spacing=2, font_size=10) # Data de nascimento
doc.write_text(especifico['idade2'], (62, 280)) # Idade
doc.write_text(especifico['tipo_idade2'], (100, 280)) # Tipo de idade
doc.write_text(especifico['sexo_num'], (210, 280)) # Sexo
doc.write_text(especifico['raca2'], (317, 280)) # Raça
doc.write_text(especifico['ocupacao'], (60, 309)) # Ocupação
doc.write_text(especifico['nome_mae2'], (315, 309)) # Nome da mãe
doc.write_text(especifico['gestante2'], (61, 341)) # Gestante
doc.write_text(especifico['mes_vacina_gest'], (178, 338)) # Mês da vacinação
doc.write_text(especifico['amamentando'], (282, 342)) # Amamentando
doc.write_text(especifico['aleitamento'], (415, 342)) # Aleitamento
##############################################
#####          DADOS DE RESIDENCIA        ####
##############################################
doc.write_text(especifico['logradouro_residencia2'], (60, 380)) # Logradouro
doc.write_text(especifico['numero_residencia2'], (317, 380)) # Número
doc.write_text(especifico['complemento_residencia2'], (370, 380)) # Complemento
doc.write_text(especifico['bairro_residencia2'], (440, 380)) # Bairro
doc.write_text(especifico['ponto_ref_residencia2'], (60, 410)) # Ponto de referência
doc.write_text(especifico['zona_residencia2'], (281, 406)) # Zona
doc.write_cep(especifico['cep_residencia2'], (348, 403), space=1, font_size=11) # CEP
doc.write_telefone(especifico['telefone_residencia2'], (445, 397), space=1, font_size=10) # Telefone
doc.write_telefone(especifico['telefone2_residencia2'], (445, 410), space=1, font_size=10) # Telefone
doc.write_text(especifico['pais_residencia2'], (60, 432)) # País
doc.write_text(especifico['uf_residencia2'], (170, 433)) # UF
doc.write_text(especifico['municipio_residencia2'], (200, 433)) # Município
####################################################
# Dados Vacinação
####################################################
###Coluna 1
doc.write_date(especifico['vacinacao_dt1'], (55, 505), font_size=9, printbars=True) # Data da vacina1
doc.write_date(especifico['vacinacao_dt2'], (55, 517), font_size=9, printbars=True) # Data da vacina2
doc.write_date(especifico['vacinacao_dt3'], (55, 530), font_size=9, printbars=True) # Data da vacina3
doc.write_date(especifico['vacinacao_dt4'], (55, 543), font_size=9, printbars=True) # Data da vacina4
doc.write_date(especifico['vacinacao_dt5'], (55, 555), font_size=9, printbars=True) # Data da vacina5
doc.write_date(especifico['vacinacao_dt6'], (55, 567), font_size=9, printbars=True) # Data da vacina6
doc.write_date(especifico['vacinacao_dt7'], (55, 579), font_size=9, printbars=True) # Data da vacina7
doc.write_date(especifico['vacinacao_dt8'], (55, 591), font_size=9, printbars=True) # Data da vacina8
doc.write_date(especifico['vacinacao_dt9'], (55, 603), font_size=9, printbars=True) # Data da vacina9
###Coluna 2
doc.write_text(especifico['vacinacao_nome1'], (108, 505), font_size=10) # Nome da vacina1
doc.write_text(especifico['vacinacao_nome2'], (108, 517), font_size=10) # Nome da vacina2
doc.write_text(especifico['vacinacao_nome3'], (108, 530), font_size=10) # Nome da vacina3
doc.write_text(especifico['vacinacao_nome4'], (108, 543), font_size=10) # Nome da vacina4
doc.write_text(especifico['vacinacao_nome6'], (108, 567), font_size=10) # Nome da vacina6
doc.write_text(especifico['vacinacao_nome7'], (108, 579), font_size=10) # Nome da vacina7
doc.write_text(especifico['vacinacao_nome8'], (108, 591), font_size=10) # Nome da vacina8
doc.write_text(especifico['vacinacao_nome9'], (108, 603), font_size=10) # Nome da vacina9
###Coluna 3
doc.write_text(especifico['vacinacao_dose1'], (192, 505), font_size=10) # Dose da vacina1
doc.write_text(especifico['vacinacao_dose2'], (192, 517), font_size=10) # Dose da vacina2
doc.write_text(especifico['vacinacao_dose3'], (192, 530), font_size=10) # Dose da vacina3
doc.write_text(especifico['vacinacao_dose4'], (192, 543), font_size=10) # Dose da vacina4
doc.write_text(especifico['vacinacao_dose5'], (192, 555), font_size=10) # Dose da vacina5
doc.write_text(especifico['vacinacao_dose6'], (192, 567), font_size=10) # Dose da vacina6
doc.write_text(especifico['vacinacao_dose7'], (192, 579), font_size=10) # Dose da vacina7
doc.write_text(especifico['vacinacao_dose8'], (192, 591), font_size=10) # Dose da vacina8
doc.write_text(especifico['vacinacao_dose9'], (192, 603), font_size=10) # Dose da vacina9
###Coluna 4
doc.write_text(especifico['vacinacao_via_adm1'], (220, 505), font_size=10) # Via de administração da vacina1
doc.write_text(especifico['vacinacao_via_adm2'], (220, 517), font_size=10) # Via de administração da vacina2
doc.write_text(especifico['vacinacao_via_adm3'], (220, 530), font_size=10) # Via de administração da vacina3
doc.write_text(especifico['vacinacao_via_adm4'], (220, 543), font_size=10) # Via de administração da vacina4
doc.write_text(especifico['vacinacao_via_adm5'], (220, 555), font_size=10) # Via de administração da vacina5
doc.write_text(especifico['vacinacao_via_adm6'], (220, 567), font_size=10) # Via de administração da vacina6
doc.write_text(especifico['vacinacao_via_adm7'], (220, 579), font_size=10) # Via de administração da vacina7
doc.write_text(especifico['vacinacao_via_adm8'], (220, 591), font_size=10) # Via de administração da vacina8
doc.write_text(especifico['vacinacao_via_adm9'], (220, 603), font_size=10) # Via de administração da vacina9
###Coluna 5
doc.write_text(especifico['vacinacao_local_aplic1'], (282, 505), font_size=10) # Local de aplicação da vacina1
doc.write_text(especifico['vacinacao_local_aplic2'], (282, 517), font_size=10) # Local de aplicação da vacina2
doc.write_text(especifico['vacinacao_local_aplic3'], (282, 530), font_size=10) # Local de aplicação da vacina3
doc.write_text(especifico['vacinacao_local_aplic4'], (282, 543), font_size=10) # Local de aplicação da vacina4
doc.write_text(especifico['vacinacao_local_aplic5'], (282, 555), font_size=10) # Local de aplicação da vacina5
doc.write_text(especifico['vacinacao_local_aplic6'], (282, 567), font_size=10) # Local de aplicação da vacina6
doc.write_text(especifico['vacinacao_local_aplic7'], (282, 579), font_size=10) # Local de aplicação da vacina7
doc.write_text(especifico['vacinacao_local_aplic8'], (282, 591), font_size=10) # Local de aplicação da vacina8
doc.write_text(especifico['vacinacao_local_aplic9'], (282, 603), font_size=10) # Local de aplicação da vacina9
###Coluna 6
doc.write_text(especifico['vacinacao_fabri1'], (341, 505), font_size=10) # Fabricante da vacina1
doc.write_text(especifico['vacinacao_fabri2'], (341, 517), font_size=10) # Fabricante da vacina2
doc.write_text(especifico['vacinacao_fabri3'], (341, 530), font_size=10) # Fabricante da vacina3
doc.write_text(especifico['vacinacao_fabri4'], (341, 543), font_size=10) # Fabricante da vacina4
doc.write_text(especifico['vacinacao_fabri5'], (341, 555), font_size=10) # Fabricante da vacina5
doc.write_text(especifico['vacinacao_fabri6'], (341, 567), font_size=10) # Fabricante da vacina6
doc.write_text(especifico['vacinacao_fabri7'], (341, 579), font_size=10) # Fabricante da vacina7
doc.write_text(especifico['vacinacao_fabri8'], (341, 591), font_size=10) # Fabricante da vacina8
doc.write_text(especifico['vacinacao_fabri9'], (341, 603), font_size=10) # Fabricante da vacina9
###Coluna 7
doc.write_text(especifico['vacinacao_num_lote1'], (420, 505), font_size=11) # Número do lote da vacina1
doc.write_text(especifico['vacinacao_num_lote2'], (420, 517), font_size=11) # Número do lote da vacina2
doc.write_text(especifico['vacinacao_num_lote3'], (420, 530), font_size=11) # Número do lote da vacina3
doc.write_text(especifico['vacinacao_num_lote4'], (420, 543), font_size=11) # Número do lote da vacina4
doc.write_text(especifico['vacinacao_num_lote5'], (420, 555), font_size=11) # Número do lote da vacina5
doc.write_text(especifico['vacinacao_num_lote6'], (420, 567), font_size=11) # Número do lote da vacina6
doc.write_text(especifico['vacinacao_num_lote7'], (420, 579), font_size=11) # Número do lote da vacina7
doc.write_text(especifico['vacinacao_num_lote8'], (420, 591), font_size=11) # Número do lote da vacina8
doc.write_text(especifico['vacinacao_num_lote9'], (420, 603), font_size=11) # Número do lote da vacina9
###Coluna 8
doc.write_date(especifico['vacinacao_dt_valid1'], (497, 505), font_size=9, printbars=True) # Data de validade da vacina1
doc.write_date(especifico['vacinacao_dt_valid2'], (497, 517), font_size=9, printbars=True) # Data de validade da vacina2
doc.write_date(especifico['vacinacao_dt_valid3'], (497, 530), font_size=9, printbars=True) # Data de validade da vacina3
doc.write_date(especifico['vacinacao_dt_valid4'], (497, 543), font_size=9, printbars=True) # Data de validade da vacina4
doc.write_date(especifico['vacinacao_dt_valid5'], (497, 555), font_size=9, printbars=True) # Data de validade da vacina5
doc.write_date(especifico['vacinacao_dt_valid6'], (497, 567), font_size=9, printbars=True) # Data de validade da vacina6
doc.write_date(especifico['vacinacao_dt_valid7'], (497, 579), font_size=9, printbars=True) # Data de validade da vacina7
doc.write_date(especifico['vacinacao_dt_valid8'], (497, 591), font_size=9, printbars=True) # Data de validade da vacina8
doc.write_date(especifico['vacinacao_dt_valid9'], (497, 603), font_size=9, printbars=True) # Data de validade da vacina9
###################################################
# Dados de Unidade de saude
###################################################
doc.write_text(especifico['pais_aplicacao'], (60, 638)) # País de aplicação
doc.write_text(especifico['uf_aplicacao'], (170, 638)) # UF de aplicação
doc.write_text(especifico['municipio_aplicacao'], (195, 638)) # Município de aplicação
doc.write_text(especifico['us_aplicacao'], (60, 667)) # Unidade de saúde de aplicação
doc.write_mini(especifico['motivo_aplicacao'], (325, 662)) # Motivo da aplicação
doc.write_mini(especifico['local_aplicacao'], (445, 662)) # Local de aplicação
###################################################
# Dados de Doenças Preexistentes 
###################################################
#coluna 1 1
doc.write_mini(especifico['doenca_preexist'], (66, 730)) # Doença preexistente
doc.write_mini(especifico['op_doenca_aids_hiv'], (227, 692)) # AIDS/HIV
doc.write_mini(especifico['op_doenca_alerg_alim'], (227, 707)) # Alergia alimentar
doc.write_mini(especifico['op_doenca_alerg_alim_espec'], (285, 710)) # Alergia alimentar específica
doc.write_mini(especifico['op_doenca_alerg_med'], (227, 722)) # Alergia medicamentosa
doc.write_mini(especifico['op_doenca_alerg_med_espc'], (285, 725)) # Alergia medicamentosa específica
doc.write_mini(especifico['op_doenca_diabete'], (227, 737)) # diabete
doc.write_mini(especifico['op_doenca_imune'], (227, 751)) # Auto-imune
doc.write_mini(especifico['op_doenca_imune_espec'], (285, 754)) # Auto-imune específica
#coluna 1 2
doc.write_mini(especifico['op_doenca_cardiaca'], (381, 692)) # Cardíaca
doc.write_mini(especifico['op_doenca_cardiaca_espec'], (435, 694)) # Cardíaca Específica
doc.write_mini(especifico['op_doenca_hepatica'], (381, 707)) # Hepática
doc.write_mini(especifico['op_doenca_hepatica_espec'], (435, 710)) # Hepática Específica
doc.write_mini(especifico['op_doenca_neuro'], (382, 723)) # Neurológica
doc.write_mini(especifico['op_doenca_neuro_espc'], (435, 725)) # Neurológica Específica
doc.write_mini(especifico['op_doenca_pulmonar'], (381, 738)) # Pulmonar
doc.write_mini(especifico['op_doenca_pulmonar_espec'], (435, 740)) # Pulmonar Específica
doc.write_mini(especifico['op_doenca_outra'], (381, 752)) # Outra
doc.write_mini(especifico['op_doenca_outra_espec'], (435, 754)) # Outra Específica
###################################################
doc.write_mini(especifico['med_anter_vacina'], (65, 797)) # Medicamento anterior a vacina
#coluna 2 1
doc.write_mini(especifico['op_med_anticonv'], (227, 766)) # Anticonvulsivante
doc.write_mini(especifico['op_med_antiterm'], (227, 781)) # Antitérmico
doc.write_mini(especifico['op_med_cort'], (227, 795)) # Corticoide
doc.write_mini(especifico['op_med_cort_via'], (258, 797)) # Via de administração do corticoide
doc.write_mini(especifico['med_tempo_uso'], (335, 797)) # Tempo de uso
doc.write_mini(especifico['op_med_imunog'], (227, 810)) # Imunoglobulinas
#coluna 2 2
doc.write_mini(especifico['op_med_homeo'], (381, 766)) # Homeopático
doc.write_mini(especifico['op_med_quimio'], (381, 781)) # Quimioterápico
doc.write_mini(especifico['op_med_outro'], (381, 796)) # Outro
doc.write_mini(especifico['op_med_outro_espec'], (417, 793)) # Outro Específico
################################################### fim da pagina 1
doc.write_mini(especifico['transfusao'], (193, 47), pg=1) # Transfusão
doc.write_date(especifico['dt_transfusao'], (424, 47), spacing=2, font_size=10, pg=1) # Data da transfusão
doc.write_mini(especifico['hist_convulsoes'], (192, 68), pg=1) # Histórico de convulsões
doc.write_mini(especifico['tipo_convulsao'], (392, 68), pg=1) # Tipo de convulsão
doc.write_mini(especifico['eapv_anterior'], (62, 105), pg=1) # EAPV anterior
doc.write_mini(especifico['qual_eapv'], (188, 107), pg=1) # Qual EAPV
doc.write_mini(especifico['vac_adm_eapv'], (308, 107), pg=1) # Vacina administrada no EAPV
doc.write_date(especifico['dt_eapv_anterior'], (414, 107), spacing=2, font_size=12, pg=1) # Data do EAPV anterior
doc.write_mini(especifico['conduta_eapv'], (60, 145), pg=1) # Conduta no EAPV
doc.write_mini(especifico['medicacao_eapv'], (325, 144), pg=1) # Medicação no EAPV
doc.write_mini(especifico['qual_medicacao_eapv'], (412, 137), pg=1) # Qual medicação no EAPV
####################################################
# Antecedentes epidemiologicos
####################################################
doc.write_mini(especifico['viajou_15dias'], (62, 185), pg=1) # viajou nos ultimos 15 dias
doc.write_mini(especifico['tipo_viagem'], (190, 185), pg=1) # País da viagem
doc.write_mini(especifico['pais_viagem'], (223, 190), pg=1) # Data da viagem
doc.write_date(especifico['dt_ida_viagem'], (290, 190), spacing=2, font_size=12, pg=1) # Data da viagem
doc.write_date(especifico['dt_volta_viagem'], (415, 190), spacing=2, font_size=12, pg=1) # Data da viagem
doc.write_mini(especifico['uf_viagem'], (62, 215), pg=1) # uf viagem
doc.write_mini(especifico['municipio_viagem'], (90, 215), pg=1) # Município de viagem
doc.write_mini(especifico['vac_antes_viagem'], (61, 249), pg=1) # vacina antes viagem
doc.write_mini(especifico['vac_durante_viagem'], (188, 249), pg=1) # vacina durante viagem
doc.write_date(especifico['dt_vac_durante_viagem'], (315, 249),spacing=1, pg=1, font_size=10, printbars=True) # Data da vacina durante viagem
doc.write_mini(especifico['qual_vac_tomou'], (402, 249), pg=1) # qual vacina tomou

####################################################
# Dados EAPV
####################################################

#coluna 1

if especifico['mani_loc_abs_frio'] == '1':
    doc.write_cross((87, 283), 1, 9) # abscesso frio
if especifico['mani_loc_abs_dren'] == '1':
    doc.write_cross((87, 291), 1, 9) # abscesso com drenagem
if especifico['mani_loc_abs_quente'] == '1':
    doc.write_cross((87, 299), 1, 9) # abscesso quente
if especifico['mani_loc_atrofia'] == '1':
    doc.write_cross((87, 307), 1, 9) # atrofia no local
if especifico['mani_loc_calor'] == '1':
    doc.write_cross((87, 315), 1, 9) # calor local
if especifico['mani_loc_celulite'] == '1':
    doc.write_cross((87, 323), 1, 9) # celulite
if especifico['mani_loc_dor'] == '1':
    doc.write_cross((87, 331), 1, 9) # dor

#coluna 2

if especifico['mani_loc_edema'] == '1':
    doc.write_cross((235, 283), 1, 9) # edema
if especifico['mani_loc_enduracao'] == '1':
    doc.write_cross((235, 291), 1, 9) # enduracao
if especifico['mani_loc_eritema'] == '1':
    doc.write_cross((235, 299), 1, 9) # eritema
if especifico['mani_loc_exan_local'] == '1':
    doc.write_cross((235, 307), 1, 9) # enxatema local
if especifico['mani_loc_exan_gene'] == '1':
    doc.write_cross((235, 315), 1, 9) # enxatema generalizado
if especifico['mani_loc_linfadenite_nao_sup'] == '1':
    doc.write_cross((235, 323), 1, 9) # linfadenite nao supurada
if especifico['mani_loc_linfadenite_sup'] == '1':
    doc.write_cross((235, 331), 1, 9) # linfadenite supurada

#coluna 3

if especifico['mani_loc_linfa3cm'] == '1':
    doc.write_cross((390, 283), 1, 9) # linfadenomegalia >3cm
if especifico['mani_loc_linfa_nao_sup'] == '1':
    doc.write_cross((390, 291), 1, 9) # linfadenomegalia nao supurada
if especifico['mani_loc_rubor'] == '1':
    doc.write_cross((390, 299), 1, 9) # rubor
if especifico['mani_loc_ulcera'] == '1':
    doc.write_cross((390, 307), 1, 9) # ulcera
if especifico['mani_loc_outras'] == '1':
    doc.write_cross((390, 315), 1, 9) # outras

doc.write_date(especifico['dt_sint_locais'], pos=(60, 358),spacing=1, pg=1, font_size=12) # data dos sintomas
doc.write_text(especifico['dia_vac_manif_loc'], pos=(178, 358), pg=1, font_size=12) # dias vacina manifestacao local
doc.write_text(especifico['hr_vac_manif_loc'], pos=(218, 358), pg=1, font_size=12) # horas vacina manifestacao local
doc.write_text(especifico['min_vac_manif_loc'], pos=(264, 358), pg=1, font_size=12) # minutos vacina manifestacao local
doc.write_text(especifico['dias_evento_loc'], pos=(390, 358), pg=1, font_size=12) # dias evento local
doc.write_text(especifico['horas_evento_loc'], pos=(430, 358), pg=1, font_size=12) # horas evento local
doc.write_text(especifico['min_evento_loc'], pos=(475, 358), pg=1, font_size=12) # minutos evento local

####################################################
# Manifestacoes clinicas sistemicas
####################################################

#Linha 1 Pele/Mucosas

if especifico['mani_sis_angi_labios'] == '1':
    doc.write_cross((86, 390), pg=1, font_size=9)
if especifico['mani_sis_cianose'] == '1':
    doc.write_cross((234, 390), pg=1, font_size=9)
if especifico['mani_sis_purpura'] == '1':
    doc.write_cross((390, 390), pg=1, font_size=9)

#Linha 2

if especifico['mani_sis_angi_laringe'] == '1':
    doc.write_cross((86, 398), 1, 9)
if especifico['mani_sis_hiper'] == '1':
    doc.write_cross((234, 398), 1, 9)
if especifico['mani_sis_urti_gener'] == '1':
    doc.write_cross((390, 398), 1, 9)

#Linha 3

if especifico['mani_sis_angi_lingua'] == '1':
    doc.write_cross((86, 406), 1, 9)
if especifico['mani_sis_ictericia'] == '1':
    doc.write_cross((234, 406), 1, 9)
if especifico['mani_sis_urti_local'] == '1':
    doc.write_cross((390, 406), 1, 9)

#Linha 4

if especifico['mani_sis_angi_membro'] == '1':
    doc.write_cross((86, 414), 1, 9)
if especifico['mani_sis_palidez'] == '1':
    doc.write_cross((234, 414), 1, 9)
if especifico['mani_sis_outro_evento'] == '1':
    doc.write_cross((390, 414), 1, 9)

#Linha 5

if especifico['mani_sis_angi_olho'] == '1':
    doc.write_cross((86, 422), 1, 9)
if especifico['mani_sis_petequia'] == '1':
    doc.write_cross((234, 422), 1, 9)

#Linha 6

if especifico['mani_sis_angi_gener'] == '1':
    doc.write_cross((86, 430), 1, 9)
if especifico['mani_sis_prurido'] == '1':
    doc.write_cross((234, 430), 1, 9)

#Linha Cardiovasculares

if especifico['mani_sis_hipotensao'] == '1':
    doc.write_cross((86, 446), 1, 9) # hipotensao
if especifico['mani_sis_taquicardia'] == '1':
    doc.write_cross((234, 446), 1, 9) # taquicardia
if especifico['mani_sis_bradicardia'] == '1':
    doc.write_cross((390, 446), 1, 9) # bradicardia

#Linha 1 Respiratorias

if especifico['mani_sis_apneia'] == '1':
    doc.write_cross((86, 463), 1, 9) # apneia
if especifico['mani_sis_garganta'] == '1':
    doc.write_cross((234, 463), 1, 9) # garganta
if especifico['mani_sis_fech_garg'] == '1':
    doc.write_cross((390, 463), 1, 9) # fechamento da garganta

#Linha 2

if especifico['mani_sis_bronco'] == '1':
    doc.write_cross((86, 471), 1, 9) # broncoespasmo
if especifico['mani_sis_espirro'] == '1':
    doc.write_cross((234, 471), 1, 9) # espirros
if especifico['mani_sis_taquipneia'] == '1':
    doc.write_cross((390, 471), 1, 9) # taquipneia

#Linha 3

if especifico['mani_sis_dif_resp'] == '1':
    doc.write_cross((86, 479), pg=1, font_size=9) # dificuldade respiratoria
if especifico['mani_sis_rinorreia'] == '1':
    doc.write_cross((234, 479), pg=1, font_size=9) # rinorreia
if especifico['mani_sis_intercost'] == '1':
    doc.write_cross((390, 479), pg=1, font_size=9) # retração intercostal

#Linha 4

if especifico['mani_sis_dispineia'] == '1':
    doc.write_cross((86, 487), 1, 9) # dispneia
if especifico['mani_sis_rouquidao'] == '1':
    doc.write_cross((234, 487), 1, 9) # rouquidão
if especifico['mani_sis_tosse_seca'] == '1':
    doc.write_cross((390, 487), 1, 9) # tosse seca

#Linha 1 Neurologicas

if especifico['mani_sis_ataxia'] == '1':
    doc.write_cross((86, 503), 1, 9) # ataxia
if especifico['mani_sis_conv_toni'] == '1':
    doc.write_cross((234, 503), 1, 9) # convulsão tônico-clônica
if especifico['mani_sis_paresia'] == '1':
    doc.write_cross((390, 503), 1, 9) # paresia

#Linha 2

if especifico['mani_sis_nivel_consc'] == '1':
    doc.write_cross((86, 511), 1, 9) # alteração do nível de consciência
if especifico['mani_sis_desmaio'] == '1':
    doc.write_cross((234, 511), 1, 9) # desmaio
if especifico['mani_sis_parestesia'] == '1':
    doc.write_cross((390, 511), 1, 9) # parestesia

#Linha 3

if especifico['mani_sis_conv_afeb'] == '1':
    doc.write_cross((86, 519), 1, 9) # convulsão afebril
if especifico['mani_sis_hipotonia'] == '1':
    doc.write_cross((234, 519), 1, 9) # hipotonia
if especifico['mani_sis_resposta'] == '1':
    doc.write_cross((390, 519), 1, 9) # resposta a estímulos

#Linha 4

if especifico['mani_sis_conv_feb'] == '1':
    doc.write_cross((86, 527), pg=1, font_size=9) # convulsão febril
if especifico['mani_sis_letargia'] == '1':
    doc.write_cross((234, 527), pg=1, font_size=9) # letargia
if especifico['mani_sis_sin_neuro'] == '1':
    doc.write_cross((390, 527), pg=1, font_size=9) # sinais neurológicos focais

#Linha 5

if especifico['mani_sis_conv_focal'] == '1':
    doc.write_cross((86, 535), pg=1, font_size=9) # convulsão focal
if especifico['mani_sis_nao_resposta'] == '1':
    doc.write_cross((234, 535), pg=1, font_size=9) # não resposta a estímulos
if especifico['mani_sis_neuro_grave'] == '1':
    doc.write_cross((390, 535), pg=1, font_size=9) # neurologia grave

#Linha 6

if especifico['mani_sis_conv_gener'] == '1':
    doc.write_cross((86, 543), pg=1, font_size=9) # convulsão generalizada
if especifico['mani_sis_memb_infer'] == '1':
    doc.write_cross((234, 543), pg=1, font_size=9) # membros inferiores
if especifico['mani_sis_outra_paral'] == '1':
    doc.write_cross((390, 543), pg=1, font_size=9) # outra paralisia

#Linha 1 Gastrointestinais

if especifico['mani_sis_diarreia'] == '1':
    doc.write_cross((86, 560), pg=1, font_size=9) # diarreia
if especifico['mani_sis_fezes_sang'] == '1':
    doc.write_cross((234, 560), pg=1, font_size=9) # fezes sanguinolentas
if especifico['mani_sis_nausea'] == '1':
    doc.write_cross((390, 560), pg=1, font_size=9) # nausea

#Linha 2

if especifico['mani_sis_abdomen'] == '1':
    doc.write_cross((86, 568), pg=1, font_size=9) # dor abdominal
if especifico['mani_sis_inva_intest'] == '1':
    doc.write_cross((234, 568), pg=1, font_size=9) # invaginação intestinal
if especifico['mani_sis_vomito'] == '1':
    doc.write_cross((390, 568), pg=1, font_size=9) # vomito

#Linha 3

if especifico['mani_sis_enterro'] == '1':
    doc.write_cross((86, 576), pg=1, font_size=9) # enterorragia
if especifico['mani_sis_melena'] == '1':
    doc.write_cross((234, 576), pg=1, font_size=9) # melena

doc.write_date(especifico['dt_sint_sistem'], (62, 602), pg=1, font_size=9, spacing=2) # data dos sintomas
doc.write_text(especifico['dia_vac_manif_sistem'], (178, 602), pg=1, font_size=12) # dias vacina manifestacao sistêmica
doc.write_text(especifico['hr_vac_manif_sistem'], (218, 602), pg=1, font_size=12) # horas vacina manifestacao sistêmica
doc.write_text(especifico['min_vac_manif_sistem'], (264, 602), pg=1, font_size=12) # minutos vacina manifestacao sistêmica
doc.write_text(especifico['dias_evento_sistem'], (390, 602), pg=1, font_size=12) # dias evento sistêmico
doc.write_text(especifico['horas_evento_sistem'], (430, 602), pg=1, font_size=12) # horas evento sistêmico
doc.write_text(especifico['min_evento_sistem'], (475, 602), pg=1, font_size=12) # minutos evento sistêmico

####################################################
# Outras manifestacoes
####################################################

#Linha 1

if especifico['otr_mani_artralgia'] == '1':
    doc.write_cross((86, 623), pg=1, font_size=9)

if especifico['otr_mani_evi_sang'] == '1':
    doc.write_cross((234, 623), pg=1, font_size=9)

if especifico['otr_mani_mialgia'] == '1':
    doc.write_cross((390, 623), pg=1, font_size=9)

#Linha 2

if especifico['otr_mani_artrite'] == '1':
    doc.write_cross((86, 631), pg=1, font_size=9)

if especifico['otr_mani_fadiga'] == '1':
    doc.write_cross((234, 631), pg=1, font_size=9)

if especifico['otr_mani_pancrea'] == '1':
    doc.write_cross((390, 631), pg=1, font_size=9)

#Linha 3

if especifico['otr_mani_cefaleia'] == '1':
    doc.write_cross((86, 639), pg=1, font_size=9)

if especifico['otr_mani_feb_mais39'] == '1':
    doc.write_cross((234, 639), pg=1, font_size=9)

if especifico['otr_mani_parotidite'] == '1':
    doc.write_cross((390, 639), pg=1, font_size=9)

#Linha 4

if especifico['otr_mani_cefa_vomito'] == '1':
    doc.write_cross((86, 647), pg=1, font_size=9) # cefaleia e vomito

if especifico['otr_mani_feb_menos39'] == '1':
    doc.write_cross((234, 647), pg=1, font_size=9) # febre <39

if especifico['otr_mani_sonolencia'] == '1':
    doc.write_cross((390, 647), pg=1, font_size=9) # sonolência

#Linha 5

if especifico['otr_mani_choro'] == '1':
    doc.write_cross((86, 655), pg=1, font_size=9) # choro persistente

if especifico['otr_mani_hiper_bila'] == '1':
    doc.write_cross((234, 655), pg=1, font_size=9) # hiperbilirrubinemia

if especifico['otr_mani_outra'] == '1':
    doc.write_cross((390, 655), pg=1, font_size=9) # outra

#Linha 6

if especifico['otr_mani_dif_deamb'] == '1':
    doc.write_cross((86, 663), pg=1, font_size=9) # dificuldade de deambulação

if especifico['otr_mani_hiper_art'] == '1':
    doc.write_cross((234, 663), pg=1, font_size=9) # hipertensão arterial

#Linha 7

if especifico['otr_mani_edem_art'] == '1':
    doc.write_cross((86, 671), pg=1, font_size=9) # edema articular

if especifico['otr_mani_lesao_bcg'] == '1':
    doc.write_cross((234, 671), pg=1, font_size=9) # lesão de BCG

doc.write_date(especifico['dt_sint_otr_mani'], (62, 697), pg=1, font_size=9, spacing=2) # data dos sintomas
doc.write_text(especifico['dia_vac_manif_otr_mani'], (185, 697), pg=1, font_size=12) # dias vacina manifestacao outras
doc.write_text(especifico['hr_vac_manif_otr_mani'], (226, 697), pg=1, font_size=12) # horas vacina manifestacao outras
doc.write_text(especifico['min_vac_manif_otr_mani'], (274, 697), pg=1, font_size=12) # minutos vacina manifestacao outras
doc.write_text(especifico['dias_evento_otr_mani'], (390, 697), pg=1, font_size=12) # dias evento outras
doc.write_text(especifico['horas_evento_otr_mani'], (430, 697), pg=1, font_size=12) # horas evento outras
doc.write_text(especifico['min_evento_otr_mani'], (475, 697), pg=1, font_size=12) # minutos evento outras

####################################################
# Atendimento Medico
####################################################
doc.write_mini(especifico['atend_medico'], (61, 756), pg=1) # atendimento médico
doc.write_mini(especifico['dt_atendimento'][:-5], (124, 752), pg=1, spacing=1, font_size=7) # data do atendimento
doc.write_mini(especifico['dt_atendimento'][-4:], (124, 761), pg=1, spacing=1, font_size=7) # data do atendimento
doc.write_mini(especifico['tipo_atendimento'], (176, 756), pg=1) # tipo de atendimento
doc.write_mini(especifico['ficou_obs'], (243, 755), pg=1) # ficou observacao
doc.write_mini(especifico['horas_obs'], (306, 752), pg=1) # horas de observacao
doc.write_mini(especifico['ficou_enfermaria'], (332, 755), pg=1) # ficou enfermaria
doc.write_mini(especifico['dias_enfermaria'], (395, 752), pg=1) # dias de enfermaria
doc.write_mini(especifico['ficou_uti'], (415, 754), pg=1) # ficou UTI
doc.write_mini(especifico['dias_uti'], (476, 752), pg=1) # dias de UTI
doc.write_mini(especifico['dt_alta'][:2], (495, 757), pg=1, font_size=9) # data da alta
doc.write_mini(especifico['dt_alta'][3:5], (510, 757), pg=1, font_size=9) # data da alta
doc.write_mini(especifico['dt_alta'][6:], (525, 757), pg=1, font_size=9) # data da alta
doc.write_text(especifico['nome_hosp_atendimento'], (61, 788), pg=1) # nome do hospital
doc.write_mini(especifico['tipo_loc_atendimento'], (414, 782), pg=1) # tipo de local de atendimento
doc.write_text(especifico['municipio_atendimento'], (61, 811), pg=1) # município de atendimento
doc.write_text(especifico['uf_atendimento'], (495, 811), pg=1) # uf de atendimento
#################################################### fim da pagina 2
# informaçoes laboratoriais complementares
doc.write_date(especifico['dt_col_hemograma'], (216, 73), pg=2, spacing=1, font_size=10, printbars=True) # data da coleta do hemograma
doc.write_mini(especifico['hemacias_hemo'], (250, 93), pg=2) # hemacias
doc.write_mini(especifico['hemoglobina_hemo'], (324, 93), pg=2) # hemoglobina
doc.write_mini(especifico['hematocrito_hemo'], (386, 93), pg=2) # hematocrito
doc.write_mini(especifico['plaquetas_hemo'], (436, 93), pg=2) # plaquetas
doc.write_mini(especifico['leucocitos_hemo'], (250, 108), pg=2) # leucocitos
doc.write_mini(especifico['monocitos_hemo'], (324, 108), pg=2) # monocitos
doc.write_mini(especifico['linfocitos_hemo'], (386, 108), pg=2) # linfocitos
doc.write_mini(especifico['neutrofilos_hemo'], (430, 108), pg=2) # neutrofilos
doc.write_mini(especifico['eosinofilos_hemo'], (490, 108), pg=2) # eosinofilos
doc.write_date(especifico['dt_col_bioquimica'], (173, 129), pg=2, spacing=1, font_size=8, printbars=True) # data da coleta da bioquimica
doc.write_mini(especifico['bili_total_bioq'], (248, 123), pg=2) # bilirrubina total
doc.write_mini(especifico['creatina_bioq'], (248, 136), pg=2) # creatinina
doc.write_mini(especifico['bili_dir_bioq'], (318, 123), pg=2) # bilirrubina direta
doc.write_mini(especifico['ast_bioq'], (386, 123), pg=2) # AST
doc.write_mini(especifico['inr_bioq'], (389, 136), pg=2) # INR
doc.write_mini(especifico['alt_bioq'], (431, 123), pg=2) # ALT
doc.write_mini(especifico['pt_bioq'], (431, 136), pg=2) # TGO
doc.write_mini(especifico['ureia_bioq'], (490, 123), pg=2) # ureia
doc.write_mini(especifico['ptt_bioq'], (492, 136), pg=2) # PTT
doc.write_mini(especifico['puncao_lombar'], (180, 153), pg=2) # punção lombar
doc.write_date(especifico['dt_puncao'], (294, 150), pg=2, spacing=1, printbars=True) # data da punção
doc.write_mini(especifico['leucocitos_cito'], (247, 171), pg=2) # leucocitos
doc.write_mini(especifico['glicose_cito'], (242, 194), pg=2) # glicose
doc.write_mini(especifico['neutrofilos_cito'], (288, 174), pg=2) # neutrofilos
doc.write_mini(especifico['proteinas_cito'], (288, 194), pg=2) # proteinas
doc.write_mini(especifico['linfocitos_cito'], (336, 174), pg=2) # linfocitos
doc.write_mini(especifico['cult_liquor'], (441, 172), pg=2) # cultura do liquor
doc.write_mini(especifico['cult_liquor_espec'], (488, 170), pg=2) # cultura do liquor especifica
doc.write_mini(especifico['bacterioscopia'], (441, 192), pg=2) # bacterioscopia
doc.write_mini(especifico['bacterio_espec'], (488, 191), pg=2) # bacterioscopia especifica
doc.write_mini(especifico['deteccao_viral'], (180, 220), pg=2) # detecção viral
doc.write_mini(especifico['dt_detec_viral'], (284, 218), pg=2, spacing=2) # data da detecção viral
doc.write_mini(especifico['detec_viral_coleta'], (390, 220), pg=2) # detecção viral coleta
doc.write_mini(especifico['detec_viral_pcr'], (242, 250), pg=2) # detecção viral PCR
doc.write_mini(especifico['detec_viral_outro'], (386, 256), pg=2) # detecção viral outro
doc.write_mini(especifico['autopsia'], (180, 274), pg=2) # autopsia
doc.write_mini(especifico['dt_autopsia'], (258, 272), pg=2, spacing=2) # data da autopsia
doc.write_mini(especifico['autop_anatomo'], (242, 295), pg=2) # autopsia anatomopatologica
doc.write_mini(especifico['autop_histo'], (242, 315), pg=2) # autopsia histopatologica
doc.write_mini(especifico['autop_imuno'], (242, 335), pg=2) # autopsia imunohistoquimica
doc.write_mini(especifico['autop_dt_anatomo'], (402, 293), pg=2, spacing=2) # autopsia data anatomopatologica
doc.write_mini(especifico['autop_dt_histo'], (402, 313), pg=2, spacing=2) # autopsia data histopatologica
doc.write_mini(especifico['autop_dt_imuno'], (402, 333), pg=2, spacing=2) # autopsia data imunohistoquimica
####################################################
doc.write_mini(especifico['dt_ecg'], (222, 351), pg=2, spacing=1) # ECG
doc.write_mini(especifico['dt_rm'], (432, 351), pg=2, spacing=1) # RM
doc.write_mini(especifico['dt_eeg'], (222, 365), pg=2, spacing=1) # EEG
doc.write_mini(especifico['dt_enmg'], (432, 365), pg=2, spacing=1) # ENMG
doc.write_mini(especifico['dt_rx'], (222, 378), pg=2, spacing=1) # RX
doc.write_mini(especifico['dt_usg'], (432, 378), pg=2, spacing=1) # USG
doc.write_mini(especifico['dt_tc'], (222, 392), pg=2, spacing=1) # TC
doc.write_box(especifico['outras_informacoes'], rect=(55, 415, 548, 490), pg=2) # Outras informações
####################################################
# Diagnostico
####################################################
doc.write_text(especifico['diag_descricao1'], (58, 523), pg=2) # Diagnóstico 1
doc.write_text(especifico['diag_cid1'], (285, 523), pg=2) # CID 1
doc.write_text(especifico['diag_descricao2'], (58, 533), pg=2) # Diagnóstico 2
doc.write_text(especifico['diag_cid2'], (285, 533), pg=2) # CID 2
doc.write_text(especifico['diag_descricao3'], (58, 543), pg=2) # Diagnóstico 3
doc.write_text(especifico['diag_cid3'], (285, 543), pg=2) # CID 3
doc.write_text(especifico['diag_descricao4'], (58, 553), pg=2) # Diagnóstico 4
doc.write_text(especifico['diag_cid4'], (285, 553), pg=2) # CID 4

doc.write_mini(especifico['erro_programa'], (66, 596), pg=2, spacing=1) # erro de programa
doc.write_mini(especifico['erro_programa_espec'], (385, 602), pg=2) # erro de programa especifico
doc.write_mini(especifico['evolucao_caso'], (63, 676), pg=2) # evolução do caso
doc.write_mini(especifico['dt_obito'], (181, 646), pg=2, spacing=1) # data do óbito
doc.write_mini(especifico['declara_obito'], (176, 672), pg=2) # declaração de óbito
doc.write_mini(especifico['declara_vivo'], (176, 699), pg=2) # declaração de vivo
doc.write_mini(especifico['conduta_vacinal'], (286, 676), pg=2) # conduta vacinal
doc.write_mini(especifico['dt_encerramento'], (464, 672), pg=2, spacing=1) # data de encerramento
doc.write_mini(especifico['nome_investigador'], (58, 740), pg=2) # nome do investigador
doc.write_mini(especifico['funcao_investigador'], (315, 740), pg=2) # função do investigador
doc.write_mini(especifico['telefone_investigador'], (430, 740), pg=2) # telefone do investigador
doc.write_mini(especifico['municipio_us_investigador'], (58, 760), pg=2) # município do investigador
doc.write_mini(especifico['unid_saude_investigador'], (58, 782), pg=2) # unidade de saúde do investigador
doc.write_mini(especifico['telefone_us_investigador'], (430, 782), pg=2) # telefone da unidade de saúde
doc.write_mini(especifico['assinatura_investigador'], (58, 802), pg=2) # assinatura do investigador
doc.write_date(especifico['data_preenchimento'], (434, 800), pg=2, spacing=4) # data de preenchimento

doc.save('evento_adv_pos_vacina.pdf')