from pdfWritter import PDFWriter
pdf = 'fichas/prioridades/MENINGITE1.pdf'
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
    "agravoDoenca_num": "9",
    "dt_notificacao2": "15/02/2022",
    "uf_notificacao2": "PI",
    "municipio_notificacao2": "observacao",
    "cod_ibge_notificacao2": "123456",
    "unidade_saude2": "25",
    "cod_unidade_saude2": "123456",
    "dt_sintomas2": "15/02/2022",
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
    "dt_investigacao": "15/02/2022",
    "ocupacao": "observacao",
    "vac_poli_ac": "9",
    "quant_poli_ac": "99",
    "dt_poli_ac": "15/02/2022",
    "vac_poli_bc": "9",
    "quant_poli_bc": "99",
    "dt_poli_bc": "15/02/2022",
    "vac_conju": "9",
    "quant_conju": "99",
    "dt_conju": "15/02/2022",
    "vac_bcg": "9",
    "quant_bcg": "99",
    "dt_bcg": "15/02/2022",
    "vac_triplice": "9",
    "quant_triplice": "99",
    "dt_triplice": "15/02/2022",
    "vac_hemo": "9",
    "quant_hemo": "99",
    "dt_hemo": "15/02/2022",
    "vac_pneumo": "9",
    "quant_pneumo": "99",
    "dt_pneumo": "15/02/2022",
    "vac_outro": "9",
    "quant_outro": "99",
    "dt_outro": "15/02/2022",
    "doenca_aids": "9",
    "doenca_trauma": "9",
    "doenca_imunos": "9",
    "doenca_infeccao": "9",
    "doenca_ira": "9",
    "doenca_tuberc": "9",
    "doenca_outro": "9",
    "doenca_outro_descricao": "observacao",
    "contat_caso_susp": "9",
    "nome_contat_susp": "joao maria",
    "telefone_contat_susp": "86988889999",
    "endereco_contat_susp": "rua 30 esquina 20",
    "caso_secundario": "9",
    "sint_cefaleia": "9",
    "sint_febre": "9",
    "sint_vomito": "9",
    "sint_convulsao": "9",
    "sint_rig_nuca": "9",
    "sint_kernig": "9",
    "sint_fontanela": "9",
    "sint_coma": "9",
    "sint_petequias": "9",
    "sint_outro": "9",
    "sint_outro_descricao": "observacao",
    "hospitalizacao2": "9",
    "dt_internacao": "15/02/2022",
    "uf_hospital2": "PI",
    "municipio_hospital2": "observacao",
    "cod_ibge_hospital2": "123456",
    "nome_hospital2": "observacao",
    "cod_hospital2": "123456",
    "puncao_lombar": "9",
    "dt_puncao": "15/02/2022",
    "aspecto_liquor": "9",
    "cult_liquor": "observacao",
    "cult_lesao": "observacao",
    "cult_sangue": "observacao",
    "cult_escarro": "observacao",
    "bac_liquor": "observacao",
    "bac_lesao": "observacao",
    "bac_sangue": "observacao",
    "bac_escarro": "observacao",
    "cie_liquor": "observacao",
    "cie_sangue": "observacao",
    "agl_liquor": "observacao",
    "agl_sangue": "observacao",
    "iso_liquor": "observacao",
    "iso_fezes": "observacao",
    "pcr_liquor": "observacao",
    "pcr_lesao": "observacao",
    "pcr_sangue": "observacao",
    "pcr_escarro": "observacao",
    "classif_caso": "9",
    "especif_confirm": "99",
    "mening_bacterias": "alguma coisa",
    "mening_assept": "alguma coisa",
    "mening_otr_etiologia": "alguma coisa",
    "criterio_confirm": "99",
    "n_mening": "99",
    "n_comun": "99",
    "quimiop_comun": "9",
    "dt_quimiop_comun": "15/02/2022",
    "doenca_rel_trab": "9",
    "evolucao_caso": "9",
    "dt_evolucao": "15/02/2022",
    "dt_encerramento": "15/02/2022",
    "quimioc_hema": "observacao",
    "quimioc_neut": "observacao",
    "quimio_glicose": "observacao",
    "quimioc_leuc": "observacao",
    "quimioc_eosin": "observacao",
    "quimioc_prot": "observacao",
    "quimioc_mono": "observacao",
    "quimioc_linf": "observacao",
    "quimio_cloreto": "observacao",
    "obs_adicionais": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc. Sed euismod, urna id aliquet tristique, nunc nisl ultrices ipsum, nec lacinia nisl nunc a nunc.",
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
doc.write_date(especifico['dt_notificacao2'], (449, 153), spacing=2) #data_notificacao
doc.write_uf(especifico['uf_notificacao2'], (58, 183)) #uf_notificacao
doc.write_text(especifico['municipio_notificacao2'], (90, 184)) #municipio_notificacao __unid_saude 55,220
doc.write_code(especifico['cod_ibge_notificacao2'], (483, 184),space=2) #cod_ibge
doc.write_text(especifico['unidade_saude2'], (65, 213)) #cod_unid_saude
doc.write_code(especifico['cod_unidade_saude2'], (342, 213),space=2) #cod_unid_saude
doc.write_date(especifico['dt_sintomas2'], (449, 212), spacing=2) #data_diagnostico
##############################################
#####          NOTIFICACAO INDIVIDUAL     ####
##############################################
doc.write_text(especifico['nome_paciente2'], (58, 243)) #nome
doc.write_date(especifico['dt_nascimento2'], (452, 242), spacing=2) #data_nascimento
doc.write_code(especifico['idade2'], (68, 272),space=2) #idade
doc.write_mini(especifico['tipo_idade2'], (114, 265)) #tipo_idade
doc.write_mini(especifico['sexo2'], (237, 258)) #sexo
doc.write_mini(especifico['gestante2'], (432, 258)) #gestante
doc.write_mini(especifico['raca2'], (557, 259)) #raça/cor
doc.write_mini(especifico['escolaridade2'], (557, 288)) #escolaridade
doc.write_code(especifico['numero_sus2'], (60, 333),space=2, font_size=10) #cartao_sus
doc.write_text(especifico['nome_mae2'], (240, 332)) #nome_mae
##############################################
#####          DADOS DE RESIDENCIA        ####
##############################################

