from pdfWritter import PDFWriter


pdf = 'sifilis_adquirida1.pdf'
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
    "dt_acidente": "15/02/2022",
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
    "ocupacao": "observacao",
    "antecedente_sifilis": "9",
    "trat_realizado_sifilis": "9",
    "comportamento_sexual": "9",
    "teste_nao_treponemico": "9",
    "titulo_laboratorial": "observacao",
    "dt_laboratorial": "15/02/2022",
    "teste_treponemico": "9",
    "classif_clinica": "9",
    "trat_realizado": "9",
    "dt_inicio_trat": "15/02/2022",
    "classif_final": "9",
    "classif_final_descricao": "observacao",
    "obs_adicionais": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc.",
    "municipio_us_investigador": "observacao",
    "cod_us_investigador": "123456",
    "nome_investigador": "observacao",
    "funcao_investigador": "observacao",
    "assinatura_investigador": "observacao"
}

###################################################
# Dados do paciente
###################################################
doc.write_text(especifico['numero_ficha2'],(440, 37))
doc.write_date(especifico['dt_notificacao2'], (418, 131), spacing=2) #data_notificacao
doc.write_uf(especifico['uf_notificacao2'], (53, 160)) #uf_notificacao
doc.write_text(especifico['municipio_notificacao2'], (90, 160)) #municipio_notificacao __unid_saude 55,space=220
doc.write_code(especifico['cod_ibge_notificacao2'], (448, 160),space=2) #cod_ibge
doc.write_text(especifico['unidade_saude2'], (64, 186)) #cod_unid_saude
doc.write_code(especifico['cod_unidade_saude2'], (317, 187),space=2) #cod_unid_saude
doc.write_date(especifico['dt_acidente'], (417, 186), spacing=2) #data acidente
##############################################
#####          NOTIFICACAO INDIVIDUAL     ####
##############################################
doc.write_text(especifico['nome_paciente2'], (60, 215)) #nome
doc.write_date(especifico['dt_nascimento2'], (419, 215), spacing=2) #data_nascimento
doc.write_code(especifico['idade2'], (60, 248),space=2) #idade
doc.write_mini(especifico['tipo_idade2'], (104, 242)) #tipo_idade
doc.write_mini(especifico['sexo2'], (218, 236)) #sexo
doc.write_mini(especifico['raca2'], (520, 236)) #raça/cor
doc.write_mini(especifico['escolaridade2'], (522, 270)) #escolaridade
doc.write_code(especifico['numero_sus2'], (51, 311),space=2, font_size=10) #cartao_sus
doc.write_text(especifico['nome_mae2'], (227, 311)) #nome_mae
##############################################
#####          DADOS DE RESIDENCIA        ####
##############################################

doc.write_uf(especifico['uf_residencia2'], (54, 340)) #uf_residencia
doc.write_text(especifico['municipio_residencia2'], (95, 340), font_size=8) #municipio_residencia
doc.write_code(especifico['cod_ibge_residencia2'], (307, 340),space=2) #cod_ibge_residencia
doc.write_text(especifico['distrito_residencia2'], (400, 340), font_size=9) #endereco
doc.write_text(especifico['bairro_residencia2'], (64, 365), font_size=8) #bairro
doc.write_text(especifico['logradouro_residencia2'], (195, 366), font_size=8) #logradouro
doc.write_code(especifico['codigo_residencia2'], (452, 366),space=2) #cod_logradouro
doc.write_text(especifico['numero_residencia2'], (65, 390)) #numero
doc.write_text(especifico['complemento_residencia2'], (120, 390), font_size=9) #complemento
doc.write_text(especifico['geo_campo1_2'], (400, 391)) #geo_campo_1
doc.write_text(especifico['geo_campo2_2'], (55, 420)) #geo_campo_2
doc.write_text(especifico['ponto_ref_residencia2'], (215, 422), font_size=9) #ponto_ref
doc.write_code(especifico['cep_residencia2'], (431, 423),space=2, font_size=12) #cep
doc.write_telefone(especifico['telefone_residencia2'], (55, 450), space=2, font_size=12) #telefone
doc.write_mini(especifico['zona_residencia2'], (316, 439)) #zona
doc.write_text(especifico['pais_residencia2'], (345, 449), font_size=9) #pais
##############################################
#####        DADOS  COMPLEMENTARES        ####
##############################################
doc.write_text(especifico['ocupacao'], (60, 502), font_size=9) #ocupacao
doc.write_mini(especifico['antecedente_sifilis'], (275, 515)) #antecedente_sifilis
doc.write_mini(especifico['trat_realizado_sifilis'], (520, 515)) #trat_realizado_sifilis
doc.write_mini(especifico['comportamento_sexual'], (519, 550)) #comportamento_sexual
doc.write_mini(especifico['teste_nao_treponemico'], (291, 597)) #teste_nao_treponemico
doc.write_text(especifico['titulo_laboratorial'], (334, 607), font_size=8) #titulo_laboratorial
doc.write_date(especifico['dt_laboratorial'], (420, 610), spacing=2) #data_laboratorial
doc.write_mini(especifico['teste_treponemico'], (515, 627)) #teste_treponemico
doc.write_mini(especifico['classif_clinica'], (518, 658)) #classif_clinica
doc.write_mini(especifico['trat_realizado'], (360, 690)) #trat_realizado
doc.write_date(especifico['dt_inicio_trat'], (422, 715), spacing=2) #data_inicio_trat
doc.write_mini(especifico['classif_final'], (242, 740)) #classif_final
doc.write_text(especifico['classif_final_descricao'], (182, 754), font_size=8) #classif_final_descricao
#*=========================== fim da pagina 1 ===========================*#
doc.write_box(especifico['obs_adicionais'], rect=(26, 20, 535, 183),pg=1, bord=True)
doc.write_text(especifico['municipio_us_investigador'], (55, 208), pg=1, font_size=9) #municipio_us_investigador
doc.write_code(especifico['cod_us_investigador'], (433, 209),space=2, pg=1) #cod_us_investigador
doc.write_text(especifico['nome_investigador'], (55, 231), pg=1, font_size=9) #nome_investigador
doc.write_text(especifico['funcao_investigador'], (240, 231), pg=1, font_size=9) #funcao_investigador
doc.write_text(especifico['assinatura_investigador'], (435, 232), pg=1, font_size=9) #assinatura_investigador

doc.save('sifilis_adquirida.pdf', notificatoria)