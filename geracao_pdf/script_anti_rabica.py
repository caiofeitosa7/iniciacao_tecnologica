from pdfWritter import PDFWriter
pdf = 'fichas/completas/Antendimento Anti-Rábica1.geracao_pdf'
document = PDFWriter(pdf)

notificatorio = {
    "numero_ficha": "99cdefg",
    "tipo_notificacao": "9",
    "agravoDoenca": "99cdefg",
    "dt_notificacao": "15/02/2022",
    "uf_notificacao": "PI",
    "municipio_notificacao": "99cdefg",
    "cod_ibge_notificacao": "123456",
    "unidade_saude": "25",
    "cod_unidade_saude": "123456",
    "dt_sintomas": "15/02/2022",
    "nome_paciente": "99cdefg",
    "dt_nascimento": "15/02/2022",
    "idade": "25",
    "tipo_idade": "25",
    "sexo": "99cdefg",
    "gestante": "99cdefg",
    "raca": "99cdefg",
    "escolaridade": "25",
    "numero_sus": "123456789012345",
    "nome_mae": "99cdefg",
    "dt_primeiro_sintoma": "15/02/2022",
    "numero_casos_suspeitos": "123456789012345",
    "local_inicial_ocorrencia": "99cdefg",
    "local_inicial_ocorrencia_outro": "99cdefg",
    "uf_residencia": "PI",
    "municipio_residencia": "9",
    "cod_ibge_residencia": "123456",
    "distrito_residencia": "9",
    "bairro_residencia": "9",
    "logradouro_residencia": "9",
    "codigo_residencia": "123456",
    "numero_residencia": "9",
    "complemento_residencia": "9",
    "geo_campo1": "99cdefg",
    "geo_campo2": "99cdefg",
    "ponto_ref_residencia": "9",
    "cep_residencia": "64000000",
    "telefone_residencia": "86999999999",
    "zona_residencia": "9",
    "pais_residencia": "9",
    "municipio_us_notificante": "99cdefg",
    "nome_notificante": "99cdefg",
    "funcao_notificante": "99cdefg",
    "assinatura_notificante": "99cdefg",
    "dt_amostra_sorologia": "15/02/2022",
    "dt_outra_amostra": "15/02/2022",
    "tipo_exame": "9",
    "obito": "99cdefg",
    "caso_semelhante": "99cdefg",
    "exantema": "99cdefg",
    "dt_inicio_exantema": "15/02/2022",
    "petequiaSufusao": "PI",
    "liquor": "99cdefg",
    "bacterioscopia": "99cdefg",
    "tomou_vacina": "99cdefg",
    "dt_ultima_dose_tomada": "15/02/2022",
    "hospitalizacao": "99cdefg",
    "dt_hospitalizacao": "15/02/2022",
    "uf_hospital": "PI",
    "municipio_hospital": "99cdefg",
    "cod_ibge_hospital": "123456",
    "nome_hospital": "99cdefg",
    "cod_hospital": "123456",
    "hipotese_diagnostica1": "99cdefg",
    "hipotese_diagnostica2": "99cdefg",
    "pais_infeccao": "99cdefg",
    "distrito_infeccao": "99cdefg",
    "uf_infeccao": "PI",
    "municipio_infeccao": "99cdefg",
    "bairro_infeccao": "99cdefg"
}
especifico = {
    "numero_ficha2": "99cdefg",
    "dt_notificacao2": "15/02/2022",
    "uf_notificacao2": "PI",
    "municipio_notificacao2": "99cdefg",
    "cod_ibge_notificacao2": "123456",
    "unidade_saude2": "25",
    "cod_unidade_saude2": "123456",
    "dt_atendimento": "15/02/2022",
    "nome_paciente2": "99cdefg",
    "dt_nascimento2": "15/02/2022",
    "idade2": "25",
    "tipo_idade2": "25",
    "sexo2": "99cdefg",
    "gestante2": "99cdefg",
    "raca2": "99cdefg",
    "escolaridade2": "25",
    "numero_sus2": "123456789012345",
    "nome_mae2": "99cdefg",
    "uf_residencia2": "PI",
    "municipio_residencia2": "9",
    "cod_ibge_residencia2": "123456",
    "distrito_residencia2": "9",
    "bairro_residencia2": "9",
    "logradouro_residencia2": "9",
    "codigo_residencia2": "123456",
    "numero_residencia2": "9",
    "complemento_residencia2": "9",
    "geo_campo1_2": "99cdefg",
    "geo_campo2_2": "99cdefg",
    "ponto_ref_residencia2": "9",
    "cep_residencia2": "64000000",
    "telefone_residencia2": "86999999999",
    "zona_residencia2": "9",
    "pais_residencia2": "9",
    "ocupacao": "99cdefg",
    "exp_virus_indireto": "99cdefg",
    "exp_virus_arranhadura": "99cdefg",
    "exp_virus_lambedura": "99cdefg",
    "exp_virus_mordedura": "99cdefg",
    "exp_virus_outro": "99cdefg",
    "loc_mucosa": "99cdefg",
    "loc_cabeca": "99cdefg",
    "loc_maos_pes": "99cdefg",
    "loc_tronco": "99cdefg",
    "loc_memb_superiores": "9",
    "loc_memb_inferiores": "9",
    "ferimento": "99cdefg",
    "tp_ferimento_prof": "9",
    "tp_ferimento_superf": "9",
    "tp_ferimento_dilac": "9",
    "dt_exposicao": "15/02/2022",
    "antec_trat_pre_exp": "99cdefg",
    "antec_trat_pos_exp": "99cdefg",
    "conclusao_trat_ant": "99cdefg",
    "num_doses_aplicadas": "99cdefg",
    "especie_animal": "99cdefg",
    "especie_animal_herb_espec": "99cdefg",
    "especie_animal_outro": "99cdefg",
    "cond_animal": "9",
    "anim_passivel_obs": "99cdefg",
    "trat_indicado": "99cdefg",
    "produtor_vacina": "99cdefg",
    "produtor_vacina_outro": "99cdefg",
    "lote_vacina": "99cdefg",
    "dt_vencimento": "15/02/2022",
    "dt_dose1": "15/02",
    "dt_dose2": "15/02",
    "dt_dose3": "15/02",
    "dt_dose4": "15/02",
    "dt_dose5": "15/02",
    "cond_final_animal": "9",
    "interrup_trat": "99cdefg",
    "motivo_interrup_trat": "99cdefg",
    "procurou_paciente": "99cdefg",
    "evento_adv_vacina": "99cdefg",
    "soro_antirabico": "99cdefg",
    "peso_paciente": "999",
    "tipo_soro_aplicado": "9",
    "quant_soro_aplicado": "999",
    "infilt_soro_ferim_total": "99cdefg",
    "infilt_soro_ferim_parcial": "99cdefg",
    "lab_produtor_soro": "99cdefg",
    "lab_produtor_soro_outro": "99cdefg",
    "num_partida": "9999999999",
    "evento_adv_soro": "99cdefg",
    "dt_encerramento": "15/02/2022",
    "obs_adicionais": "99cdefg",
    "municipio_us_investigador": "99cdefg",
    "cod_us_investigador": "123456",
    "nome_investigador": "99cdefg",
    "funcao_investigador": "99cdefg",
    "assinatura_investigador": "99cdefg"
}

