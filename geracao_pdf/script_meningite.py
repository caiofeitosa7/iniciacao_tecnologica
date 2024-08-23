from .pdfWritter import PDFWriter


def gerar_pdf_meningite(notificatoriaCSV: dict, dict_especifico: dict, modelo_pdf: str, modelo_pdf_base: str, path_pdf_gerado: str, nome_arquivo: str):
    document = PDFWriter(modelo_pdf)

    ###################################################
    # Dados do paciente
    ###################################################

    document.write_text(dict_especifico['numero_ficha2'],(470, 47))
    document.write_date(dict_especifico['dt_notificacao2'], (449, 153), spacing=2) #data_notificacao
    document.write_uf(dict_especifico['uf_notificacao2'], (58, 183)) #uf_notificacao
    document.write_text(dict_especifico['municipio_notificacao2'], (90, 184)) #municipio_notificacao __unid_saude 55,220
    document.write_code(dict_especifico['cod_ibge_notificacao2'], (483, 184),space=2) #cod_ibge
    document.write_text(dict_especifico['unidade_saude2'], (65, 213)) #cod_unid_saude
    document.write_code(dict_especifico['cod_unidade_saude2'], (342, 213),space=2) #cod_unid_saude
    document.write_date(dict_especifico['dt_sintomas2'], (449, 212), spacing=2) #data_diagnostico
    ##############################################
    #####          NOTIFICACAO INDIVIDUAL     ####
    ##############################################
    document.write_text(dict_especifico['nome_paciente2'], (58, 243)) #nome
    document.write_date(dict_especifico['dt_nascimento2'], (452, 242), spacing=2) #data_nascimento
    document.write_code(dict_especifico['idade2'], (68, 272),space=2) #idade
    document.write_mini(dict_especifico['tipo_idade2'], (114, 265)) #tipo_idade
    document.write_mini(dict_especifico['sexo2'], (237, 258)) #sexo
    document.write_mini(dict_especifico['gestante2'], (432, 258)) #gestante
    document.write_mini(dict_especifico['raca2'], (557, 259)) #raça/cor
    document.write_mini(dict_especifico['escolaridade2'], (557, 288)) #escolaridade
    document.write_code(dict_especifico['numero_sus2'], (60, 333),space=2, font_size=10) #cartao_sus
    document.write_text(dict_especifico['nome_mae2'], (240, 332)) #nome_mae
    ##############################################
    #####          DADOS DE RESIDENCIA        ####
    ##############################################

    document.write_uf(dict_especifico['uf_residencia2'], (59, 362)) #uf_residencia
    document.write_text(dict_especifico['municipio_residencia2'], (95, 361)) #municipio_residencia
    document.write_code(dict_especifico['cod_ibge_residencia2'], (329, 361),space=2) #cod_ibge_residencia
    document.write_text(dict_especifico['distrito_residencia2'], (422, 361)) #endereco
    document.write_text(dict_especifico['bairro_residencia2'], (64, 386)) #bairro
    document.write_text(dict_especifico['logradouro_residencia2'], (210, 388)) #logradouro
    document.write_code(dict_especifico['codigo_residencia2'], (483, 388),space=2) #cod_logradouro
    document.write_text(dict_especifico['numero_residencia2'], (65, 411)) #numero
    document.write_text(dict_especifico['complemento_residencia2'], (120, 411)) #complemento
    document.write_text(dict_especifico['geo_campo1_2'], (415, 413)) #geo_campo_1
    document.write_text(dict_especifico['geo_campo2_2'], (58, 436)) #geo_campo_2
    document.write_text(dict_especifico['ponto_ref_residencia2'], (230, 437)) #ponto_ref
    document.write_code(dict_especifico['cep_residencia2'], (458, 439),space=2) #cep
    document.write_telefone(dict_especifico['telefone_residencia2'], (58, 464), space=2) #telefone
    document.write_mini(dict_especifico['zona_residencia2'], (336, 451)) #zona
    document.write_text(dict_especifico['pais_residencia2'], (368, 463)) #pais
    ##############################################
    #####        DADOS  COMPLEMENTARES        ####
    ##############################################
    document.write_date(dict_especifico['dt_investigacao'], (63, 514), spacing=2) #data_investigacao
    document.write_text(dict_especifico['ocupacao'], (185, 514)) #ocupacao
    document.write_mini(dict_especifico['vac_poli_ac'], (114, 542)) #vac_poli_ac
    document.write_code(dict_especifico['quant_poli_ac'], (187, 542), space=1) #quant_poli_ac
    document.write_date(dict_especifico['dt_poli_ac'], (222, 542), spacing=2) #dt_poli_ac
    document.write_mini(dict_especifico['vac_poli_bc'], (114, 562)) #vac_poli_bc
    document.write_code(dict_especifico['quant_poli_bc'], (187, 562), space=1) #quant_poli_bc
    document.write_date(dict_especifico['dt_poli_bc'], (222, 562), spacing=2) #dt_poli_bc
    document.write_mini(dict_especifico['vac_conju'], (114, 581)) #vac_conju
    document.write_code(dict_especifico['quant_conju'], (187, 581), space=1) #quant_conju
    document.write_date(dict_especifico['dt_conju'], (222, 581), spacing=2) #dt_conju
    document.write_mini(dict_especifico['vac_bcg'], (114, 601)) #vac_bcg
    document.write_code(dict_especifico['quant_bcg'], (187, 601), space=1) #quant_bcg
    document.write_date(dict_especifico['dt_bcg'], (222, 601), spacing=2) #dt_bcg
    document.write_mini(dict_especifico['vac_triplice'], (350, 540)) #vac_triplice
    document.write_code(dict_especifico['quant_triplice'], (415, 541), space=1) #quant_triplice
    document.write_date(dict_especifico['dt_triplice'], (450, 541), spacing=2) #dt_triplice
    document.write_mini(dict_especifico['vac_hemo'], (350, 563)) #vac_hemo
    document.write_code(dict_especifico['quant_hemo'], (415, 563), space=1) #quant_hemo
    document.write_date(dict_especifico['dt_hemo'], (450, 563), spacing=2) #dt_hemo
    document.write_mini(dict_especifico['vac_pneumo'], (350, 583)) #vac_pneumo
    document.write_code(dict_especifico['quant_pneumo'], (415, 584), space=1) #quant_pneumo
    document.write_date(dict_especifico['dt_pneumo'], (450, 584), spacing=2) #dt_pneumo
    document.write_mini(dict_especifico['vac_outro'], (349, 602)) #vac_outro
    document.write_mini(dict_especifico['quant_outro'], (382, 603)) #quant_outro
    document.write_date(dict_especifico['dt_outro'], (448, 603), spacing=2) #dt_outro
    document.write_mini(dict_especifico['doenca_aids'], (80, 643)) #doenca_aids
    document.write_mini(dict_especifico['doenca_trauma'], (80, 657)) #doenca_trauma
    document.write_mini(dict_especifico['doenca_imunos'], (166, 641)) #doenca_imunos
    document.write_mini(dict_especifico['doenca_infeccao'], (166, 659)) #doenca_infeccao
    document.write_mini(dict_especifico['doenca_ira'], (333, 643)) #doenca_ira
    document.write_mini(dict_especifico['doenca_tuberc'], (402, 643)) #doenca_tuberc
    document.write_mini(dict_especifico['doenca_outro'], (287, 657)) #doenca_outro
    document.write_mini(dict_especifico['doenca_outro_descricao'], (320, 657)) #doenca_outro_descricao
    document.write_mini(dict_especifico['contat_caso_susp'], (555, 683)) #contat_caso_susp
    document.write_text(dict_especifico['nome_contat_susp'], (65, 729)) #nome_contat_susp
    document.write_telefone(dict_especifico['telefone_contat_susp'], (442, 729), space=2, font_size=12) #telefone_contat_susp
    document.write_text(dict_especifico['endereco_contat_susp'], (65, 755)) #endereco_contat_susp
    document.write_mini(dict_especifico['caso_secundario'], (552, 745)) #caso_secundario
    document.write_mini(dict_especifico['sint_cefaleia'], (180, 769)) #sint_cefaleia
    document.write_mini(dict_especifico['sint_febre'], (180, 784)) #sint_febre
    document.write_mini(dict_especifico['sint_vomito'], (227, 769)) #sint_vomito
    document.write_mini(dict_especifico['sint_convulsao'], (227, 784)) #sint_convulsao
    document.write_mini(dict_especifico['sint_rig_nuca'], (282, 769)) #sint_rig_nuca
    document.write_mini(dict_especifico['sint_kernig'], (282, 784)) #sint_kernig
    document.write_mini(dict_especifico['sint_fontanela'], (361, 769)) #sint_fontanela
    document.write_mini(dict_especifico['sint_coma'], (361, 784)) #sint_coma
    document.write_mini(dict_especifico['sint_petequias'], (426, 769)) #sint_petequias
    document.write_mini(dict_especifico['sint_outro'], (426, 784)) #sint_outro
    document.write_mini(dict_especifico['sint_outro_descricao'], (464, 781)) #sint_outro_descricao
    ####################### fim da pagina 1 ############################
    document.write_mini(dict_especifico['hospitalizacao2'], (154, 47), pg=1) #hospitalizacao
    document.write_date(dict_especifico['dt_internacao'], (180, 57), spacing=2, pg=1) #dt_internacao
    document.write_uf(dict_especifico['uf_hospital2'], (301, 57), pg=1) #uf_hospital
    document.write_text(dict_especifico['municipio_hospital2'], (335, 57), pg=1) #municipio_hospital
    document.write_code(dict_especifico['cod_ibge_hospital2'], (481, 57),space=2, pg=1) #cod_ibge_hospital
    document.write_text(dict_especifico['nome_hospital2'], (60, 84), pg=1) #nome_hospital
    document.write_code(dict_especifico['cod_hospital2'], (463, 84),space=2, pg=1) #cod_hospital
    document.write_mini(dict_especifico['puncao_lombar'], (158, 104), pg=1) #puncao_lombar
    document.write_date(dict_especifico['dt_puncao'], (181, 116), spacing=2, pg=1) #dt_puncao
    document.write_mini(dict_especifico['aspecto_liquor'], (551, 103), pg=1) #aspecto_liquor
    document.write_text(dict_especifico['cult_liquor'], (118, 158), pg=1) #cult_liquor
    document.write_text(dict_especifico['cult_lesao'], (118, 174), pg=1) #cult_lesao
    document.write_text(dict_especifico['cult_sangue'], (118, 190), pg=1) #cult_sangue
    document.write_text(dict_especifico['cult_escarro'], (118, 206), pg=1) #cult_escarro
    document.write_text(dict_especifico['bac_liquor'], (118, 234), pg=1) #bac_liquor
    document.write_text(dict_especifico['bac_lesao'], (118, 250), pg=1) #bac_lesao
    document.write_text(dict_especifico['bac_sangue'], (118, 266), pg=1) #bac_sangue
    document.write_text(dict_especifico['bac_escarro'], (118, 282), pg=1) #bac_escarro
    document.write_text(dict_especifico['cie_liquor'], (291, 158), pg=1) #cie_liquor
    document.write_text(dict_especifico['cie_sangue'], (291, 176), pg=1) #cie_sangue
    document.write_text(dict_especifico['agl_liquor'], (291, 204), pg=1) #agl_liquor
    document.write_text(dict_especifico['agl_sangue'], (291, 222), pg=1) #agl_sangue
    document.write_text(dict_especifico['iso_liquor'], (280, 249), pg=1) #iso_liquor
    document.write_text(dict_especifico['iso_fezes'], (280, 265), pg=1) #iso_fezes
    document.write_text(dict_especifico['pcr_liquor'], (465, 162), pg=1) #pcr_liquor
    document.write_text(dict_especifico['pcr_lesao'], (465, 178), pg=1) #pcr_lesao
    document.write_text(dict_especifico['pcr_sangue'], (465, 194), pg=1) #pcr_sangue
    document.write_text(dict_especifico['pcr_escarro'], (465, 211), pg=1) #pcr_escarro
    document.write_mini(dict_especifico['classif_caso'], (135, 310), pg=1) #classif_caso
    document.write_code(dict_especifico['especif_confirm'], (535, 316), pg=1, space=1) #especif_confirm
    document.write_mini(dict_especifico['mening_bacterias'], (289, 367), pg=1) #mening_bacterias
    document.write_mini(dict_especifico['mening_assept'], (447, 327), pg=1) #mening_assept
    document.write_mini(dict_especifico['mening_otr_etiologia'], (473, 340), pg=1) #mening_otr_etiologia
    document.write_code(dict_especifico['criterio_confirm'], (345, 386), pg=1, space=1) #criterio_confirm
    document.write_code(dict_especifico['n_mening'], (525, 420), pg=1,space=1) #n_mening
    document.write_code(dict_especifico['n_comun'], (78, 461), pg=1, space=1) #n_comun
    document.write_mini(dict_especifico['quimiop_comun'], (282, 444), pg=1) #quimiop_comun
    document.write_date(dict_especifico['dt_quimiop_comun'], (318, 460), spacing=2, pg=1) #dt_quimiop_comun
    document.write_mini(dict_especifico['doenca_rel_trab'], (545, 445), pg=1) #doenca_rel_trab
    document.write_mini(dict_especifico['evolucao_caso'], (300, 480), pg=1) #evolucao_caso
    document.write_date(dict_especifico['dt_evolucao'], (327, 497), spacing=2, pg=1) #dt_evolucao
    document.write_date(dict_especifico['dt_encerramento'], (452, 497), spacing=2, pg=1) #dt_encerramento
    document.write_text(dict_especifico['quimioc_hema'], (108, 552), pg=1) #quimioc_hema
    document.write_text(dict_especifico['quimioc_neut'], (108, 573), pg=1) #quimioc_neut
    document.write_text(dict_especifico['quimio_glicose'], (108, 593), pg=1) #quimio_glicose
    document.write_text(dict_especifico['quimioc_leuc'], (280, 552), pg=1) #quimioc_leuc
    document.write_text(dict_especifico['quimioc_eosin'], (280, 572), pg=1) #quimioc_eosin
    document.write_text(dict_especifico['quimioc_prot'], (280, 593), pg=1) #quimioc_prot
    document.write_text(dict_especifico['quimioc_mono'], (465, 551), pg=1) #quimioc_mono
    document.write_text(dict_especifico['quimioc_linf'], (465, 572), pg=1) #quimioc_linf
    document.write_text(dict_especifico['quimio_cloreto'], (465, 592), pg=1) #quimio_cloreto
    document.write_box(dict_especifico['obs_adicionais'], rect=(30, 650,568,736), pg=1) #obs_adicionais
    document.write_text(dict_especifico['municipio_us_investigador'], (60, 765), pg=1) #municipio_us_investigador
    document.write_code(dict_especifico['cod_us_investigador'], (470, 765),space=2, pg=1) #cod_us_investigador
    document.write_text(dict_especifico['nome_investigador'], (60, 794), pg=1) #nome_investigador
    document.write_text(dict_especifico['funcao_investigador'], (258, 794), pg=1) #funcao_investigador
    document.write_text(dict_especifico['assinatura_investigador'], (470, 794), pg=1) #assinatura_investigador

    document.save(nome_arquivo, path_pdf_gerado, notificatoriaCSV, modelo_pdf_base)