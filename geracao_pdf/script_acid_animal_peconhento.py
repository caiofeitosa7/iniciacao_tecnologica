from pdfWritter import PDFWriter
pdf = 'fichas/completas/Acid Anim Peçonhento.geracao_pdf'
document = PDFWriter(pdf)

notificatoria = {
    "numero_ficha": "abcdefg",
    "tipo_notificacao": "abcdefg",
    "agravoDoenca": "abcdefg",
    "dt_notificacao": "abcdefg",
    "uf_notificacao": "abcdefg",
    "municipio_notificacao": "abcdefg",
    "cod_ibge_notificacao": "abcdefg",
    "unidade_saude": "abcdefg",
    "cod_unidade_saude": "abcdefg",
    "dt_sintomas": "abcdefg",
    "nome_paciente": "abcdefg",
    "dt_nascimento": "abcdefg",
    "idade": "abcdefg",
    "tipo_idade": "abcdefg",
    "sexo": "abcdefg",
    "gestante": "abcdefg",
    "raca": "abcdefg",
    "escolaridade": "abcdefg",
    "numero_sus": "abcdefg",
    "nome_mae": "abcdefg",
    "dt_primeiro_sintoma": "abcdefg",
    "numero_casos_suspeitos": "abcdefg",
    "local_inicial_ocorrencia": "abcdefg",
    "local_inicial_ocorrencia_outro": "abcdefg",
    "uf_residencia": "abcdefg",
    "municipio_residencia": "abcdefg",
    "cod_ibge_residencia": "abcdefg",
    "distrito_residencia": "abcdefg",
    "bairro_residencia": "abcdefg",
    "logradouro_residencia": "abcdefg",
    "codigo_residencia": "abcdefg",
    "numero_residencia": "abcdefg",
    "complemento_residencia": "abcdefg",
    "geo_campo1": "abcdefg",
    "geo_campo2": "abcdefg",
    "ponto_ref_residencia": "abcdefg",
    "cep_residencia": "abcdefg",
    "telefone_residencia": "abcdefg",
    "zona_residencia": "abcdefg",
    "pais_residencia": "abcdefg",
    "municipio_us_notificante": "abcdefg",
    "nome_notificante": "abcdefg",
    "funcao_notificante": "abcdefg",
    "assinatura_notificante": "abcdefg",
    "dt_amostra_sorologia": "abcdefg",
    "dt_outra_amostra": "abcdefg",
    "tipo_exame": "abcdefg",
    "obito": "abcdefg",
    "caso_semelhante": "abcdefg",
    "exantema": "abcdefg",
    "dt_inicio_exantema": "abcdefg",
    "petequiaSufusao": "abcdefg",
    "liquor": "abcdefg",
    "bacterioscopia": "abcdefg",
    "tomou_vacina": "abcdefg",
    "dt_ultima_dose_tomada": "abcdefg",
    "hospitalizacao": "abcdefg",
    "dt_hospitalizacao": "abcdefg",
    "uf_hospital": "abcdefg",
    "municipio_hospital": "abcdefg",
    "cod_ibge_hospital": "abcdefg",
    "nome_hospital": "abcdefg",
    "cod_hospital": "abcdefg",
    "hipotese_diagnostica1": "abcdefg",
    "hipotese_diagnostica2": "abcdefg",
    "pais_infeccao": "abcdefg",
    "distrito_infeccao": "abcdefg",
    "uf_infeccao": "abcdefg",
    "municipio_infeccao": "abcdefg",
    "bairro_infeccao": "abcdefg"
}
especifico = {
    "numero_ficha2": "15648",
    "dt_notificacao2": "15/02/2022",
    "uf_notificacao2": "PI",
    "municipio_notificacao2": "abcdefg",
    "cod_ibge_notificacao2": "123456",
    "unidade_saude2": "abcdefg",
    "cod_unidade_saude2": "1234567",
    "dt_sintomas2": "15/02/2022",
    "nome_paciente2": "abcdefg",
    "dt_nascimento2": "15/02/2022",
    "idade2": "55",
    "tipo_idade2": "9",
    "sexo2": "9",
    "gestante2": "9",
    "raca2": "9",
    "escolaridade2": "9",
    "numero_sus2": "152648596325614",
    "nome_mae2": "abcdefg",
    "uf_residencia2": "PI",
    "municipio_residencia2": "abcdefg",
    "cod_ibge_residencia2": "123456",
    "distrito_residencia2": "abcdefg",
    "bairro_residencia2": "abcdefg",
    "logradouro_residencia2": "abcdefg",
    "codigo_residencia2": "abcdefg",
    "numero_residencia2": "5486",
    "complemento_residencia2": "abcdefg",
    "geo_campo1_2": "abcdefg",
    "geo_campo2_2": "abcdefg",
    "ponto_ref_residencia2": "abcdefg",
    "cep_residencia2": "64016666",
    "telefone_residencia2": "8688254585",
    "zona_residencia2": "abcdefg",
    "pais_residencia2": "abcdefg",
    "dt_investigacao": "15/02/2022",
    "ocupacao": "abcdefg",
    "dt_acidente": "15/02/2022",
    "uf_ocorr": "PI",
    "municipio_ocorr": "abcdefg",
    "cod_ibge_ocorr": "123456",
    "local_ocorr": "abcdefg",
    "zona_ocorr": "abcdefg",
    "tempo_picada": "abcdefg",
    "local_picada": "07",
    "manif_local": "9",
    "manif_dor": "9",
    "manif_edema": "9",
    "manif_equimose": "9",
    "manif_necrose": "9",
    "manif_outro": "9",
    "manif_outro_descricao": "9",
    "manif_sistemica": "9",
    "manif_sist_neurop": "9",
    "manif_sist_miolit": "9",
    "manif_sist_hemorr": "9",
    "manif_sist_renais": "9",
    "manif_sist_vagais": "9",
    "manif_sist_outra": "9",
    "manif_sist_outra_descricao": "9",
    "tempo_coagulacao": "9",
    "tipo_acidente": "9",
    "tipo_acidente_outro": "9",
    "serp_tipo_acid": "9",
    "aran_tipo_acid": "9",
    "lagar_tipo_acid": "9",
    "classif_caso": "9",
    "soroterapia": "9",
    "soroterapia_sab": "9",
    "soroterapia_sabl": "9",
    "soroterapia_sabc": "9",
    "soroterapia_sac": "9",
    "soroterapia_sae": "9",
    "soroterapia_saes": "9",
    "soroterapia_saar": "9",
    "soroterapia_salox": "9",
    "soroterapia_salon": "9",
    "comp_locais": "9",
    "comp_loc_infec": "9",
    "comp_loc_necrose": "9",
    "comp_loc_sindrome": "9",
    "comp_loc_deficit": "9",
    "comp_loc_amputacao": "9",
    "comp_sistemica": "9",
    "comp_sist_renal": "9",
    "comp_sist_edema": "9",
    "comp_sist_septi": "9",
    "comp_sist_choque": "9",
    "doenca_rel_trab": "9",
    "evolucao_caso": "abcdefg",
    "dt_obito": "15/02/2022",
    "dt_encerramento": "15/02/2022",
    "obs_adicionais": "abcdefg",
    "municipio_us_investigador": "abcdefg",
    "cod_us_investigador": "abcdefg",
    "nome_investigador": "abcdefg",
    "funcao_investigador": "abcdefg",
    "assinatura_investigador": "abcdefg"
}

