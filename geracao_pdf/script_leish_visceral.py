from pdfWritter import PDFWriter
pdf = 'fichas/completas/LEISH_VISCERAL1.geracao_pdf'
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
    "sintoma_febre": "99cdefg",
    "sintoma_fraqueza": "99cdefg",
    "sintoma_edema": "99cdefg",
    "sintoma_emagrecimento": "99cdefg",
    "sintoma_tosse": "99cdefg",
    "sintoma_palidez": "99cdefg",
    "sintoma_baco": "99cdefg",
    "sintoma_quadro_infec": "99cdefg",
    "sintoma_hemorragia": "99cdefg",
    "sintoma_figado": "99cdefg",
    "sintoma_icteria": "99cdefg",
    "sintoma_outro": "99cdefg",
    "sintoma_outro_descricao": "99cdefg",
    "co_infec_hiv": "99cdefg",
    "diag_parasitologica": "9",
    "diag_imuno_ifi": "99cdefg",
    "diag_imuno_outro": "99cdefg",
    "tipo_entrada": "9",
    "dt_inicio_trat": "15/02/2022",
    "droga_inicial_adm": "99cdefg",
    "peso": "99cdefg",
    "dose_prescrita": "9",
    "quant_ampolas": "99cdefg",
    "droga_falencia_trat": "99cdefg",
    "classif_final": "99cdefg",
    "criterio_confirm": "99cdefg",
    "caso_autoctone": "99cdefg",
    "uf_conclusao": "PI",
    "pais_conclusao": "99cdefg",
    "municipio_conclusao": "99cdefg",
    "cod_ibge_conclusao": "123456",
    "distrito_conclusao": "99cdefg",
    "bairro_conclusao": "99cdefg",
    "doenca_rel_trab": "99cdefg",
    "evolucao_caso": "99cdefg",
    "dt_obito": "15/02/2022",
    "dt_encerramento": "15/02/2022",
    "dt_desloc1": "15/02/2022",
    "uf_desloc1": "PI",
    "municipio_desloc1": "99cdefg",
    "pais_desloc1": "99cdefg",
    "transporte_desloc1": "99cdefg",
    "dt_desloc2": "15/02/2022",
    "uf_desloc2": "PI",
    "municipio_desloc2": "99cdefg",
    "pais_desloc2": "99cdefg",
    "transporte_desloc2": "99cdefg",
    "dt_desloc3": "15/02/2022",
    "uf_desloc3": "PI",
    "municipio_desloc3": "99cdefg",
    "pais_desloc3": "99cdefg",
    "transporte_desloc3": "99cdefg",
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
document.write_text(especifico['numero_ficha2'],(470, 44))
document.write_date(especifico['dt_notificacao2'], (453, 155), spacing=2) #data_notificacao
document.write_uf(especifico['uf_notificacao2'], (60, 185)) #uf_notificacao
document.write_text(especifico['municipio_notificacao2'], (100, 185)) #municipio_notificacao __unid_saude 55,space=220
document.write_code(especifico['cod_ibge_notificacao2'], (484, 186),space=2) #cod_ibge
document.write_text(especifico['unidade_saude2'], (70, 214)) #cod_unid_saude
document.write_code(especifico['cod_unidade_saude2'], (344, 214),space=2) #cod_unid_saude
document.write_date(especifico['dt_sintomas2'], (452, 213), spacing=2) #data_diagnostico
##############################################
#####          NOTIFICACAO INDIVIDUAL     ####
##############################################
document.write_text(especifico['nome_paciente2'], (65, 245)) #nome
document.write_date(especifico['dt_nascimento2'], (455, 244), spacing=2) #data_nascimento
document.write_code(especifico['idade2'], (70, 274),space=2) #idade
document.write_mini(especifico['tipo_idade2'], (117, 267)) #tipo_idade
document.write_mini(especifico['sexo2'], (239, 260)) #sexo
document.write_mini(especifico['gestante2'], (434, 260)) #gestante
document.write_mini(especifico['raca2'], (560, 261)) #raça/cor
document.write_mini(especifico['escolaridade2'], (560, 290)) #escolaridade
document.write_code(especifico['numero_sus2'], (64, 334),space=2, font_size=10) #cartao_sus
document.write_text(especifico['nome_mae2'], (250, 334)) #nome_mae
##############################################
#####          DADOS DE RESIDENCIA        ####
##############################################

