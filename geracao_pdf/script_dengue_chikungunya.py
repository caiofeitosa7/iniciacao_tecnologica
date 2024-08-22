from pdfWritter import PDFWriter
pdf = 'fichas/completas/Dengue-Chikungunya1.geracao_pdf'
doc = PDFWriter(pdf)

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
    "agravoDoenca_num": "99cdefg",
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
    "telefone_residencia2": "86789999999",
    "zona_residencia2": "9",
    "pais_residencia2": "9",
    "dt_investigacao": "15/02/2022",
    "ocupacao": "99cdefg",
    "sinal_febre": "9",
    "sinal_mialgia": "9",
    "sinal_cefaleia": "9",
    "sinal_exantema": "9",
    "sinal_vomito": "9",
    "sinal_nausea": "9",
    "sinal_dor_costas": "9",
    "sinal_conjuntivite": "9",
    "sinal_artrite": "9",
    "sinal_artralgia": "9",
    "sinal_petequias": "9",
    "sinal_leucopenia": "9",
    "sinal_prova_laco": "9",
    "sinal_dor_retroorbital": "9",
    "doenca_diabete": "9",
    "doenca_hemato": "9",
    "doenca_hepato": "9",
    "doenca_renal": "9",
    "doenca_hipertensao": "9",
    "doenca_peptica": "9",
    "doenca_auto_imune": "9",
    "dt_coleta_s1_ck": "15/02/2022",
    "dt_coleta_s2_ck": "15/02/2022",
    "dt_coleta_prnt": "15/02/2022",
    "resultado_s1_ck": "9",
    "resultado_s2_ck": "9",
    "resultado_prnt": "9",
    "dt_coleta_dengue": "15/02/2022",
    "resultado_dengue": "9",
    "dt_coleta_ns1": "15/02/2022",
    "resultado_ns1": "9",
    "dt_isol_dengue": "15/02/2022",
    "resultado_isol_dengue": "9",
    "dt_coleta_pcr": "15/02/2022",
    "resultado_pcr": "9",
    "sorotipo": "9",
    "histopatologia": "9",
    "imunohistoq": "9",
    "hospitalizacao2": "9",
    "dt_internacao": "15/02/2022",
    "uf_hospital2": "PI",
    "municipio_hospital2": "99cdefg",
    "cod_ibge_hospital2": "123456",
    "nome_hospital2": "99cdefg",
    "cod_hospital2": "123456",
    "telefone_hospital2": "86999999999",
    "caso_autoctone": "9",
    "uf_infeccao2": "PI",
    "pais_infeccao2": "99cdefg",
    "municipio_infeccao2": "99cdefg",
    "cod_ibge_infeccao2": "123456",
    "distrito_infeccao2": "99cdefg",
    "bairro_infeccao2": "99cdefg",
    "classif_caso": "9",
    "criterio_confirm": "9",
    "apresentacao_clinica": "9",
    "evolucao_caso": "9",
    "dt_obito": "15/02/2022",
    "dt_encerramento": "15/02/2022",
    "alarme_hipotensao": "9",
    "alarme_plaqueta": "9",
    "alarme_vomito": "9",
    "alarme_abdomem": "9",
    "alarme_letargia": "9",
    "alarme_sangramento": "9",
    "alarme_hematocito": "9",
    "alarme_hepatomeglagia": "9",
    "alarme_liquido": "9",
    "dt_sinal_alarme": "15/02/2022",
    "deng_grav_pulso": "9",
    "deng_grav_pa_conv": "9",
    "deng_grav_capilar": "9",
    "deng_grav_liquido": "9",
    "deng_grav_taqui": "9",
    "deng_grav_extrem": "9",
    "deng_grav_hipo": "9",
    "deng_grav_hemat": "9",
    "deng_grav_melena": "9",
    "deng_grav_metror": "9",
    "deng_grav_snc": "9",
    "deng_grav_ast": "9",
    "deng_grave_miocardite": "9",
    "deng_grav_consc": "9",
    "deng_grav_outro": "9",
    "deng_grav_outro_descricao": "9",
    "dt_sinal_gravidade": "15/02/2022",
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
doc.write_text(especifico['numero_ficha2'],(470, 48))
doc.write_date(especifico['dt_notificacao2'], (449, 191), spacing=2) #data_notificacao
doc.write_uf(especifico['uf_notificacao2'], (59, 220)) #uf_notificacao
doc.write_text(especifico['municipio_notificacao2'], (90, 220)) #municipio_notificacao __unid_saude 55,space=220
doc.write_code(especifico['cod_ibge_notificacao2'], (480, 220),space=2) #cod_ibge
doc.write_text(especifico['unidade_saude2'], (65, 248)) #cod_unid_saude
doc.write_code(especifico['cod_unidade_saude2'], (340, 248),space=2) #cod_unid_saude
doc.write_date(especifico['dt_sintomas2'], (447, 248), spacing=2) #data_diagnostico
##############################################
#####          NOTIFICACAO INDIVIDUAL     ####
##############################################
doc.write_text(especifico['nome_paciente2'], (60, 279)) #nome
doc.write_date(especifico['dt_nascimento2'], (446, 279), spacing=2) #data_nascimento
doc.write_code(especifico['idade2'], (63, 308),space=2) #idade
doc.write_mini(especifico['tipo_idade2'], (109, 301)) #tipo_idade
doc.write_mini(especifico['sexo2'], (230, 294)) #sexo
doc.write_mini(especifico['gestante2'], (426, 294)) #gestante
doc.write_mini(especifico['raca2'], (551, 294)) #raça/cor
doc.write_mini(especifico['escolaridade2'], (552, 324)) #escolaridade
doc.write_code(especifico['numero_sus2'], (57, 369),space=2, font_size=10) #cartao_sus
doc.write_text(especifico['nome_mae2'], (240, 368)) #nome_mae
##############################################
#####          DADOS DE RESIDENCIA        ####
##############################################

