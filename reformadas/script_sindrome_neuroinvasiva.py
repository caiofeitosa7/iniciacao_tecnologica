from pdfWritter import PDFWriter
pdf = 'sindrome Neuroinvasiva1.pdf'
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
    "tipo_notificacao2": "9",
    "agravoDoenca_num": "9",
    "agravoDoenca_outro": "observacao",
    "dt_notificacao2": "15/02/2022",
    "uf_notificacao2": "PI",
    "municipio_notificacao2": "observacao",
    "cod_ibge_notificacao2": "123456",
    "dt_hospitalizacao": "15/02/2022",
    "serv_vigilancia": "observacao",
    "cod_serv_vigilancia": "123456",
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
    "cep_residencia2": "64000000",
    "complemento_residencia2": "observacao",
    "geo_campo1_2": "observacao",
    "telefone_residencia2": "86999999999",
    "zona_residencia2": "9",
    "pais_residencia2": "observacao",
    "dt_investigacao": "15/02/2022",
    "ocupacao": "observacao",
    "dt_sintomas2": "15/02/2022",
    "viagem_recente": "9",
    "destino_viagem": "observacao",
    "vac_febre_amarela": "9",
    "loc_ave_equina": "9",
    "caso_semelhante": "9",
    "infec_gripe": "9",
    "infec_diarreia": "9",
    "infec_dengue": "9",
    "infec_outro": "9",
    "infec_outro_descricao": "observacao",
    "dt_adoecimento": "15/02/2022",
    "imunodepressao": "9",
    "vacinacao_recente": "9",
    "dados_vacinacao": "observacao",
    "imunoglobulina": "9",
    "dt_infusao": "15/02/2022",
    "ex_hemograma": "9",
    "ex_liquor": "9",
    "ex_tomografia": "9",
    "ex_ressonancia": "9",
    "ex_enm": "9",
    "ex_eeg": "9",
    "ex_biopsia": "9",
    "ex_necropsia": "9",
    "desf_hospitalar": "9",
    "diag_alta": "observacao",
    "dt_alta_obito": "15/02/2022",
    "dt_encerramento": "15/02/2022",
    "diag_etiologico": "9",
    "diag_etiol_outro_descricao": "observacao",
    "classif_caso": "9",
    "criterio_classif": "9",
    "obs_adicionais": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc.",
    "nome_investigador": "observacao",
    "funcao_investigador": "observacao",
    "telefone_investigador": "86999999999"
}

###################################################
# Dados do paciente
###################################################
doc.write_text(especifico['numero_ficha2'],(470, 57))
if especifico['tipo_notificacao2'] == '1':
  doc.write_cross((170, 114))
else:
  doc.write_cross((310, 115))
doc.write_date(especifico['dt_notificacao2'], (444, 144), spacing=2) #data_notificacao
doc.write_uf(especifico['uf_notificacao2'], (70, 172)) #uf_notificacao
doc.write_text(especifico['municipio_notificacao2'], (98, 172)) #municipio_notificacao __unid_saude 55,space=220
doc.write_code(especifico['cod_ibge_notificacao2'], (478, 170),space=2) #cod_ibge
doc.write_text(especifico['dt_hospitalizacao'], (82, 196)) #data_hospitalizacao
doc.write_text(especifico['serv_vigilancia'], (200, 196)) #servico_vigilancia
doc.write_code(especifico['cod_serv_vigilancia'], (467, 196),space=2) #cod_servico_vigilancia
##############################################
#####          NOTIFICACAO INDIVIDUAL     ####
##############################################
doc.write_text(especifico['nome_paciente2'], (75, 225)) #nome
doc.write_date(especifico['dt_nascimento2'], (442, 227), spacing=2) #data_nascimento
doc.write_code(especifico['idade2'], (75, 256),space=2) #idade
doc.write_mini(especifico['tipo_idade2'], (122, 250)) #tipo_idade
doc.write_mini(especifico['sexo2'], (240, 251)) #sexo
doc.write_mini(especifico['gestante2'], (430, 251)) #gestante
doc.write_mini(especifico['raca2'], (547, 251)) #raça/cor
doc.write_mini(especifico['escolaridade2'], (546, 279)) #escolaridade
doc.write_code(especifico['numero_sus2'], (68, 320), font_size=12) #cartao_sus
doc.write_text(especifico['nome_mae2'], (245, 321)) #nome_mae
##############################################
#####          DADOS DE RESIDENCIA        ####
##############################################

