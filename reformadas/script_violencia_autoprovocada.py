from pdfWritter import PDFWriter

pdf = 'violencia_interpessoal_autoprovocada.pdf'
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
    "unid_notif_num": "9",
    "nome_unid_notif": "observacao",
    "cod_unid_notif": "123456",
    "unid_saude": "observacao",
    "cod_cnes_us": "123456",
    "dt_violencia": "15/02/2022",
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
    "nome_social": "observacao",
    "ocupacao": "observacao",
    "sit_conjugal": "9",
    "orient_sexual": "9",
    "ident_genero": "9",
    "possui_def": "9",
    "def_fisica": "9",
    "def_intel": "9",
    "def_visual": "9",
    "def_audi": "9",
    "def_mental": "9",
    "def_comport": "9",
    "def_outra": "9",
    "def_outra_descricao": "observacao",
    "uf_ocorr": "PI",
    "municipio_ocorr": "observacao",
    "cod_ibge_ocorr": "123456",
    "distrito_ocorr": "observacao",
    "bairro_ocorr": "observacao",
    "logradouro_ocorr": "observacao",
    "codigo_ocorr": "123456",
    "numero_ocorr": "15485",
    "complemento_ocorr": "observacao",
    "geocampo3": "observacao",
    "geocampo4": "observacao",
    "ponto_ref_ocorr": "observacao",
    "zona_ocorr": "9",
    "hora_ocorr": "observacao",
    "loc_ocorr_num": "9",
    "loc_ocorr_outro": "observacao",
    "ocorr_outras_vezes": "9",
    "lesao_autoprov": "9",
    "motiv_violencia": "9",
    "motiv_violencia_outro": "observacao",
    "viol_fisica": "9",
    "viol_psico": "9",
    "viol_tort": "9",
    "viol_sexual": "9",
    "viol_traf": "9",
    "viol_finan": "9",
    "viol_negli": "9",
    "viol_trab": "9",
    "viol_inter": "9",
    "viol_outro": "9",
    "viol_outro_descricao": "observacao",
    "agress_espanc": "9",
    "agress_enforc": "9",
    "agress_contund": "9",
    "agress_perfuro": "9",
    "agress_subst": "9",
    "agress_intox": "9",
    "agress_arma": "9",
    "agress_ameaca": "9",
    "agress_outro": "9",
    "agress_outro_descricao": "observacao",
    "vio_sex_assedio": "9",
    "vio_sex_estupro": "9",
    "vio_sex_porno": "9",
    "vio_sex_explora": "9",
    "vio_sex_outros": "9",
    "vio_sex_outros_descricao": "observacao",
    "proced_dst": "9",
    "proced_hiv": "9",
    "proced_hepB": "9",
    "proced_sangue": "9",
    "proced_semen": "9",
    "proced_vaginal": "9",
    "proced_contra": "9",
    "proced_aborto": "9",
    "num_envolvidos": "9",
    "grau_pai": "9",
    "grau_mae": "9",
    "grau_padr": "9",
    "grau_madr": "9",
    "grau_conj": "9",
    "grau_ex_conj": "9",
    "grau_namor": "9",
    "grau_ex_namor": "9",
    "grau_filho": "9",
    "grau_irmao": "9",
    "grau_amigos": "9",
    "grau_desco": "9",
    "grau_cuida": "9",
    "grau_chefe": "9",
    "grau_pessoa": "9",
    "grau_policia": "9",
    "grau_proprio": "9",
    "grau_outro": "9",
    "grau_outro_descricao": "observacao",
    "sexo_autor": "9",
    "uso_alcool": "9",
    "ciclo_autor": "9",
    "enca_saude": "9",
    "enca_social": "9",
    "enca_educa": "9",
    "enca_rede_mulher": "9",
    "enca_tutelar": "9",
    "enca_cons_idoso": "9",
    "enca_del_idoso": "9",
    "enca_dir_humano": "9",
    "enca_ministerio": "9",
    "enca_del_crianca": "9",
    "enca_del_mulher": "9",
    "enca_outra_del": "9",
    "enca_jus_infancia": "9",
    "enca_def_publica": "9",
    "doenca_rel_trab": "9",
    "comun_acid_trab": "9",
    "circunst_lesao": "observacao",
    "dt_encerramento": "15/02/2022",
    "nome_acompanha": "observacao",
    "vinculo_acompanha": "observacao",
    "telefone_acompanha": "86999999999",
    "obs_adicionais": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc.",
    "municipio_us_investigador": "observacao",
    "cod_us_investigador": "123456",
    "nome_investigador": "observacao",
    "funcao_investigador": "observacao",
    "assinatura_investigador": "observacao"
}






