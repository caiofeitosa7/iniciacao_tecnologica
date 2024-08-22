from pdfWritter import PDFWriter

pdf = 'fichas/completas/Intoxicação Exógena1.geracao_pdf'
document = PDFWriter(pdf)

notificatoria = {
    "numero_ficha": "15485",
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
    "numero_residencia": "15485",
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
    "numero_ficha2": "15485",
    "dt_notificacao2": "15/02/2022",
    "uf_notificacao2": "PI",
    "municipio_notificacao2": "99cdefg",
    "cod_ibge_notificacao2": "123456",
    "unidade_saude2": "25",
    "cod_unidade_saude2": "123456",
    "dt_sintomas2": "15/02/2022",
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
    "numero_residencia2": "15485",
    "complemento_residencia2": "9",
    "geo_campo1_2": "99cdefg",
    "geo_campo2_2": "99cdefg",
    "ponto_ref_residencia2": "9",
    "cep_residencia2": "64000000",
    "telefone_residencia2": "86999999999",
    "zona_residencia2": "9",
    "pais_residencia2": "9",
    "dt_investigacao": "15/02/2022",
    "ocupacao": "99cdefg",
    "sit_merc_trabalho": "9",
    "sit_merc_trabalho_outro": "9",
    "loc_exposicao": "99cdefg",
    "loc_exposicao_outro": "99cdefg",
    "nome_estab_ocorr": "99cdefg",
    "atv_econ_estab_ocorr": "99cdefg",
    "uf_estab_ocorr": "PI",
    "municipio_estab_ocorr": "99cdefg",
    "cod_ibge_estab_ocorr": "123456",
    "distrito_estab_ocorr": "99cdefg",
    "bairro_estab_ocorr": "99cdefg",
    "lograd_estab_ocorr": "99cdefg",
    "numero_estab_ocorr": "15485",
    "complem_estab_ocorr": "99cdefg",
    "pt_ref_estab_ocorr": "99cdefg",
    "cep_estab_ocorr": "64000000",
    "telefone_estab_ocorr": "86999999999",
    "zona_estab_ocorr": "99cdefg",
    "pais_estab_ocorr": "99cdefg",
    "agente_toxico": "99cdefg",
    "agente_toxico_outro": "99cdefg",
    "nome_agente_tox1": "99cdefg",
    "nome_agente_tox2": "99cdefg",
    "nome_agente_tox3": "99cdefg",
    "princ_agente_tox1": "99cdefg",
    "princ_agente_tox2": "99cdefg",
    "princ_agente_tox3": "99cdefg",
    "finalid_agrotox": "99cdefg",
    "finalid_agrotox_outro": "99cdefg",
    "atv_agrotox1": "99cdefg",
    "atv_agrotox2": "99cdefg",
    "atv_agrotox3": "99cdefg",
    "lavoura": "99cdefg",
    "via_exp1": "99cdefg",
    "via_exp2": "99cdefg",
    "via_exp3": "99cdefg",
    "circ_exp": "99cdefg",
    "circ_exp_outro": "99cdefg",
    "exp_decor_trab": "99cdefg",
    "tipo_exposicao": "9",
    "tempo_exp_atend": "99cdefg",
    "tipo_tempo_exp_atend": "9",
    "tipo_atendimento": "9",
    "hospitalizacao2": "99cdefg",
    "dt_internacao": "15/02/2022",
    "uf_hospital2": "PI",
    "municipio_hospital2": "99cdefg",
    "cod_ibge_hospital2": "123456",
    "nome_hospital2": "99cdefg",
    "cod_hospital2": "123456",
    "classif_final": "99cdefg",
    "diag_intox_conf": "99cdefg",
    "cid_intox_conf": "99cdefg",
    "criterio_confirm": "99cdefg",
    "evolucao_caso": "99cdefg",
    "dt_obito": "15/02/2022",
    "comun_acid_trab": "99cdefg",
    "dt_encerramento": "15/02/2022",
    "obs_adicionais": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc.",
    "municipio_us_investigador": "99cdefg",
    "cod_us_investigador": "123456",
    "nome_investigador": "99cdefg",
    "funcao_investigador": "99cdefg",
    "assinatura_investigador": "99cdefg"
}

