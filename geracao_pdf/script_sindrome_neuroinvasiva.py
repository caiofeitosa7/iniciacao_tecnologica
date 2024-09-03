from .pdfWritter import PDFWriter


def gerar_pdf_sind_neuroinvasiva(notificatoriaCSV: dict, dict_especifico: dict, modelo_pdf: str, modelo_pdf_base: str,
                                 path_pdf_gerado: str, nome_arquivo: str):
    document = PDFWriter(modelo_pdf)

    ###################################################
    # Dados do paciente
    ###################################################

    document.write_text(dict_especifico['numero_ficha2'], (470, 57))

    if dict_especifico['tipo_notificacao2'] == '1':
        document.write_cross((167, 115))
    else:
        document.write_cross((310, 115))

    document.write_mini(dict_especifico['agravoDoenca_num'], (420, 136))  # agravo doenca numerico
    document.write_text(dict_especifico['agravoDoenca_outro'], (168, 146), font_size=8)  # agravo doenca outro
    document.write_date(dict_especifico['dt_notificacao2'], (444, 144), spacing=2)  # data_notificacao
    document.write_uf(dict_especifico['uf_notificacao2'], (70, 172))  # uf_notificacao
    document.write_text(dict_especifico['municipio_notificacao2'],
                        (98, 172))  # municipio_notificacao __unid_saude 55,space=220
    document.write_code(dict_especifico['cod_ibge_notificacao2'], (478, 170), space=2)  # cod_ibge
    document.write_text(dict_especifico['dt_hospitalizacao2'], (82, 196))  # data_hospitalizacao2
    document.write_text(dict_especifico['serv_vigilancia'], (200, 196), font_size=9)  # servico_vigilancia
    document.write_code(dict_especifico['cod_serv_vigilancia'], (467, 196), space=2)  # cod_servico_vigilancia
    ##############################################
    #####          NOTIFICACAO INDIVIDUAL     ####
    ##############################################
    document.write_text(dict_especifico['nome_paciente2'], (75, 225))  # nome
    document.write_date(dict_especifico['dt_nascimento2'], (442, 227), spacing=2)  # data_nascimento
    document.write_code(dict_especifico['idade2'], (75, 256), space=2)  # idade
    document.write_mini(dict_especifico['tipo_idade2'], (122, 250))  # tipo_idade
    document.write_mini(dict_especifico['sexo2'], (240, 251))  # sexo
    document.write_mini(dict_especifico['gestante2'], (430, 251))  # gestante
    document.write_mini(dict_especifico['raca2'], (547, 251))  # raça/cor
    document.write_mini(dict_especifico['escolaridade2'], (546, 279))  # escolaridade
    document.write_code(dict_especifico['numero_sus2'], (68, 320), font_size=12)  # cartao_sus
    document.write_text(dict_especifico['nome_mae2'], (245, 321), font_size=9)  # nome_mae
    ##############################################
    #####          DADOS DE RESIDENCIA        ####
    ##############################################

    document.write_uf(dict_especifico['uf_residencia2'], (68, 350))  # uf_residencia
    document.write_text(dict_especifico['municipio_residencia2'], (100, 349), font_size=8)  # municipio_residencia
    document.write_code(dict_especifico['cod_ibge_residencia2'], (326, 349), space=2)  # cod_ibge_residencia
    document.write_text(dict_especifico['distrito_residencia2'], (420, 348))  # endereco
    document.write_text(dict_especifico['bairro_residencia2'], (75, 373), font_size=8)  # bairro
    document.write_text(dict_especifico['logradouro_residencia2'], (210, 373), font_size=8)  # logradouro
    document.write_code(dict_especifico['codigo_residencia2'], (406, 372), space=2)  # cod_logradouro
    document.write_text(dict_especifico['numero_residencia2'], (510, 372))  # numero
    document.write_code(dict_especifico['cep_residencia2'], (67, 397), font_size=12)  # cep
    document.write_text(dict_especifico['complemento_residencia2'], (145, 397), font_size=8)  # complemento
    document.write_text(dict_especifico['geo_campo1_2'], (415, 396))  # geo_campo_1
    document.write_telefone(dict_especifico['telefone_residencia2'], (70, 422), space=2, font_size=12)  # telefone
    document.write_mini(dict_especifico['zona_residencia2'], (343, 415))  # zona
    document.write_text(dict_especifico['pais_residencia2'], (370, 421), font_size=8)  # pais
    ###################################################
    # Dados Complementares _ Ficha de Investigação #
    ###################################################
    document.write_date(dict_especifico['dt_investigacao'], (73, 463), spacing=2)  # data_investigacao
    document.write_text(dict_especifico['ocupacao'], (200, 463), font_size=8)  # ocupacao
    document.write_date(dict_especifico['dt_sintomas2'], (435, 463), spacing=2)  # data_sintomas
    document.write_mini(dict_especifico['viagem_recente'], (293, 482))  # viagem_recente
    document.write_text(dict_especifico['destino_viagem'], (325, 490), font_size=8)  # destino_viagem
    document.write_mini(dict_especifico['vac_febre_amarela'], (200, 512))  # vac_febre_amarela
    document.write_mini(dict_especifico['loc_ave_equina'], (357, 519))  # local_ave_equina
    document.write_mini(dict_especifico['caso_semelhante_viz'], (534, 516))  # caso_semelhante_viz
    document.write_mini(dict_especifico['infec_gripe'], (71, 554))  # infec_gripe
    document.write_mini(dict_especifico['infec_diarreia'], (71, 570))  # infec_diarreia
    document.write_mini(dict_especifico['infec_dengue'], (160, 554))  # infec_dengue
    document.write_mini(dict_especifico['infec_outro'], (160, 570))  # infec_outro
    document.write_text(dict_especifico['infec_outro_descricao'], (232, 569), font_size=8)  # infec_outro_descricao
    document.write_date(dict_especifico['dt_adoecimento'], (396, 570), spacing=3)  # data_adoecimento
    document.write_mini(dict_especifico['imunodepressao'], (204, 599))  # imunodepressao
    document.write_mini(dict_especifico['vacinacao_recente'], (356, 599))  # vacinacao_recente
    document.write_text(dict_especifico['dados_vacinacao'], (400, 605), font_size=7)  # dados_vacinacao
    document.write_mini(dict_especifico['imunoglobulina'], (408, 620))  # imunoglobulina
    document.write_date(dict_especifico['dt_infusao'], (429, 628), spacing=2)  # data_infusao
    document.write_mini(dict_especifico['ex_hemograma'], (226, 640))  # ex_hemograma
    document.write_mini(dict_especifico['ex_liquor'], (226, 655))  # ex_liquor
    document.write_mini(dict_especifico['ex_tomografia'], (292, 641))  # ex_tomografia
    document.write_mini(dict_especifico['ex_ressonancia'], (292, 655))  # ex_ressonancia
    document.write_mini(dict_especifico['ex_enm'], (394, 641))  # ex_enm
    document.write_mini(dict_especifico['ex_eeg'], (394, 655))  # ex_eeg
    document.write_mini(dict_especifico['ex_biopsia'], (490, 641))  # ex_biopsia
    document.write_mini(dict_especifico['ex_necropsia'], (490, 655))  # ex_necropsia
    document.write_mini(dict_especifico['desf_hospitalar'], (205, 680))  # desf_hospitalar
    document.write_text(dict_especifico['diag_alta'], (230, 689), font_size=6)  # diagnostico_alta
    document.write_date(dict_especifico['dt_alta_obito'], (348, 689), spacing=1)  # data_alta_obito
    document.write_date(dict_especifico['dt_encerramento'], (450, 689), spacing=2)  # data_encerramento
    document.write_mini(dict_especifico['diag_etiologico'], (180, 716))  # diagnostico_etiologico
    document.write_text(dict_especifico['diag_etiol_outro_descricao'], (98, 726), font_size=6)  # diagnostico_etiologico_outro
    document.write_mini(dict_especifico['classif_caso'], (303, 718))  # classificacao_caso
    document.write_mini(dict_especifico['criterio_classif'], (544, 720))  # criterio_classificacao
    document.write_box(dict_especifico['obs_adicionais'], rect=(70, 740, 558, 800))  # observacoes_adicionais

    document.save(nome_arquivo, path_pdf_gerado, notificatoriaCSV, modelo_pdf_base)
