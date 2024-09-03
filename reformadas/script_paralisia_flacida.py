from pdfWritter import PDFWriter


pdf = 'Paralisia Flácida Aguda1.pdf'
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
    "dt_1_consulta": "15/02/2022",
    "dt_investigacao": "15/02/2022",
    "vac_polio": "9",
    "num_dose_polio": "9",
    "dt_ult_dose_polio": "15/02/2022",
    "viajou_30_dias": "9",
    "pais_viagem_polio": "observacao",
    "sint_febre": "9",
    "sint_vomito": "9",
    "sint_diarreia": "9",
    "sint_obstipacao": "9",
    "sint_dor_muscular": "9",
    "sint_cefaleia": "9",
    "sint_alter_resp": "9",
    "sint_outro": "9",
    "sint_outro_descricao": "observacao",
    "dt_def_motora": "15/02/2022",
    "def_aguda": "9",
    "def_flacida": "9",
    "def_assim": "9",
    "def_progess": "9",
    "def_ascend": "9",
    "def_descend": "9",
    "forca_mie": "9",
    "forca_mse": "9",
    "forca_mid": "9",
    "forca_msd": "9",
    "loc_mie": "9",
    "loc_mse": "9",
    "loc_mid": "9",
    "loc_msd": "9",
    "compr_resp": "9",
    "compr_cerv": "9",
    "compr_face": "9",
    "dt_exam_aguda": "15/02/2022",
    "forca_mie_aguda": "9",
    "forca_mse_aguda": "9",
    "forca_mid_aguda": "9",
    "forca_msd_aguda": "9",
    "tonus_mie": "9",
    "tonus_cerv": "9",
    "tonus_mse": "9",
    "tonus_mid": "9",
    "tonus_face": "9",
    "tonus_msd": "9",
    "sensi_mie": "9",
    "sensi_mse": "9",
    "sensi_mid": "9",
    "sensi_msd": "9",
    "sensi_face": "9",
    "reflex_aquE": "9",
    "reflex_aquD": "9",
    "reflex_patE": "9",
    "reflex_patD": "9",
    "reflex_bicE": "9",
    "reflex_bicD": "9",
    "reflex_triE": "9",
    "reflex_triD": "9",
    "reflex_cut_flexE": "9",
    "reflex_cut_flexD": "9",
    "reflex_cut_extE": "9",
    "reflex_cut_extD": "9",
    "meningea_kernig": "9",
    "meningea_nuca": "9",
    "meningea_brud": "9",
    "ingest_toxica": "9",
    "esp_ingest_toxica": "observacao",
    "inj_intramusc": "9",
    "loc_inj_intramusc": "9",
    "hipotese_diag": "9999",
    "hospitalizacao2": "9",
    "dt_internacao": "15/02/2022",
    "uf_hospital2": "PI",
    "municipio_hospital2": "observacao",
    "cod_ibge_hospital2": "123456",
    "dt_col_lab": "15/02/2022",
    "dt_env_estado": "15/02/2022",
    "dt_env_lrr": "15/02/2022",
    "dt_receb_lrr": "15/02/2022",
    "quant_fez_col": "9",
    "cond_fez_col": "9",
    "dt_res_lab": "15/02/2022",
    "res_laboratorial1": "99",
    "res_laboratorial2": "99",
    "res_laboratorial3": "99",
    "liq_dt1": "15/02/2022",
    "liq_cel1": "observacao",
    "liq_linf1": "observacao",
    "liq_prot1": "observacao",
    "liq_gli1": "observacao",
    "liq_clo1": "observacao",
    "liq_dt2": "15/02/2022",
    "liq_cel2": "observacao",
    "liq_linf2": "observacao",
    "liq_prot2": "observacao",
    "liq_gli2": "observacao",
    "liq_clo2": "observacao",
    "dt_eletrone": "15/02/2022",
    "diag_sugestivo": "observacao",
    "anatomo_cereb": "9",
    "anatomo_medula": "9",
    "anatomo_intest": "9",
    "dt_anatomo": "15/02/2022",
    "res_anatomo": "9",
    "dt_revisita": "15/02/2022",
    "forca_mie2": "9",
    "forca_mse2": "9",
    "forca_mid2": "9",
    "forca_msd2": "9",
    "tonus_mie2": "9",
    "tonus_cerv2": "9",
    "tonus_mse2": "9",
    "tonus_mid2": "9",
    "tonus_face2": "9",
    "tonus_msd2": "9",
    "reflex_aquE2": "9",
    "reflex_aquD2": "9",
    "reflex_patE2": "9",
    "reflex_patD2": "9",
    "reflex_bicE2": "9",
    "reflex_bicD2": "9",
    "reflex_triE2": "9",
    "reflex_triD2": "9",
    "reflex_cut_flexE2": "9",
    "reflex_cut_flexD2": "9",
    "reflex_cut_extE2": "9",
    "reflex_cut_extD2": "9",
    "atrofia_mie": "9",
    "atrofia_mse": "9",
    "atrofia_mid": "9",
    "atrofia_msd": "9",
    "sensi_mie2": "9",
    "sensi_mse2": "9",
    "sensi_mid2": "9",
    "sensi_msd2": "9",
    "sensi_face2": "9",
    "dt_revisao": "15/02/2022",
    "classif_final": "9",
    "criterio_classif": "9",
    "diag_descartado": "9999",
    "evolucao_caso": "9",
    "dt_obito": "15/02/2022",
    "dt_encerramento": "15/02/2022",
    "municipio_us_investigador": "observacao",
    "cod_us_investigador": "123456",
    "nome_investigador": "observacao",
    "funcao_investigador": "observacao",
    "assinatura_investigador": "observacao"
}