doc.write_uf(especifico['uf_residencia2'], (68, 350)) #uf_residencia
doc.write_text(especifico['municipio_residencia2'], (100, 349)) #municipio_residencia
doc.write_code(especifico['cod_ibge_residencia2'], (326, 349),space=2) #cod_ibge_residencia
doc.write_text(especifico['distrito_residencia2'], (420, 348)) #endereco
doc.write_text(especifico['bairro_residencia2'], (75, 373)) #bairro
doc.write_text(especifico['logradouro_residencia2'], (210, 373)) #logradouro
doc.write_code(especifico['codigo_residencia2'], (406, 372),space=2) #cod_logradouro
doc.write_text(especifico['numero_residencia2'], (510, 372)) #numero
doc.write_code(especifico['cep_residencia2'], (67, 397), font_size=12) #cep
doc.write_text(especifico['complemento_residencia2'], (145, 397)) #complemento
doc.write_text(especifico['geo_campo1_2'], (415, 396)) #geo_campo_1
doc.write_telefone(especifico['telefone_residencia2'], (70, 422), space=2,font_size=12) #telefone
doc.write_mini(especifico['zona_residencia2'], (343, 415)) #zona
doc.write_text(especifico['pais_residencia2'], (370, 421)) #pais
###################################################
# Dados Complementares _ Ficha de Investigação    #
###################################################
doc.write_date(especifico['dt_investigacao'], (73, 463), spacing=2) #data_investigacao
doc.write_text(especifico['ocupacao'], (200, 463)) #ocupacao
doc.write_date(especifico['dt_sintomas2'], (435, 463), spacing=2) #data_sintomas
doc.write_mini(especifico['viagem_recente'], (293, 482)) #viagem_recente
doc.write_text(especifico['destino_viagem'], (325, 490)) #destino_viagem
doc.write_mini(especifico['vac_febre_amarela'], (200, 512)) #vac_febre_amarela
doc.write_mini(especifico['loc_ave_equina'], (357, 519)) #local_ave_equina
doc.write_mini(especifico['caso_semelhante'], (534, 516)) #caso_semelhante
doc.write_mini(especifico['infec_gripe'], (71, 554)) #infec_gripe
doc.write_mini(especifico['infec_diarreia'], (71, 570)) #infec_diarreia
doc.write_mini(especifico['infec_dengue'], (160, 554)) #infec_dengue
doc.write_mini(especifico['infec_outro'], (160, 570)) #infec_outro
doc.write_text(especifico['infec_outro_descricao'], (232, 569)) #infec_outro_descricao
doc.write_date(especifico['dt_adoecimento'], (396, 570), spacing=3) #data_adoecimento
doc.write_mini(especifico['imunodepressao'], (204, 599)) #imunodepressao
doc.write_mini(especifico['vacinacao_recente'], (356, 599)) #vacinacao_recente
doc.write_text(especifico['dados_vacinacao'], (400, 605)) #dados_vacinacao
doc.write_mini(especifico['imunoglobulina'], (408, 620)) #imunoglobulina
doc.write_date(especifico['dt_infusao'], (429, 628), spacing=2) #data_infusao
doc.write_mini(especifico['ex_hemograma'], (226, 640)) #ex_hemograma
doc.write_mini(especifico['ex_liquor'], (226, 655)) #ex_liquor
doc.write_mini(especifico['ex_tomografia'], (292, 641)) #ex_tomografia
doc.write_mini(especifico['ex_ressonancia'], (292, 655)) #ex_ressonancia
doc.write_mini(especifico['ex_enm'], (394, 641)) #ex_enm
doc.write_mini(especifico['ex_eeg'], (394, 655)) #ex_eeg
doc.write_mini(especifico['ex_biopsia'], (490, 641)) #ex_biopsia
doc.write_mini(especifico['ex_necropsia'], (490, 655)) #ex_necropsia
doc.write_mini(especifico['desf_hospitalar'], (205, 680)) #desf_hospitalar
doc.write_text(especifico['diag_alta'], (230, 689)) #diagnostico_alta
doc.write_date(especifico['dt_alta_obito'], (348, 689), spacing=1) #data_alta_obito
doc.write_date(especifico['dt_encerramento'], (450, 689), spacing=2) #data_encerramento
doc.write_mini(especifico['diag_etiologico'], (180, 716)) #diagnostico_etiologico
doc.write_text(especifico['diag_etiol_outro_descricao'], (98, 726)) #diagnostico_etiologico_outro
doc.write_mini(especifico['classif_caso'], (303, 718)) #classificacao_caso
doc.write_mini(especifico['criterio_classif'], (544, 720)) #criterio_classificacao
doc.write_box(especifico['obs_adicionais'], rect=(70, 740,558,800)) #observacoes_adicionais


doc.save('sindrome_neuroinvasiva1.pdf', notificatoria)