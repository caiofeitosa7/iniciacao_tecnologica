from .pdfWritter import PDFWriter


def gerar_pdf_anti_rabica(notificatoriaCSV: dict, dict_especifico: dict, modelo_pdf: str, modelo_pdf_base: str, path_pdf_gerado: str, nome_arquivo: str):
    document = PDFWriter(modelo_pdf)

    ###################################################
    # Dados do paciente
    ###################################################
    document.write_text(dict_especifico['numero_ficha2'],(470, 47))
    document.write_date(dict_especifico['dt_notificacao2'], (448, 111), spacing=2) #data_notificacao
    document.write_uf(dict_especifico['uf_notificacao2'], (55, 139)) #uf_notificacao
    document.write_text(dict_especifico['municipio_notificacao2'], (90, 140)) #municipio_notificacao __unid_saude 55,space=220
    document.write_code(dict_especifico['cod_ibge_notificacao2'], (475, 140),space=2) #cod_ibge
    document.write_text(dict_especifico['unidade_saude2'], (65, 168)) #cod_unid_saude
    document.write_code(dict_especifico['cod_unidade_saude2'], (335, 168),space=2) #cod_unid_saude
    document.write_date(dict_especifico['dt_atendimento'], (448, 168), spacing=2) #data_diagnostico
    ##############################################
    #####          NOTIFICACAO INDIVIDUAL     ####
    ##############################################
    document.write_text(dict_especifico['nome_paciente2'], (55, 198)) #nome
    document.write_date(dict_especifico['dt_nascimento2'], (448, 198), spacing=2) #data_nascimento
    document.write_code(dict_especifico['idade2'], (63, 228),space=2) #idade
    document.write_mini(dict_especifico['tipo_idade2'], (110, 220)) #tipo_idade
    document.write_mini(dict_especifico['sexo2'], (232, 213)) #sexo
    document.write_mini(dict_especifico['gestante2'], (428, 213)) #gestante
    document.write_mini(dict_especifico['raca2'], (553, 213)) #raça/cor
    document.write_mini(dict_especifico['escolaridade2'], (553, 243)) #escolaridade
    document.write_code(dict_especifico['numero_sus2'], (57, 288),space=2, font_size=10) #cartao_sus
    document.write_text(dict_especifico['nome_mae2'], (240, 288)) #nome_mae
    ##############################################
    #####          DADOS DE RESIDENCIA        ####
    ##############################################

    document.write_uf(dict_especifico['uf_residencia2'], (56, 318)) #uf_residencia
    document.write_text(dict_especifico['municipio_residencia2'], (95, 318)) #municipio_residencia
    document.write_code(dict_especifico['cod_ibge_residencia2'], (326, 318),space=2) #cod_ibge_residencia
    document.write_text(dict_especifico['distrito_residencia2'], (422, 318)) #endereco
    document.write_text(dict_especifico['bairro_residencia2'], (64, 342)) #bairro
    document.write_text(dict_especifico['logradouro_residencia2'], (210, 344)) #logradouro
    document.write_code(dict_especifico['codigo_residencia2'], (480, 344),space=2) #cod_logradouro
    document.write_text(dict_especifico['numero_residencia2'], (65, 367)) #numero
    document.write_text(dict_especifico['complemento_residencia2'], (120, 367)) #complemento
    document.write_text(dict_especifico['geo_campo1_2'], (415, 370)) #geo_campo_1
    document.write_text(dict_especifico['geo_campo2_2'], (55, 393)) #geo_campo_2
    document.write_text(dict_especifico['ponto_ref_residencia2'], (230, 393)) #ponto_ref
    document.write_code(dict_especifico['cep_residencia2'], (455, 396),space=2) #cep
    document.write_telefone(dict_especifico['telefone_residencia2'], (57, 420), space=2) #telefone
    document.write_mini(dict_especifico['zona_residencia2'], (333, 408)) #zona
    document.write_text(dict_especifico['pais_residencia2'], (380, 420)) #pais
    ####################################################
    # Dados Complementares
    ####################################################
    document.write_text(dict_especifico['ocupacao'], (60, 470)) #ocupacao
    document.write_mini(dict_especifico['exp_virus_indireto'], (192, 492)) #tipo_exposicao
    document.write_mini(dict_especifico['exp_virus_arranhadura'], (271, 492)) #virus_arranhadura
    document.write_mini(dict_especifico['exp_virus_lambedura'], (340, 492)) #virus_lambedura
    document.write_mini(dict_especifico['exp_virus_mordedura'], (405, 492)) #virus_mordedura
    document.write_mini(dict_especifico['exp_virus_outro'], (468, 492)) #virus_outra
    document.write_mini(dict_especifico['loc_mucosa'], (190, 521)) #local_mucosa
    document.write_mini(dict_especifico['loc_cabeca'], (233, 520)) #local_cabeca
    document.write_mini(dict_especifico['loc_maos_pes'], (309, 520)) #local_maos
    document.write_mini(dict_especifico['loc_tronco'], (360, 520)) #local_tronco
    document.write_mini(dict_especifico['loc_memb_superiores'], (400, 520)) #local_membros_sup
    document.write_mini(dict_especifico['loc_memb_inferiores'], (488, 521)) #local_membros_inf
    document.write_mini(dict_especifico['ferimento'], (204, 542)) #ferimento
    document.write_mini(dict_especifico['tp_ferimento_prof'], (357, 552)) #ferimento_profundo
    document.write_mini(dict_especifico['tp_ferimento_superf'], (425, 552)) #ferimento_superficial
    document.write_mini(dict_especifico['tp_ferimento_dilac'], (490, 551)) #ferimento_dilacerante
    document.write_date(dict_especifico['dt_exposicao'], (64, 585), spacing=2) #data_exposicao
    document.write_mini(dict_especifico['antec_trat_pre_exp'], (354, 582)) #antecedente_ar_pre_expo
    document.write_mini(dict_especifico['antec_trat_pos_exp'], (482, 582)) #antecedente_ar_pos_expo
    document.write_mini(dict_especifico['conclusao_trat_ant'], (298, 601)) #anti_rabico_concluido
    document.write_code(dict_especifico['num_doses_aplicadas'], (509, 613),space=2) #n_doses
    document.write_mini(dict_especifico['especie_animal'], (552, 625)) #espec_anim_agressor
    document.write_mini(dict_especifico['especie_animal_herb_espec'], (365, 635)) #herb_espec
    document.write_mini(dict_especifico['especie_animal_outro'], (460, 635)) #espec_outras
    document.write_mini(dict_especifico['cond_animal'], (289, 655)) #cond_animal
    document.write_mini(dict_especifico['anim_passivel_obs'], (554, 654)) #animal_obs
    document.write_mini(dict_especifico['trat_indicado'], (557, 692)) #trat_indicado
    document.write_mini(dict_especifico['produtor_vacina'], (559, 727)) #vacina_lab
    document.write_mini(dict_especifico['produtor_vacina_outro'], (425, 738)) #vacina_outros
    document.write_text(dict_especifico['lote_vacina'], (70, 770)) #num_lote
    document.write_date(dict_especifico['dt_vencimento'], (464, 770), spacing=2) #dt_vencimento
    ############################################## fim page
    document.write_date(dict_especifico['dt_dose1'], (72, 80),pg=1, spacing=2) #dt_dose_1
    document.write_date(dict_especifico['dt_dose2'], (160, 80),pg=1, spacing=2) #dt_dose_2
    document.write_date(dict_especifico['dt_dose3'], (248, 80),pg=1, spacing=2) #dt_dose_3
    document.write_date(dict_especifico['dt_dose4'], (336, 80),pg=1, spacing=2) #dt_dose_4
    document.write_date(dict_especifico['dt_dose5'], (424, 80),pg=1, spacing=2) #dt_dose_5
    document.write_mini(dict_especifico['cond_final_animal'], (552, 98),pg=1) #cond_fin_animal
    document.write_mini(dict_especifico['interrup_trat'], (203, 140),pg=1) #interr_tratamento
    document.write_mini(dict_especifico['motivo_interrup_trat'], (549, 142),pg=1) #motivo_interrupcao
    document.write_mini(dict_especifico['procurou_paciente'], (408, 181),pg=1) #abandono
    document.write_mini(dict_especifico['evento_adv_vacina'], (561, 175),pg=1) #evento_adverso_vac
    document.write_mini(dict_especifico['soro_antirabico'], (198, 210),pg=1) #indic_soro_ar
    document.write_code(dict_especifico['peso_paciente'], (249, 232),pg=1,space=1) #peso_paciente
    document.write_mini(dict_especifico['tipo_soro_aplicado'], (551, 210),pg=1) #tipo_soro_aplic
    document.write_code(dict_especifico['quant_soro_aplicado'], (349, 230),pg=1,space=1) #qtd_soro_aplic
    document.write_mini(dict_especifico['infilt_soro_ferim_total'], (178, 265),pg=1) #infiltra_soro_total
    document.write_mini(dict_especifico['infilt_soro_ferim_parcial'], (227, 265),pg=1) #infiltra_soro_parcial
    document.write_mini(dict_especifico['lab_produtor_soro'], (551, 249),pg=1) #lab_prod_soro
    document.write_mini(dict_especifico['lab_produtor_soro_outro'], (487, 266),pg=1) #lab_prod_text
    document.write_code(dict_especifico['num_partida'], (58, 303),pg=1,space=2) #num_partida
    document.write_mini(dict_especifico['evento_adv_soro'], (355, 295),pg=1) #evento_adv_soro
    document.write_date(dict_especifico['dt_encerramento'], (382, 303),pg=1, spacing=2) #dt_encerramento
    document.write_box(dict_especifico['obs_adicionais'],pg=1, rect=(32, 320, 569, 515)) #obs
    document.write_text(dict_especifico['municipio_us_investigador'], (60, 543),pg=1) #municipio_investigador
    document.write_code(dict_especifico['cod_us_investigador'], (470, 543),pg=1,space=2) #cod_unid_saud
    document.write_text(dict_especifico['nome_investigador'], (60, 573),pg=1) #nome_investigador
    document.write_text(dict_especifico['funcao_investigador'], (265, 573),pg=1) #funcao_investigador
    document.write_text(dict_especifico['assinatura_investigador'], (473, 571),pg=1) #asign_investigador

    document.save(nome_arquivo, path_pdf_gerado, notificatoriaCSV, modelo_pdf_base)