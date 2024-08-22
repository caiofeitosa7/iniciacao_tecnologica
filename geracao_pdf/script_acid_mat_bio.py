from pdfWritter import PDFWriter
pdf = 'fichas/completas/Acid Exp Mat Biológico_1.geracao_pdf'
document = PDFWriter(pdf)

notificatoria = {
    "numero_ficha": "abcdefg",
    "tipo_notificacao": "abcdefg",
    "agravoDoenca": "abcdefg",
    "dt_notificacao": "15/02/2022",
    "uf_notificacao": "PI",
    "municipio_notificacao": "abcdefg",
    "cod_ibge_notificacao": "123456",
    "unidade_saude": "abcdefg",
    "cod_unidade_saude": "123456",
    "dt_sintomas": "15/02/2022",
    "nome_paciente": "abcdefg",
    "dt_nascimento": "15/02/2022",
    "idade": "abcdefg",
    "tipo_idade": "abcdefg",
    "sexo": "abcdefg",
    "gestante": "abcdefg",
    "raca": "abcdefg",
    "escolaridade": "abcdefg",
    "numero_sus": "abcdefg",
    "nome_mae": "abcdefg",
    "dt_primeiro_sintoma": "15/02/2022",
    "numero_casos_suspeitos": "abcdefg",
    "local_inicial_ocorrencia": "abcdefg",
    "local_inicial_ocorrencia_outro": "abcdefg",
    "uf_residencia": "PI",
    "municipio_residencia": "abcdefg",
    "cod_ibge_residencia": "123456",
    "distrito_residencia": "abcdefg",
    "bairro_residencia": "abcdefg",
    "logradouro_residencia": "abcdefg",
    "codigo_residencia": "123456",
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
    "dt_amostra_sorologia": "15/02/2022",
    "dt_outra_amostra": "15/02/2022",
    "tipo_exame": "abcdefg",
    "obito": "abcdefg",
    "caso_semelhante": "abcdefg",
    "exantema": "abcdefg",
    "dt_inicio_exantema": "15/02/2022",
    "petequiaSufusao": "PI",
    "liquor": "abcdefg",
    "bacterioscopia": "abcdefg",
    "tomou_vacina": "abcdefg",
    "dt_ultima_dose_tomada": "15/02/2022",
    "hospitalizacao": "abcdefg",
    "dt_hospitalizacao": "15/02/2022",
    "uf_hospital": "PI",
    "municipio_hospital": "abcdefg",
    "cod_ibge_hospital": "123456",
    "nome_hospital": "abcdefg",
    "cod_hospital": "123456",
    "hipotese_diagnostica1": "abcdefg",
    "hipotese_diagnostica2": "abcdefg",
    "pais_infeccao": "abcdefg",
    "distrito_infeccao": "abcdefg",
    "uf_infeccao": "PI",
    "municipio_infeccao": "abcdefg",
    "bairro_infeccao": "abcdefg"
}
especifico = {
    "numero_ficha2": "abcdefg",
    "dt_notificacao2": "15/02/2022",
    "uf_notificacao2": "PI",
    "municipio_notificacao2": "abcdefg",
    "cod_ibge_notificacao2": "123456",
    "unidade_saude2": "abcdefg",
    "cod_unidade_saude2": "123456",
    "dt_acidente": "15/02/2022",
    "nome_paciente2": "abcdefg",
    "dt_nascimento2": "15/02/2022",
    "idade2": "25",
    "tipo_idade2": "9",
    "sexo2": "9",
    "gestante2": "9",
    "raca2": "9",
    "escolaridade2": "9",
    "numero_sus2": "12345678985648",
    "nome_mae2": "asdadasd",
    "uf_residencia2": "PI",
    "municipio_residencia2": "abcdefg",
    "cod_ibge_residencia2": "123456",
    "distrito_residencia2": "abcdefg",
    "bairro_residencia2": "abcdefg",
    "logradouro_residencia2": "abcdefg",
    "codigo_residencia2": "123456",
    "numero_residencia2": "abcdefg",
    "complemento_residencia2": "abcdefg",
    "geo_campo1_2": "abcdefg",
    "geo_campo2_2": "abcdefg",
    "ponto_ref_residencia2": "abcdefg",
    "cep_residencia2": "64000000",
    "telefone_residencia2": "86988256784",
    "zona_residencia2": "abcdefg",
    "pais_residencia2": "abcdefg",
    "ocupacao": "abcdefg",
    "sit_merc_trabalho": "99",
    "tempo_trabalho": "99",
    "tipo_tempo_trabalho": "4",
    "cnpj_contratante": "12123123111212",
    "nome_contratante": "abcdefg",
    "ativ_contratante": "abcdefg",
    "uf_contratante": "PI",
    "municipio_contratante": "abcdefg",
    "cod_ibge_contratante": "123456",
    "distrito_contratante": "abcdefg",
    "bairro_contratante": "abcdefg",
    "endereco_contratante": "abcdefg",
    "numero_contratante": "abcdefg",
    "ponto_ref_contratante": "abcdefg",
    "telefone_contratante": "86999999999",
    "empresa_terceirizada": "abcdefg",
    "tp_exp_percutanea": "abcdefg",
    "tp_exp_mucosa": "abcdefg",
    "tp_exp_pele_integra": "abcdefg",
    "tp_exp_pele_nao_integra": "abcdefg",
    "tp_exp_outro": "abcdefg",
    "tp_exp_outro_descricao": "abcdefg",
    "mat_organico": "abcdefg",
    "mat_organico_outro": "abcdefg",
    "circunst_acidente": "abcdefg",
    "agente": "abcdefg",
    "epi_luva": "abcdefg",
    "epi_avental": "abcdefg",
    "epi_oculos": "abcdefg",
    "epi_mascara": "abcdefg",
    "epi_prot_facial": "abcdefg",
    "epi_bota": "abcdefg",
    "sit_vacinal_hepB": "abcdefg",
    "res_exam_anti_hiv": "abcdefg",
    "res_exam_hbsag": "abcdefg",
    "res_exam_anti_hbs": "abcdefg",
    "res_exam_anti_hcv": "abcdefg",
    "paciente_ft_conhecida": "abcdefg",
    "teste_anti_hiv": "abcdefg",
    "teste_hbsag": "abcdefg",
    "teste_anti_hbs": "abcdefg",
    "teste_anti_hcv": "abcdefg",
    "cond_sem_indicacao": "abcdefg",
    "cond_rec_quimio": "abcdefg",
    "cond_azt_3tc": "abcdefg",
    "cond_azt_indinavir": "abcdefg",
    "cond_azt_nelfinavir": "abcdefg",
    "cond_imuno_hepb": "abcdefg",
    "cond_vac_hepb": "abcdefg",
    "cond_outro_arv": "abcdefg",
    "cond_outro_arv_descricao": "abcdefg",
    "evolucao_caso": "abcdefg",
    "conversao_sorologica": "abcdefg",
    "dt_obito": "15/02/2022",
    "comun_acid_trab": "abcdefg",
    "outras_informacoes": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc.",
    "municipio_us_investigador": "abcdefg",
    "cod_us_investigador": "123456",
    "nome_investigador": "abcdefg",
    "funcao_investigador": "abcdefg",
    "assinatura_investigador": "abcdefg"
}

