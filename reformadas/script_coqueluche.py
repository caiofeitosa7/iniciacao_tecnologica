from pdfWritter import PDFWriter

pdf = 'fichas/completas/Coqueluche1.pdf'
doc = PDFWriter(pdf)

notificatoriaCSV= {
      "numero_ficha": "1758",
      "tipo_notificacao": "1",
      "agravoDoenca": "abcdefg",
      "dt_notificacao": "15/12/2021",
      "uf_notificacao": "PI",
      "municipio_notificacao": "abcdefg",
      "cod_ibge_notificacao": "123456",
      "unidade_saude": "abcdefg",
      "cod_unidade_saude": "1234567",
      "dt_sintomas": "15/12/2021",
      "nome_paciente": "abcdefg",
      "dt_nascimento": "15/12/2021",
      "idade": "25",
      "tipo_idade": "1",
      "sexo": "4",
      "gestante": "2",
      "raca": "9",
      "escolaridade": "9",
      "numero_sus": "123564879563245",
      "nome_mae": "abcdefg",
      "dt_primeiro_sintoma": "15/12/2021",
      "numero_casos_suspeitos": "10",
      "local_inicial_ocorrencia": "99",
      "local_inicial_ocorrencia_outro": "abcdefg",
      "uf_residencia": "PI",
      "municipio_residencia": "abcdefg",
      "cod_ibge_residencia": "123456",
      "distrito_residencia": "abcdefg",
      "bairro_residencia": "abcdefg",
      "logradouro_residencia": "abcdefg",
      "codigo_residencia": "123456",
      "numero_residencia": "3678",
      "complemento_residencia": "abcdefg",
      "geo_campo1": "abcdefg",
      "geo_campo2": "abcdefg",
      "ponto_ref_residencia": "abcdefg",
      "cep_residencia": "64016-630",
      "telefone_residencia": "86988256784",
      "zona_residencia": "9",
      "pais_residencia": "abcdefg",
      "municipio_us_notificante": "abcdefg",
      "nome_notificante": "abcdefg",
      "funcao_notificante": "abcdefg",
      "assinatura_notificante": "abcdefg",
      "dt_amostra_sorologia": "15/12/2021",
      "dt_outra_amostra": "15/12/2021",
      "tipo_exame": "abcdefg",
      "obito": "2",
      "caso_semelhante": "9",
      "exantema": "9",
      "dt_inicio_exantema": "15/12/2021",
      "petequiaSufusao": "9",
      "liquor": "9",
      "bacterioscopia": "abcdefg",
      "tomou_vacina": "9",
      "dt_ultima_dose_tomada": "15/12/2021",
      "hospitalizacao": "9",
      "dt_hospitalizacao": "15/12/2021",
      "uf_hospital": "PI",
      "municipio_hospital": "abcdefg",
      "cod_ibge_hospital": "1234567",
      "nome_hospital": "abcdefg",
      "cod_hospital": "1234567",
      "hipotese_diagnostica1": "abcdefg",
      "hipotese_diagnostica2": "abcdefg",
      "pais_infeccao": "abcdefg",
      "distrito_infeccao": "abcdefg",
      "uf_infeccao": "PI",
      "municipio_infeccao": "abcdefg",
      "bairro_infeccao": "abcdefg"
      }