###################################################
# Dados do paciente
###################################################

doc.write_text(especifico['numero_ficha2'],(467, 45))
doc.write_date(especifico['dt_notificacao2'], (446, 158), spacing=2) #data_notificacao
doc.write_uf(especifico['uf_notificacao2'], (55, 189)) #uf_notificacao
doc.write_text(especifico['municipio_notificacao2'], (90, 188)) #municipio_notificacao __unid_saude 55,220
doc.write_code(especifico['cod_ibge_notificacao2'], (479, 189),space=2) #cod_ibge
doc.write_text(especifico['unidade_saude2'], (65, 217)) #cod_unid_saude
doc.write_code(especifico['cod_unidade_saude2'], (339, 218),space=2) #cod_unid_saude
doc.write_date(especifico['dt_sintomas2'], (446, 217), spacing=2) #data_diagnostico
##############################################
#####          NOTIFICACAO INDIVIDUAL     ####
##############################################
doc.write_text(especifico['nome_paciente2'], (55, 248)) #nome
doc.write_date(especifico['dt_nascimento2'], (449, 248), spacing=2) #data_nascimento
doc.write_code(especifico['idade2'], (65, 277),space=2) #idade
doc.write_mini(especifico['tipo_idade2'], (111, 270)) #tipo_idade
doc.write_mini(especifico['sexo2'], (234, 263)) #sexo
doc.write_mini(especifico['gestante2'], (429, 263)) #gestante
doc.write_mini(especifico['raca2'], (554, 264)) #raça/cor
doc.write_mini(especifico['escolaridade2'], (554, 293)) #escolaridade
doc.write_code(especifico['numero_sus2'], (57, 338),space=2, font_size=10) #cartao_sus
doc.write_text(especifico['nome_mae2'], (240, 338), font_size=9) #nome_mae
##############################################
#####          DADOS DE RESIDENCIA        ####
##############################################

doc.write_uf(especifico['uf_residencia2'], (57, 368)) #uf_residencia
doc.write_text(especifico['municipio_residencia2'], (90, 368), font_size=9) #municipio_residencia
doc.write_code(especifico['cod_ibge_residencia2'], (325, 368),space=2) #cod_ibge_residencia
doc.write_text(especifico['distrito_residencia2'], (420, 368), font_size=9) #endereco
doc.write_text(especifico['bairro_residencia2'], (62, 392), font_size=9) #bairro
doc.write_text(especifico['logradouro_residencia2'], (208, 393), font_size=9) #logradouro
doc.write_code(especifico['codigo_residencia2'], (480, 394),space=2) #cod_logradouro
doc.write_text(especifico['numero_residencia2'], (62, 417)) #numero
doc.write_text(especifico['complemento_residencia2'], (120, 417), font_size=9) #complemento
doc.write_text(especifico['geo_campo1_2'], (415, 420)) #geo_campo_1
doc.write_text(especifico['geo_campo2_2'], (55, 443)) #geo_campo_2
doc.write_text(especifico['ponto_ref_residencia2'], (230, 443), font_size=9) #ponto_ref
doc.write_code(especifico['cep_residencia2'], (456, 446),space=2) #cep
doc.write_telefone(especifico['telefone_residencia2'], (55, 470), space=2) #telefone
doc.write_mini(especifico['zona_residencia2'], (333, 458)) #zona
doc.write_text(especifico['pais_residencia2'], (360, 469), font_size=9) #pais
##############################################
#####        DADOS  COMPLEMENTARES        ####
##############################################
doc.write_date(especifico['dt_1_consulta'], (63, 525), spacing=2) #data_primeira_consulta
doc.write_date(especifico['dt_investigacao'], (182, 525), spacing=2) #data_investigacao
doc.write_mini(especifico['vac_polio'], (439, 520)) #vacina_polio
doc.write_code(especifico['num_dose_polio']+'9', (500, 524), space=2) #num_doses_polio
doc.write_date(especifico['dt_ult_dose_polio'], (63, 572), spacing=2) #data_ultima_dose_polio
doc.write_mini(especifico['viajou_30_dias'], (421, 547)) #viajou_30_dias
doc.write_text(especifico['pais_viagem_polio'], (440, 555)) #pais_viagem