###################################################
# Dados do paciente
###################################################
document.write_text(especifico['numero_ficha2'],(470, 46))
document.write_date(especifico['dt_notificacao2'], (455, 195), spacing=2) #data_notificacao
document.write_uf(especifico['uf_notificacao2'], (62, 222)) #uf_notificacao
document.write_text(especifico['municipio_notificacao2'], (100, 222)) #municipio_notificacao __unid_saude 55,space=220
document.write_code(especifico['cod_ibge_notificacao2'], (485, 222),space=2) #cod_ibge
document.write_text(especifico['unidade_saude2'], (70, 251)) #cod_unid_saude
document.write_code(especifico['cod_unidade_saude2'], (345, 251),space=2) #cod_unid_saude
document.write_date(especifico['dt_acidente'], (453, 250), spacing=2) #data_diagnostico
##############################################
#####          NOTIFICACAO INDIVIDUAL     ####
##############################################
document.write_text(especifico['nome_paciente2'], (65, 282)) #nome
document.write_date(especifico['dt_nascimento2'], (455, 281),spacing=2) #data_nascimento
document.write_code(especifico['idade2'], (70, 311),space=2) #idade
document.write_mini(especifico['tipo_idade2'], (117, 303)) #tipo_idade
document.write_mini(especifico['sexo2'], (238, 297)) #sexo
document.write_mini(especifico['gestante2'], (433, 297)) #gestante
document.write_mini(especifico['raca2'], (559, 297)) #raça/cor
document.write_mini(especifico['escolaridade2'], (559, 326)) #escolaridade
document.write_code(especifico['numero_sus2'], (63, 371),space=2, font_size=10) #cartao_sus
document.write_text(especifico['nome_mae2'], (250, 371)) #nome_mae
##############################################
#####          DADOS DE RESIDENCIA        ####
##############################################