###################################################
# Dados do paciente
###################################################
document.write_text(especifico['numero_ficha2'],(470, 47))
document.write_date(especifico['dt_notificacao2'], (448, 111), spacing=2) #data_notificacao
document.write_uf(especifico['uf_notificacao2'], (55, 139)) #uf_notificacao
document.write_text(especifico['municipio_notificacao2'], (90, 140)) #municipio_notificacao __unid_saude 55,space=220
document.write_code(especifico['cod_ibge_notificacao2'], (475, 140),space=2) #cod_ibge
document.write_text(especifico['unidade_saude2'], (65, 168)) #cod_unid_saude
document.write_code(especifico['cod_unidade_saude2'], (335, 168),space=2) #cod_unid_saude
document.write_date(especifico['dt_atendimento'], (448, 168), spacing=2) #data_diagnostico
##############################################
#####          NOTIFICACAO INDIVIDUAL     ####
##############################################
document.write_text(especifico['nome_paciente2'], (55, 198)) #nome
document.write_date(especifico['dt_nascimento2'], (448, 198), spacing=2) #data_nascimento
document.write_code(especifico['idade2'], (63, 228),space=2) #idade
document.write_mini(especifico['tipo_idade2'], (110, 220)) #tipo_idade
document.write_mini(especifico['sexo2'], (232, 213)) #sexo
document.write_mini(especifico['gestante2'], (428, 213)) #gestante
document.write_mini(especifico['raca2'], (553, 213)) #raça/cor
document.write_mini(especifico['escolaridade2'], (553, 243)) #escolaridade
document.write_code(especifico['numero_sus2'], (57, 288),space=2, font_size=10) #cartao_sus
document.write_text(especifico['nome_mae2'], (240, 288)) #nome_mae
##############################################
#####          DADOS DE RESIDENCIA        ####
##############################################