#!campo 38
doc.write_mini(especifico['sint_febre'], (77, 606)) #sint_febre
doc.write_mini(especifico['sint_vomito'], (77, 625)) #sint_vomito
doc.write_mini(especifico['sint_diarreia'], (142, 606)) #sint_diarreia
doc.write_mini(especifico['sint_obstipacao'], (142, 625)) #sint_obstipacao
doc.write_mini(especifico['sint_dor_muscular'], (221, 606)) #sint_dor_muscular
doc.write_mini(especifico['sint_cefaleia'], (221, 625)) #sint_cefaleia
doc.write_mini(especifico['sint_alter_resp'], (315, 606)) #sint_alter_resp
doc.write_mini(especifico['sint_outro'], (315, 625)) #sint_outro
doc.write_text(especifico['sint_outro_descricao'], (353, 623), font_size=8) #sint_outro_descricao

#! campo 39
doc.write_date(especifico['dt_def_motora'], (452, 630), spacing=2) #data_def_motora

#! campo 40 deficiencia motora
doc.write_mini(especifico['def_aguda'], (92, 660)) #aguda
doc.write_mini(especifico['def_flacida'], (157, 660)) #flacida
doc.write_mini(especifico['def_assim'], (223, 660)) #assimetrica
doc.write_mini(especifico['def_progess'], (302, 660)) #progressiva
doc.write_mini(especifico['def_ascend'], (415, 660)) #ascendente
doc.write_mini(especifico['def_descend'], (503, 660)) #descendente

#! campo 41 força muscular
doc.write_mini(especifico['forca_mie'], (103, 694)) #membro_inferior_esquerdo
doc.write_mini(especifico['forca_mse'], (154, 694)) #membro_superior_esquerdo
doc.write_mini(especifico['forca_mid'], (206, 694)) #membro_inferior_direito
doc.write_mini(especifico['forca_msd'], (257, 694)) #membro_superior_direito

#! campo 42 localização da deficiencia
doc.write_mini(especifico['loc_mie'], (356, 694)) #membro_inferior_esquerdo
doc.write_mini(especifico['loc_mse'], (407, 694)) #membro_superior_esquerdo
doc.write_mini(especifico['loc_mid'], (458, 694)) #membro_inferior_direito
doc.write_mini(especifico['loc_msd'], (509, 694)) #membro_superior_direito

#! campo 43 comprometimento de
doc.write_mini(especifico['compr_resp'], (68, 735)) #respiracao
doc.write_mini(especifico['compr_cerv'], (173, 734)) #cervical
doc.write_mini(especifico['compr_face'], (268, 735)) #facial

#! campo 44 exame fisico na fase aguda
doc.write_date(especifico['dt_exam_aguda'], (312, 737), spacing=2) #data_exame_fisico_agudo

#! campo 45 força muscular
doc.write_mini(especifico['forca_mie_aguda'], (446, 721)) #membro_inferior_esquerdo
doc.write_mini(especifico['forca_mse_aguda'], (486, 721)) #membro_superior_esquerdo
doc.write_mini(especifico['forca_mid_aguda'], (446, 734)) #membro_inferior_direito
doc.write_mini(especifico['forca_msd_aguda'], (486, 734)) #membro_superior_direito