document.write_uf(especifico['uf_residencia2'], (62, 400)) #uf_residencia
document.write_text(especifico['municipio_residencia2'], (100, 400)) #municipio_residencia
document.write_code(especifico['cod_ibge_residencia2'], (333, 400),space=2) #cod_ibge_residencia
document.write_text(especifico['distrito_residencia2'], (430, 400)) #endereco
document.write_text(especifico['bairro_residencia2'], (70, 425)) #bairro
document.write_text(especifico['logradouro_residencia2'], (210, 425)) #logradouro
document.write_code(especifico['codigo_residencia2'], (485, 426),space=2) #cod_logradouro
document.write_text(especifico['numero_residencia2'], (68, 449)) #numero
document.write_text(especifico['complemento_residencia2'], (120, 449)) #complemento
document.write_text(especifico['geo_campo1_2'], (420, 452)) #geo_campo_1
document.write_text(especifico['geo_campo2_2'], (65, 475)) #geo_campo_2
document.write_text(especifico['ponto_ref_residencia2'], (235, 476)) #ponto_ref
document.write_code(especifico['cep_residencia2'], (462, 478),space=2) #cep
document.write_telefone(especifico['telefone_residencia2'], (63, 502), space=2) #telefone
document.write_mini(especifico['zona_residencia2'], (340, 490)) #zona
document.write_text(especifico['pais_residencia2'], (380, 502)) #pais
###################################################
# Dados complementares                            #
###################################################
document.write_text(especifico['ocupacao'], (70, 553)) #ocupacao
document.write_code(especifico['sit_merc_trabalho'], (241, 569),space=1) #merc_trabalho
document.write_code(especifico['tempo_trabalho'], (460, 605),space=1) #tempo_trabalho
document.write_mini(especifico['tipo_tempo_trabalho'], (507, 604)) #tempo_tipo
document.write_code(especifico['cnpj_contratante'], (62, 654),space=2, font_size=12) #cnpj_cpf
document.write_text(especifico['nome_contratante'], (255, 654)) #nome_empresa_dono
document.write_text(especifico['ativ_contratante'], (70, 680)) #CNAE
document.write_uf(especifico['uf_contratante'], (284, 682)) #uf_empresa
document.write_text(especifico['municipio_contratante'], (320, 682)) #municipio_empresa
document.write_code(especifico['cod_ibge_contratante'], (485, 682),space=2) #ibge_empresa
document.write_text(especifico['distrito_contratante'], (70, 707)) #distrito_empresa
document.write_text(especifico['bairro_contratante'], (230, 707)) #bairro_empresa
document.write_text(especifico['endereco_contratante'], (390, 707)) #endereco
document.write_text(especifico['numero_contratante'], (70, 730)) #numero
document.write_text(especifico['ponto_ref_contratante'], (130, 730)) #ponto_referencia
document.write_telefone(especifico['telefone_contratante'], (431, 732), space=2) #telefone_empresa
document.write_mini(especifico['empresa_terceirizada'], (482, 748)) #tercerizado
###################################################
document.write_mini(especifico['tp_exp_percutanea'], (196, 50),pg=1) #exposicao_percutanea
document.write_mini(especifico['tp_exp_mucosa'], (196, 62),pg=1) #exposicao_mucosa
document.write_mini(especifico['tp_exp_pele_integra'], (304, 49),pg=1) #exposicao_pele_integra
document.write_mini(especifico['tp_exp_pele_nao_integra'], (304, 62),pg=1) #exposicao_pele_n_integra
document.write_mini(especifico['tp_exp_outro'], (421, 48),pg=1) #exposicao_outros
document.write_mini(especifico['tp_exp_outro_descricao'], (459, 45),pg=1) #text_outras
document.write_mini(especifico['mat_organico'], (547, 85),pg=1) #mat_organico
document.write_mini(especifico['mat_organico_outro'], (380, 100),pg=1) #mat_organico_outros
document.write_code(especifico['circunst_acidente'], (539, 121),pg=1,space=1) #cirscunstancia_acid
document.write_mini(especifico['agente'], (546, 250),pg=1) #agente
document.write_mini(especifico['epi_luva'], (71, 307),pg=1) #epi_luva
document.write_mini(especifico['epi_avental'], (130, 306),pg=1) #epi_avental
document.write_mini(especifico['epi_oculos'], (198, 307),pg=1) #epi_oculos
document.write_mini(especifico['epi_mascara'], (270, 306),pg=1) #epi_mascara
document.write_mini(especifico['epi_prot_facial'], (356, 306),pg=1) #epi_protecao_facial
document.write_mini(especifico['epi_bota'], (470, 308),pg=1) #epi_bota
document.write_mini(especifico['sit_vacinal_hepB'], (271, 334),pg=1) #situacao_vacinal
document.write_mini(especifico['res_exam_anti_hiv'], (295, 356),pg=1) #res_anti_hiv
document.write_mini(especifico['res_exam_hbsag'], (354, 356),pg=1) #res_anti_hbsag
document.write_mini(especifico['res_exam_anti_hbs'], (426, 357),pg=1) #res_anti_hbs
document.write_mini(especifico['res_exam_anti_hcv'], (493, 356),pg=1) #res_anti_hcv
document.write_mini(especifico['paciente_ft_conhecida'], (284, 377),pg=1) #paciente_fonte_conhecida
document.write_mini(especifico['teste_hbsag'], (329, 397),pg=1) #res_soro_hbsag
document.write_mini(especifico['teste_anti_hiv'], (329, 413),pg=1) #res_soro_anti_hiv
document.write_mini(especifico['teste_anti_hbs'], (450, 397),pg=1) #res_soro_anti_hbc trocou o c por s
document.write_mini(especifico['teste_anti_hcv'], (451, 412),pg=1) #res_soro_anti_hcv
document.write_mini(especifico['cond_sem_indicacao'], (65, 446),pg=1) #conduta_quimioprofilaxia
document.write_mini(especifico['cond_rec_quimio'], (65, 461),pg=1) #conduta_neg_quimioprofilaxia
document.write_mini(especifico['cond_azt_3tc'], (65, 478),pg=1) #conduta_azt_3tc
document.write_mini(especifico['cond_azt_indinavir'], (241, 445),pg=1) #conduta_azt_3tc_indinavir
document.write_mini(especifico['cond_azt_nelfinavir'], (241, 466),pg=1) #conduta_azt_3tc_nelfivanir
document.write_mini(especifico['cond_imuno_hepb'], (241, 486),pg=1) #conduta_hbig
document.write_mini(especifico['cond_vac_hepb'], (394, 445),pg=1) #conduta_vacina_hep_b
document.write_mini(especifico['cond_outro_arv'], (393, 468),pg=1) #conduta_outros
document.write_mini(especifico['cond_outro_arv_descricao'], (449, 470),pg=1) #conduta_text
document.write_mini(especifico['evolucao_caso'], (552, 505),pg=1) #evolucao_caso
document.write_mini(especifico['conversao_sorologica'], (248, 519),pg=1) #virus_espec
document.write_date(especifico['dt_obito'], (66, 573),pg=1, spacing=2) #dt_obito
document.write_mini(especifico['comun_acid_trab'], (548, 560),pg=1) #emitido_comun_trab
document.write_box(especifico['outras_informacoes'],pg=1, rect=(30, 600, 560, 740)) #obs
document.write_text(especifico['municipio_us_investigador'], (59, 765),pg=1) #municipio_investigador
document.write_code(especifico['cod_us_investigador'], (464, 764),pg=1,space=2) #cod_unid_saude
document.write_text(especifico['nome_investigador'], (59, 792),pg=1) #nome_investigador
document.write_text(especifico['funcao_investigador'], (260, 792),pg=1) #funcao_investigador
document.write_text(especifico['assinatura_investigador'], (470, 792),pg=1) #asign_investigador


document.save('acidente_material_biologico.geracao_pdf', notificatoria)