document.write_uf(especifico['uf_residencia2'], (62, 365)) #uf_residencia
document.write_text(especifico['municipio_residencia2'], (100, 365)) #municipio_residencia
document.write_code(especifico['cod_ibge_residencia2'], (333, 366),space=2) #cod_ibge_residencia
document.write_text(especifico['distrito_residencia2'], (430, 365)) #endereco
document.write_text(especifico['bairro_residencia2'], (70, 390)) #bairro
document.write_text(especifico['logradouro_residencia2'], (210, 392)) #logradouro
document.write_code(especifico['codigo_residencia2'], (487, 392),space=2) #cod_logradouro
document.write_text(especifico['numero_residencia2'], (68, 415)) #numero
document.write_text(especifico['complemento_residencia2'], (120, 415)) #complemento
document.write_text(especifico['geo_campo1_2'], (420, 417)) #geo_campo_1
document.write_text(especifico['geo_campo2_2'], (63, 440)) #geo_campo_2
document.write_text(especifico['ponto_ref_residencia2'], (235, 440)) #ponto_ref
document.write_code(especifico['cep_residencia2'], (462, 443),space=2) #cep
document.write_telefone(especifico['telefone_residencia2'], (62, 467), space=2) #telefone
document.write_mini(especifico['zona_residencia2'], (340, 455)) #zona
document.write_text(especifico['pais_residencia2'], (380, 466)) #pais
###################################################
# Dados Complementares _ Ficha de Investigação    #
###################################################

document.write_date(especifico['dt_investigacao'], (68, 520), spacing=2) #data_investigacao
document.write_text(especifico['ocupacao'], (190, 520)) #ocupacao
document.write_mini(especifico['sintoma_febre'], (98, 552)) #febre
document.write_mini(especifico['sintoma_fraqueza'], (98, 565)) #fraqueza
document.write_mini(especifico['sintoma_edema'], (98, 579)) #edema
document.write_mini(especifico['sintoma_emagrecimento'], (180, 553)) #emagrecimento
document.write_mini(especifico['sintoma_tosse'], (180, 566)) #tosse_diarreia
document.write_mini(especifico['sintoma_palidez'], (181, 579)) #palidez
document.write_mini(especifico['sintoma_baco'], (278, 553)) #baco
document.write_mini(especifico['sintoma_quadro_infec'], (278, 567)) #infeccioso
document.write_mini(especifico['sintoma_hemorragia'], (278, 580)) #fen_hemorragico
document.write_mini(especifico['sintoma_figado'], (416, 553)) #aumento_figado
document.write_mini(especifico['sintoma_icteria'], (417, 566)) #ictericia
document.write_text(especifico['sintoma_outro'], (416, 581)) #outros
document.write_mini(especifico['sintoma_outro_descricao'], (454, 577)) #outros_text
document.write_mini(especifico['co_infec_hiv'], (536, 608)) #co_infec_hiv
document.write_mini(especifico['diag_parasitologica'], (217, 653)) #diag_parasitologico
document.write_mini(especifico['diag_imuno_ifi'], (362, 661)) #diag_imunologico
document.write_mini(especifico['diag_imuno_outro'], (362, 678)) #diag_imuno_outro
document.write_mini(especifico['tipo_entrada'], (548, 649)) #tipo_entrada
document.write_date(especifico['dt_inicio_trat'], (68, 717), spacing=2) #data_tratamento
document.write_mini(especifico['droga_inicial_adm'], (554, 698)) #drug_administrada
document.write_code(especifico['peso'], (98, 749),space=1) #peso
document.write_mini(especifico['dose_prescrita'], (398, 733)) #dose_presc
document.write_code(especifico['quant_ampolas'], (452, 758),space=1) #total_ampola
document.write_mini(especifico['droga_falencia_trat'], (542, 777)) #outra_droga