###################################################
# Dados do paciente
###################################################
doc.write_text(especifico['numero_ficha2'],(470, 47))
doc.write_date(especifico['dt_notificacao2'], (446, 146), spacing=2) #data_notificacao
doc.write_uf(especifico['uf_notificacao2'], (56, 168)) #uf_notificacao
doc.write_text(especifico['municipio_notificacao2'], (90, 168)) #municipio_notificacao __unid_saude 55,space=220
doc.write_code(especifico['cod_ibge_notificacao2'], (478, 166),space=2) #cod_ibge
doc.write_mini(especifico['unid_notif_num'], (149, 180)) #unidade_notificacao
doc.write_text(especifico['nome_unid_notif'], (70, 210)) #nome_unidade_notificacao
doc.write_code(especifico['cod_unid_notif'], (335, 210)) #cod_unidade_notificacao
doc.write_text(especifico['unid_saude'], (70, 231)) #unidade_saude
doc.write_code(especifico['cod_cnes_us'], (337, 231), space=2) #cod_cnes
doc.write_date(especifico['dt_violencia'], (446, 221), spacing=2) #data_violencia
##############################################
#####          NOTIFICACAO INDIVIDUAL     ####
##############################################
doc.write_text(especifico['nome_paciente2'], (65, 253)) #nome
doc.write_date(especifico['dt_nascimento2'], (450, 251), spacing=2) #data_nascimento
doc.write_code(especifico['idade2'], (65, 282),space=2) #idade
doc.write_mini(especifico['tipo_idade2'], (111, 274)) #tipo_idade
doc.write_mini(especifico['sexo2'], (233, 267)) #sexo
doc.write_mini(especifico['gestante2'], (420, 267)) #gestante
doc.write_mini(especifico['raca2'], (553, 268)) #raça/cor
doc.write_mini(especifico['escolaridade2'], (554, 297)) #escolaridade
doc.write_code(especifico['numero_sus2'], (51, 342),space=2, font_size=11) #cartao_sus
doc.write_text(especifico['nome_mae2'], (240, 341)) #nome_mae
##############################################
#####          DADOS DE RESIDENCIA        ####
##############################################

doc.write_uf(especifico['uf_residencia2'], (57, 370)) #uf_residencia
doc.write_text(especifico['municipio_residencia2'], (100, 372)) #municipio_residencia
doc.write_code(especifico['cod_ibge_residencia2'], (328, 371),space=2) #cod_ibge_residencia
doc.write_text(especifico['distrito_residencia2'], (430, 371)) #endereco
doc.write_text(especifico['bairro_residencia2'], (70, 396)) #bairro
doc.write_text(especifico['logradouro_residencia2'], (210, 398)) #logradouro
doc.write_code(especifico['codigo_residencia2'], (481, 397),space=2) #cod_logradouro
doc.write_text(especifico['numero_residencia2'], (66, 419)) #numero
doc.write_text(especifico['complemento_residencia2'], (120, 420)) #complemento
doc.write_text(especifico['geo_campo1_2'], (420, 421)) #geo_campo_1
doc.write_text(especifico['geo_campo2_2'], (63, 445)) #geo_campo_2
doc.write_text(especifico['ponto_ref_residencia2'], (232, 447)) #ponto_ref
doc.write_code(especifico['cep_residencia2'], (461, 448),space=2, font_size=12) #cep
doc.write_telefone(especifico['telefone_residencia2'], (58, 472), space=2) #telefone
doc.write_mini(especifico['zona_residencia2'], (334, 460)) #zona
doc.write_text(especifico['pais_residencia2'], (365, 473)) #pais
###################################################
# Dados Complementares _ Ficha de Investigação    #
###################################################
doc.write_text(especifico['nome_social'], (65, 515)) #nome_social
doc.write_text(especifico['ocupacao'], (370, 515)) #ocupacao
doc.write_mini(especifico['sit_conjugal'], (550, 537)) #situacao_conjugal
doc.write_mini(especifico['orient_sexual'], (291, 565)) #orientacao_sexual
doc.write_mini(especifico['ident_genero'], (552, 566)) #identidade_genero
doc.write_mini(especifico['possui_def'], (170, 598)) #possui_deficiencia