doc.write_uf(especifico['uf_residencia2'], (56, 398)) #uf_residencia
doc.write_text(especifico['municipio_residencia2'], (95, 398)) #municipio_residencia
doc.write_code(especifico['cod_ibge_residencia2'], (325, 398),space=2) #cod_ibge_residencia
doc.write_text(especifico['distrito_residencia2'], (422, 398)) #endereco
doc.write_text(especifico['bairro_residencia2'], (64, 423)) #bairro
doc.write_text(especifico['logradouro_residencia2'], (207, 424)) #logradouro
doc.write_code(especifico['codigo_residencia2'], (478, 424),space=2) #cod_logradouro
doc.write_text(especifico['numero_residencia2'], (65, 447)) #numero
doc.write_text(especifico['complemento_residencia2'], (120, 447)) #complemento
doc.write_text(especifico['geo_campo1_2'], (415, 450)) #geo_campo_1
doc.write_text(especifico['geo_campo2_2'], (55, 473)) #geo_campo_2
doc.write_text(especifico['ponto_ref_residencia2'], (230, 474)) #ponto_ref
doc.write_code(especifico['cep_residencia2'], (454, 477),space=2) #cep
doc.write_telefone(especifico['telefone_residencia2'], (57, 500), space=2) #telefone
doc.write_mini(especifico['zona_residencia2'], (335, 488)) #zona
doc.write_text(especifico['pais_residencia2'], (380, 499)) #pais
####################################################
# Dados Complementares
####################################################
doc.write_date(especifico['dt_investigacao'], (63, 548), spacing=2) #data_investigacao
doc.write_text(especifico['ocupacao'], (195, 548)) #ocupacao
doc.write_mini(especifico['sinal_febre'], (58, 580)) #sinal_febre
doc.write_mini(especifico['sinal_mialgia'], (58, 595)) #sinal_mialgia
doc.write_mini(especifico['sinal_cefaleia'], (105, 580)) #sinal_cefaleia
doc.write_mini(especifico['sinal_exantema'], (105, 595)) #sinal_exantema
doc.write_mini(especifico['sinal_vomito'], (162, 580)) #sinal_vomito
doc.write_mini(especifico['sinal_nausea'], (162, 595)) #sinal_nausea
doc.write_mini(especifico['sinal_dor_costas'], (219, 581)) #sinal_dor_costas
doc.write_mini(especifico['sinal_conjuntivite'], (219, 596)) #sinal_conjuntivite
doc.write_mini(especifico['sinal_artrite'], (302, 579)) #sinal_artrite
doc.write_mini(especifico['sinal_artralgia'], (302, 594)) #sinal_artralgia
doc.write_mini(especifico['sinal_petequias'], (390, 577)) #sinal_petequias
doc.write_mini(especifico['sinal_leucopenia'], (390, 592)) #sinal_leucopenia
doc.write_mini(especifico['sinal_prova_laco'], (474, 577)) #sinal_prova_laco
doc.write_mini(especifico['sinal_dor_retroorbital'], (474, 595)) #sinal_dor_retroorbital
doc.write_mini(especifico['doenca_diabete'], (58, 632)) #doenca_diabete
doc.write_mini(especifico['doenca_hemato'], (58, 648)) #doenca_hemato
doc.write_mini(especifico['doenca_hepato'], (193, 630)) #doenca_hepato
doc.write_mini(especifico['doenca_renal'], (193, 645)) #doenca_renal
doc.write_mini(especifico['doenca_hipertensao'], (314, 630)) #doenca_hipertensao
doc.write_mini(especifico['doenca_peptica'], (314, 645)) #doenca_peptica
doc.write_mini(especifico['doenca_auto_imune'], (428, 629)) #doenca_auto_imune
doc.write_date(especifico['dt_coleta_s1_ck'], (58, 697), spacing=2) #data_coleta_ck
doc.write_date(especifico['dt_coleta_s2_ck'], (184, 697), spacing=2) #data_coleta_ck
doc.write_date(especifico['dt_coleta_prnt'], (310, 697), spacing=2) #data_coleta_prnt
doc.write_mini(especifico['resultado_s1_ck'], (464, 676)) #resultado_ck
doc.write_mini(especifico['resultado_s2_ck'], (498, 676)) #resultado_ck
doc.write_mini(especifico['resultado_prnt'], (538, 677)) #resultado_prnt
doc.write_date(especifico['dt_coleta_dengue'], (65, 742), spacing=2) #data_coleta_dengue
doc.write_mini(especifico['resultado_dengue'], (296, 722)) #resultado_dengue
doc.write_date(especifico['dt_coleta_ns1'], (326, 742), spacing=2) #data_coleta_ns1
doc.write_mini(especifico['resultado_ns1'], (550, 720)) #resultado_ns1
doc.write_date(especifico['dt_isol_dengue'], (57, 776), spacing=2) #data_isolamento
doc.write_mini(especifico['resultado_isol_dengue'], (285, 758)) #resultado_isolamento
doc.write_date(especifico['dt_coleta_pcr'], (328, 777), spacing=2) #data_coleta_pcr
doc.write_mini(especifico['resultado_pcr'], (551, 755)) #resultado_pcr
doc.write_mini(especifico['sorotipo'], (150, 790)) #sorotipo
doc.write_mini(especifico['histopatologia'], (285, 792)) #histopatologia
doc.write_mini(especifico['imunohistoq'], (431, 791)) #imunohistoq