################################################### fim page

document.write_mini(especifico['classif_final'], (299, 50),pg=1) #class_final
document.write_mini(especifico['criterio_confirm'], (545, 46),pg=1) #crit_confirmacao
document.write_mini(especifico['caso_autoctone'], (306, 103),pg=1) #autoctone
document.write_uf(especifico['uf_conclusao'], (350, 113),pg=1) #uf
document.write_text(especifico['pais_conclusao'], (400, 113),pg=1) #pais
document.write_text(especifico['municipio_conclusao'], (70, 144),pg=1) #municipio
document.write_code(especifico['cod_ibge_conclusao'], (211, 144),pg=1,space=2) #ibge
document.write_text(especifico['distrito_conclusao'], (310, 143),pg=1) #distrito
document.write_text(especifico['bairro_conclusao'], (450, 143),pg=1) #bairro
document.write_mini(especifico['doenca_rel_trab'], (283, 160),pg=1) #doenca_rel_trabalho
document.write_mini(especifico['evolucao_caso'], (550, 160),pg=1) #evolucao_caso
document.write_date(especifico['dt_obito'], (62, 210),pg=1, spacing=2) #data_obito
document.write_date(especifico['dt_encerramento'], (188, 210),pg=1, spacing=2) #data_encerramento
document.write_text(especifico['dt_desloc1'], (36, 281),pg=1) #data_1_obs
document.write_text(especifico['dt_desloc2'], (36, 294),pg=1) #data_2_obs
document.write_text(especifico['dt_desloc3'], (36, 306),pg=1) #data_3_obs
document.write_uf(especifico['uf_desloc1'], (120, 281),pg=1) #uf_1_obs
document.write_uf(especifico['uf_desloc2'], (120, 294),pg=1) #uf_2_obs
document.write_uf(especifico['uf_desloc3'], (120, 306),pg=1) #uf_3_obs
document.write_text(especifico['municipio_desloc1'], (160, 281),pg=1) #municipio_1_obs
document.write_text(especifico['municipio_desloc2'], (160, 294),pg=1) #municipio_2_obs
document.write_text(especifico['municipio_desloc3'], (160, 306),pg=1) #municipio_3_obs
document.write_text(especifico['pais_desloc1'], (340, 281),pg=1) #pais_1_obs
document.write_text(especifico['pais_desloc2'], (340, 294),pg=1) #pais_2_obs
document.write_text(especifico['pais_desloc3'], (340, 306),pg=1) #pais_3_obs
document.write_text(especifico['transporte_desloc1'], (460, 281),pg=1) #meio_1_transporte
document.write_text(especifico['transporte_desloc2'], (460, 294),pg=1) #meio_2_transporte
document.write_text(especifico['transporte_desloc3'], (460, 306),pg=1) #meio_3_transporte
document.write_box(especifico['obs_adicionais'], 1,(35,349, 570, 660)) #text_obs
document.write_text(especifico['municipio_us_investigador'], (65, 695),pg=1) #municipio_unid_saude
document.write_code(especifico['cod_us_investigador'], (466, 695),pg=1,space=2) #cod_municipio_un
document.write_text(especifico['nome_investigador'], (65, 723),pg=1) #investigador
document.write_text(especifico['funcao_investigador'], (265, 723),pg=1) #funcao
document.write_text(especifico['assinatura_investigador'], (470, 723),pg=1) #assinatura_investigador


document.save('leish.geracao_pdf')