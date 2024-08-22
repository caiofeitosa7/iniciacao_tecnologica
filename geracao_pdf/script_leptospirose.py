from pdfWritter import PDFWriter
pdf = 'fichas/completas/LEPTOSPIROSE1.geracao_pdf'
document = PDFWriter(pdf)

notificatoria ={
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
especifico ={
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
    "risco_lama": "99cdefg",
    "risco_fossa": "99cdefg",
    "risco_rio": "99cdefg",
    "risco_terreno": "99cdefg",
    "risco_animais": "99cdefg",
    "risco_sinal_roed": "99cdefg",
    "risco_roed_dir": "99cdefg",
    "risco_lixo": "99cdefg",
    "risco_cx_dagua": "99cdefg",
    "risco_plantio": "99cdefg",
    "risco_graos": "99cdefg",
    "risco_outras": "99cdefg",
    "risco_outras_descricao": "99cdefg",
    "caso_lept_ant_humano": "99cdefg",
    "caso_lept_ant_animal": "99cdefg",
    "dt_atendimento": "15/02/2022",
    "sint_febre": "99cdefg",
    "sint_cong_conju": "99cdefg",
    "sint_ictericia": "99cdefg",
    "sint_hemo_pulmonar": "99cdefg",
    "sint_mialgia": "99cdefg",
    "sint_panturrilha": "99cdefg",
    "sint_renal": "99cdefg",
    "sint_outra_hemo": "99cdefg",
    "sint_cefaleia": "99cdefg",
    "sint_vomito": "99cdefg",
    "sint_alter_resp": "9",
    "sint_mening": "99cdefg",
    "sint_prostracao": "99cdefg",
    "sint_diarreia": "99cdefg",
    "sint_alter_cardi": "99cdefg",
    "sint_outro": "99cdefg",
    "sint_outro_descricao": "99cdefg",
    "hospitalizacao2": "99cdefg",
    "dt_internacao": "15/02/2022",
    "dt_alta": "15/02/2022",
    "uf_hospital2": "PI",
    "municipio_hospital2": "99cdefg",
    "cod_ibge_hospital2": "123456",
    "nome_hospital2": "99cdefg",
    "cod_hospital2": "123456",
    "dt_igm_elisa1": "15/02/2022",
    "res_amostra_elisa1": "9",
    "dt_igm_elisa2": "15/02/2022",
    "res_amostra_elisa2": "9",
    "dt_micro1": "15/02/2022",
    "sorovar1_micro1": "99cdefg",
    "titulo1_micro1": "99cdefg",
    "sorovar2_micro1": "99cdefg",
    "titulo2_micro1": "99cdefg",
    "res_aglu_micro1": "9",
    "dt_micro2": "15/02/2022",
    "sorovar1_micro2": "99cdefg",
    "titulo1_micro2": "99cdefg",
    "sorovar2_micro2": "99cdefg",
    "titulo2_micro2": "99cdefg",
    "res_aglu_micro2": "9",
    "dt_col_isola": "15/02/2022",
    "res_col_isola": "9",
    "dt_col_imunohist": "15/02/2022",
    "res_col_imunohist": "9",
    "dt_coleta_pcr": "15/02/2022",
    "resultado_pcr": "9",
    "classif_final": "99cdefg",
    "criterio_confirm": "99cdefg",
    "caso_autoctone": "99cdefg",
    "uf_infeccao2": "PI",
    "pais_infeccao2": "99cdefg",
    "municipio_infeccao2": "99cdefg",
    "cod_ibge_infeccao2": "123456",
    "distrito_infeccao2": "99cdefg",
    "bairro_infeccao2": "99cdefg",
    "area_infeccao": "99cdefg",
    "ambiente_infecao": "99cdefg",
    "doenca_rel_trab": "99cdefg",
    "evolucao_caso": "99cdefg",
    "dt_obito": "15/02/2022",
    "dt_encerramento": "15/02/2022",
    "dt_risco1": "15/02/2022",
    "uf_risco1": "PI",
    "municipio_risco1": "99cdefg",
    "ender_risco1": "99cdefg",
    "localid_risco1": "99cdefg",
    "dt_risco2": "15/02/2022",
    "uf_risco2": "PI",
    "municipio_risco2": "99cdefg",
    "ender_risco2": "99cdefg",
    "localid_risco2": "99cdefg",
    "dt_risco3": "15/02/2022",
    "uf_risco3": "PI",
    "municipio_risco3": "99cdefg",
    "ender_risco3": "99cdefg",
    "localid_risco3": "99cdefg",
    "dt_risco4": "15/02/2022",
    "uf_risco4": "PI",
    "municipio_risco4": "99cdefg",
    "ender_risco4": "99cdefg",
    "localid_risco4": "99cdefg",
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
document.write_text(especifico['numero_ficha2'],(470, 46))
document.write_date(especifico['dt_notificacao2'], (450, 172), spacing=2) #data_notificacao
document.write_uf(especifico['uf_notificacao2'], (60, 202)) #uf_notificacao
document.write_text(especifico['municipio_notificacao2'], (100, 204)) #municipio_notificacao __unid_saude 55,space=220
document.write_code(especifico['cod_ibge_notificacao2'], (485, 205),space=2) #cod_ibge
document.write_text(especifico['unidade_saude2'], (70, 232)) #cod_unid_saude
document.write_code(especifico['cod_unidade_saude2'], (342, 232),space=2) #cod_unid_saude
document.write_date(especifico['dt_sintomas2'], (451, 231), spacing=2) #data_diagnostico
##############################################
#####          NOTIFICACAO INDIVIDUAL     ####
##############################################
document.write_text(especifico['nome_paciente2'], (65, 262)) #nome
document.write_date(especifico['dt_nascimento2'], (455, 261), spacing=2) #data_nascimento
document.write_code(especifico['idade2'], (70, 291),space=2) #idade
document.write_mini(especifico['tipo_idade2'], (117, 284)) #tipo_idade
document.write_mini(especifico['sexo2'], (237, 277)) #sexo
document.write_mini(especifico['gestante2'], (433, 277)) #gestante
document.write_mini(especifico['raca2'], (558, 277)) #raça/cor
document.write_mini(especifico['escolaridade2'], (558, 307)) #escolaridade
document.write_code(especifico['numero_sus2'], (61, 352),space=2, font_size=10) #cartao_sus
document.write_text(especifico['nome_mae2'], (250, 352)) #nome_mae
##############################################
#####          DADOS DE RESIDENCIA        ####
##############################################

document.write_uf(especifico['uf_residencia2'], (62, 380)) #uf_residencia
document.write_text(especifico['municipio_residencia2'], (100, 380)) #municipio_residencia
document.write_code(especifico['cod_ibge_residencia2'], (328, 380),space=2) #cod_ibge_residencia
document.write_text(especifico['distrito_residencia2'], (430, 380)) #endereco
document.write_text(especifico['bairro_residencia2'], (70, 405)) #bairro
document.write_text(especifico['logradouro_residencia2'], (210, 405)) #logradouro
document.write_code(especifico['codigo_residencia2'], (481, 406),space=2) #cod_logradouro
document.write_text(especifico['numero_residencia2'], (68, 429)) #numero
document.write_text(especifico['complemento_residencia2'], (120, 429)) #complemento
document.write_text(especifico['geo_campo1_2'], (420, 432)) #geo_campo_1
document.write_text(especifico['geo_campo2_2'], (63, 456)) #geo_campo_2
document.write_text(especifico['ponto_ref_residencia2'], (235, 456)) #ponto_ref
document.write_code(especifico['cep_residencia2'], (458, 458),space=2) #cep
document.write_telefone(especifico['telefone_residencia2'], (60, 482), space=2) #telefone
document.write_mini(especifico['zona_residencia2'], (338, 470)) #zona
document.write_text(especifico['pais_residencia2'], (380, 482)) #pais

###################################################
#              Dados complementares               #
###################################################
document.write_date(especifico['dt_investigacao'], (60, 532), spacing=2) #data_investigacao
document.write_text(especifico['ocupacao'], (200, 532)) #ocupacao
document.write_mini(especifico['risco_lama'], (65, 565)) #sit_risc_agua
document.write_mini(especifico['risco_fossa'], (65, 582)) #sit_risc_esgoto
document.write_mini(especifico['risco_rio'], (65, 598)) #sit_risc_rio
document.write_mini(especifico['risco_terreno'], (65, 613)) #sit_risc_terr_baldio
document.write_mini(especifico['risco_animais'], (250, 566)) #sit_risc_animais
document.write_mini(especifico['risco_sinal_roed'], (250, 582)) #sit_risc_sinais_roedor
document.write_mini(especifico['risco_roed_dir'], (250, 599)) #sit_risc_roedor
document.write_mini(especifico['risco_lixo'], (251, 615)) #sit_risc_lixo
document.write_mini(especifico['risco_cx_dagua'], (410, 566)) #sit_risc_cx_dagua
document.write_mini(especifico['risco_plantio'], (410, 580)) #sit_risc_plantas
document.write_mini(especifico['risco_graos'], (410, 595)) #sit_risc_armaz_graos
document.write_mini(especifico['risco_outras'], (410, 611)) #sit_risc_outras
document.write_text(especifico['risco_outras_descricao'], (447, 610)) #sit_risc_outras
document.write_mini(especifico['caso_lept_ant_humano'], (128, 643)) #case_lepto_anterior_human
document.write_mini(especifico['caso_lept_ant_animal'], (304, 643)) #case_lepto_anterior_animal
document.write_date(especifico['dt_atendimento'], (64, 678), spacing=2) #data_atendimento
document.write_mini(especifico['sint_febre'], (188, 678)) #sins_sintomas_febre
document.write_mini(especifico['sint_cong_conju'], (188, 693)) #sins_sintomas_conjuntival
document.write_mini(especifico['sint_ictericia'], (188, 708)) #sins_sintomas_ictericia
document.write_mini(especifico['sint_hemo_pulmonar'], (188, 722)) #sins_sintomas_hemorr_pulmonar
document.write_mini(especifico['sint_mialgia'], (283, 679)) #sins_sintomas_mialgia
document.write_mini(especifico['sint_panturrilha'], (283, 693)) #sins_sintomas_panturrilha
document.write_mini(especifico['sint_renal'], (283, 708)) #sins_sintomas_insuf_renal
document.write_mini(especifico['sint_outra_hemo'], (283, 723)) #sins_sintomas_outras_hemorr
document.write_mini(especifico['sint_cefaleia'], (372, 677)) #sins_sintomas_cefaleia
document.write_mini(especifico['sint_vomito'], (372, 691)) #sins_sintomas_vomito
document.write_mini(especifico['sint_alter_resp'], (372, 707)) #sins_sintomas_alt_respiracao
document.write_mini(especifico['sint_mening'], (372, 723)) #sins_sintomas_meningismo
document.write_mini(especifico['sint_prostracao'], (443, 677)) #sins_sintomas_prostacao
document.write_mini(especifico['sint_diarreia'], (443, 692)) #sins_sintomas_diarreia
document.write_mini(especifico['sint_alter_cardi'], (443, 707)) #sins_sintomas_cardiaca
document.write_mini(especifico['sint_outro'], (443, 723)) #sins_sintomas_outras
document.write_text(especifico['sint_outro_descricao'], (509, 721)) #text_sintomas_outras
document.write_mini(especifico['hospitalizacao2'], (283, 750)) #ocorreu_hospital
document.write_date(especifico['dt_internacao'], (322, 760), spacing=2) #data_internacao
document.write_date(especifico['dt_alta'], (452, 760), spacing=2) #data_alta
document.write_uf(especifico['uf_hospital2'], (63, 785)) #uf_internacao
document.write_text(especifico['municipio_hospital2'], (100, 785)) #municipio_internacao
document.write_code(especifico['cod_ibge_hospital2'], (484, 785),space=2) #cod_ibge_internacao
document.write_text(especifico['nome_hospital2'], (60, 810)) #instituicao_internacao
document.write_code(especifico['cod_hospital2'], (466, 810),space=2) #cod_instituicao_internacao
###################### fim pag 0 ####################
document.write_date(especifico['dt_igm_elisa1'], (68, 71),pg=1, spacing=2) #data_coleta_sorologia_1
document.write_mini(especifico['res_amostra_elisa1'], (300, 52),pg=1) #res_sorologia_1
document.write_date(especifico['dt_igm_elisa2'], (320, 71),pg=1, spacing=2) #data_coleta_sorologia_2
document.write_mini(especifico['res_amostra_elisa2'], (552, 51),pg=1) #res_sorologia_2
document.write_date(especifico['dt_micro1'], (72, 124),pg=1, spacing=2) #data_coleta_micro_aglut_1
document.write_text(especifico['sorovar1_micro1'], (219, 122),pg=1) #micro_1_sorovar
document.write_code(especifico['titulo1_micro1'], (303, 124),pg=1,space=2) #micro_1_titulo
document.write_text(especifico['sorovar2_micro1'], (413, 123),pg=1) #micro_1_sorovar2
document.write_code(especifico['titulo2_micro1'], (496, 124),pg=1,space=2) #micro_1_titulo2
document.write_mini(especifico['res_aglu_micro1'], (542, 149),pg=1) #res_micro_1
document.write_date(especifico['dt_micro2'], (70, 200),pg=1, spacing=2) #data_coleta_micro_aglut_2
document.write_text(especifico['sorovar1_micro2'], (218, 197),pg=1) #micro_2_sorovar
document.write_code(especifico['titulo1_micro2'], (302, 200),pg=1,space=2) #micro_2_titulo
document.write_text(especifico['sorovar2_micro2'], (412, 199),pg=1) #micro_2_sorovar2
document.write_code(especifico['titulo2_micro2'], (495, 200),pg=1,space=2) #micro_2_titulo2
document.write_mini(especifico['res_aglu_micro2'], (541, 225),pg=1) #res_micro_2
document.write_date(especifico['dt_col_isola'], (68, 285),pg=1, spacing=2) #data_iso_coleta
document.write_mini(especifico['res_col_isola'], (552, 270),pg=1) #iso_res
document.write_date(especifico['dt_col_imunohist'], (68, 327),pg=1, spacing=2) #data_coleta_imuno
document.write_mini(especifico['res_col_imunohist'], (551, 314),pg=1) #res_imuno
document.write_date(especifico['dt_coleta_pcr'], (68, 368),pg=1, spacing=2) #data_coleta_pcr
document.write_mini(especifico['resultado_pcr'], (551, 351),pg=1) #res_pcr
document.write_mini(especifico['classif_final'], (330, 394),pg=1) #class_final
document.write_mini(especifico['criterio_confirm'], (553, 392),pg=1) #criterio
document.write_mini(especifico['caso_autoctone'], (310, 435),pg=1) #case_autoctone
document.write_uf(especifico['uf_infeccao2'], (350, 445),pg=1) #uf_conclusao
document.write_text(especifico['pais_infeccao2'], (400, 445),pg=1) #pais
document.write_text(especifico['municipio_infeccao2'], (70, 475),pg=1) #municipio_conclusao
document.write_code(especifico['cod_ibge_infeccao2'], (212, 476),pg=1,space=2) #cod_ibge_conclusao
document.write_text(especifico['distrito_infeccao2'], (305, 475),pg=1) #distrito_conclusao
document.write_text(especifico['bairro_infeccao2'], (450, 475),pg=1) #bairro_conclusao
document.write_mini(especifico['area_infeccao'], (293, 503),pg=1) #area_infec
document.write_mini(especifico['ambiente_infecao'], (553, 494),pg=1) #ambient_infec
document.write_mini(especifico['doenca_rel_trab'], (230, 527),pg=1) #doenca_trabalho
document.write_mini(especifico['evolucao_caso'], (548, 528),pg=1) #evolucao_case
document.write_date(especifico['dt_obito'], (76, 567),pg=1, spacing=2) #data_obito
document.write_date(especifico['dt_encerramento'], (209, 567),pg=1, spacing=2) #data_encerramento
document.write_mini(especifico['dt_risco1'], (40, 623),pg=1) #tab_data_1
document.write_uf(especifico['uf_risco1'], (120, 624),pg=1) #tab_uf_1
document.write_text(especifico['municipio_risco1'], (160, 623),pg=1, font_size=11) #tab_municipio_1
document.write_text(especifico['ender_risco1'], (299, 623),pg=1, font_size=12) #tab_adress_1
document.write_text(especifico['localid_risco1'], (458, 623),pg=1, font_size=11) #tab_local_1
document.write_mini(especifico['dt_risco2'], (40, 634),pg=1) #tab_data_2
document.write_uf(especifico['uf_risco2'], (120, 635),pg=1) #tab_uf_2
document.write_text(especifico['municipio_risco2'], (160, 634),pg=1, font_size=11) #tab_municipio_2
document.write_text(especifico['ender_risco2'], (299, 634),pg=1, font_size=12) #tab_adress_2
document.write_text(especifico['localid_risco2'], (458, 634),pg=1, font_size=11) #tab_local_2
document.write_mini(especifico['dt_risco3'], (40, 644),pg=1) #tab_data_3
document.write_uf(especifico['uf_risco3'], (120, 645),pg=1) #tab_uf_3
document.write_text(especifico['municipio_risco3'], (160, 644),pg=1, font_size=11) #tab_municipio_3
document.write_text(especifico['ender_risco3'], (299, 644),pg=1, font_size=12) #tab_adress_3
document.write_text(especifico['localid_risco3'], (458, 644),pg=1, font_size=11) #tab_local_3
document.write_mini(especifico['dt_risco4'], (40, 654),pg=1) #tab_data_4
document.write_uf(especifico['uf_risco4'], (120, 655),pg=1) #tab_uf_4
document.write_text(especifico['municipio_risco4'], (160, 654),pg=1, font_size=11) #tab_municipio_4
document.write_text(especifico['ender_risco4'], (299, 654),pg=1, font_size=12) #tab_adress_4
document.write_text(especifico['localid_risco4'], (458, 654),pg=1, font_size=11) #tab_local_4
document.write_box(especifico['obs_adicionais'], 1,(35, 670, 569, 730)) #obs
document.write_text(especifico['municipio_us_investigador'], (62, 747),pg=1) #municipio_investigador
document.write_code(especifico['cod_us_investigador'], (467, 747),pg=1,space=2) #cod_unid_investigador
document.write_text(especifico['nome_investigador'], (64, 778),pg=1) #nome_investigador
document.write_text(especifico['funcao_investigador'], (265, 778),pg=1) #func_investigador
document.write_text(especifico['assinatura_investigador'], (475, 778),pg=1) #assign_investigador




document.save('LEPTOS.geracao_pdf', notificatoria)