#################################################### fim page

doc.write_mini(especifico['hospitalizacao2'], (167, 57), pg=1) #hospitalizacao
doc.write_date(especifico['dt_internacao'], (193, 59), pg=1, spacing=2) #data_internacao
doc.write_uf(especifico['uf_hospital2'], (315, 59), pg=1) #uf_hospital
doc.write_text(especifico['municipio_hospital2'], (354, 59), pg=1) #municipio_hospital
doc.write_code(especifico['cod_ibge_hospital2'], (483, 59), pg=1,space=2) #cod_ibge_hospital
doc.write_text(especifico['nome_hospital2'], (66, 93), pg=1) #nome_hospital
doc.write_code(especifico['cod_hospital2'], (332, 93), pg=1,space=2) #cod_hospital
doc.write_telefone(especifico['telefone_hospital2'], (436, 93), pg=1, space=2, font_size=12) #telefone_hospital
doc.write_mini(especifico['caso_autoctone'], (301, 130), pg=1) #caso_autoctone
doc.write_uf(especifico['uf_infeccao2'], (343, 135), pg=1) #uf_infeccao
doc.write_text(especifico['pais_infeccao2'], (385, 135), pg=1) #pais_infeccao
doc.write_text(especifico['municipio_infeccao2'], (66, 162), pg=1) #municipio_infeccao
doc.write_code(especifico['cod_ibge_infeccao2'], (204, 162), pg=1,space=2) #cod_ibge_infeccao
doc.write_text(especifico['distrito_infeccao2'], (303, 162), pg=1) #distrito_infeccao
doc.write_text(especifico['bairro_infeccao2'], (440, 162), pg=1) #bairro_infeccao
doc.write_mini(especifico['classif_caso'], (278, 182), pg=1) #classif_caso
doc.write_mini(especifico['criterio_confirm'], (428, 184), pg=1) #criterio_confirm
doc.write_mini(especifico['apresentacao_clinica'], (472, 194), pg=1) #apresentacao_clinica
doc.write_mini(especifico['evolucao_caso'], (166, 221), pg=1) #evolucao_caso
doc.write_date(especifico['dt_obito'], (313, 243), pg=1, spacing=2) #data_obito
doc.write_date(especifico['dt_encerramento'], (448, 244), pg=1, spacing=2) #data_encerramento
doc.write_mini(especifico['alarme_hipotensao'], (58, 304), pg=1) #alarme_hipotensao
doc.write_mini(especifico['alarme_plaqueta'], (58, 319), pg=1) #alarme_plaqueta
doc.write_mini(especifico['alarme_vomito'], (215, 275), pg=1) #alarme_vomito
doc.write_mini(especifico['alarme_abdomem'], (214, 290), pg=1) #alarme_abdomem
doc.write_mini(especifico['alarme_letargia'], (213, 307), pg=1) #alarme_letargia
doc.write_mini(especifico['alarme_sangramento'], (213, 322), pg=1) #alarme_sangramento
doc.write_mini(especifico['alarme_hematocito'], (346, 276), pg=1) #alarme_hematocito
doc.write_mini(especifico['alarme_hepatomeglagia'], (346, 294), pg=1) #alarme_hepatomeglagia
doc.write_mini(especifico['alarme_liquido'], (346, 310), pg=1) #alarme_liquido
doc.write_date(especifico['dt_sinal_alarme'], (458, 323), pg=1, spacing=2) #data_sinal_alarme
doc.write_mini(especifico['deng_grav_pulso'], (60, 372), pg=1) #deng_grav_pulso
doc.write_mini(especifico['deng_grav_pa_conv'], (60, 389), pg=1) #deng_grav_pa_conv
doc.write_mini(especifico['deng_grav_capilar'], (60, 405), pg=1) #deng_grav_capilar
doc.write_mini(especifico['deng_grav_liquido'], (60, 420), pg=1) #deng_grav_liquido
doc.write_mini(especifico['deng_grav_taqui'], (204, 374), pg=1) #deng_grav_taqui
doc.write_mini(especifico['deng_grav_extrem'], (204, 389), pg=1) #deng_grav_extrem
doc.write_mini(especifico['deng_grav_hipo'], (204, 405), pg=1) #deng_grav_hipo
doc.write_mini(especifico['deng_grav_hemat'], (335, 358), pg=1) #deng_grav_hemat
doc.write_mini(especifico['deng_grav_melena'], (335, 374), pg=1) #deng_grav_melena
doc.write_mini(especifico['deng_grav_metror'], (429, 356), pg=1) #deng_grav_metror
doc.write_mini(especifico['deng_grav_snc'], (429, 374), pg=1) #deng_grav_snc
doc.write_mini(especifico['deng_grav_ast'], (333, 408), pg=1) #deng_grav_ast
doc.write_mini(especifico['deng_grave_miocardite'], (428, 406), pg=1) #deng_grave_miocardite
doc.write_mini(especifico['deng_grav_consc'], (488, 406), pg=1) #deng_grav_consc
doc.write_mini(especifico['deng_grav_outro'], (334, 426), pg=1) #deng_grav_outro
doc.write_mini(especifico['deng_grav_outro_descricao'], (458, 426), pg=1) #deng_grav_outro_descricao
doc.write_date(especifico['dt_sinal_gravidade'], (58, 469), pg=1, spacing=2) #data_sinal_gravidade
doc.write_box(especifico['obs_adicionais'],pg=1, rect=(30,520,566,750)) #obs_adicionais
doc.write_text(especifico['municipio_us_investigador'], (60, 759), pg=1) #municipio_us_investigador
doc.write_code(especifico['cod_us_investigador'], (463, 758), pg=1,space=2) #cod_us_investigador
doc.write_text(especifico['nome_investigador'], (60, 789), pg=1) #nome_investigador
doc.write_text(especifico['funcao_investigador'], (257, 789), pg=1) #funcao_investigador
doc.write_text(especifico['assinatura_investigador'], (468, 789), pg=1) #assinatura_investigador

doc.save('dengue_chikungunya.geracao_pdf', notificatoria)