#! campo 46 tonus muscular
doc.write_mini(especifico['tonus_mie'], (68, 768)) #membro_inferior_esquerdo
doc.write_mini(especifico['tonus_cerv'], (68, 782)) #cervical
doc.write_mini(especifico['tonus_mse'], (106, 768)) #membro_superior_esquerdo
doc.write_mini(especifico['tonus_mid'], (140, 768)) #membro_inferior_direito
doc.write_mini(especifico['tonus_face'], (140, 782)) #facial
doc.write_mini(especifico['tonus_msd'], (174, 767)) #membro_superior_direito

#! campo 47 sensibilidade
doc.write_mini(especifico['sensi_mie'], (285, 778)) #membro_inferior_esquerdo
doc.write_mini(especifico['sensi_mse'], (325, 778)) #membro_superior_esquerdo
doc.write_mini(especifico['sensi_mid'], (365, 778)) #membro_inferior_direito
doc.write_mini(especifico['sensi_msd'], (415, 778)) #membro_superior_direito
doc.write_mini(especifico['sensi_face'], (471, 778)) #facial

#! campo 48 reflexos
doc.write_mini(especifico['reflex_aquE'], (88, 818)) #aquileu_esquerdo
doc.write_mini(especifico['reflex_aquD'], (146, 818)) #aquileu_direito
doc.write_mini(especifico['reflex_patE'], (208, 818)) #patelar_esquerdo
doc.write_mini(especifico['reflex_patD'], (266, 818)) #patelar_direito
doc.write_mini(especifico['reflex_bicE'], (328, 818)) #bicipital_esquerdo
doc.write_mini(especifico['reflex_bicD'], (389, 818)) #bicipital_direito
doc.write_mini(especifico['reflex_triE'], (448, 818)) #tricipital_esquerdo
doc.write_mini(especifico['reflex_triD'], (508, 818)) #tricipital_direito

#*====================== fim da pagina 1 ===============================*#

#! campo 49 reflexos cutaneos
doc.write_mini(especifico['reflex_cut_flexE'], (75, 59), pg=1) #cutaneo_flexor_esquerdo
doc.write_mini(especifico['reflex_cut_flexD'], (75, 76), pg=1) #cutaneo_flexor_direito
doc.write_mini(especifico['reflex_cut_extE'], (181, 59), pg=1) #cutaneo_extensor_esquerdo
doc.write_mini(especifico['reflex_cut_extD'], (181, 75), pg=1) #cutaneo_extensor_direito

#! campo 50 sinais meningeos
doc.write_mini(especifico['meningea_kernig'], (328, 72), pg=1) #kernig
doc.write_mini(especifico['meningea_nuca'], (382, 72), pg=1) #nuca
doc.write_mini(especifico['meningea_brud'], (461, 72), pg=1) #brudzinski

#! campo 51 ingestao toxica
doc.write_mini(especifico['ingest_toxica'], (265, 92), pg=1) #ingestao_toxica

#! campo 52 especificacao da ingestao toxica
doc.write_text(especifico['esp_ingest_toxica'], (290, 110), pg=1, font_size=9) #especificacao_ingestao_toxica

#! campo 53 injecao intramuscular
doc.write_mini(especifico['inj_intramusc'], (199, 126), pg=1) #injecao_intramuscular

#! campo 54 local da injecao intramuscular
doc.write_mini(especifico['loc_inj_intramusc'], (492, 128), pg=1) #local_injecao_intramuscular

#! campo 55 hipotese diagnostica
doc.write_code(especifico['hipotese_diag'], (200, 173), pg=1, space=2) #hipotese_diagnostica

#! campo 56 hospitalizacao
doc.write_mini(especifico['hospitalizacao2'], (426, 164), pg=1) #hospitalizacao

#! campo 57 data de internacao
doc.write_date(especifico['dt_internacao'], (454, 175), pg=1, spacing=2) #data_internacao

#! campo 58 local de internacao
doc.write_uf(especifico['uf_hospital2'], (57, 202), pg=1) #uf_hospital

#! campo 59 municipio de internacao
doc.write_text(especifico['municipio_hospital2'], (90, 202), pg=1) #municipio_hospital
doc.write_code(especifico['cod_ibge_hospital2'], (485, 202), pg=1, space=2) #cod_ibge_hospital

#! campo 60 data da coleta de amostra
doc.write_date(especifico['dt_col_lab'], (62, 235), pg=1, spacing=2) #data_coleta_amostra

#! campo 61 data do envio ao estado
doc.write_date(especifico['dt_env_estado'], (190, 236), pg=1, spacing=2) #data_env

