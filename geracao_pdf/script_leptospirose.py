from .pdfWritter import PDFWriter


def gerar_pdf_leptospirose(notificatoriaCSV: dict, dict_especifico: dict, modelo_pdf: str, modelo_pdf_base: str, path_pdf_gerado: str, nome_arquivo: str):
    document = PDFWriter(modelo_pdf)

    ###################################################
    # Dados do paciente
    ###################################################
    document.write_text(dict_especifico['numero_ficha2'],(470, 46))
    document.write_date(dict_especifico['dt_notificacao2'], (450, 172), spacing=2) #data_notificacao
    document.write_uf(dict_especifico['uf_notificacao2'], (60, 202)) #uf_notificacao
    document.write_text(dict_especifico['municipio_notificacao2'], (100, 204)) #municipio_notificacao __unid_saude 55,space=220
    document.write_code(dict_especifico['cod_ibge_notificacao2'], (485, 205),space=2) #cod_ibge
    document.write_text(dict_especifico['unidade_saude2'], (70, 232)) #cod_unid_saude
    document.write_code(dict_especifico['cod_unidade_saude2'], (342, 232),space=2) #cod_unid_saude
    document.write_date(dict_especifico['dt_sintomas2'], (451, 231), spacing=2) #data_diagnostico
    ##############################################
    #####          NOTIFICACAO INDIVIDUAL     ####
    ##############################################
    document.write_text(dict_especifico['nome_paciente2'], (65, 262)) #nome
    document.write_date(dict_especifico['dt_nascimento2'], (455, 261), spacing=2) #data_nascimento
    document.write_code(dict_especifico['idade2'], (70, 291),space=2) #idade
    document.write_mini(dict_especifico['tipo_idade2'], (117, 284)) #tipo_idade
    document.write_mini(dict_especifico['sexo2'], (237, 277)) #sexo
    document.write_mini(dict_especifico['gestante2'], (433, 277)) #gestante
    document.write_mini(dict_especifico['raca2'], (558, 277)) #raça/cor
    document.write_mini(dict_especifico['escolaridade2'], (558, 307)) #escolaridade
    document.write_code(dict_especifico['numero_sus2'], (61, 352),space=2, font_size=10) #cartao_sus
    document.write_text(dict_especifico['nome_mae2'], (250, 352)) #nome_mae
    ##############################################
    #####          DADOS DE RESIDENCIA        ####
    ##############################################

    document.write_uf(dict_especifico['uf_residencia2'], (62, 380)) #uf_residencia
    document.write_text(dict_especifico['municipio_residencia2'], (100, 380)) #municipio_residencia
    document.write_code(dict_especifico['cod_ibge_residencia2'], (328, 380),space=2) #cod_ibge_residencia
    document.write_text(dict_especifico['distrito_residencia2'], (430, 380)) #endereco
    document.write_text(dict_especifico['bairro_residencia2'], (70, 405)) #bairro
    document.write_text(dict_especifico['logradouro_residencia2'], (210, 405)) #logradouro
    document.write_code(dict_especifico['codigo_residencia2'], (481, 406),space=2) #cod_logradouro
    document.write_text(dict_especifico['numero_residencia2'], (68, 429)) #numero
    document.write_text(dict_especifico['complemento_residencia2'], (120, 429)) #complemento
    document.write_text(dict_especifico['geo_campo1_2'], (420, 432)) #geo_campo_1
    document.write_text(dict_especifico['geo_campo2_2'], (63, 456)) #geo_campo_2
    document.write_text(dict_especifico['ponto_ref_residencia2'], (235, 456)) #ponto_ref
    document.write_code(dict_especifico['cep_residencia2'], (458, 458),space=2) #cep
    document.write_telefone(dict_especifico['telefone_residencia2'], (60, 482), space=2) #telefone
    document.write_mini(dict_especifico['zona_residencia2'], (338, 470)) #zona
    document.write_text(dict_especifico['pais_residencia2'], (380, 482)) #pais

    ###################################################
    #              Dados complementares               #
    ###################################################
    document.write_date(dict_especifico['dt_investigacao'], (60, 532), spacing=2) #data_investigacao
    document.write_text(dict_especifico['ocupacao'], (200, 532)) #ocupacao
    document.write_mini(dict_especifico['risco_lama'], (65, 565)) #sit_risc_agua
    document.write_mini(dict_especifico['risco_fossa'], (65, 582)) #sit_risc_esgoto
    document.write_mini(dict_especifico['risco_rio'], (65, 598)) #sit_risc_rio
    document.write_mini(dict_especifico['risco_terreno'], (65, 613)) #sit_risc_terr_baldio
    document.write_mini(dict_especifico['risco_animais'], (250, 566)) #sit_risc_animais
    document.write_mini(dict_especifico['risco_sinal_roed'], (250, 582)) #sit_risc_sinais_roedor
    document.write_mini(dict_especifico['risco_roed_dir'], (250, 599)) #sit_risc_roedor
    document.write_mini(dict_especifico['risco_lixo'], (251, 615)) #sit_risc_lixo
    document.write_mini(dict_especifico['risco_cx_dagua'], (410, 566)) #sit_risc_cx_dagua
    document.write_mini(dict_especifico['risco_plantio'], (410, 580)) #sit_risc_plantas
    document.write_mini(dict_especifico['risco_graos'], (410, 595)) #sit_risc_armaz_graos
    document.write_mini(dict_especifico['risco_outras'], (410, 611)) #sit_risc_outras
    document.write_text(dict_especifico['risco_outras_descricao'], (447, 610)) #sit_risc_outras
    document.write_mini(dict_especifico['caso_lept_ant_humano'], (128, 643)) #case_lepto_anterior_human
    document.write_mini(dict_especifico['caso_lept_ant_animal'], (304, 643)) #case_lepto_anterior_animal
    document.write_date(dict_especifico['dt_atendimento'], (64, 678), spacing=2) #data_atendimento
    document.write_mini(dict_especifico['sint_febre'], (188, 678)) #sins_sintomas_febre
    document.write_mini(dict_especifico['sint_cong_conju'], (188, 693)) #sins_sintomas_conjuntival
    document.write_mini(dict_especifico['sint_ictericia'], (188, 708)) #sins_sintomas_ictericia
    document.write_mini(dict_especifico['sint_hemo_pulmonar'], (188, 722)) #sins_sintomas_hemorr_pulmonar
    document.write_mini(dict_especifico['sint_mialgia'], (283, 679)) #sins_sintomas_mialgia
    document.write_mini(dict_especifico['sint_panturrilha'], (283, 693)) #sins_sintomas_panturrilha
    document.write_mini(dict_especifico['sint_renal'], (283, 708)) #sins_sintomas_insuf_renal
    document.write_mini(dict_especifico['sint_outra_hemo'], (283, 723)) #sins_sintomas_outras_hemorr
    document.write_mini(dict_especifico['sint_cefaleia'], (372, 677)) #sins_sintomas_cefaleia
    document.write_mini(dict_especifico['sint_vomito'], (372, 691)) #sins_sintomas_vomito
    document.write_mini(dict_especifico['sint_alter_resp'], (372, 707)) #sins_sintomas_alt_respiracao
    document.write_mini(dict_especifico['sint_mening'], (372, 723)) #sins_sintomas_meningismo
    document.write_mini(dict_especifico['sint_prostracao'], (443, 677)) #sins_sintomas_prostacao
    document.write_mini(dict_especifico['sint_diarreia'], (443, 692)) #sins_sintomas_diarreia
    document.write_mini(dict_especifico['sint_alter_cardi'], (443, 707)) #sins_sintomas_cardiaca
    document.write_mini(dict_especifico['sint_outro'], (443, 723)) #sins_sintomas_outras
    document.write_text(dict_especifico['sint_outro_descricao'], (509, 721)) #text_sintomas_outras
    document.write_mini(dict_especifico['hospitalizacao2'], (283, 750)) #ocorreu_hospital
    document.write_date(dict_especifico['dt_internacao'], (322, 760), spacing=2) #data_internacao
    document.write_date(dict_especifico['dt_alta'], (452, 760), spacing=2) #data_alta
    document.write_uf(dict_especifico['uf_hospital2'], (63, 785)) #uf_internacao
    document.write_text(dict_especifico['municipio_hospital2'], (100, 785)) #municipio_internacao
    document.write_code(dict_especifico['cod_ibge_hospital2'], (484, 785),space=2) #cod_ibge_internacao
    document.write_text(dict_especifico['nome_hospital2'], (60, 810)) #instituicao_internacao
    document.write_code(dict_especifico['cod_hospital2'], (466, 810),space=2) #cod_instituicao_internacao
    ###################### fim pag 0 ####################
    document.write_date(dict_especifico['dt_igm_elisa1'], (68, 71),pg=1, spacing=2) #data_coleta_sorologia_1
    document.write_mini(dict_especifico['res_amostra_elisa1'], (300, 52),pg=1) #res_sorologia_1
    document.write_date(dict_especifico['dt_igm_elisa2'], (320, 71),pg=1, spacing=2) #data_coleta_sorologia_2
    document.write_mini(dict_especifico['res_amostra_elisa2'], (552, 51),pg=1) #res_sorologia_2
    document.write_date(dict_especifico['dt_micro1'], (72, 124),pg=1, spacing=2) #data_coleta_micro_aglut_1
    document.write_text(dict_especifico['sorovar1_micro1'], (219, 122),pg=1) #micro_1_sorovar
    document.write_code(dict_especifico['titulo1_micro1'], (283, 125), pg=1, space=2)  # micro_1_titulo
    document.write_text(dict_especifico['sorovar2_micro1'], (413, 123), pg=1)  # micro_1_sorovar2
    document.write_code(dict_especifico['titulo2_micro1'], (476, 126), pg=1, space=2)  # micro_1_titulo2
    document.write_mini(dict_especifico['res_aglu_micro1'], (542, 149), pg=1)  # res_micro_1
    document.write_date(dict_especifico['dt_micro2'], (70, 200), pg=1, spacing=2)  # data_coleta_micro_aglut_2
    document.write_text(dict_especifico['sorovar1_micro2'], (218, 197), pg=1)  # micro_2_sorovar
    document.write_code(dict_especifico['titulo1_micro2'], (282, 200), pg=1, space=2)  # micro_2_titulo
    document.write_text(dict_especifico['sorovar2_micro2'], (412, 199), pg=1)  # micro_2_sorovar2
    document.write_code(dict_especifico['titulo2_micro2'], (475, 201), pg=1, space=2)  # micro_2_titulo2
    document.write_mini(dict_especifico['res_aglu_micro2'], (541, 225),pg=1) #res_micro_2
    document.write_date(dict_especifico['dt_col_isola'], (68, 285),pg=1, spacing=2) #data_iso_coleta
    document.write_mini(dict_especifico['res_col_isola'], (552, 270),pg=1) #iso_res
    document.write_date(dict_especifico['dt_col_imunohist'], (68, 327),pg=1, spacing=2) #data_coleta_imuno
    document.write_mini(dict_especifico['res_col_imunohist'], (551, 314),pg=1) #res_imuno
    document.write_date(dict_especifico['dt_coleta_pcr'], (68, 368),pg=1, spacing=2) #data_coleta_pcr
    document.write_mini(dict_especifico['resultado_pcr'], (551, 351),pg=1) #res_pcr
    document.write_mini(dict_especifico['classif_final'], (330, 394),pg=1) #class_final
    document.write_mini(dict_especifico['criterio_confirm'], (553, 392),pg=1) #criterio
    document.write_mini(dict_especifico['caso_autoctone'], (310, 435),pg=1) #case_autoctone
    document.write_uf(dict_especifico['uf_infeccao2'], (350, 445),pg=1) #uf_conclusao
    document.write_text(dict_especifico['pais_infeccao2'], (400, 445),pg=1) #pais
    document.write_text(dict_especifico['municipio_infeccao2'], (70, 475),pg=1) #municipio_conclusao
    document.write_code(dict_especifico['cod_ibge_infeccao2'], (212, 476),pg=1,space=2) #cod_ibge_conclusao
    document.write_text(dict_especifico['distrito_infeccao2'], (305, 475),pg=1) #distrito_conclusao
    document.write_text(dict_especifico['bairro_infeccao2'], (450, 475),pg=1) #bairro_conclusao
    document.write_mini(dict_especifico['area_infeccao'], (293, 503),pg=1) #area_infec
    document.write_mini(dict_especifico['ambiente_infecao'], (553, 494),pg=1) #ambient_infec
    document.write_mini(dict_especifico['doenca_rel_trab'], (230, 527),pg=1) #doenca_trabalho
    document.write_mini(dict_especifico['evolucao_caso'], (548, 528),pg=1) #evolucao_case
    document.write_date(dict_especifico['dt_obito'], (76, 567),pg=1, spacing=2) #data_obito
    document.write_date(dict_especifico['dt_encerramento'], (209, 567),pg=1, spacing=2) #data_encerramento
    document.write_mini(dict_especifico['dt_risco1'], (40, 623),pg=1) #tab_data_1
    document.write_uf(dict_especifico['uf_risco1'], (120, 624),pg=1) #tab_uf_1
    document.write_text(dict_especifico['municipio_risco1'], (160, 623),pg=1, font_size=11) #tab_municipio_1
    document.write_text(dict_especifico['ender_risco1'], (299, 623),pg=1, font_size=12) #tab_adress_1
    document.write_text(dict_especifico['localid_risco1'], (458, 623),pg=1, font_size=11) #tab_local_1
    document.write_mini(dict_especifico['dt_risco2'], (40, 634),pg=1) #tab_data_2
    document.write_uf(dict_especifico['uf_risco2'], (120, 635),pg=1) #tab_uf_2
    document.write_text(dict_especifico['municipio_risco2'], (160, 634),pg=1, font_size=11) #tab_municipio_2
    document.write_text(dict_especifico['ender_risco2'], (299, 634),pg=1, font_size=12) #tab_adress_2
    document.write_text(dict_especifico['localid_risco2'], (458, 634),pg=1, font_size=11) #tab_local_2
    document.write_mini(dict_especifico['dt_risco3'], (40, 644),pg=1) #tab_data_3
    document.write_uf(dict_especifico['uf_risco3'], (120, 645),pg=1) #tab_uf_3
    document.write_text(dict_especifico['municipio_risco3'], (160, 644),pg=1, font_size=11) #tab_municipio_3
    document.write_text(dict_especifico['ender_risco3'], (299, 644),pg=1, font_size=12) #tab_adress_3
    document.write_text(dict_especifico['localid_risco3'], (458, 644),pg=1, font_size=11) #tab_local_3
    document.write_mini(dict_especifico['dt_risco4'], (40, 654),pg=1) #tab_data_4
    document.write_uf(dict_especifico['uf_risco4'], (120, 655),pg=1) #tab_uf_4
    document.write_text(dict_especifico['municipio_risco4'], (160, 654),pg=1, font_size=11) #tab_municipio_4
    document.write_text(dict_especifico['ender_risco4'], (299, 654),pg=1, font_size=12) #tab_adress_4
    document.write_text(dict_especifico['localid_risco4'], (458, 654),pg=1, font_size=11) #tab_local_4
    document.write_box(dict_especifico['obs_adicionais'], pg=1, rect=(35, 670, 569, 730)) #obs
    document.write_text(dict_especifico['municipio_us_investigador'], (62, 747),pg=1) #municipio_investigador
    document.write_code(dict_especifico['cod_us_investigador'], (467, 747),pg=1,space=2) #cod_unid_investigador
    document.write_text(dict_especifico['nome_investigador'], (64, 778),pg=1) #nome_investigador
    document.write_text(dict_especifico['funcao_investigador'], (265, 778),pg=1) #func_investigador
    document.write_text(dict_especifico['assinatura_investigador'], (475, 778),pg=1) #assign_investigador

    document.save(nome_arquivo, path_pdf_gerado, notificatoriaCSV, modelo_pdf_base)