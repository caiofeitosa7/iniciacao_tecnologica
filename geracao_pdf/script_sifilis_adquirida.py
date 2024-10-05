from .pdfWritter import PDFWriter


def gerar_pdf_sifilis_adquirida(notificatoriaCSV: dict, dict_especifico: dict, modelo_pdf: str, modelo_pdf_base: str, path_pdf_gerado: str, nome_arquivo: str):
    document = PDFWriter(modelo_pdf)

    ###################################################
    # Dados do paciente
    ###################################################
    document.write_text(dict_especifico['numero_ficha2'], (440, 37))
    document.write_date(dict_especifico['dt_notificacao2'], (418, 131), spacing=2)  # data_notificacao
    document.write_uf(dict_especifico['uf_notificacao2'], (53, 160))  # uf_notificacao
    document.write_text(dict_especifico['municipio_notificacao2'], (90, 160))  # municipio_notificacao __unid_saude 55,space=220
    document.write_code(dict_especifico['cod_ibge_notificacao2'], (448, 160), space=2)  # cod_ibge
    document.write_text(dict_especifico['unidade_saude2'], (64, 186))  # cod_unid_saude
    document.write_code(dict_especifico['cod_unidade_saude2'], (317, 187), space=2)  # cod_unid_saude
    document.write_date(dict_especifico['dt_diagnostico'], (417, 186), spacing=2)  # data diagnostico
    ##############################################
    #####          NOTIFICACAO INDIVIDUAL     ####
    ##############################################
    document.write_text(dict_especifico['nome_paciente2'], (60, 215))  # nome
    document.write_date(dict_especifico['dt_nascimento2'], (419, 215), spacing=2)  # data_nascimento
    document.write_code(dict_especifico['idade2'], (60, 248), space=2)  # idade
    document.write_mini(dict_especifico['tipo_idade2'], (104, 242))  # tipo_idade
    document.write_mini(dict_especifico['sexo2'], (218, 236))  # sexo
    document.write_mini(dict_especifico['raca2'], (520, 236))  # raça/cor
    document.write_mini(dict_especifico['escolaridade2'], (522, 270))  # escolaridade
    document.write_code(dict_especifico['numero_sus2'], (51, 311), space=2, font_size=10)  # cartao_sus
    document.write_text(dict_especifico['nome_mae2'], (227, 311))  # nome_mae
    ##############################################
    #####          DADOS DE RESIDENCIA        ####
    ##############################################

    document.write_uf(dict_especifico['uf_residencia2'], (54, 340))  # uf_residencia
    document.write_text(dict_especifico['municipio_residencia2'], (95, 340))  # municipio_residencia
    document.write_code(dict_especifico['cod_ibge_residencia2'], (307, 340), space=2)  # cod_ibge_residencia
    document.write_text(dict_especifico['distrito_residencia2'], (400, 340))  # endereco
    document.write_text(dict_especifico['bairro_residencia2'], (64, 365))  # bairro
    document.write_text(dict_especifico['logradouro_residencia2'], (195, 366))  # logradouro
    document.write_code(dict_especifico['codigo_residencia2'], (452, 366), space=2)  # cod_logradouro
    document.write_text(dict_especifico['numero_residencia2'], (65, 390))  # numero
    document.write_text(dict_especifico['complemento_residencia2'], (120, 390))  # complemento
    document.write_text(dict_especifico['geo_campo1_2'], (400, 391))  # geo_campo_1
    document.write_text(dict_especifico['geo_campo2_2'], (55, 420))  # geo_campo_2
    document.write_text(dict_especifico['ponto_ref_residencia2'], (215, 422))  # ponto_ref
    document.write_code(dict_especifico['cep_residencia2'], (431, 423), space=2, font_size=12)  # cep
    document.write_telefone(dict_especifico['telefone_residencia2'], (55, 450), space=2, font_size=12)  # telefone
    document.write_mini(dict_especifico['zona_residencia2'], (316, 439))  # zona
    document.write_text(dict_especifico['pais_residencia2'], (345, 449))  # pais
    ##############################################
    #####        DADOS  COMPLEMENTARES        ####
    ##############################################
    document.write_text(dict_especifico['ocupacao'], (60, 502), font_size=9)  # ocupacao
    document.write_mini(dict_especifico['antecedente_sifilis'], (275, 515))  # antecedente_sifilis
    document.write_mini(dict_especifico['trat_realizado_sifilis'], (520, 515))  # trat_realizado_sifilis
    document.write_mini(dict_especifico['comportamento_sexual'], (519, 550))  # comportamento_sexual
    document.write_mini(dict_especifico['teste_nao_treponemico'], (291, 597))  # teste_nao_treponemico
    document.write_text(dict_especifico['titulo_laboratorial'], (334, 607), font_size=8)  # titulo_laboratorial
    document.write_date(dict_especifico['dt_laboratorial'], (420, 610), spacing=2)  # data_laboratorial
    document.write_mini(dict_especifico['teste_treponemico'], (515, 627))  # teste_treponemico
    document.write_mini(dict_especifico['classif_clinica'], (518, 658))  # classif_clinica
    document.write_mini(dict_especifico['trat_realizado'], (360, 690))  # trat_realizado
    document.write_date(dict_especifico['dt_inicio_trat'], (422, 715), spacing=2)  # data_inicio_trat
    document.write_mini(dict_especifico['classif_final'], (242, 740))  # classif_final
    document.write_text(dict_especifico['classif_final_descricao'], (182, 754), font_size=8)  # classif_final_descricao
    # *=========================== fim da pagina 1 ===========================*#
    document.write_box(dict_especifico['obs_adicionais'], rect=(26, 20, 535, 183), pg=1, bord=True)
    document.write_text(dict_especifico['municipio_us_investigador'], (55, 208), pg=1, font_size=9)  # municipio_us_investigador
    document.write_code(dict_especifico['cod_us_investigador'], (433, 209), space=2, pg=1)  # cod_us_investigador
    document.write_text(dict_especifico['nome_investigador'], (55, 231), pg=1, font_size=9)  # nome_investigador
    document.write_text(dict_especifico['funcao_investigador'], (240, 231), pg=1, font_size=9)  # funcao_investigador
    document.write_text(dict_especifico['assinatura_investigador'], (435, 232), pg=1, font_size=9)  # assinatura_investigador

    document.save(nome_arquivo, path_pdf_gerado, notificatoriaCSV, modelo_pdf_base)