doc.write_mini(especifico['def_fisica'],(198, 607))
doc.write_mini(especifico['def_intel'],(198, 619))
doc.write_mini(especifico['def_visual'],(295, 608))
doc.write_mini(especifico['def_audi'],(295, 619))
doc.write_mini(especifico['def_mental'],(389, 608))
doc.write_mini(especifico['def_comport'],(389, 620))
doc.write_mini(especifico['def_outra'],(475, 609))

doc.write_text(especifico['def_outra_descricao'], (510, 607))

doc.write_uf(especifico['uf_ocorr'], (59, 650)) #uf_ocorrencia
doc.write_text(especifico['municipio_ocorr'], (100, 650)) #municipio_ocorrencia
doc.write_code(especifico['cod_ibge_ocorr'], (328, 650),space=2) #cod_ibge_ocorrencia
doc.write_text(especifico['distrito_ocorr'], (430, 650)) #distrito_ocorrencia
doc.write_text(especifico['bairro_ocorr'], (70, 675)) #bairro_ocorrencia
doc.write_text(especifico['logradouro_ocorr'], (210, 675)) #logradouro_ocorrencia
doc.write_code(especifico['codigo_ocorr'], (483, 677),space=2) #cod_logradouro_ocorrencia
doc.write_text(especifico['numero_ocorr'], (66, 700)) #numero_ocorrencia
doc.write_text(especifico['complemento_ocorr'], (120, 700)) #complemento_ocorrencia
doc.write_text(especifico['geocampo3'], (310, 700)) #geo_campo_1_ocorrencia
doc.write_text(especifico['geocampo4'], (430, 700)) #geo_campo_2_ocorrencia
doc.write_text(especifico['ponto_ref_ocorr'], (63, 725)) #ponto_ref_ocorrencia
doc.write_mini(especifico['zona_ocorr'], (334, 713)) #zona_ocorrencia
doc.write_hrmin(especifico['hora_ocorr'], (494, 725), space=2) #hora_ocorrencia
doc.write_code(especifico['loc_ocorr_num']+'9', (380, 740), space=2) #local_ocorrencia
doc.write_text(especifico['loc_ocorr_outro'], (317, 761)) #local_ocorrencia_outro
doc.write_mini(especifico['ocorr_outras_vezes'], (555, 737)) #ocorrencia_outras_vezes
doc.write_mini(especifico['lesao_autoprov'], (554, 764)) #lesao_autoprovocada

#*=========================== fim pagina 1 ===========================*#
doc.write_code(especifico['motiv_violencia'], (543, 62),space=2, pg=1) #motivacao_violencia
#! campos 56
doc.write_mini(especifico['viol_fisica'],(70, 95), pg=1) #fisica
doc.write_mini(especifico['viol_psico'],(70, 109), pg=1) #psicologica
doc.write_mini(especifico['viol_tort'],(70, 121), pg=1) #tortura
doc.write_mini(especifico['viol_sexual'],(70, 134), pg=1) #sexual
doc.write_mini(especifico['viol_traf'],(155, 95), pg=1) #trafico
doc.write_mini(especifico['viol_finan'],(155, 109), pg=1) #financeira
doc.write_mini(especifico['viol_negli'],(155, 121), pg=1) #negligencia
doc.write_mini(especifico['viol_trab'],(155, 134), pg=1) #trabalho
doc.write_mini(especifico['viol_inter'],(258, 107), pg=1) #interfamiliar
doc.write_mini(especifico['viol_outro'],(258, 122), pg=1) #outros