###################################################
# Dados do paciente
###################################################
document.write_text(especifico['numero_ficha2'],(475, 49))
document.write_date(especifico['dt_notificacao2'], (448, 158), spacing=2) #data_notificacao
document.write_uf(especifico['uf_notificacao2'], (55, 187)) #uf_notificacao
document.write_text(especifico['municipio_notificacao2'], (90, 187)) #municipio_notificacao __unid_saude 55,space=220
document.write_code(especifico['cod_ibge_notificacao2'], (477, 187),space=2) #cod_ibge
document.write_text(especifico['unidade_saude2'], (70, 216)) #cod_unid_saude
document.write_code(especifico['cod_unidade_saude2'], (338, 216),space=2) #cod_unid_saude
document.write_date(especifico['dt_sintomas2'], (446, 215), spacing=2) #data_diagnostico
##############################################
#####          NOTIFICACAO INDIVIDUAL     ####
##############################################
document.write_text(especifico['nome_paciente2'], (55, 247)) #nome
document.write_date(especifico['dt_nascimento2'], (448, 247), spacing=2) #data_nascimento
document.write_code(especifico['idade2'], (65, 276),space=2) #idade
document.write_mini(especifico['tipo_idade2'], (112, 269)) #tipo_idade
document.write_mini(especifico['sexo2'], (233, 261)) #sexo
document.write_mini(especifico['gestante2'], (429, 261)) #gestante
document.write_mini(especifico['raca2'], (555, 262)) #raça/cor
document.write_mini(especifico['escolaridade2'], (555, 291)) #escolaridade
document.write_code(especifico['numero_sus2'], (57, 337),space=2, font_size=10) #cartao_sus
document.write_text(especifico['nome_mae2'], (240, 337)) #nome_mae
##############################################
#####          DADOS DE RESIDENCIA        ####
##############################################

document.write_uf(especifico['uf_residencia2'], (56, 366)) #uf_residencia
document.write_text(especifico['municipio_residencia2'], (95, 366)) #municipio_residencia
document.write_code(especifico['cod_ibge_residencia2'], (325, 366),space=2) #cod_ibge_residencia
document.write_text(especifico['distrito_residencia2'], (424, 366)) #endereco
document.write_text(especifico['bairro_residencia2'], (64, 390)) #bairro
document.write_text(especifico['logradouro_residencia2'], (210, 392)) #logradouro
document.write_code(especifico['codigo_residencia2'], (480, 392),space=2) #cod_logradouro
document.write_text(especifico['numero_residencia2'], (65, 415)) #numero
document.write_text(especifico['complemento_residencia2'], (120, 415)) #complemento
document.write_text(especifico['geo_campo1_2'], (415, 418)) #geo_campo_1
document.write_text(especifico['geo_campo2_2'], (55, 440)) #geo_campo_2
document.write_text(especifico['ponto_ref_residencia2'], (230, 442)) #ponto_ref
document.write_code(especifico['cep_residencia2'], (457, 444),space=2) #cep
document.write_telefone(especifico['telefone_residencia2'], (57, 468), space=2) #telefone
document.write_mini(especifico['zona_residencia2'], (335, 455)) #zona
document.write_text(especifico['pais_residencia2'], (380, 466)) #pais
##############################################
#####        DADOS  COMPLEMENTARES        ####
##############################################
document.write_date(especifico['dt_investigacao'], (60, 523), spacing=2) #data_investigacao
document.write_text(especifico['ocupacao'], (200, 524)) #ocupacao
document.write_code(especifico['sit_merc_trabalho'], (533, 543),space=1) #sit_mercado_tr
document.write_mini(especifico['sit_merc_trabalho_outro'], (470, 574)) #sit_mercado_tr_outros
document.write_mini(especifico['loc_exposicao'], (542, 604)) #loc_exposicao
document.write_mini(especifico['loc_exposicao_outro'], (350, 620)) #loc_exposicao_outros
##############################################
#####        DADOS  EXPOSICAO             ####
##############################################
document.write_text(especifico['nome_estab_ocorr'], (55, 650)) #local
document.write_text(especifico['atv_econ_estab_ocorr'], (410, 650)) #cnae
document.write_uf(especifico['uf_estab_ocorr'], (57, 677)) #uf
document.write_text(especifico['municipio_estab_ocorr'], (100, 676)) #municipio
document.write_code(especifico['cod_ibge_estab_ocorr'], (313, 676),space=2) #ibge
document.write_text(especifico['distrito_estab_ocorr'], (420, 676)) #distrito
document.write_text(especifico['bairro_estab_ocorr'], (55, 705)) #bairro
document.write_text(especifico['lograd_estab_ocorr'], (222, 705)) #logradouro
document.write_text(especifico['numero_estab_ocorr'], (62, 730)) #numero
document.write_text(especifico['complem_estab_ocorr'], (120, 730)) #complemento
document.write_text(especifico['pt_ref_estab_ocorr'], (283, 728)) #ponto_ref
document.write_code(especifico['cep_estab_ocorr'], (456, 729),space=2) #cep
document.write_telefone(especifico['telefone_estab_ocorr'], (57, 758), space=2) #telefone
document.write_mini(especifico['zona_estab_ocorr'], (330, 745)) #zona
document.write_text(especifico['pais_estab_ocorr'], (380, 758)) #pais
document.write_code(especifico['agente_toxico'], (532, 42),pg=1, space=1) #gp_agente_toxic
document.write_mini(especifico['agente_toxico_outro'], (240, 84),pg=1) #gp_agente_toxico_outros
document.write_text(especifico['nome_agente_tox1'], (83, 122),pg=1) #agente_toxico_1
document.write_text(especifico['nome_agente_tox2'], (83, 141),pg=1) #agente_toxico_2
document.write_text(especifico['nome_agente_tox3'], (83, 159),pg=1) #agente_toxico_3
document.write_text(especifico['princ_agente_tox1'], (350, 124),pg=1) #principio_ativo_1
document.write_text(especifico['princ_agente_tox2'], (350, 142),pg=1) #principio_ativo_2
document.write_text(especifico['princ_agente_tox3'], (350, 160),pg=1) #principio_ativo_3
document.write_mini(especifico['finalid_agrotox'], (535, 179),pg=1) #agrotoxico_fin
document.write_mini(especifico['finalid_agrotox_outro'], (235, 196),pg=1) #agrotoxico_fin_outros
document.write_code(especifico['atv_agrotox1'], (486, 219),pg=1, space=1) #agrotoxico_ativ_1
document.write_code(especifico['atv_agrotox2'], (486, 234),pg=1, space=1) #agrotoxico_ativ_2
document.write_code(especifico['atv_agrotox3'], (486, 249),pg=1, space=1) #agrotoxico_ativ_3
document.write_text(especifico['lavoura'], (80, 285),pg=1) #agrotoxico_cult
document.write_mini(especifico['via_exp1'], (488, 306),pg=1) #via_exposicao_1
document.write_mini(especifico['via_exp2'], (488, 320),pg=1) #via_exposicao_2
document.write_mini(especifico['via_exp3'], (488, 336),pg=1) #via_exposicao_3
document.write_code(especifico['circ_exp'], (233, 360),pg=1,space=1) #circunstancia_cont
document.write_mini(especifico['circ_exp_outro'], (295, 390),pg=1) #circunstancia_outros
document.write_mini(especifico['exp_decor_trab'], (285, 420),pg=1) #decorrente_trab
document.write_mini(especifico['tipo_exposicao'], (538, 422),pg=1) #tipo_exposicao
##############################################
#####        DADOS  ATENDIMENTO           ####
##############################################

