from .pdfWritter import PDFWriter


def gerar_pdf_evento_adv_pos_vacina(notificatoriaCSV: dict, dict_especifico: dict, modelo_pdf: str,
                                    modelo_pdf_base: str, path_pdf_gerado: str, nome_arquivo: str):
    document = PDFWriter(modelo_pdf)

    document.write_text(dict_especifico['numero_ficha2'], (438, 68))  # Número da ficha
    document.write_date(dict_especifico['dt_notificacao2'], (439, 79), spacing=2, font_size=10)  # Data da notificação
    document.write_date(dict_especifico['dt_investigacao'], (438, 92), spacing=2, font_size=10)  # Data da investigação
    document.write_text(dict_especifico['numero_sus2'], (438, 114), font_size=11)  # Número do SUS
    document.write_text(dict_especifico['pais_notificacao'], (60, 197))  # País da notificação
    document.write_text(dict_especifico['uf_notificacao2'], (180, 197))  # UF da notificação
    document.write_text(dict_especifico['municipio_notificacao2'], (210, 197))  # Município da notificação
    document.write_text(dict_especifico['us_notificacao'], (60, 218))  # Unidade de saúde da notificação
    ###################################################
    # Dados do paciente
    ###################################################
    document.write_text(dict_especifico['nome_paciente2'], (60, 252))  # Nome do paciente
    document.write_text(dict_especifico['iniciais_paciente'], (380, 252))  # Iniciais do paciente
    document.write_date(dict_especifico['dt_nascimento2'], (452, 250), spacing=2, font_size=10)  # Data de nascimento
    document.write_text(dict_especifico['idade2'], (62, 280))  # Idade
    document.write_text(dict_especifico['tipo_idade2'], (100, 280))  # Tipo de idade
    document.write_text(dict_especifico['sexo_num'], (210, 280))  # Sexo
    document.write_text(dict_especifico['raca2'], (317, 280))  # Raça
    document.write_text(dict_especifico['ocupacao'], (60, 309))  # Ocupação
    document.write_text(dict_especifico['nome_mae2'], (315, 309), font_size=9)  # Nome da mãe
    document.write_text(dict_especifico['gestante2'], (61, 341))  # Gestante
    document.write_text(dict_especifico['mes_vacina_gest'], (178, 338))  # Mês da vacinação
    document.write_text(dict_especifico['amamentando'], (282, 342))  # Amamentando
    document.write_text(dict_especifico['aleitamento'], (415, 342))  # Aleitamento
    ##############################################
    #####          DADOS DE RESIDENCIA        ####
    ##############################################
    document.write_text(dict_especifico['logradouro_residencia2'], (60, 380), font_size=7)  # Logradouro
    document.write_text(dict_especifico['numero_residencia2'], (317, 380))  # Número
    document.write_text(dict_especifico['complemento_residencia2'], (370, 380), font_size=7)  # Complemento
    document.write_text(dict_especifico['bairro_residencia2'], (440, 380), font_size=7)  # Bairro
    document.write_text(dict_especifico['ponto_ref_residencia2'], (60, 410), font_size=9)  # Ponto de referência
    document.write_text(dict_especifico['zona_residencia2'], (281, 406))  # Zona
    document.write_cep(dict_especifico['cep_residencia2'], (348, 403), space=1, font_size=11)  # CEP
    document.write_telefone(dict_especifico['telefone_residencia2'], (445, 397), space=1, font_size=10)  # Telefone
    document.write_telefone(dict_especifico['telefone2_residencia2'], (445, 410), space=1, font_size=10)  # Telefone
    document.write_text(dict_especifico['pais_residencia2'], (60, 432))  # País
    document.write_text(dict_especifico['uf_residencia2'], (170, 433))  # UF
    document.write_text(dict_especifico['municipio_residencia2'], (200, 433))  # Município
    ####################################################
    # Dados Vacinação
    ####################################################
    ###Coluna 1
    document.write_date(dict_especifico['vacinacao_dt1'], (55, 505), font_size=9, printbars=True)  # Data da vacina1
    document.write_date(dict_especifico['vacinacao_dt2'], (55, 517), font_size=9, printbars=True)  # Data da vacina2
    document.write_date(dict_especifico['vacinacao_dt3'], (55, 530), font_size=9, printbars=True)  # Data da vacina3
    document.write_date(dict_especifico['vacinacao_dt4'], (55, 543), font_size=9, printbars=True)  # Data da vacina4
    document.write_date(dict_especifico['vacinacao_dt5'], (55, 555), font_size=9, printbars=True)  # Data da vacina5
    document.write_date(dict_especifico['vacinacao_dt6'], (55, 567), font_size=9, printbars=True)  # Data da vacina6
    document.write_date(dict_especifico['vacinacao_dt7'], (55, 579), font_size=9, printbars=True)  # Data da vacina7
    document.write_date(dict_especifico['vacinacao_dt8'], (55, 591), font_size=9, printbars=True)  # Data da vacina8
    document.write_date(dict_especifico['vacinacao_dt9'], (55, 603), font_size=9, printbars=True)  # Data da vacina9
    ###Coluna 2
    document.write_text(dict_especifico['vacinacao_nome1'], (108, 505), font_size=10)  # Nome da vacina1
    document.write_text(dict_especifico['vacinacao_nome2'], (108, 517), font_size=10)  # Nome da vacina2
    document.write_text(dict_especifico['vacinacao_nome3'], (108, 530), font_size=10)  # Nome da vacina3
    document.write_text(dict_especifico['vacinacao_nome4'], (108, 543), font_size=10)  # Nome da vacina4
    document.write_text(dict_especifico['vacinacao_nome6'], (108, 567), font_size=10)  # Nome da vacina6
    document.write_text(dict_especifico['vacinacao_nome7'], (108, 579), font_size=10)  # Nome da vacina7
    document.write_text(dict_especifico['vacinacao_nome8'], (108, 591), font_size=10)  # Nome da vacina8
    document.write_text(dict_especifico['vacinacao_nome9'], (108, 603), font_size=10)  # Nome da vacina9
    ###Coluna 3
    document.write_text(dict_especifico['vacinacao_dose1'], (192, 505), font_size=10)  # Dose da vacina1
    document.write_text(dict_especifico['vacinacao_dose2'], (192, 517), font_size=10)  # Dose da vacina2
    document.write_text(dict_especifico['vacinacao_dose3'], (192, 530), font_size=10)  # Dose da vacina3
    document.write_text(dict_especifico['vacinacao_dose4'], (192, 543), font_size=10)  # Dose da vacina4
    document.write_text(dict_especifico['vacinacao_dose5'], (192, 555), font_size=10)  # Dose da vacina5
    document.write_text(dict_especifico['vacinacao_dose6'], (192, 567), font_size=10)  # Dose da vacina6
    document.write_text(dict_especifico['vacinacao_dose7'], (192, 579), font_size=10)  # Dose da vacina7
    document.write_text(dict_especifico['vacinacao_dose8'], (192, 591), font_size=10)  # Dose da vacina8
    document.write_text(dict_especifico['vacinacao_dose9'], (192, 603), font_size=10)  # Dose da vacina9
    ###Coluna 4
    document.write_text(dict_especifico['vacinacao_via_adm1'], (220, 505), font_size=10)  # Via de administração da vacina1
    document.write_text(dict_especifico['vacinacao_via_adm2'], (220, 517), font_size=10)  # Via de administração da vacina2
    document.write_text(dict_especifico['vacinacao_via_adm3'], (220, 530), font_size=10)  # Via de administração da vacina3
    document.write_text(dict_especifico['vacinacao_via_adm4'], (220, 543), font_size=10)  # Via de administração da vacina4
    document.write_text(dict_especifico['vacinacao_via_adm5'], (220, 555), font_size=10)  # Via de administração da vacina5
    document.write_text(dict_especifico['vacinacao_via_adm6'], (220, 567), font_size=10)  # Via de administração da vacina6
    document.write_text(dict_especifico['vacinacao_via_adm7'], (220, 579), font_size=10)  # Via de administração da vacina7
    document.write_text(dict_especifico['vacinacao_via_adm8'], (220, 591), font_size=10)  # Via de administração da vacina8
    document.write_text(dict_especifico['vacinacao_via_adm9'], (220, 603), font_size=10)  # Via de administração da vacina9
    ###Coluna 5
    document.write_text(dict_especifico['vacinacao_local_aplic1'], (282, 505), font_size=10)  # Local de aplicação da vacina1
    document.write_text(dict_especifico['vacinacao_local_aplic2'], (282, 517), font_size=10)  # Local de aplicação da vacina2
    document.write_text(dict_especifico['vacinacao_local_aplic3'], (282, 530), font_size=10)  # Local de aplicação da vacina3
    document.write_text(dict_especifico['vacinacao_local_aplic4'], (282, 543), font_size=10)  # Local de aplicação da vacina4
    document.write_text(dict_especifico['vacinacao_local_aplic5'], (282, 555), font_size=10)  # Local de aplicação da vacina5
    document.write_text(dict_especifico['vacinacao_local_aplic6'], (282, 567), font_size=10)  # Local de aplicação da vacina6
    document.write_text(dict_especifico['vacinacao_local_aplic7'], (282, 579), font_size=10)  # Local de aplicação da vacina7
    document.write_text(dict_especifico['vacinacao_local_aplic8'], (282, 591), font_size=10)  # Local de aplicação da vacina8
    document.write_text(dict_especifico['vacinacao_local_aplic9'], (282, 603), font_size=10)  # Local de aplicação da vacina9
    ###Coluna 6
    document.write_text(dict_especifico['vacinacao_fabri1'], (341, 505), font_size=10)  # Fabricante da vacina1
    document.write_text(dict_especifico['vacinacao_fabri2'], (341, 517), font_size=10)  # Fabricante da vacina2
    document.write_text(dict_especifico['vacinacao_fabri3'], (341, 530), font_size=10)  # Fabricante da vacina3
    document.write_text(dict_especifico['vacinacao_fabri4'], (341, 543), font_size=10)  # Fabricante da vacina4
    document.write_text(dict_especifico['vacinacao_fabri5'], (341, 555), font_size=10)  # Fabricante da vacina5
    document.write_text(dict_especifico['vacinacao_fabri6'], (341, 567), font_size=10)  # Fabricante da vacina6
    document.write_text(dict_especifico['vacinacao_fabri7'], (341, 579), font_size=10)  # Fabricante da vacina7
    document.write_text(dict_especifico['vacinacao_fabri8'], (341, 591), font_size=10)  # Fabricante da vacina8
    document.write_text(dict_especifico['vacinacao_fabri9'], (341, 603), font_size=10)  # Fabricante da vacina9
    ###Coluna 7
    document.write_text(dict_especifico['vacinacao_num_lote1'], (420, 505), font_size=11)  # Número do lote da vacina1
    document.write_text(dict_especifico['vacinacao_num_lote2'], (420, 517), font_size=11)  # Número do lote da vacina2
    document.write_text(dict_especifico['vacinacao_num_lote3'], (420, 530), font_size=11)  # Número do lote da vacina3
    document.write_text(dict_especifico['vacinacao_num_lote4'], (420, 543), font_size=11)  # Número do lote da vacina4
    document.write_text(dict_especifico['vacinacao_num_lote5'], (420, 555), font_size=11)  # Número do lote da vacina5
    document.write_text(dict_especifico['vacinacao_num_lote6'], (420, 567), font_size=11)  # Número do lote da vacina6
    document.write_text(dict_especifico['vacinacao_num_lote7'], (420, 579), font_size=11)  # Número do lote da vacina7
    document.write_text(dict_especifico['vacinacao_num_lote8'], (420, 591), font_size=11)  # Número do lote da vacina8
    document.write_text(dict_especifico['vacinacao_num_lote9'], (420, 603), font_size=11)  # Número do lote da vacina9
    ###Coluna 8
    document.write_date(dict_especifico['vacinacao_dt_valid1'], (497, 505), font_size=9,
                   printbars=True)  # Data de validade da vacina1
    document.write_date(dict_especifico['vacinacao_dt_valid2'], (497, 517), font_size=9,
                   printbars=True)  # Data de validade da vacina2
    document.write_date(dict_especifico['vacinacao_dt_valid3'], (497, 530), font_size=9,
                   printbars=True)  # Data de validade da vacina3
    document.write_date(dict_especifico['vacinacao_dt_valid4'], (497, 543), font_size=9,
                   printbars=True)  # Data de validade da vacina4
    document.write_date(dict_especifico['vacinacao_dt_valid5'], (497, 555), font_size=9,
                   printbars=True)  # Data de validade da vacina5
    document.write_date(dict_especifico['vacinacao_dt_valid6'], (497, 567), font_size=9,
                   printbars=True)  # Data de validade da vacina6
    document.write_date(dict_especifico['vacinacao_dt_valid7'], (497, 579), font_size=9,
                   printbars=True)  # Data de validade da vacina7
    document.write_date(dict_especifico['vacinacao_dt_valid8'], (497, 591), font_size=9,
                   printbars=True)  # Data de validade da vacina8
    document.write_date(dict_especifico['vacinacao_dt_valid9'], (497, 603), font_size=9,
                   printbars=True)  # Data de validade da vacina9
    ###################################################
    # Dados de Unidade de saude
    ###################################################
    document.write_text(dict_especifico['pais_aplicacao'], (60, 638))  # País de aplicação
    document.write_text(dict_especifico['uf_aplicacao'], (170, 638))  # UF de aplicação
    document.write_text(dict_especifico['municipio_aplicacao'], (195, 638))  # Município de aplicação
    document.write_text(dict_especifico['us_aplicacao'], (60, 667))  # Unidade de saúde de aplicação
    document.write_mini(dict_especifico['motivo_aplicacao'], (325, 662))  # Motivo da aplicação
    document.write_mini(dict_especifico['local_aplicacao'], (445, 662))  # Local de aplicação
    ###################################################
    # Dados de Doenças Preexistentes 
    ###################################################
    # coluna 1 1
    document.write_mini(dict_especifico['doenca_preexist'], (66, 730))  # Doença preexistente
    document.write_mini(dict_especifico['op_doenca_aids_hiv'], (227, 692))  # AIDS/HIV
    document.write_mini(dict_especifico['op_doenca_alerg_alim'], (227, 707))  # Alergia alimentar
    document.write_mini(dict_especifico['op_doenca_alerg_alim_espec'], (285, 710))  # Alergia alimentar específica
    document.write_mini(dict_especifico['op_doenca_alerg_med'], (227, 722))  # Alergia medicamentosa
    document.write_mini(dict_especifico['op_doenca_alerg_med_espc'], (285, 725))  # Alergia medicamentosa específica
    document.write_mini(dict_especifico['op_doenca_diabete'], (227, 737))  # diabete
    document.write_mini(dict_especifico['op_doenca_imune'], (227, 751))  # Auto-imune
    document.write_mini(dict_especifico['op_doenca_imune_espec'], (285, 754))  # Auto-imune específica
    # coluna 1 2
    document.write_mini(dict_especifico['op_doenca_cardiaca'], (381, 692))  # Cardíaca
    document.write_mini(dict_especifico['op_doenca_cardiaca_espec'], (435, 694))  # Cardíaca Específica
    document.write_mini(dict_especifico['op_doenca_hepatica'], (381, 707))  # Hepática
    document.write_mini(dict_especifico['op_doenca_hepatica_espec'], (435, 710))  # Hepática Específica
    document.write_mini(dict_especifico['op_doenca_neuro'], (382, 723))  # Neurológica
    document.write_mini(dict_especifico['op_doenca_neuro_espc'], (435, 725))  # Neurológica Específica
    document.write_mini(dict_especifico['op_doenca_pulmonar'], (381, 738))  # Pulmonar
    document.write_mini(dict_especifico['op_doenca_pulmonar_espec'], (435, 740))  # Pulmonar Específica
    document.write_mini(dict_especifico['op_doenca_outra'], (381, 752))  # Outra
    document.write_mini(dict_especifico['op_doenca_outra_espec'], (435, 754))  # Outra Específica
    ###################################################
    document.write_mini(dict_especifico['med_anter_vacina'], (65, 797))  # Medicamento anterior a vacina
    # coluna 2 1
    document.write_mini(dict_especifico['op_med_anticonv'], (227, 766))  # Anticonvulsivante
    document.write_mini(dict_especifico['op_med_antiterm'], (227, 781))  # Antitérmico
    document.write_mini(dict_especifico['op_med_cort'], (227, 795))  # Corticoide
    document.write_mini(dict_especifico['op_med_cort_via'], (258, 797))  # Via de administração do corticoide
    document.write_mini(dict_especifico['med_tempo_uso'], (335, 797))  # Tempo de uso
    document.write_mini(dict_especifico['op_med_imunog'], (227, 810))  # Imunoglobulinas
    # coluna 2 2
    document.write_mini(dict_especifico['op_med_homeo'], (381, 766))  # Homeopático
    document.write_mini(dict_especifico['op_med_quimio'], (381, 781))  # Quimioterápico
    document.write_mini(dict_especifico['op_med_outro'], (381, 796))  # Outro
    document.write_mini(dict_especifico['op_med_outro_espec'], (417, 793))  # Outro Específico
    ################################################### fim da pagina 1
    document.write_mini(dict_especifico['transfusao'], (193, 47), pg=1)  # Transfusão
    document.write_date(dict_especifico['dt_transfusao'], (424, 47), spacing=2, font_size=10, pg=1)  # Data da transfusão
    document.write_mini(dict_especifico['hist_convulsoes'], (192, 68), pg=1)  # Histórico de convulsões
    document.write_mini(dict_especifico['tipo_convulsao'], (392, 68), pg=1)  # Tipo de convulsão
    document.write_mini(dict_especifico['eapv_anterior'], (62, 105), pg=1)  # EAPV anterior
    document.write_mini(dict_especifico['qual_eapv'], (188, 107), pg=1)  # Qual EAPV
    document.write_mini(dict_especifico['vac_adm_eapv'], (308, 107), pg=1)  # Vacina administrada no EAPV
    document.write_date(dict_especifico['dt_eapv_anterior'], (414, 107), spacing=2, font_size=12, pg=1)  # Data do EAPV anterior
    document.write_mini(dict_especifico['conduta_eapv'], (60, 145), pg=1)  # Conduta no EAPV
    document.write_mini(dict_especifico['medicacao_eapv'], (325, 144), pg=1)  # Medicação no EAPV
    document.write_mini(dict_especifico['qual_medicacao_eapv'], (412, 137), pg=1)  # Qual medicação no EAPV
    ####################################################
    # Antecedentes epidemiologicos
    ####################################################
    document.write_mini(dict_especifico['viajou_15dias'], (62, 185), pg=1)  # viajou nos ultimos 15 dias
    document.write_mini(dict_especifico['tipo_viagem'], (190, 185), pg=1)  # País da viagem
    document.write_mini(dict_especifico['pais_viagem'], (223, 190), pg=1)  # Data da viagem
    document.write_date(dict_especifico['dt_ida_viagem'], (290, 190), spacing=2, font_size=12, pg=1)  # Data da viagem
    document.write_date(dict_especifico['dt_volta_viagem'], (415, 190), spacing=2, font_size=12, pg=1)  # Data da viagem
    document.write_mini(dict_especifico['uf_viagem'], (62, 215), pg=1)  # uf viagem
    document.write_mini(dict_especifico['municipio_viagem'], (90, 215), pg=1)  # Município de viagem
    document.write_mini(dict_especifico['vac_antes_viagem'], (61, 249), pg=1)  # vacina antes viagem
    document.write_mini(dict_especifico['vac_durante_viagem'], (188, 249), pg=1)  # vacina durante viagem
    document.write_date(dict_especifico['dt_vac_durante_viagem'], (315, 249), spacing=1, pg=1, font_size=10,
                   printbars=True)  # Data da vacina durante viagem
    document.write_mini(dict_especifico['qual_vac_tomou'], (402, 249), pg=1)  # qual vacina tomou

    ####################################################
    # Dados EAPV
    ####################################################

    # coluna 1

    if dict_especifico['mani_loc_abs_frio'] == '1':
        document.write_cross((87, 283), 1, 9)  # abscesso frio
    if dict_especifico['mani_loc_abs_dren'] == '1':
        document.write_cross((87, 291), 1, 9)  # abscesso com drenagem
    if dict_especifico['mani_loc_abs_quente'] == '1':
        document.write_cross((87, 299), 1, 9)  # abscesso quente
    if dict_especifico['mani_loc_atrofia'] == '1':
        document.write_cross((87, 307), 1, 9)  # atrofia no local
    if dict_especifico['mani_loc_calor'] == '1':
        document.write_cross((87, 315), 1, 9)  # calor local
    if dict_especifico['mani_loc_celulite'] == '1':
        document.write_cross((87, 323), 1, 9)  # celulite
    if dict_especifico['mani_loc_dor'] == '1':
        document.write_cross((87, 331), 1, 9)  # dor

    # coluna 2

    if dict_especifico['mani_loc_edema'] == '1':
        document.write_cross((235, 283), 1, 9)  # edema
    if dict_especifico['mani_loc_enduracao'] == '1':
        document.write_cross((235, 291), 1, 9)  # enduracao
    if dict_especifico['mani_loc_eritema'] == '1':
        document.write_cross((235, 299), 1, 9)  # eritema
    if dict_especifico['mani_loc_exan_local'] == '1':
        document.write_cross((235, 307), 1, 9)  # enxatema local
    if dict_especifico['mani_loc_exan_gene'] == '1':
        document.write_cross((235, 315), 1, 9)  # enxatema generalizado
    if dict_especifico['mani_loc_linfadenite_nao_sup'] == '1':
        document.write_cross((235, 323), 1, 9)  # linfadenite nao supurada
    if dict_especifico['mani_loc_linfadenite_sup'] == '1':
        document.write_cross((235, 331), 1, 9)  # linfadenite supurada

    # coluna 3

    if dict_especifico['mani_loc_linfa3cm'] == '1':
        document.write_cross((390, 283), 1, 9)  # linfadenomegalia >3cm
    if dict_especifico['mani_loc_linfa_nao_sup'] == '1':
        document.write_cross((390, 291), 1, 9)  # linfadenomegalia nao supurada
    if dict_especifico['mani_loc_rubor'] == '1':
        document.write_cross((390, 299), 1, 9)  # rubor
    if dict_especifico['mani_loc_ulcera'] == '1':
        document.write_cross((390, 307), 1, 9)  # ulcera
    if dict_especifico['mani_loc_outras'] == '1':
        document.write_cross((390, 315), 1, 9)  # outras

    document.write_date(dict_especifico['dt_sint_locais'], pos=(60, 358), spacing=1, pg=1, font_size=12)  # data dos sintomas
    document.write_text(dict_especifico['dia_vac_manif_loc'], pos=(178, 358), pg=1,
                   font_size=12)  # dias vacina manifestacao local
    document.write_text(dict_especifico['hr_vac_manif_loc'], pos=(218, 358), pg=1,
                   font_size=12)  # horas vacina manifestacao local
    document.write_text(dict_especifico['min_vac_manif_loc'], pos=(264, 358), pg=1,
                   font_size=12)  # minutos vacina manifestacao local
    document.write_text(dict_especifico['dias_evento_loc'], pos=(390, 358), pg=1, font_size=12)  # dias evento local
    document.write_text(dict_especifico['horas_evento_loc'], pos=(430, 358), pg=1, font_size=12)  # horas evento local
    document.write_text(dict_especifico['min_evento_loc'], pos=(475, 358), pg=1, font_size=12)  # minutos evento local

    ####################################################
    # Manifestacoes clinicas sistemicas
    ####################################################

    # Linha 1 Pele/Mucosas

    if dict_especifico['mani_sis_angi_labios'] == '1':
        document.write_cross((86, 390), pg=1, font_size=9)
    if dict_especifico['mani_sis_cianose'] == '1':
        document.write_cross((234, 390), pg=1, font_size=9)
    if dict_especifico['mani_sis_purpura'] == '1':
        document.write_cross((390, 390), pg=1, font_size=9)

    # Linha 2

    if dict_especifico['mani_sis_angi_laringe'] == '1':
        document.write_cross((86, 398), 1, 9)
    if dict_especifico['mani_sis_hiper'] == '1':
        document.write_cross((234, 398), 1, 9)
    if dict_especifico['mani_sis_urti_gener'] == '1':
        document.write_cross((390, 398), 1, 9)

    # Linha 3

    if dict_especifico['mani_sis_angi_lingua'] == '1':
        document.write_cross((86, 406), 1, 9)
    if dict_especifico['mani_sis_ictericia'] == '1':
        document.write_cross((234, 406), 1, 9)
    if dict_especifico['mani_sis_urti_local'] == '1':
        document.write_cross((390, 406), 1, 9)

    # Linha 4

    if dict_especifico['mani_sis_angi_membro'] == '1':
        document.write_cross((86, 414), 1, 9)
    if dict_especifico['mani_sis_palidez'] == '1':
        document.write_cross((234, 414), 1, 9)
    if dict_especifico['mani_sis_outro_evento'] == '1':
        document.write_cross((390, 414), 1, 9)

    # Linha 5

    if dict_especifico['mani_sis_angi_olho'] == '1':
        document.write_cross((86, 422), 1, 9)
    if dict_especifico['mani_sis_petequia'] == '1':
        document.write_cross((234, 422), 1, 9)

    # Linha 6

    if dict_especifico['mani_sis_angi_gener'] == '1':
        document.write_cross((86, 430), 1, 9)
    if dict_especifico['mani_sis_prurido'] == '1':
        document.write_cross((234, 430), 1, 9)

    # Linha Cardiovasculares

    if dict_especifico['mani_sis_hipotensao'] == '1':
        document.write_cross((86, 446), 1, 9)  # hipotensao
    if dict_especifico['mani_sis_taquicardia'] == '1':
        document.write_cross((234, 446), 1, 9)  # taquicardia
    if dict_especifico['mani_sis_bradicardia'] == '1':
        document.write_cross((390, 446), 1, 9)  # bradicardia

    # Linha 1 Respiratorias

    if dict_especifico['mani_sis_apneia'] == '1':
        document.write_cross((86, 463), 1, 9)  # apneia
    if dict_especifico['mani_sis_garganta'] == '1':
        document.write_cross((234, 463), 1, 9)  # garganta
    if dict_especifico['mani_sis_fech_garg'] == '1':
        document.write_cross((390, 463), 1, 9)  # fechamento da garganta

    # Linha 2

    if dict_especifico['mani_sis_bronco'] == '1':
        document.write_cross((86, 471), 1, 9)  # broncoespasmo
    if dict_especifico['mani_sis_espirro'] == '1':
        document.write_cross((234, 471), 1, 9)  # espirros
    if dict_especifico['mani_sis_taquipneia'] == '1':
        document.write_cross((390, 471), 1, 9)  # taquipneia

    # Linha 3

    if dict_especifico['mani_sis_dif_resp'] == '1':
        document.write_cross((86, 479), pg=1, font_size=9)  # dificuldade respiratoria
    if dict_especifico['mani_sis_rinorreia'] == '1':
        document.write_cross((234, 479), pg=1, font_size=9)  # rinorreia
    if dict_especifico['mani_sis_intercost'] == '1':
        document.write_cross((390, 479), pg=1, font_size=9)  # retração intercostal

    # Linha 4

    if dict_especifico['mani_sis_dispineia'] == '1':
        document.write_cross((86, 487), 1, 9)  # dispneia
    if dict_especifico['mani_sis_rouquidao'] == '1':
        document.write_cross((234, 487), 1, 9)  # rouquidão
    if dict_especifico['mani_sis_tosse_seca'] == '1':
        document.write_cross((390, 487), 1, 9)  # tosse seca

    # Linha 1 Neurologicas

    if dict_especifico['mani_sis_ataxia'] == '1':
        document.write_cross((86, 503), 1, 9)  # ataxia
    if dict_especifico['mani_sis_conv_toni'] == '1':
        document.write_cross((234, 503), 1, 9)  # convulsão tônico-clônica
    if dict_especifico['mani_sis_paresia'] == '1':
        document.write_cross((390, 503), 1, 9)  # paresia

    # Linha 2

    if dict_especifico['mani_sis_nivel_consc'] == '1':
        document.write_cross((86, 511), 1, 9)  # alteração do nível de consciência
    if dict_especifico['mani_sis_desmaio'] == '1':
        document.write_cross((234, 511), 1, 9)  # desmaio
    if dict_especifico['mani_sis_parestesia'] == '1':
        document.write_cross((390, 511), 1, 9)  # parestesia

    # Linha 3

    if dict_especifico['mani_sis_conv_afeb'] == '1':
        document.write_cross((86, 519), 1, 9)  # convulsão afebril
    if dict_especifico['mani_sis_hipotonia'] == '1':
        document.write_cross((234, 519), 1, 9)  # hipotonia
    if dict_especifico['mani_sis_resposta'] == '1':
        document.write_cross((390, 519), 1, 9)  # resposta a estímulos

    # Linha 4

    if dict_especifico['mani_sis_conv_feb'] == '1':
        document.write_cross((86, 527), pg=1, font_size=9)  # convulsão febril
    if dict_especifico['mani_sis_letargia'] == '1':
        document.write_cross((234, 527), pg=1, font_size=9)  # letargia
    if dict_especifico['mani_sis_sin_neuro'] == '1':
        document.write_cross((390, 527), pg=1, font_size=9)  # sinais neurológicos focais

    # Linha 5

    if dict_especifico['mani_sis_conv_focal'] == '1':
        document.write_cross((86, 535), pg=1, font_size=9)  # convulsão focal
    if dict_especifico['mani_sis_nao_resposta'] == '1':
        document.write_cross((234, 535), pg=1, font_size=9)  # não resposta a estímulos
    if dict_especifico['mani_sis_neuro_grave'] == '1':
        document.write_cross((390, 535), pg=1, font_size=9)  # neurologia grave

    # Linha 6

    if dict_especifico['mani_sis_conv_gener'] == '1':
        document.write_cross((86, 543), pg=1, font_size=9)  # convulsão generalizada
    if dict_especifico['mani_sis_memb_infer'] == '1':
        document.write_cross((234, 543), pg=1, font_size=9)  # membros inferiores
    if dict_especifico['mani_sis_outra_paral'] == '1':
        document.write_cross((390, 543), pg=1, font_size=9)  # outra paralisia

    # Linha 1 Gastrointestinais

    if dict_especifico['mani_sis_diarreia'] == '1':
        document.write_cross((86, 560), pg=1, font_size=9)  # diarreia
    if dict_especifico['mani_sis_fezes_sang'] == '1':
        document.write_cross((234, 560), pg=1, font_size=9)  # fezes sanguinolentas
    if dict_especifico['mani_sis_nausea'] == '1':
        document.write_cross((390, 560), pg=1, font_size=9)  # nausea

    # Linha 2

    if dict_especifico['mani_sis_abdomen'] == '1':
        document.write_cross((86, 568), pg=1, font_size=9)  # dor abdominal
    if dict_especifico['mani_sis_inva_intest'] == '1':
        document.write_cross((234, 568), pg=1, font_size=9)  # invaginação intestinal
    if dict_especifico['mani_sis_vomito'] == '1':
        document.write_cross((390, 568), pg=1, font_size=9)  # vomito

    # Linha 3

    if dict_especifico['mani_sis_enterro'] == '1':
        document.write_cross((86, 576), pg=1, font_size=9)  # enterorragia
    if dict_especifico['mani_sis_melena'] == '1':
        document.write_cross((234, 576), pg=1, font_size=9)  # melena

    document.write_date(dict_especifico['dt_sint_sistem'], (62, 602), pg=1, font_size=9, spacing=2)  # data dos sintomas
    document.write_text(dict_especifico['dia_vac_manif_sistem'], (178, 602), pg=1,
                   font_size=12)  # dias vacina manifestacao sistêmica
    document.write_text(dict_especifico['hr_vac_manif_sistem'], (218, 602), pg=1,
                   font_size=12)  # horas vacina manifestacao sistêmica
    document.write_text(dict_especifico['min_vac_manif_sistem'], (264, 602), pg=1,
                   font_size=12)  # minutos vacina manifestacao sistêmica
    document.write_text(dict_especifico['dias_evento_sistem'], (390, 602), pg=1, font_size=12)  # dias evento sistêmico
    document.write_text(dict_especifico['horas_evento_sistem'], (430, 602), pg=1, font_size=12)  # horas evento sistêmico
    document.write_text(dict_especifico['min_evento_sistem'], (475, 602), pg=1, font_size=12)  # minutos evento sistêmico

    ####################################################
    # Outras manifestacoes
    ####################################################

    # Linha 1

    if dict_especifico['otr_mani_artralgia'] == '1':
        document.write_cross((86, 623), pg=1, font_size=9)

    if dict_especifico['otr_mani_evi_sang'] == '1':
        document.write_cross((234, 623), pg=1, font_size=9)

    if dict_especifico['otr_mani_mialgia'] == '1':
        document.write_cross((390, 623), pg=1, font_size=9)

    # Linha 2

    if dict_especifico['otr_mani_artrite'] == '1':
        document.write_cross((86, 631), pg=1, font_size=9)

    if dict_especifico['otr_mani_fadiga'] == '1':
        document.write_cross((234, 631), pg=1, font_size=9)

    if dict_especifico['otr_mani_pancrea'] == '1':
        document.write_cross((390, 631), pg=1, font_size=9)

    # Linha 3

    if dict_especifico['otr_mani_cefaleia'] == '1':
        document.write_cross((86, 639), pg=1, font_size=9)

    if dict_especifico['otr_mani_feb_mais39'] == '1':
        document.write_cross((234, 639), pg=1, font_size=9)

    if dict_especifico['otr_mani_parotidite'] == '1':
        document.write_cross((390, 639), pg=1, font_size=9)

    # Linha 4

    if dict_especifico['otr_mani_cefa_vomito'] == '1':
        document.write_cross((86, 647), pg=1, font_size=9)  # cefaleia e vomito

    if dict_especifico['otr_mani_feb_menos39'] == '1':
        document.write_cross((234, 647), pg=1, font_size=9)  # febre <39

    if dict_especifico['otr_mani_sonolencia'] == '1':
        document.write_cross((390, 647), pg=1, font_size=9)  # sonolência

    # Linha 5

    if dict_especifico['otr_mani_choro'] == '1':
        document.write_cross((86, 655), pg=1, font_size=9)  # choro persistente

    if dict_especifico['otr_mani_hiper_bila'] == '1':
        document.write_cross((234, 655), pg=1, font_size=9)  # hiperbilirrubinemia

    if dict_especifico['otr_mani_outra'] == '1':
        document.write_cross((390, 655), pg=1, font_size=9)  # outra

    # Linha 6

    if dict_especifico['otr_mani_dif_deamb'] == '1':
        document.write_cross((86, 663), pg=1, font_size=9)  # dificuldade de deambulação

    if dict_especifico['otr_mani_hiper_art'] == '1':
        document.write_cross((234, 663), pg=1, font_size=9)  # hipertensão arterial

    # Linha 7

    if dict_especifico['otr_mani_edem_art'] == '1':
        document.write_cross((86, 671), pg=1, font_size=9)  # edema articular

    if dict_especifico['otr_mani_lesao_bcg'] == '1':
        document.write_cross((234, 671), pg=1, font_size=9)  # lesão de BCG

    document.write_date(dict_especifico['dt_sint_otr_mani'], (62, 697), pg=1, font_size=9, spacing=2)  # data dos sintomas
    document.write_text(dict_especifico['dia_vac_manif_otr_mani'], (185, 697), pg=1,
                   font_size=12)  # dias vacina manifestacao outras
    document.write_text(dict_especifico['hr_vac_manif_otr_mani'], (226, 697), pg=1,
                   font_size=12)  # horas vacina manifestacao outras
    document.write_text(dict_especifico['min_vac_manif_otr_mani'], (274, 697), pg=1,
                   font_size=12)  # minutos vacina manifestacao outras
    document.write_text(dict_especifico['dias_evento_otr_mani'], (390, 697), pg=1, font_size=12)  # dias evento outras
    document.write_text(dict_especifico['horas_evento_otr_mani'], (430, 697), pg=1, font_size=12)  # horas evento outras
    document.write_text(dict_especifico['min_evento_otr_mani'], (475, 697), pg=1, font_size=12)  # minutos evento outras

    ####################################################
    # Atendimento Medico
    ####################################################
    document.write_mini(dict_especifico['atend_medico'], (61, 756), pg=1)  # atendimento médico

    if dict_especifico['dt_atendimento']:
        document.write_mini(dict_especifico['dt_atendimento'][:-5], (124, 752), pg=1, spacing=1, font_size=7)  # data do atendimento
        document.write_mini(dict_especifico['dt_atendimento'][-4:], (124, 761), pg=1, spacing=1, font_size=7)  # data do atendimento

    document.write_mini(dict_especifico['tipo_atendimento'], (176, 756), pg=1)  # tipo de atendimento
    document.write_mini(dict_especifico['ficou_obs'], (243, 755), pg=1)  # ficou observacao
    document.write_mini(dict_especifico['horas_obs'], (306, 752), pg=1)  # horas de observacao
    document.write_mini(dict_especifico['ficou_enfermaria'], (332, 755), pg=1)  # ficou enfermaria
    document.write_mini(dict_especifico['dias_enfermaria'], (395, 752), pg=1)  # dias de enfermaria
    document.write_mini(dict_especifico['ficou_uti'], (415, 754), pg=1)  # ficou UTI
    document.write_mini(dict_especifico['dias_uti'], (476, 752), pg=1)  # dias de UTI

    if dict_especifico['dt_alta']:
        document.write_mini(dict_especifico['dt_alta'][:2], (495, 757), pg=1, font_size=9)  # data da alta
        document.write_mini(dict_especifico['dt_alta'][3:5], (510, 757), pg=1, font_size=9)  # data da alta
        document.write_mini(dict_especifico['dt_alta'][6:], (525, 757), pg=1, font_size=9)  # data da alta

    document.write_text(dict_especifico['nome_hosp_atendimento'], (61, 788), pg=1)  # nome do hospital
    document.write_mini(dict_especifico['tipo_loc_atendimento'], (414, 782), pg=1)  # tipo de local de atendimento
    document.write_text(dict_especifico['municipio_atendimento'], (61, 811), pg=1)  # município de atendimento
    document.write_text(dict_especifico['uf_atendimento'], (495, 811), pg=1)  # uf de atendimento

    #################################################### fim da pagina 2

    # informaçoes laboratoriais complementares
    document.write_date(dict_especifico['dt_col_hemograma'], (216, 73), pg=2, spacing=1, font_size=10,
                   printbars=True)  # data da coleta do hemograma
    document.write_mini(dict_especifico['hemacias_hemo'], (250, 93), pg=2)  # hemacias
    document.write_mini(dict_especifico['hemoglobina_hemo'], (324, 93), pg=2)  # hemoglobina
    document.write_mini(dict_especifico['hematocrito_hemo'], (386, 93), pg=2)  # hematocrito
    document.write_mini(dict_especifico['plaquetas_hemo'], (436, 93), pg=2)  # plaquetas
    document.write_mini(dict_especifico['leucocitos_hemo'], (250, 108), pg=2)  # leucocitos
    document.write_mini(dict_especifico['monocitos_hemo'], (324, 108), pg=2)  # monocitos
    document.write_mini(dict_especifico['linfocitos_hemo'], (386, 108), pg=2)  # linfocitos
    document.write_mini(dict_especifico['neutrofilos_hemo'], (430, 108), pg=2)  # neutrofilos
    document.write_mini(dict_especifico['eosinofilos_hemo'], (490, 108), pg=2)  # eosinofilos
    document.write_date(dict_especifico['dt_col_bioquimica'], (173, 129), pg=2, spacing=1, font_size=8,
                   printbars=True)  # data da coleta da bioquimica
    document.write_mini(dict_especifico['bili_total_bioq'], (248, 123), pg=2)  # bilirrubina total
    document.write_mini(dict_especifico['creatina_bioq'], (248, 136), pg=2)  # creatinina
    document.write_mini(dict_especifico['bili_dir_bioq'], (318, 123), pg=2)  # bilirrubina direta
    document.write_mini(dict_especifico['ast_bioq'], (386, 123), pg=2)  # AST
    document.write_mini(dict_especifico['inr_bioq'], (389, 136), pg=2)  # INR
    document.write_mini(dict_especifico['alt_bioq'], (431, 123), pg=2)  # ALT
    document.write_mini(dict_especifico['pt_bioq'], (431, 136), pg=2)  # TGO
    document.write_mini(dict_especifico['ureia_bioq'], (490, 123), pg=2)  # ureia
    document.write_mini(dict_especifico['ptt_bioq'], (492, 136), pg=2)  # PTT
    document.write_mini(dict_especifico['puncao_lombar'], (180, 153), pg=2)  # punção lombar
    document.write_date(dict_especifico['dt_puncao'], (294, 150), pg=2, spacing=1, printbars=True)  # data da punção
    document.write_mini(dict_especifico['leucocitos_cito'], (247, 171), pg=2)  # leucocitos
    document.write_mini(dict_especifico['glicose_cito'], (242, 194), pg=2)  # glicose
    document.write_mini(dict_especifico['neutrofilos_cito'], (288, 174), pg=2)  # neutrofilos
    document.write_mini(dict_especifico['proteinas_cito'], (288, 194), pg=2)  # proteinas
    document.write_mini(dict_especifico['linfocitos_cito'], (336, 174), pg=2)  # linfocitos
    document.write_mini(dict_especifico['cult_liquor'], (441, 172), pg=2)  # cultura do liquor
    document.write_mini(dict_especifico['cult_liquor_espec'], (488, 170), pg=2)  # cultura do liquor especifica
    document.write_mini(dict_especifico['bacterioscopia2'], (441, 192), pg=2)  # bacterioscopia
    document.write_mini(dict_especifico['bacterio_espec'], (488, 191), pg=2)  # bacterioscopia especifica
    document.write_mini(dict_especifico['deteccao_viral'], (180, 220), pg=2)  # detecção viral
    document.write_mini(dict_especifico['dt_detec_viral'], (284, 218), pg=2, spacing=2)  # data da detecção viral
    document.write_mini(dict_especifico['detec_viral_coleta'], (390, 220), pg=2)  # detecção viral coleta
    document.write_mini(dict_especifico['detec_viral_pcr'], (242, 250), pg=2)  # detecção viral PCR
    document.write_mini(dict_especifico['detec_viral_outro'], (386, 256), pg=2)  # detecção viral outro
    document.write_mini(dict_especifico['autopsia'], (180, 274), pg=2)  # autopsia
    document.write_mini(dict_especifico['dt_autopsia'], (258, 272), pg=2, spacing=2)  # data da autopsia
    document.write_mini(dict_especifico['autop_anatomo'], (242, 295), pg=2)  # autopsia anatomopatologica
    document.write_mini(dict_especifico['autop_histo'], (242, 315), pg=2)  # autopsia histopatologica
    document.write_mini(dict_especifico['autop_imuno'], (242, 335), pg=2)  # autopsia imunohistoquimica
    document.write_mini(dict_especifico['autop_dt_anatomo'], (402, 293), pg=2, spacing=2)  # autopsia data anatomopatologica
    document.write_mini(dict_especifico['autop_dt_histo'], (402, 313), pg=2, spacing=2)  # autopsia data histopatologica
    document.write_mini(dict_especifico['autop_dt_imuno'], (402, 333), pg=2, spacing=2)  # autopsia data imunohistoquimica
    ####################################################
    document.write_mini(dict_especifico['dt_ecg'], (222, 351), pg=2, spacing=1)  # ECG
    document.write_mini(dict_especifico['dt_rm'], (432, 351), pg=2, spacing=1)  # RM
    document.write_mini(dict_especifico['dt_eeg'], (222, 365), pg=2, spacing=1)  # EEG
    document.write_mini(dict_especifico['dt_enmg'], (432, 365), pg=2, spacing=1)  # ENMG
    document.write_mini(dict_especifico['dt_rx'], (222, 378), pg=2, spacing=1)  # RX
    document.write_mini(dict_especifico['dt_usg'], (432, 378), pg=2, spacing=1)  # USG
    document.write_mini(dict_especifico['dt_tc'], (222, 392), pg=2, spacing=1)  # TC
    document.write_box(dict_especifico['outras_informacoes'], rect=(55, 415, 548, 490), pg=2)  # Outras informações
    ####################################################
    # Diagnostico
    ####################################################
    document.write_text(dict_especifico['diag_descricao1'], (58, 523), pg=2)  # Diagnóstico 1
    document.write_text(dict_especifico['diag_cid1'], (285, 523), pg=2)  # CID 1
    document.write_text(dict_especifico['diag_descricao2'], (58, 533), pg=2)  # Diagnóstico 2
    document.write_text(dict_especifico['diag_cid2'], (285, 533), pg=2)  # CID 2
    document.write_text(dict_especifico['diag_descricao3'], (58, 543), pg=2)  # Diagnóstico 3
    document.write_text(dict_especifico['diag_cid3'], (285, 543), pg=2)  # CID 3
    document.write_text(dict_especifico['diag_descricao4'], (58, 553), pg=2)  # Diagnóstico 4
    document.write_text(dict_especifico['diag_cid4'], (285, 553), pg=2)  # CID 4

    document.write_mini(dict_especifico['erro_programa'], (66, 596), pg=2, spacing=1)  # erro de programa
    document.write_mini(dict_especifico['erro_programa_espec'], (385, 602), pg=2)  # erro de programa dict_especifico
    document.write_mini(dict_especifico['evolucao_caso'], (63, 676), pg=2)  # evolução do caso
    document.write_mini(dict_especifico['dt_obito'], (177, 646), pg=2, spacing=1)  # data do óbito
    document.write_mini(dict_especifico['declara_obito'], (176, 672), pg=2)  # declaração de óbito
    document.write_mini(dict_especifico['declara_vivo'], (176, 699), pg=2)  # declaração de vivo
    document.write_mini(dict_especifico['conduta_vacinal'], (286, 676), pg=2)  # conduta vacinal
    document.write_mini(dict_especifico['dt_encerramento'], (460, 672), pg=2, spacing=1)  # data de encerramento
    document.write_mini(dict_especifico['nome_investigador'], (58, 740), pg=2)  # nome do investigador
    document.write_mini(dict_especifico['funcao_investigador'], (315, 740), pg=2)  # função do investigador
    document.write_mini(dict_especifico['telefone_investigador'], (430, 740), pg=2)  # telefone do investigador
    document.write_mini(dict_especifico['municipio_us_investigador'], (58, 760), pg=2)  # município do investigador
    document.write_mini(dict_especifico['unid_saude_investigador'], (58, 782), pg=2)  # unidade de saúde do investigador
    document.write_mini(dict_especifico['telefone_us_investigador'], (430, 782), pg=2)  # telefone da unidade de saúde
    document.write_mini(dict_especifico['assinatura_investigador'], (58, 802), pg=2)  # assinatura do investigador
    document.write_date(dict_especifico['dt_preenchimento'], (431, 800), pg=2, spacing=2)  # data de preenchimento

    document.save(nome_arquivo, path_pdf_gerado, notificatoriaCSV, modelo_pdf_base)