###################################################
# Dados do paciente
###################################################

document.write_text(especifico['numero_ficha2'],(467, 37))
document.write_date(especifico['dt_notificacao2'], (446, 150), spacing=2) #data_notificacao
document.write_uf(especifico['uf_notificacao2'], (55, 180)) #uf_notificacao
document.write_text(especifico['municipio_notificacao2'], (90, 179)) #municipio_notificacao __unid_saude 55,220
document.write_code(especifico['cod_ibge_notificacao2'], (475, 179),space=2) #cod_ibge
document.write_text(especifico['unidade_saude2'], (65, 208)) #cod_unid_saude
document.write_code(especifico['cod_unidade_saude2'], (335, 208),space=2) #cod_unid_saude
document.write_date(especifico['dt_sintomas2'], (444, 206), spacing=2) #data_diagnostico
##############################################
#####          NOTIFICACAO INDIVIDUAL     ####
##############################################
document.write_text(especifico['nome_paciente2'], (55, 238)) #nome
document.write_date(especifico['dt_nascimento2'], (446, 238), spacing=2) #data_nascimento
document.write_code(especifico['idade2'], (63, 268),space=2) #idade
document.write_mini(especifico['tipo_idade2'], (110, 260)) #tipo_idade
document.write_mini(especifico['sexo2'], (231, 253)) #sexo
document.write_mini(especifico['gestante2'], (427, 253)) #gestante
document.write_mini(especifico['raca2'], (552, 253)) #raça/cor
document.write_mini(especifico['escolaridade2'], (552, 283)) #escolaridade
document.write_code(especifico['numero_sus2'], (56, 328),space=2, font_size=10) #cartao_sus
document.write_text(especifico['nome_mae2'], (240, 328)) #nome_mae
##############################################
#####          DADOS DE RESIDENCIA        ####
##############################################

