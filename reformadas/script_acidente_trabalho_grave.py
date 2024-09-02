from pdfWritter import PDFWriter
pdf = 'fichas/prioridades/acidenteTrabalhoGrave.pdf'
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
    "tipo_idade2": "25",
    "sexo2": "observacao",
    "gestante2": "9",
    "raca2": "9",
    "escolaridade2": "25",
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
    "sit_merc_trabalho": "99",
    "tempo_trabalho": "999",
    "tipo_tempo_trabalho": "2",
    "local_acidente": "9",
    "cnpj_contratante": "99999999999999",
    "nome_contratante": "observacao",
    "ativ_contratante": "observacao",
    "uf_contratante": "PI",
    "municipio_contratante": "observacao",
    "cod_ibge_contratante": "123456",
    "distrito_contratante": "observacao",
    "bairro_contratante": "observacao",
    "endereco_contratante": "observacao",
    "numero_contratante": "15485",
    "ponto_ref_contratante": "observacao",
    "telefone_contratante": "86999999999",
    "empresa_terceirizada": "9",
    "cnae_emp_principal": "12356487",
    "cnpj_emp_principal": "12345678912548",
    "rz_social_emp_principal": "observacao",
    "hr_acidente": "99",
    "min_acidente": "99",
    "hr_apos_inicio_jornada": "99",
    "min_apos_inicio_jornada": "99",
    "uf_acidente": "PI",
    "municipio_acidente": "observacao",
    "cod_ibge_acidente": "123456",
    "cod_causa_acidente": "1234",
    "tipo_acidente": "9",
    "outros_atingidos": "9",
    "quant_trab_atingidos": "999",
    "ocorreu_atendimento": "9",
    "dt_atendimento": "15/02/2022",
    "uf_atendimento": "PI",
    "municipio_atendimento": "observacao",
    "cod_ibge_atendimento": "123456",
    "nome_hosp_atendimento": "observacao",
    "cod_us_atendimento": "123456",
    "parte_corpo_atend1": "99",
    "parte_corpo_atend2": "99",
    "parte_corpo_atend3": "99",
    "diag_lesao": "1234",
    "regime_tratamento": "9",
    "evolucao_caso": "9",
    "dt_obito": "15/02/2022",
    "comun_acid_trab": "9",
    "obs_adicionais": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc.",
    "outras_informacoes": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. ",
    "municipio_us_investigador": "observacao",
    "cod_us_investigador": "123456",
    "nome_investigador": "observacao",
    "funcao_investigador": "observacao",
    "assinatura_investigador": "observacao"
}


###################################################
# Dados do paciente
###################################################
doc.write_text(especifico['numero_ficha2'],(470, 45))
doc.write_date(especifico['dt_notificacao2'], (448, 205), spacing=2) #data_notificacao
doc.write_uf(especifico['uf_notificacao2'], (55, 234)) #uf_notificacao
doc.write_text(especifico['municipio_notificacao2'], (88, 235)) #municipio_notificacao __unid_saude 55,space=220
doc.write_code(especifico['cod_ibge_notificacao2'], (478, 235),space=2) #cod_ibge
doc.write_text(especifico['unidade_saude2'], (65, 262)) #cod_unid_saude
doc.write_code(especifico['cod_unidade_saude2'], (338, 262),space=2) #cod_unid_saude
doc.write_date(especifico['dt_acidente'], (444, 262), spacing=2) #data_diagnostico
##############################################
#####          NOTIFICACAO INDIVIDUAL     ####
##############################################
doc.write_text(especifico['nome_paciente2'], (62, 294)) #nome
doc.write_date(especifico['dt_nascimento2'], (449, 293), spacing=2) #data_nascimento
doc.write_code(especifico['idade2'], (63, 323),space=2) #idade
doc.write_mini(especifico['tipo_idade2'], (110, 315)) #tipo_idade
doc.write_mini(especifico['sexo2'], (233, 308)) #sexo
doc.write_mini(especifico['gestante2'], (428, 308)) #gestante
doc.write_mini(especifico['raca2'], (553, 309)) #raça/cor
doc.write_mini(especifico['escolaridade2'], (553, 338)) #escolaridade
doc.write_code(especifico['numero_sus2'], (56, 384),space=2, font_size=10) #cartao_sus
doc.write_text(especifico['nome_mae2'], (240, 384)) #nome_mae
##############################################
#####          DADOS DE RESIDENCIA        ####
##############################################