especializado = {
    "numero_ficha2": "15428",
    "dt_notificacao2": "15/12/2021",
    "uf_notificacao2": "PI",
    "municipio_notificacao2": "Teresina",
    "cod_ibge_notificacao2": "123456",
    "unidade_saude2": "abcdefg",
    "cod_unidade_saude2": "123456",
    "dt_sintomas2": "15/02/2021",
    "nome_paciente2": "elton john",
    "dt_nascimento2": "15/02/2021",
    "idade2": "25",
    "tipo_idade2": "1",
    "sexo2": "9",
    "gestante2": "9",
    "raca2": "9",
    "escolaridade2": "9",
    "numero_sus2": "123564879563245",
    "nome_mae2": "maria m m m",
    "uf_residencia2": "PI",
    "municipio_residencia2": "Teresina",
    "cod_ibge_residencia2": "123456",
    "distrito_residencia2": "5",
    "bairro_residencia2": "cristo rei",
    "logradouro_residencia2": "rua 2",
    "codigo_residencia2": "123456",
    "numero_residencia2": "3598",
    "complemento_residencia2": "abcdefg",
    "geo_campo1_2": "abcdefg",
    "geo_campo2_2": "abcdefg",
    "ponto_ref_residencia2": "casa de esquina",
    "cep_residencia2": "64016000",
    "telefone_residencia2": "8688256784",
    "zona_residencia2": "9",
    "pais_residencia2": "abcdefg",
    "dt_investigacao": "15/02/2021",
    "ocupacao": "abcdefg",
    "notif_sentinela": "9",
    "contat_caso_susp": "9",
    "contat_caso_susp_outro": "dsadsad",
    "nome_contato": "jhon",
    "endereco_contato": "abcdefg",
    "doses_tri_treta": "9",
    "dt_ult_dose_tri_treta": "15/02/2021",
    "dt_tosse": "15/02/2021",
    "sint_tosse": "9",
    "sint_tosse_parox": "9",
    "sint_resp_ruidosa": "9",
    "sint_cianose": "9",
    "sint_vomito": "9",
    "sint_apneia": "9",
    "sint_temp_inferior38": "9",
    "sint_temp_superior38": "9",
    "sint_outro": "9",
    "sint_outro_descricao": "abcdefg",
    "comp_pneumonia": "9",
    "comp_encefalopatia": "9",
    "comp_desidratacao": "9",
    "comp_otite": "9",
    "comp_desnutricao": "9",
    "comp_outro": "9",
    "comp_outro_descricao": "abcdefg",
    "hospitalizacao2": "9",
    "dt_internacao": "15/02/2021",
    "uf_atendimento": "PI",
    "municipio_atendimento": "abcdefg",
    "cod_ibge_atendimento": "abcdefg",
    "nome_hosp_atendimento": "abcdefg",
    "cod_ibge_hosp_atendimento": "abcdefg",
    "utilizou_antibiotico": "9",
    "dt_adm_antibiotico": "15/02/2022",
    "nasofaringe": "9",
    "dt_nasofaringe": "15/02/2021",
    "resultado_cultura": "9",
    "identif_comun": "9",
    "quant_comunicantes": "10",
    "caso_secundario": "9",
    "coleta_naso": "9",
    "quant_coleta_naso": "020",
    "quant_coleta_posit": "020",
    "medida_controle": "9",
    "classif_final": "9",
    "crit_confimacao": "9",
    "doenca_rel_trab": "9",
    "evolucao_caso": "9",
    "dt_obito": "15/02/2022",
    "dt_encerramento": "15/02/2022",
    "obs_adicionais": "Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur. Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "municipio_us_investigador": "teresina",
    "cod_us_investigador": "12345678",
    "nome_investigador": "abcdefg",
    "funcao_investigador": "abcdefg",
    "assinatura_investigador": "abcdefg"
}

###################################################
# Dados do paciente
###################################################
doc.write_text(especializado['numero_ficha2'],(467, 49))
doc.write_date(especializado['dt_notificacao2'], (449, 183),spacing=2) #especializado-notificacao
doc.write_uf(especializado['uf_notificacao2'], (55, 212)) #uf-notificacao
doc.write_text(especializado['municipio_notificacao2'], (90, 212)) #municipio-notificacao --unid-saude 55,220
doc.write_code(especializado['cod_ibge_notificacao2'], (477, 212),space=2) #cod-ibge
doc.write_text(especializado['unidade_saude2'], (65, 240)) #cod-unid-saude
doc.write_code(especializado['cod_unidade_saude2'], (340, 240),space=2) #cod-unid-saude
doc.write_date(especializado['dt_sintomas2'], (446, 240), spacing=2) #especializado-diagnostico
##############################################
#####          NOTIFICACAO INDIVIDUAL     ####
##############################################
doc.write_text(especializado['nome_paciente2'], (60, 271)) #nome
doc.write_date(especializado['dt_nascimento2'], (449, 270), spacing=2) #especializado-nascimento
doc.write_code(especializado['idade2'], (65, 300),space=2) #idade
doc.write_mini(especializado['tipo_idade2'], (112, 292)) #tipo-idade
doc.write_mini(especializado['sexo2'], (233, 286)) #sexo
doc.write_mini(especializado['gestante2'], (429, 286)) #gestante
doc.write_mini(especializado['raca2'], (554, 286)) #raça/cor
doc.write_mini(especializado['escolaridade2'], (554, 316)) #escolaridade
doc.write_code(especializado['numero_sus2'], (58, 361),space=2, font_size=10) #cartao-sus
doc.write_text(especializado['nome_mae2'], (240, 360)) #nome-mae
##############################################
#####          DADOS DE RESIDENCIA        ####
##############################################