doc.write_text(especifico['viol_outro_descricao'], (270, 130), pg=1) #violencia_outro_descricao

#! campo 57
doc.write_mini(especifico['agress_espanc'],(349, 102), pg=1) #espancamento
doc.write_mini(especifico['agress_enforc'],(349, 118), pg=1) #enforcamento
doc.write_mini(especifico['agress_contund'],(349, 134), pg=1) #contundente
doc.write_mini(especifico['agress_perfuro'],(425, 98), pg=1) #perfurocortante
doc.write_mini(especifico['agress_subst'],(425, 114), pg=1) #substancia quente
doc.write_mini(especifico['agress_intox'],(425, 130), pg=1) #intoxicacao
doc.write_mini(especifico['agress_arma'],(498, 99), pg=1) #arma de fogo
doc.write_mini(especifico['agress_ameaca'],(498, 112), pg=1) #ameaca
doc.write_mini(especifico['agress_outro'],(498, 124), pg=1) #outros

doc.write_text(especifico['agress_outro_descricao'], (531, 122), pg=1, font_size=10) #agressao_outro_descricao

#! campo 58
doc.write_mini(especifico['vio_sex_assedio'],(69, 160), pg=1) #assedio
doc.write_mini(especifico['vio_sex_estupro'],(154, 160), pg=1) #estupro
doc.write_mini(especifico['vio_sex_porno'],(233,159),pg=1) #pornografia infantil
doc.write_mini(especifico['vio_sex_explora'],(337,159),pg=1) #exploração sexual
doc.write_mini(especifico['vio_sex_outros'],(440,158),pg=1) #exploração sexual

doc.write_text(especifico['vio_sex_outros_descricao'], (478, 156), pg=1)

#!campo 59
doc.write_mini(especifico['proced_dst'],(70,195),pg=1) #profilaxia dst
doc.write_mini(especifico['proced_hiv'],(70,208),pg=1) #profilaxia hiv
doc.write_mini(especifico['proced_hepB'],(156,195),pg=1) #profilaxia hep b
doc.write_mini(especifico['proced_sangue'],(156,208),pg=1) #coleta de sangue
doc.write_mini(especifico['proced_semen'],(268,194),pg=1) #coleta de semen
doc.write_mini(especifico['proced_vaginal'],(268,207),pg=1) #coleta de segrecao vaginal
doc.write_mini(especifico['proced_contra'],(409,195),pg=1) #contracepção de emergencia
doc.write_mini(especifico['proced_aborto'],(409,208),pg=1) #aborto previsto em lei

#!campo 60
doc.write_mini(especifico['num_envolvidos'],(94, 246), pg=1) #num_envolvidos

#!campo 61
doc.write_mini(especifico['grau_pai'],(119, 238), pg=1) #pai
doc.write_mini(especifico['grau_mae'],(119, 251), pg=1) #mae
doc.write_mini(especifico['grau_padr'],(119, 264), pg=1) #padrasto
doc.write_mini(especifico['grau_madr'],(119, 275), pg=1) #madrasta
doc.write_mini(especifico['grau_conj'],(119, 288), pg=1) #conjuge
doc.write_mini(especifico['grau_ex_conj'],(173, 238), pg=1) #ex_conjuge
doc.write_mini(especifico['grau_namor'],(173, 251), pg=1) #namorado
doc.write_mini(especifico['grau_ex_namor'],(173, 264), pg=1) #ex_namorado
doc.write_mini(especifico['grau_filho'],(173, 275), pg=1) #filho
doc.write_mini(especifico['grau_irmao'],(173, 288), pg=1) #irmao
doc.write_mini(especifico['grau_amigos'],(252, 238), pg=1) #amigos
doc.write_mini(especifico['grau_desco'],(252, 251), pg=1) #desconhecido
doc.write_mini(especifico['grau_cuida'],(252, 264), pg=1) #cuidador
doc.write_mini(especifico['grau_chefe'],(252, 275), pg=1) #chefe
doc.write_mini(especifico['grau_pessoa'],(252, 288), pg=1) #pessoa com relação institucional
doc.write_mini(especifico['grau_policia'],(340, 238), pg=1) #policia
doc.write_mini(especifico['grau_proprio'],(340, 264), pg=1) #proprio
doc.write_mini(especifico['grau_outro'],(340, 276), pg=1) #outro