doc.write_uf(especifico['uf_residencia2'], (57, 412)) #uf_residencia
doc.write_text(especifico['municipio_residencia2'], (95, 410)) #municipio_residencia
doc.write_code(especifico['cod_ibge_residencia2'], (325, 410),space=2) #cod_ibge_residencia
doc.write_text(especifico['distrito_residencia2'], (422, 410)) #endereco
doc.write_text(especifico['bairro_residencia2'], (64, 435)) #bairro
doc.write_text(especifico['logradouro_residencia2'], (207, 438)) #logradouro
doc.write_code(especifico['codigo_residencia2'], (478, 438),space=2) #cod_logradouro
doc.write_text(especifico['numero_residencia2'], (65, 460)) #numero
doc.write_text(especifico['complemento_residencia2'], (120, 460)) #complemento
doc.write_text(especifico['geo_campo1_2'], (415, 462)) #geo_campo_1
doc.write_text(especifico['geo_campo2_2'], (55, 485)) #geo_campo_2
doc.write_text(especifico['ponto_ref_residencia2'], (230, 487)) #ponto_ref
doc.write_code(especifico['cep_residencia2'], (456, 489),space=2) #cep
doc.write_telefone(especifico['telefone_residencia2'], (57, 513), space=2) #telefone
doc.write_mini(especifico['zona_residencia2'], (334, 501)) #zona
doc.write_text(especifico['pais_residencia2'], (380, 512)) #pais
####################################################
# Dados Complementares
####################################################
doc.write_text(especifico['ocupacao'], (60, 567)) #ocupacao
doc.write_mini(especifico['sit_merc_trabalho'], (535, 582), spacing=3) #sit_merc_trabalho
doc.write_code(especifico['tempo_trabalho'], (68, 664), space=2) #tempo_trabalho
doc.trab_tempo_ocupacao(especifico['tipo_tempo_trabalho']) #tipo_tempo_trabalho
doc.write_mini(especifico['local_acidente'], (554, 645)) #local_acidente
doc.write_code(especifico['cnpj_contratante'], (60, 705), space=2, font_size=12) #cnpj_contratante
doc.write_text(especifico['nome_contratante'], (260, 705)) #nome_contratante
doc.write_text(especifico['ativ_contratante'], (62, 736)) #ativ_contratante
doc.write_uf(especifico['uf_contratante'], (221, 736)) #uf_contratante
doc.write_text(especifico['municipio_contratante'], (260, 734)) #municipio_contratante
doc.write_code(especifico['cod_ibge_contratante'], (484, 734), space=2) #cod_ibge_contratante
doc.write_text(especifico['distrito_contratante'], (62, 761)) #distrito_contratante
doc.write_text(especifico['bairro_contratante'], (223, 761)) #bairro_contratante
doc.write_text(especifico['endereco_contratante'], (388, 761)) #endereco_contratante
doc.write_text(especifico['numero_contratante'], (66, 784)) #numero_contratante
doc.write_text(especifico['ponto_ref_contratante'], (120, 784)) #ponto_ref_contratante
doc.write_telefone(especifico['telefone_contratante'], (430, 785), space=2) #telefone_contratante
doc.write_mini(especifico['empresa_terceirizada'], (480, 800)) #empresa_terceirizada
#################################################### fim da pagina 1