#! campo 62 data do envio ao LRR
doc.write_date(especifico['dt_env_lrr'], (314, 236), pg=1, spacing=2) #data_env_lrr

#! campo 63 data do recebimento no LRR
doc.write_date(especifico['dt_receb_lrr'], (61, 267), pg=1, spacing=2) #data

#! campo 64 quantidade de amostras coletadas
doc.write_mini(especifico['quant_fez_col'], (287, 252), pg=1) #quant

#! campo 65 condicoes da amostra
doc.write_mini(especifico['cond_fez_col'], (433, 249), pg=1) #condicoes

#! campo 66 data do resultado laboratorial
doc.write_date(especifico['dt_res_lab'], (455, 268), pg=1, spacing=2) #data

#! campo 67 resultado laboratorial 1
doc.write_code(especifico['res_laboratorial1'], (535, 285), pg=1, font_size=11, space=2) #resultado
doc.write_code(especifico['res_laboratorial2'], (535, 297), pg=1, font_size=11, space=2) #resultado2
doc.write_code(especifico['res_laboratorial3'], (535, 309), pg=1, font_size=11, space=2) #resultado3

#! campo 68 exames complementares

if especifico['liq_dt1']:
    doc.write_code(especifico['liq_dt1'][:2], (75, 385), pg=1) #data
    doc.write_code(especifico['liq_dt1'][3:5], (112, 385), pg=1) #data
    doc.write_code(especifico['liq_dt1'][6:], (149, 385), pg=1) #data

doc.write_code(especifico['liq_cel1'], (190, 385), pg=1) #celulas
doc.write_code(especifico['liq_linf1'], (282, 385), pg=1) #linfocitos
doc.write_code(especifico['liq_prot1'], (358, 385), pg=1) #proteinas
doc.write_code(especifico['liq_gli1'], (432, 385), pg=1) #glicose
doc.write_code(especifico['liq_clo1'], (501, 385), pg=1) #cloreto

if especifico['liq_dt2']:
    doc.write_code(especifico['liq_dt2'][:2], (75, 407), pg=1) #data
    doc.write_code(especifico['liq_dt2'][3:5], (112, 407), pg=1) #data
    doc.write_code(especifico['liq_dt2'][6:], (149, 407), pg=1) #data

doc.write_code(especifico['liq_cel2'], (190, 407), pg=1) #celulas
doc.write_code(especifico['liq_linf2'], (282, 407), pg=1) #linfocitos
doc.write_code(especifico['liq_prot2'], (358, 407), pg=1) #proteinas
doc.write_code(especifico['liq_gli2'], (432, 407), pg=1) #glicose
doc.write_code(especifico['liq_clo2'], (501, 407), pg=1) #cloreto

#! campo 69 data do exame eletroneuromiografico
doc.write_date(especifico['dt_eletrone'], (61, 442), pg=1, spacing=2) #data
#! campo 70 diagnostico sugestivo
doc.write_text(especifico['diag_sugestivo'], (200, 442), pg=1) #diagnostico_sug
#! campo 71 anatomopatologico
doc.write_mini(especifico['anatomo_cereb'], (89, 476), pg=1) #cerebro
doc.write_mini(especifico['anatomo_medula'], (134, 476), pg=1) #medula
doc.write_mini(especifico['anatomo_intest'], (179, 475), pg=1) #intestino

#! campo 72 data do exame anatomopatologico
doc.write_date(especifico['dt_anatomo'], (280, 485), pg=1, spacing=2) #data da coleta

#! campo 73 resultado
doc.write_mini(especifico['res_anatomo'], (556, 472), pg=1) #resultado

#! campo 74 data da revisita
doc.write_date(especifico['dt_revisita'], (61, 534), pg=1, spacing=2) #data da revisita

#! campo 75 força muscular
doc.write_mini(especifico['forca_mie2'], (194, 520), pg=1) #membro_inferior_esquerdo
doc.write_mini(especifico['forca_mse2'], (233, 520), pg=1) #membro_superior_esquerdo
doc.write_mini(especifico['forca_mid2'], (194, 533), pg=1) #membro_inferior_direito
doc.write_mini(especifico['forca_msd2'], (233, 533), pg=1) #membro_superior_direito