document.write_uf(especifico['uf_residencia2'], (56, 318)) #uf_residencia
document.write_text(especifico['municipio_residencia2'], (95, 318)) #municipio_residencia
document.write_code(especifico['cod_ibge_residencia2'], (326, 318),space=2) #cod_ibge_residencia
document.write_text(especifico['distrito_residencia2'], (422, 318)) #endereco
document.write_text(especifico['bairro_residencia2'], (64, 342)) #bairro
document.write_text(especifico['logradouro_residencia2'], (210, 344)) #logradouro
document.write_code(especifico['codigo_residencia2'], (480, 344),space=2) #cod_logradouro
document.write_text(especifico['numero_residencia2'], (65, 367)) #numero
document.write_text(especifico['complemento_residencia2'], (120, 367)) #complemento
document.write_text(especifico['geo_campo1_2'], (415, 370)) #geo_campo_1
document.write_text(especifico['geo_campo2_2'], (55, 393)) #geo_campo_2
document.write_text(especifico['ponto_ref_residencia2'], (230, 393)) #ponto_ref
document.write_code(especifico['cep_residencia2'], (455, 396),space=2) #cep
document.write_telefone(especifico['telefone_residencia2'], (57, 420), space=2) #telefone
document.write_mini(especifico['zona_residencia2'], (333, 408)) #zona
document.write_text(especifico['pais_residencia2'], (380, 420)) #pais
####################################################
# Dados Complementares
####################################################
document.write_text(especifico['ocupacao'], (60, 470)) #ocupacao
document.write_mini(especifico['exp_virus_indireto'], (192, 492)) #tipo_exposicao
document.write_mini(especifico['exp_virus_arranhadura'], (271, 492)) #virus_arranhadura
document.write_mini(especifico['exp_virus_lambedura'], (340, 492)) #virus_lambedura
document.write_mini(especifico['exp_virus_mordedura'], (405, 492)) #virus_mordedura
document.write_mini(especifico['exp_virus_outro'], (468, 492)) #virus_outra
document.write_mini(especifico['loc_mucosa'], (190, 521)) #local_mucosa
document.write_mini(especifico['loc_cabeca'], (233, 520)) #local_cabeca
document.write_mini(especifico['loc_maos_pes'], (309, 520)) #local_maos
document.write_mini(especifico['loc_tronco'], (360, 520)) #local_tronco
document.write_mini(especifico['loc_memb_superiores'], (400, 520)) #local_membros_sup
document.write_mini(especifico['loc_memb_inferiores'], (488, 521)) #local_membros_inf
document.write_mini(especifico['ferimento'], (204, 542)) #ferimento
document.write_mini(especifico['tp_ferimento_prof'], (357, 552)) #ferimento_profundo
document.write_mini(especifico['tp_ferimento_superf'], (425, 552)) #ferimento_superficial
document.write_mini(especifico['tp_ferimento_dilac'], (490, 551)) #ferimento_dilacerante
document.write_date(especifico['dt_exposicao'], (64, 585), spacing=2) #data_exposicao
document.write_mini(especifico['antec_trat_pre_exp'], (354, 582)) #antecedente_ar_pre_expo
document.write_mini(especifico['antec_trat_pos_exp'], (482, 582)) #antecedente_ar_pos_expo
document.write_mini(especifico['conclusao_trat_ant'], (298, 601)) #anti_rabico_concluido
document.write_code(especifico['num_doses_aplicadas'], (509, 613),space=2) #n_doses
document.write_mini(especifico['especie_animal'], (552, 625)) #espec_anim_agressor
document.write_mini(especifico['especie_animal_herb_espec'], (365, 635)) #herb_espec
document.write_mini(especifico['especie_animal_outro'], (460, 635)) #espec_outras
document.write_mini(especifico['cond_animal'], (289, 655)) #cond_animal
document.write_mini(especifico['anim_passivel_obs'], (554, 654)) #animal_obs
document.write_mini(especifico['trat_indicado'], (557, 692)) #trat_indicado
document.write_mini(especifico['produtor_vacina'], (559, 727)) #vacina_lab
document.write_mini(especifico['produtor_vacina_outro'], (425, 738)) #vacina_outros
document.write_text(especifico['lote_vacina'], (70, 770)) #num_lote
document.write_date(especifico['dt_vencimento'], (464, 770), spacing=2) #dt_vencimento
############################################## fim page
document.write_date(especifico['dt_dose1'], (72, 80),pg=1, spacing=2) #dt_dose_1
document.write_date(especifico['dt_dose2'], (160, 80),pg=1, spacing=2) #dt_dose_2
document.write_date(especifico['dt_dose3'], (248, 80),pg=1, spacing=2) #dt_dose_3
document.write_date(especifico['dt_dose4'], (336, 80),pg=1, spacing=2) #dt_dose_4
document.write_date(especifico['dt_dose5'], (424, 80),pg=1, spacing=2) #dt_dose_5
document.write_mini(especifico['cond_final_animal'], (552, 98),pg=1) #cond_fin_animal
document.write_mini(especifico['interrup_trat'], (203, 140),pg=1) #interr_tratamento
document.write_mini(especifico['motivo_interrup_trat'], (549, 142),pg=1) #motivo_interrupcao
document.write_mini(especifico['procurou_paciente'], (408, 181),pg=1) #abandono
document.write_mini(especifico['evento_adv_vacina'], (561, 175),pg=1) #evento_adverso_vac
document.write_mini(especifico['soro_antirabico'], (198, 210),pg=1) #indic_soro_ar
document.write_code(especifico['peso_paciente'], (249, 232),pg=1,space=1) #peso_paciente
document.write_mini(especifico['tipo_soro_aplicado'], (551, 210),pg=1) #tipo_soro_aplic
document.write_code(especifico['quant_soro_aplicado'], (349, 230),pg=1,space=1) #qtd_soro_aplic
document.write_mini(especifico['infilt_soro_ferim_total'], (178, 265),pg=1) #infiltra_soro_total
document.write_mini(especifico['infilt_soro_ferim_parcial'], (227, 265),pg=1) #infiltra_soro_parcial
document.write_mini(especifico['lab_produtor_soro'], (551, 249),pg=1) #lab_prod_soro
document.write_mini(especifico['lab_produtor_soro_outro'], (487, 266),pg=1) #lab_prod_text
document.write_code(especifico['num_partida'], (58, 303),pg=1,space=2) #num_partida
document.write_mini(especifico['evento_adv_soro'], (355, 295),pg=1) #evento_adv_soro
document.write_date(especifico['dt_encerramento'], (382, 303),pg=1, spacing=2) #dt_encerramento
document.write_box(especifico['obs_adicionais'],pg=1, rect=(32, 320, 569, 515)) #obs
document.write_text(especifico['municipio_us_investigador'], (60, 543),pg=1) #municipio_investigador
document.write_code(especifico['cod_us_investigador'], (470, 543),pg=1,space=2) #cod_unid_saud
document.write_text(especifico['nome_investigador'], (60, 573),pg=1) #nome_investigador
document.write_text(especifico['funcao_investigador'], (265, 573),pg=1) #funcao_investigador
document.write_text(especifico['assinatura_investigador'], (473, 571),pg=1) #asign_investigador







document.save('anti_rabica.geracao_pdf', notificatorio)