doc.write_uf(especializado['uf_residencia2'], (56, 390)) #uf-residencia
doc.write_text(especializado['municipio_residencia2'], (95, 390)) #municipio-residencia
doc.write_code(especializado['cod_ibge_residencia2'], (327, 391),space=2) #cod-ibge-residencia
doc.write_text(especializado['distrito_residencia2'], (422, 390)) #endereco
doc.write_text(especializado['bairro_residencia2'], (64, 415)) #bairro
doc.write_text(especializado['logradouro_residencia2'], (210, 416)) #logradouro
doc.write_code(especializado['codigo_residencia2'], (481, 417),space=2) #cod-logradouro
doc.write_text(especializado['numero_residencia2'], (65, 439)) #numero
doc.write_text(especializado['complemento_residencia2'], (120, 439)) #complemento
doc.write_text(especializado['geo_campo1_2'], (415, 442)) #geo-campo-1
doc.write_text(especializado['geo_campo2_2'], (55, 465)) #geo-campo-2
doc.write_text(especializado['ponto_ref_residencia2'], (230, 466)) #ponto-ref
doc.write_code(especializado['cep_residencia2'], (457, 467),space=2) #cep
doc.write_telefone(especializado['telefone_residencia2'], (59, 491), space=2) #telefone
doc.write_mini(especializado['zona_residencia2'], (335, 480)) #zona
doc.write_text(especializado['pais_residencia2'], (380, 491)) #pais
####################################################
# Dados Complementares
####################################################
doc.write_date(especializado['dt_investigacao'], (64, 542), spacing=2) #especializado-investigacao
doc.write_text(especializado['ocupacao'], (190, 542)) #ocupacao
doc.write_mini(especializado['notif_sentinela'], (555, 531)) #unidade-sentinela
doc.write_mini(especializado['contat_caso_susp'], (555, 555)) #contato-coqueluche
doc.write_text(especializado['contat_caso_susp_outro'], (242, 577)) #contato-outros
doc.write_text(especializado['nome_contato'], (65, 607)) #nome-contato
doc.write_text(especializado['endereco_contato'], (75, 631)) #endereco
doc.write_mini(especializado['doses_tri_treta'], (432, 661)) #n-doses-dtp
doc.write_date(especializado['dt_ult_dose_tri_treta'], (461, 672), spacing=2) #dt-ultima-dose
doc.write_date(especializado['dt_tosse'], (67, 703), spacing=2) #dt-inicio-tosse
doc.write_mini(especializado['sint_tosse'], (168, 724)) #tosse
doc.write_mini(especializado['sint_tosse_parox'], (168, 739)) #tosse-paroxistica
doc.write_mini(especializado['sint_resp_ruidosa'], (168, 754)) #respiracao-ruidosa
doc.write_mini(especializado['sint_cianose'], (345, 724)) #cianose
doc.write_mini(especializado['sint_vomito'], (345, 741)) #vomito
doc.write_mini(especializado['sint_apneia'], (345, 757)) #apneia
doc.write_mini(especializado['sint_temp_inferior38'], (459, 723)) #temperatura<38
doc.write_mini(especializado['sint_temp_superior38'], (459, 739)) #temperatura>38
doc.write_mini(especializado['sint_outro'], (459, 756)) #outros
doc.write_mini(especializado['sint_outro_descricao'], (498, 755)) #sintomas-text
doc.write_mini(especializado['comp_pneumonia'], (226, 778)) #pneumonia
doc.write_mini(especializado['comp_encefalopatia'], (226, 794)) #encefalopatia
doc.write_mini(especializado['comp_desidratacao'], (366, 778)) #desidratacao
doc.write_mini(especializado['comp_otite'], (366, 794)) #otite
doc.write_mini(especializado['comp_desnutricao'], (441, 778)) #desnutricao
doc.write_mini(especializado['comp_outro'], (441, 794)) #outros
doc.write_mini(especializado['comp_outro_descricao'], (480, 792)) #complica-text
#############FIM PG 1#############