document.write_uf(especifico['uf_residencia2'], (56, 358)) #uf_residencia
document.write_text(especifico['municipio_residencia2'], (95, 358)) #municipio_residencia
document.write_code(especifico['cod_ibge_residencia2'], (323, 358),space=2) #cod_ibge_residencia
document.write_text(especifico['distrito_residencia2'], (422, 358)) #endereco
document.write_text(especifico['bairro_residencia2'], (64, 382)) #bairro
document.write_text(especifico['logradouro_residencia2'], (210, 383)) #logradouro
document.write_code(especifico['codigo_residencia2'], (479, 383),space=2) #cod_logradouro
document.write_text(especifico['numero_residencia2'], (65, 407)) #numero
document.write_text(especifico['complemento_residencia2'], (120, 407)) #complemento
document.write_text(especifico['geo_campo1_2'], (415, 410)) #geo_campo_1
document.write_text(especifico['geo_campo2_2'], (55, 433)) #geo_campo_2
document.write_text(especifico['ponto_ref_residencia2'], (230, 433)) #ponto_ref
document.write_code(especifico['cep_residencia2'], (456, 436),space=2) #cep
document.write_telefone(especifico['telefone_residencia2'], (55, 460), space=2) #telefone
document.write_mini(especifico['zona_residencia2'], (333, 448)) #zona
document.write_text(especifico['pais_residencia2'], (380, 459)) #pais
##############################################
#####        DADOS  COMPLEMENTARES        ####
##############################################
document.write_date(especifico['dt_investigacao'], (60, 509),spacing=2) #data_investigacao
document.write_text(especifico['ocupacao'], (180, 510)) #ocupacao
document.write_date(especifico['dt_acidente'], (453, 510),spacing=2) #data_acidente
document.write_uf(especifico['uf_ocorr'], (57, 538)) #uf_acidente
document.write_text(especifico['municipio_ocorr'], (95, 538),font_size=12) #municipio_acidente
document.write_code(especifico['cod_ibge_ocorr'], (264, 537),space=2) #cod_ibge_acidente
document.write_text(especifico['local_ocorr'], (365, 538)) #local_acidente
document.write_mini(especifico['zona_ocorr'], (230, 551)) #zona_acidente
document.write_mini(especifico['tempo_picada'], (553, 553)) #tempo_decorrido
document.write_code(especifico['local_picada'], (139, 587), space=1) #local_picada
document.write_mini(especifico['manif_local'], (177, 610)) #manifes_locais
document.write_mini(especifico['manif_dor'], (212, 625)) #manifes_dor
document.write_mini(especifico['manif_edema'], (252, 626)) #manifes_edema
document.write_mini(especifico['manif_equimose'], (306, 625)) #manifes_equimose
document.write_mini(especifico['manif_necrose'], (364, 626)) #manifes_necrose
document.write_mini(especifico['manif_outro'], (428, 627)) #manifes_outras
document.write_mini(especifico['manif_outro_descricao'], (500, 626)) #manifes_text
document.write_mini(especifico['manif_sistemica'], (123, 666)) #manifes_sistemica
document.write_mini(especifico['manif_sist_neurop'], (155, 672)) #neuroparaliticas
document.write_mini(especifico['manif_sist_miolit'], (155, 693)) #mioliticas
document.write_mini(especifico['manif_sist_hemorr'], (289, 664)) #hemorragicas
document.write_mini(especifico['manif_sist_renais'], (291, 687)) #renais
document.write_mini(especifico['manif_sist_vagais'], (410, 665)) #vagais
document.write_mini(especifico['manif_sist_outra'], (410, 685)) #sistemic_outras
document.write_mini(especifico['manif_sist_outra_descricao'], (426, 693)) #sistemic_text
document.write_mini(especifico['tempo_coagulacao'], (555, 670)) #tempo_coagular
document.write_mini(especifico['tipo_acidente'], (288, 716)) #tipo_acidente
document.write_mini(especifico['tipo_acidente_outro'], (175, 732)) #acidente_text
document.write_mini(especifico['serp_tipo_acid'], (539, 715)) #serpe_tipo
document.write_mini(especifico['aran_tipo_acid'], (286, 751)) #aranha_tipo
document.write_mini(especifico['lagar_tipo_acid'], (544, 753)) #lagarta_tipo
####### fim da pagina 1######################
document.write_mini(especifico['classif_caso'], (335, 45),pg=1) #class_caso
document.write_mini(especifico['soroterapia'], (549, 44),pg=1) #soroterapia
document.write_code(especifico['soroterapia_sab'], (187, 80),pg=1,space=2) #SAB
document.write_code(especifico['soroterapia_sabl'], (187, 97),pg=1,space=2) #SABL
document.write_code(especifico['soroterapia_sabc'], (187, 114),pg=1,space=2) #SABC
document.write_code(especifico['soroterapia_sac'], (355, 76),pg=1,space=2) #SAC
document.write_code(especifico['soroterapia_sae'], (355, 96),pg=1,space=2) #SAE
document.write_code(especifico['soroterapia_saes'], (355, 113),pg=1,space=2) #SAEs
document.write_code(especifico['soroterapia_saar'], (523, 76),pg=1,space=2) #SAAr
document.write_code(especifico['soroterapia_salox'], (525, 95),pg=1,space=2) #SALox
document.write_code(especifico['soroterapia_salon'], (526, 112),pg=1,space=2) #SALon
document.write_mini(especifico['comp_locais'], (163, 135),pg=1) #complica_locais
document.write_mini(especifico['comp_loc_infec'], (188, 150),pg=1) #infec_secundaria
document.write_mini(especifico['comp_loc_necrose'], (263, 150),pg=1) #necrose_extensa
document.write_mini(especifico['comp_loc_sindrome'], (328, 150),pg=1) #sindrome_compartimental
document.write_mini(especifico['comp_loc_deficit'], (422, 151),pg=1) #deficit_funcional
document.write_mini(especifico['comp_loc_amputacao'], (506, 150),pg=1) #amputacao
document.write_mini(especifico['comp_sistemica'], (178, 171),pg=1) #complica_sistemica
document.write_mini(especifico['comp_sist_renal'], (208, 185),pg=1) #sist_insuf_renal
document.write_mini(especifico['comp_sist_edema'], (286, 186),pg=1) #sist_edema_pulmonar
document.write_mini(especifico['comp_sist_septi'], (416, 186),pg=1) #sist_sepicemia
document.write_mini(especifico['comp_sist_choque'], (515, 185),pg=1) #sist_choque
document.write_mini(especifico['doenca_rel_trab'], (139, 214),pg=1) #acidente_trabalho
document.write_mini(especifico['evolucao_caso'], (279, 205),pg=1) #evolucao_caso
document.write_date(especifico['dt_obito'], (330, 233),pg=1,spacing=2) #data_obito
document.write_date(especifico['dt_encerramento'], (460, 233),pg=1,spacing=2) #data_encerramento
document.write_box(especifico['obs_adicionais'], 1,(32, 680, 568,740)) #observacoes
document.write_text(especifico['municipio_us_investigador'], (60, 745),pg=1) #municipio_investigador
document.write_code(especifico['cod_us_investigador'], (471, 745),pg=1,space=2) #cod_unid_investigador
document.write_text(especifico['nome_investigador'], (60, 768),pg=1) #nome_investigador
document.write_text(especifico['funcao_investigador'], (260, 768),pg=1) #funcao_investigador
document.write_text(especifico['assinatura_investigador'], (472, 768),pg=1) #assign_investigador

document.save('acidente_animal_peconhento.geracao_pdf', notificatoria)