doc.write_uf(especifico['uf_residencia2'], (59, 362)) #uf_residencia
doc.write_text(especifico['municipio_residencia2'], (95, 361)) #municipio_residencia
doc.write_code(especifico['cod_ibge_residencia2'], (329, 361),space=2) #cod_ibge_residencia
doc.write_text(especifico['distrito_residencia2'], (422, 361)) #endereco
doc.write_text(especifico['bairro_residencia2'], (64, 386)) #bairro
doc.write_text(especifico['logradouro_residencia2'], (210, 388)) #logradouro
doc.write_code(especifico['codigo_residencia2'], (483, 388),space=2) #cod_logradouro
doc.write_text(especifico['numero_residencia2'], (65, 411)) #numero
doc.write_text(especifico['complemento_residencia2'], (120, 411)) #complemento
doc.write_text(especifico['geo_campo1_2'], (415, 413)) #geo_campo_1
doc.write_text(especifico['geo_campo2_2'], (58, 436)) #geo_campo_2
doc.write_text(especifico['ponto_ref_residencia2'], (230, 437)) #ponto_ref
doc.write_code(especifico['cep_residencia2'], (458, 439),space=2) #cep
doc.write_telefone(especifico['telefone_residencia2'], (58, 464), space=2) #telefone
doc.write_mini(especifico['zona_residencia2'], (336, 451)) #zona
doc.write_text(especifico['pais_residencia2'], (368, 463)) #pais
##############################################
#####        DADOS  COMPLEMENTARES        ####
##############################################
doc.write_date(especifico['dt_investigacao'], (63, 514), spacing=2) #data_investigacao
doc.write_text(especifico['ocupacao'], (185, 514)) #ocupacao
doc.write_mini(especifico['vac_poli_ac'], (114, 542)) #vac_poli_ac
doc.write_code(especifico['quant_poli_ac'], (187, 542), space=1) #quant_poli_ac
doc.write_date(especifico['dt_poli_ac'], (222, 542), spacing=2) #dt_poli_ac
doc.write_mini(especifico['vac_poli_bc'], (114, 562)) #vac_poli_bc
doc.write_code(especifico['quant_poli_bc'], (187, 562), space=1) #quant_poli_bc
doc.write_date(especifico['dt_poli_bc'], (222, 562), spacing=2) #dt_poli_bc
doc.write_mini(especifico['vac_conju'], (114, 581)) #vac_conju
doc.write_code(especifico['quant_conju'], (187, 581), space=1) #quant_conju
doc.write_date(especifico['dt_conju'], (222, 581), spacing=2) #dt_conju
doc.write_mini(especifico['vac_bcg'], (114, 601)) #vac_bcg
doc.write_code(especifico['quant_bcg'], (187, 601), space=1) #quant_bcg
doc.write_date(especifico['dt_bcg'], (222, 601), spacing=2) #dt_bcg
doc.write_mini(especifico['vac_triplice'], (350, 540)) #vac_triplice
doc.write_code(especifico['quant_triplice'], (415, 541), space=1) #quant_triplice
doc.write_date(especifico['dt_triplice'], (450, 541), spacing=2) #dt_triplice
doc.write_mini(especifico['vac_hemo'], (350, 563)) #vac_hemo
doc.write_code(especifico['quant_hemo'], (415, 563), space=1) #quant_hemo
doc.write_date(especifico['dt_hemo'], (450, 563), spacing=2) #dt_hemo
doc.write_mini(especifico['vac_pneumo'], (350, 583)) #vac_pneumo
doc.write_code(especifico['quant_pneumo'], (415, 584), space=1) #quant_pneumo
doc.write_date(especifico['dt_pneumo'], (450, 584), spacing=2) #dt_pneumo
doc.write_mini(especifico['vac_outro'], (349, 602)) #vac_outro
doc.write_mini(especifico['quant_outro'], (382, 603)) #quant_outro
doc.write_date(especifico['dt_outro'], (448, 603), spacing=2) #dt_outro
doc.write_mini(especifico['doenca_aids'], (80, 643)) #doenca_aids
doc.write_mini(especifico['doenca_trauma'], (80, 657)) #doenca_trauma
doc.write_mini(especifico['doenca_imunos'], (166, 641)) #doenca_imunos
doc.write_mini(especifico['doenca_infeccao'], (166, 659)) #doenca_infeccao
doc.write_mini(especifico['doenca_ira'], (333, 643)) #doenca_ira
doc.write_mini(especifico['doenca_tuberc'], (402, 643)) #doenca_tuberc
doc.write_mini(especifico['doenca_outro'], (287, 657)) #doenca_outro
doc.write_mini(especifico['doenca_outro_descricao'], (320, 657)) #doenca_outro_descricao
doc.write_mini(especifico['contat_caso_susp'], (555, 683)) #contat_caso_susp
doc.write_text(especifico['nome_contat_susp'], (65, 729)) #nome_contat_susp
doc.write_telefone(especifico['telefone_contat_susp'], (442, 729), space=2, font_size=12) #telefone_contat_susp
doc.write_text(especifico['endereco_contat_susp'], (65, 755)) #endereco_contat_susp
doc.write_mini(especifico['caso_secundario'], (552, 745)) #caso_secundario
doc.write_mini(especifico['sint_cefaleia'], (180, 769)) #sint_cefaleia
doc.write_mini(especifico['sint_febre'], (180, 784)) #sint_febre
doc.write_mini(especifico['sint_vomito'], (227, 769)) #sint_vomito
doc.write_mini(especifico['sint_convulsao'], (227, 784)) #sint_convulsao
doc.write_mini(especifico['sint_rig_nuca'], (282, 769)) #sint_rig_nuca
doc.write_mini(especifico['sint_kernig'], (282, 784)) #sint_kernig
doc.write_mini(especifico['sint_fontanela'], (361, 769)) #sint_fontanela
doc.write_mini(especifico['sint_coma'], (361, 784)) #sint_coma
doc.write_mini(especifico['sint_petequias'], (426, 769)) #sint_petequias
doc.write_mini(especifico['sint_outro'], (426, 784)) #sint_outro
doc.write_mini(especifico['sint_outro_descricao'], (464, 781)) #sint_outro_descricao
####################### fim da pagina 1 ############################
doc.write_mini(especifico['hospitalizacao2'], (154, 47), pg=1) #hospitalizacao
doc.write_date(especifico['dt_internacao'], (180, 57), spacing=2, pg=1) #dt_internacao
doc.write_uf(especifico['uf_hospital2'], (301, 57), pg=1) #uf_hospital
doc.write_text(especifico['municipio_hospital2'], (335, 57), pg=1) #municipio_hospital
doc.write_code(especifico['cod_ibge_hospital2'], (481, 57),space=2, pg=1) #cod_ibge_hospital
doc.write_text(especifico['nome_hospital2'], (60, 84), pg=1) #nome_hospital
doc.write_code(especifico['cod_hospital2'], (463, 84),space=2, pg=1) #cod_hospital
doc.write_mini(especifico['puncao_lombar'], (158, 104), pg=1) #puncao_lombar
doc.write_date(especifico['dt_puncao'], (181, 116), spacing=2, pg=1) #dt_puncao
doc.write_mini(especifico['aspecto_liquor'], (551, 103), pg=1) #aspecto_liquor
doc.write_text(especifico['cult_liquor'], (118, 158), pg=1) #cult_liquor
doc.write_text(especifico['cult_lesao'], (118, 174), pg=1) #cult_lesao
doc.write_text(especifico['cult_sangue'], (118, 190), pg=1) #cult_sangue
doc.write_text(especifico['cult_escarro'], (118, 206), pg=1) #cult_escarro
doc.write_text(especifico['bac_liquor'], (118, 234), pg=1) #bac_liquor
doc.write_text(especifico['bac_lesao'], (118, 250), pg=1) #bac_lesao
doc.write_text(especifico['bac_sangue'], (118, 266), pg=1) #bac_sangue
doc.write_text(especifico['bac_escarro'], (118, 282), pg=1) #bac_escarro
doc.write_text(especifico['cie_liquor'], (291, 158), pg=1) #cie_liquor
doc.write_text(especifico['cie_sangue'], (291, 176), pg=1) #cie_sangue
doc.write_text(especifico['agl_liquor'], (291, 204), pg=1) #agl_liquor
doc.write_text(especifico['agl_sangue'], (291, 222), pg=1) #agl_sangue
doc.write_text(especifico['iso_liquor'], (280, 249), pg=1) #iso_liquor
doc.write_text(especifico['iso_fezes'], (280, 265), pg=1) #iso_fezes
doc.write_text(especifico['pcr_liquor'], (465, 162), pg=1) #pcr_liquor
doc.write_text(especifico['pcr_lesao'], (465, 178), pg=1) #pcr_lesao
doc.write_text(especifico['pcr_sangue'], (465, 194), pg=1) #pcr_sangue
doc.write_text(especifico['pcr_escarro'], (465, 211), pg=1) #pcr_escarro
doc.write_mini(especifico['classif_caso'], (135, 310), pg=1) #classif_caso
doc.write_code(especifico['especif_confirm'], (535, 316), pg=1, space=1) #especif_confirm
doc.write_mini(especifico['mening_bacterias'], (289, 367), pg=1) #mening_bacterias
doc.write_mini(especifico['mening_assept'], (447, 327), pg=1) #mening_assept
doc.write_mini(especifico['mening_otr_etiologia'], (473, 340), pg=1) #mening_otr_etiologia
doc.write_code(especifico['criterio_confirm'], (345, 386), pg=1, space=1) #criterio_confirm
doc.write_code(especifico['n_mening'], (525, 420), pg=1,space=1) #n_mening
doc.write_code(especifico['n_comun'], (78, 461), pg=1, space=1) #n_comun
doc.write_mini(especifico['quimiop_comun'], (282, 444), pg=1) #quimiop_comun
doc.write_date(especifico['dt_quimiop_comun'], (318, 460), spacing=2, pg=1) #dt_quimiop_comun
doc.write_mini(especifico['doenca_rel_trab'], (545, 445), pg=1) #doenca_rel_trab
doc.write_mini(especifico['evolucao_caso'], (300, 480), pg=1) #evolucao_caso
doc.write_date(especifico['dt_evolucao'], (327, 497), spacing=2, pg=1) #dt_evolucao
doc.write_date(especifico['dt_encerramento'], (452, 497), spacing=2, pg=1) #dt_encerramento
doc.write_text(especifico['quimioc_hema'], (108, 552), pg=1) #quimioc_hema
doc.write_text(especifico['quimioc_neut'], (108, 573), pg=1) #quimioc_neut
doc.write_text(especifico['quimio_glicose'], (108, 593), pg=1) #quimio_glicose
doc.write_text(especifico['quimioc_leuc'], (280, 552), pg=1) #quimioc_leuc
doc.write_text(especifico['quimioc_eosin'], (280, 572), pg=1) #quimioc_eosin
doc.write_text(especifico['quimioc_prot'], (280, 593), pg=1) #quimioc_prot
doc.write_text(especifico['quimioc_mono'], (465, 551), pg=1) #quimioc_mono
doc.write_text(especifico['quimioc_linf'], (465, 572), pg=1) #quimioc_linf
doc.write_text(especifico['quimio_cloreto'], (465, 592), pg=1) #quimio_cloreto
doc.write_box(especifico['obs_adicionais'], rect=(30, 650,568,736), pg=1) #obs_adicionais
doc.write_text(especifico['municipio_us_investigador'], (60, 765), pg=1) #municipio_us_investigador
doc.write_code(especifico['cod_us_investigador'], (470, 765),space=2, pg=1) #cod_us_investigador
doc.write_text(especifico['nome_investigador'], (60, 794), pg=1) #nome_investigador
doc.write_text(especifico['funcao_investigador'], (258, 794), pg=1) #funcao_investigador
doc.write_text(especifico['assinatura_investigador'], (470, 794), pg=1) #assinatura_investigador
















doc.save('meningite.pdf')