doc.write_mini(especializado['hospitalizacao2'], (165, 38),pg=1) #hospitalizacao
doc.write_date(especializado['dt_internacao'], (185, 53),pg=1, spacing=2) #dt-internacao
doc.write_uf(especializado['uf_atendimento'], (305, 53),pg=1) #uf-internacao
doc.write_text(especializado['municipio_atendimento'], (338, 53),pg=1) #municipio-internacao
doc.write_code(especializado['cod_ibge_atendimento'], (484, 53),pg=1,space=2) #ibge-internacao
doc.write_text(especializado['nome_hosp_atendimento'], (65, 84),pg=1) #hospital-internacao
doc.write_code(especializado['cod_ibge_hosp_atendimento'], (472, 85),pg=1,space=2) #cod-hosp-internacao
doc.write_mini(especializado['utilizou_antibiotico'], (432, 106),pg=1) #antibiotico
doc.write_date(especializado['dt_adm_antibiotico'], (454, 122),pg=1, spacing=2) #dt-antibiotico
doc.write_mini(especializado['nasofaringe'], (208, 141),pg=1) #coleta-nasofaringe
doc.write_date(especializado['dt_nasofaringe'], (238, 160),pg=1, spacing=2) #dt-coleta-naso
doc.write_mini(especializado['resultado_cultura'], (551, 139),pg=1) #res-cultura
doc.write_mini(especializado['identif_comun'], (184, 190),pg=1) #comunicante-intimo
doc.write_code(especializado['quant_comunicantes'], (250, 200),pg=1, space=2) #qtd-comunicante
doc.write_mini(especializado['caso_secundario'], (552, 183),pg=1) #qtd-caso-secundarios
doc.write_mini(especializado['coleta_naso'], (188, 235),pg=1) #coleta-naso-comunicante
doc.write_code(especializado['quant_coleta_naso'], (253, 247),pg=1, space=2) #qtd-coleta
doc.write_code(especializado['quant_coleta_posit'], (377, 247),pg=1, space=2) #qtd-res-positivo
doc.write_mini(especializado['medida_controle'], (562, 223),pg=1) #medida-preventiva
doc.write_mini(especializado['classif_final'], (200, 270),pg=1) #class-final
doc.write_mini(especializado['crit_confimacao'], (548, 271),pg=1) #crit-confirmacao
doc.write_mini(especializado['doenca_rel_trab'], (246, 307),pg=1) #doenca-trabalho
doc.write_mini(especializado['evolucao_caso'], (555, 303),pg=1) #evolucao
doc.write_date(especializado['dt_obito'], (63, 350),pg=1, spacing=2) #dt-obito
doc.write_date(especializado['dt_encerramento'], (182, 349),pg=1, spacing=2) #dt-encerramento
doc.write_box(especializado['obs_adicionais'], 1,(33, 413,570,660)) #obs
doc.write_text(especializado['municipio_us_investigador'], (60, 690),pg=1) #municipio-investigador
doc.write_code(especializado['cod_us_investigador'], (477, 692),pg=1, space=1) #cod-unid-saud
doc.write_text(especializado['nome_investigador'], (60, 720),pg=1) #nome-investigador
doc.write_text(especializado['funcao_investigador'], (268, 720),pg=1) #funcao-investigador
doc.write_text(especializado['assinatura_investigador'], (470, 720),pg=1) #asign-investigador


doc.save('coqueluche.pdf', notificatoriaCSV)