#! campo 76 tonus muscular
doc.write_mini(especifico['tonus_mie2'], (330, 516), pg=1) #membro_inferior_esquerdo
doc.write_mini(especifico['tonus_cerv2'], (332, 530), pg=1) #cervical
doc.write_mini(especifico['tonus_mse2'], (369, 516), pg=1) #membro_superior_esquerdo
doc.write_mini(especifico['tonus_mid2'], (404, 516), pg=1) #membro_inferior_direito
doc.write_mini(especifico['tonus_face2'], (404, 530), pg=1) #facial
doc.write_mini(especifico['tonus_msd2'], (438, 515), pg=1) #membro_superior_direito

#! campo 77 reflexos
doc.write_mini(especifico['reflex_aquE2'], (80, 565), pg=1) #aquileu_esquerdo
doc.write_mini(especifico['reflex_aquD2'], (138, 565), pg=1) #aquileu_direito
doc.write_mini(especifico['reflex_patE2'], (200, 565), pg=1) #patelar_esquerdo
doc.write_mini(especifico['reflex_patD2'], (258, 565), pg=1) #patelar_direito
doc.write_mini(especifico['reflex_bicE2'], (326, 565), pg=1) #bicipital_esquerdo
doc.write_mini(especifico['reflex_bicD2'], (388, 565), pg=1) #bicipital_direito
doc.write_mini(especifico['reflex_triE2'], (447, 565), pg=1) #tricipital_esquerdo
doc.write_mini(especifico['reflex_triD2'], (510, 565), pg=1) #tricipital_direito

#! campo 78 reflexos cutaneos
doc.write_mini(especifico['reflex_cut_flexE2'], (70, 596), pg=1) #cutaneo_flexor_esquerdo
doc.write_mini(especifico['reflex_cut_flexD2'], (125, 596), pg=1) #cutaneo_flexor_direito
doc.write_mini(especifico['reflex_cut_extE2'], (190, 596), pg=1) #cutaneo_extensor_esquerdo
doc.write_mini(especifico['reflex_cut_extD2'], (265, 596), pg=1) #cutaneo_extensor_direito

#! campo 79 atrofia muscular
doc.write_mini(especifico['atrofia_mie'], (366, 596), pg=1) #membro_inferior_esquerdo
doc.write_mini(especifico['atrofia_mse'], (418, 596), pg=1) #membro_superior_esquerdo
doc.write_mini(especifico['atrofia_mid'], (470, 596), pg=1) #membro_inferior_direito
doc.write_mini(especifico['atrofia_msd'], (522, 596), pg=1) #membro_superior_direito

#! campo 80 sensibilidade
doc.write_mini(especifico['sensi_mie2'], (136, 625), pg=1) #membro_inferior_esquerdo
doc.write_mini(especifico['sensi_mse2'], (200, 625), pg=1) #membro_superior_esquerdo
doc.write_mini(especifico['sensi_mid2'], (272, 625), pg=1) #membro_inferior_direito
doc.write_mini(especifico['sensi_msd2'], (348, 625), pg=1) #membro_superior_direito
doc.write_mini(especifico['sensi_face2'], (429, 624), pg=1) #facial

#! campo 81 data da revisao
doc.write_date(especifico['dt_revisao'], (60, 672), pg=1, spacing=2) #data_revisao

#! campo 82 classificacao final
doc.write_mini(especifico['classif_final'], (372, 648), pg=1) #classificacao_final

#! campo 83 criterio de classificacao
doc.write_mini(especifico['criterio_classif'], (555, 647), pg=1) #criterio_classificacao

#! campo 84 diagnostico descartado
doc.write_code(especifico['diag_descartado'], (105, 707), pg=1, space=2) #diagnostico_descartado

#! campo 85 evolucao do caso
doc.write_mini(especifico['evolucao_caso'], (553, 690), pg=1) #evolucao

#! campo 86 data do obito
doc.write_date(especifico['dt_obito'], (60, 736), pg=1, spacing=2) #data_obito

#! campo 87 data do encerramento
doc.write_date(especifico['dt_encerramento'], (180, 735), pg=1, spacing=2) #data_encerramento

doc.write_text(especifico['municipio_us_investigador'], (60, 769), pg=1, font_size=9) #municipio_investigador
doc.write_code(especifico['cod_us_investigador'], (469, 769), pg=1, space=2) #cod_unidade_investigador
doc.write_text(especifico['nome_investigador'], (55, 797), pg=1, font_size=9) #nome_investigador
doc.write_text(especifico['funcao_investigador'], (260, 797), pg=1, font_size=9) #funcao_investigador
doc.write_text(especifico['assinatura_investigador'], (470, 797), pg=1, font_size=9) #assinatura_investigador

doc.save('paralisia_flacida.pdf', notificatoria)