doc.write_text(especifico['grau_outro_descricao'], (378, 275), pg=1) #grau_outro_descricao

#!campo 62
doc.write_mini(especifico['sexo_autor'],(482, 248), pg=1) #sexo_autor
#!campo 63
doc.write_mini(especifico['uso_alcool'],(552, 245), pg=1) #uso_alcool

#!campo 64
doc.write_mini(especifico['ciclo_autor'],(233, 308), pg=1) #ciclo_violencia

#!campo 65
doc.write_mini(especifico['enca_saude'],(53, 368), pg=1) #saude
doc.write_mini(especifico['enca_social'],(53, 383), pg=1) #social
doc.write_mini(especifico['enca_educa'],(53, 398), pg=1) #educacional
doc.write_mini(especifico['enca_rede_mulher'],(53, 412), pg=1) #rede de mulher
doc.write_mini(especifico['enca_tutelar'],(53, 427), pg=1) #conselho tutelar
doc.write_mini(especifico['enca_cons_idoso'],(286, 363), pg=1) #conselho do idoso
doc.write_mini(especifico['enca_del_idoso'],(286, 378), pg=1) #delegacia do idoso
doc.write_mini(especifico['enca_dir_humano'],(286, 393), pg=1) #direitos humanos
doc.write_mini(especifico['enca_ministerio'],(286, 407), pg=1) #ministerio publico
doc.write_mini(especifico['enca_del_crianca'],(286, 424), pg=1) #delegacia da criança
doc.write_mini(especifico['enca_del_mulher'],(435, 360), pg=1) #delegacia da mulher
doc.write_mini(especifico['enca_outra_del'],(435, 378), pg=1) #outra delegacia
doc.write_mini(especifico['enca_jus_infancia'],(435, 393), pg=1) #justiça da infancia
doc.write_mini(especifico['enca_def_publica'],(435, 411), pg=1) #defensoria publica

#!campo 66
doc.write_mini(especifico['doenca_rel_trab'],(166, 456), pg=1) #doenca_relacionada_trabalho

#!campo 67
doc.write_mini(especifico['comun_acid_trab'],(356, 455), pg=1) #comunicado_acidente_trabalho

#!campo 68
doc.write_code(especifico['circunst_lesao'], (508, 475), pg=1, space=2) #circunstancia_lesao

#!campo 69
doc.write_date(especifico['dt_encerramento'], (57, 515), spacing=2, pg=1) #data_encerramento

doc.write_text(especifico['nome_acompanha'], (35, 560), pg=1) #nome_acompanhante
doc.write_text(especifico['vinculo_acompanha'], (240, 560), pg=1) #vinculo_acompanhante
doc.write_telefone(especifico['telefone_acompanha'], (422, 560), pg=1, space=2) #telefone_acompanhante
doc.write_box(especifico['obs_adicionais'], rect=(29, 575,565,636), pg=1) #observacoes_adicionais
doc.write_text(especifico['municipio_us_investigador'], (57, 706), pg=1) #municipio_investigador,
doc.write_code(especifico['cod_us_investigador'], (453, 706), pg=1, space=2) #codigo_investigador
doc.write_text(especifico['nome_investigador'], (57, 736), pg=1) #nome_investigador
doc.write_text(especifico['funcao_investigador'], (260, 736), pg=1) #funcao_investigador
doc.write_text(especifico['assinatura_investigador'], (465, 736), pg=1) #assinatura_investigador



  

  













doc.save('violencia_interpessoal_autoprovocada.pdf', notificatoria)