document.write_code(especifico['tempo_exp_atend'], (170, 465),pg=1,space=1) #tempo_expo_atend
document.write_mini(especifico['tipo_tempo_exp_atend'], (228, 462),pg=1) #tempo_expo_atend_un
document.write_mini(especifico['tipo_atendimento'], (247, 487),pg=1) #tipo_atendimento
document.write_mini(especifico['hospitalizacao2'], (390, 488),pg=1) #hospitalizacao
document.write_date(especifico['dt_internacao'], (418, 511),pg=1, spacing=2) #dt_internacao
document.write_uf(especifico['uf_hospital2'], (537, 510),pg=1) #uf_internacao
document.write_text(especifico['municipio_hospital2'], (65, 542),pg=1) #municipio_internacao
document.write_code(especifico['cod_ibge_hospital2'], (225, 542),pg=1,space=2) #ibge_internacao
document.write_text(especifico['nome_hospital2'], (330, 542),pg=1) #instituicao_internacao
document.write_code(especifico['cod_hospital2'], (465, 542),pg=1,space=2) #cod_instituicao_internacao
##############################################
#####        CONCLUSAO                    ####
##############################################
document.write_mini(especifico['classif_final'], (545, 568),pg=1) #class_final
document.write_text(especifico['diag_intox_conf'], (70, 600),pg=1) #diagnostico
document.write_code(especifico['cid_intox_conf'], (490, 602),pg=1,space=2) #cid_10
document.write_mini(especifico['criterio_confirm'], (205, 617),pg=1) #crit_confirmacao
document.write_mini(especifico['evolucao_caso'], (544, 617),pg=1) #evolucao
document.write_date(especifico['dt_obito'], (63, 665),pg=1, spacing=2) #dt_obito
document.write_mini(especifico['comun_acid_trab'], (428, 653),pg=1) #cat
document.write_date(especifico['dt_encerramento'], (458, 665),pg=1, spacing=2) #dt_encerramento
document.write_box(especifico['obs_adicionais'], 1, (35,705, 565, 750)) #obs
document.write_text(especifico['municipio_us_investigador'], (65, 778),pg=1) #municipio_unid_saude
document.write_code(especifico['cod_us_investigador'], (468, 780),pg=1, space=2) #cod_unidade_saude
document.write_text(especifico['nome_investigador'], (70, 810),pg=1) #nome_investigador
document.write_text(especifico['funcao_investigador'], (280, 810),pg=1) #func_investigador
document.write_text(especifico['assinatura_investigador'], (470, 810),pg=1) #assign_investigador



document.save('intox.geracao_pdf', notificatoria)