doc.write_code(especifico['cnae_emp_principal'], (190, 52),space=2, pg=1) #cnae_emp_principal
doc.write_code(especifico['cnpj_emp_principal'], (368, 54),space=2, pg=1) #cnpj_emp_principal
doc.write_text(especifico['rz_social_emp_principal'], (60, 80), pg=1) #rz_social_emp_principal
doc.write_code(especifico['hr_acidente'], (95, 118),space=2, pg=1) #hr_acidente
doc.write_code(especifico['min_acidente'], (198, 117),space=2, pg=1) #min_acidente
doc.write_code(especifico['hr_apos_inicio_jornada'], (407, 117),space=2, pg=1) #hr_apos_inicio_jornada
doc.write_code(especifico['min_apos_inicio_jornada'], (474, 117),space=2, pg=1) #min_apos_inicio_jornada
doc.write_uf(especifico['uf_acidente'], (62, 146), pg=1) #uf_acidente
doc.write_text(especifico['municipio_acidente'], (95, 146), pg=1) #municipio_acidente
doc.write_code(especifico['cod_ibge_acidente'], (240, 146),space=2, pg=1) #cod_ibge_acidente
doc.write_code(especifico['cod_causa_acidente'], (494, 147),space=2, pg=1) #cod_causa_acidente
doc.write_mini(especifico['tipo_acidente'], (222, 162), pg=1) #tipo_acidente
doc.write_mini(especifico['outros_atingidos'], (435, 162), pg=1) #outros_atingidos
doc.write_code(especifico['quant_trab_atingidos'], (494, 175),space=2, pg=1) #quant_trab_atingidos
doc.write_mini(especifico['ocorreu_atendimento'], (368, 196), pg=1) #ocorreu_atendimento
doc.write_date(especifico['dt_atendimento'], (412, 206), spacing=2, pg=1) #dt_atendimento
doc.write_uf(especifico['uf_atendimento'], (539, 206), pg=1) #uf_atendimento
doc.write_text(especifico['municipio_atendimento'], (60, 234), pg=1) #municipio_atendimento
doc.write_code(especifico['cod_ibge_atendimento'], (196, 235),space=2, pg=1) #cod_ibge_atendimento
doc.write_text(especifico['nome_hosp_atendimento'], (310, 235), pg=1) #nome_hosp_atendimento
doc.write_code(especifico['cod_us_atendimento'], (465, 235),space=2, pg=1) #cod_us_atendimento
doc.write_mini(especifico['parte_corpo_atend1'], (312, 263),spacing=2, pg=1) #parte_corpo_atend1
doc.write_mini(especifico['parte_corpo_atend2'], (312, 278),spacing=2, pg=1) #parte_corpo_atend2
doc.write_mini(especifico['parte_corpo_atend3'], (312, 291),spacing=2, pg=1) #parte_corpo_atend3
doc.write_code(especifico['diag_lesao'], (360, 293),space=2, pg=1) #diag_lesao
doc.write_mini(especifico['regime_tratamento'], (550, 268), pg=1) #regime_tratamento
doc.write_mini(especifico['evolucao_caso'], (545, 317), pg=1) #evolucao_caso
doc.write_date(especifico['dt_obito'], (65, 380), spacing=2, pg=1) #dt_obito
doc.write_mini(especifico['comun_acid_trab'], (547, 373), pg=1) #comun_acid_trab
doc.write_box(especifico['obs_adicionais'], rect=(34, 440, 565, 532), pg=1) #obs_adicionais
doc.write_box(especifico['outras_informacoes'], rect=(36, 553, 566, 650), pg=1) #outras_informacoes
doc.write_text(especifico['municipio_us_investigador'], (60, 680), pg=1) #municipio_us_investigador
doc.write_code(especifico['cod_us_investigador'], (468, 681),space=2, pg=1) #cod_us_investigador
doc.write_text(especifico['nome_investigador'], (60, 710), pg=1) #nome_investigador
doc.write_text(especifico['funcao_investigador'], (265, 710), pg=1) #funcao_investigador
doc.write_text(especifico['assinatura_investigador'], (470, 709), pg=1) #assinatura_investigador

doc.save('acidenteTrabalhoGrave.pdf', notificatoria)