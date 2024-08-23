from .pdfWritter import PDFWriter


def gerar_pdf_acid_animal_peconhento(notificatoriaCSV: dict, dict_especifico: dict, modelo_pdf: str, modelo_pdf_base: str, path_pdf_gerado: str, nome_arquivo: str):
    document = PDFWriter(modelo_pdf)

    ###################################################
    # Dados do paciente
    ###################################################

    document.write_text(dict_especifico['numero_ficha2'],(467, 37))
    document.write_date(dict_especifico['dt_notificacao2'], (446, 150), spacing=2) #data_notificacao
    document.write_uf(dict_especifico['uf_notificacao2'], (55, 180)) #uf_notificacao
    document.write_text(dict_especifico['municipio_notificacao2'], (90, 179)) #municipio_notificacao __unid_saude 55,220
    document.write_code(dict_especifico['cod_ibge_notificacao2'], (475, 179),space=2) #cod_ibge
    document.write_text(dict_especifico['unidade_saude2'], (65, 208)) #cod_unid_saude
    document.write_code(dict_especifico['cod_unidade_saude2'], (335, 208),space=2) #cod_unid_saude
    document.write_date(dict_especifico['dt_sintomas2'], (444, 206), spacing=2) #data_diagnostico
    ##############################################
    #####          NOTIFICACAO INDIVIDUAL     ####
    ##############################################
    document.write_text(dict_especifico['nome_paciente2'], (55, 238)) #nome
    document.write_date(dict_especifico['dt_nascimento2'], (446, 238), spacing=2) #data_nascimento
    document.write_code(dict_especifico['idade2'], (63, 268),space=2) #idade
    document.write_mini(dict_especifico['tipo_idade2'], (110, 260)) #tipo_idade
    document.write_mini(dict_especifico['sexo2'], (231, 253)) #sexo
    document.write_mini(dict_especifico['gestante2'], (427, 253)) #gestante
    document.write_mini(dict_especifico['raca2'], (552, 253)) #raça/cor
    document.write_mini(dict_especifico['escolaridade2'], (552, 283)) #escolaridade
    document.write_code(dict_especifico['numero_sus2'], (56, 328),space=2, font_size=10) #cartao_sus
    document.write_text(dict_especifico['nome_mae2'], (240, 328)) #nome_mae
    ##############################################
    #####          DADOS DE RESIDENCIA        ####
    ##############################################

    document.write_uf(dict_especifico['uf_residencia2'], (56, 358)) #uf_residencia
    document.write_text(dict_especifico['municipio_residencia2'], (95, 358)) #municipio_residencia
    document.write_code(dict_especifico['cod_ibge_residencia2'], (323, 358),space=2) #cod_ibge_residencia
    document.write_text(dict_especifico['distrito_residencia2'], (422, 358)) #endereco
    document.write_text(dict_especifico['bairro_residencia2'], (64, 382)) #bairro
    document.write_text(dict_especifico['logradouro_residencia2'], (210, 383)) #logradouro
    document.write_code(dict_especifico['codigo_residencia2'], (479, 383),space=2) #cod_logradouro
    document.write_text(dict_especifico['numero_residencia2'], (65, 407)) #numero
    document.write_text(dict_especifico['complemento_residencia2'], (120, 407)) #complemento
    document.write_text(dict_especifico['geo_campo1_2'], (415, 410)) #geo_campo_1
    document.write_text(dict_especifico['geo_campo2_2'], (55, 433)) #geo_campo_2
    document.write_text(dict_especifico['ponto_ref_residencia2'], (230, 433)) #ponto_ref
    document.write_code(dict_especifico['cep_residencia2'], (456, 436),space=2) #cep
    document.write_telefone(dict_especifico['telefone_residencia2'], (55, 460), space=2) #telefone
    document.write_mini(dict_especifico['zona_residencia2'], (333, 448)) #zona
    document.write_text(dict_especifico['pais_residencia2'], (380, 459)) #pais
    ##############################################
    #####        DADOS  COMPLEMENTARES        ####
    ##############################################
    document.write_date(dict_especifico['dt_investigacao'], (60, 509),spacing=2) #data_investigacao
    document.write_text(dict_especifico['ocupacao'], (180, 510)) #ocupacao
    document.write_date(dict_especifico['dt_acidente'], (453, 510),spacing=2) #data_acidente
    document.write_uf(dict_especifico['uf_ocorr'], (57, 538)) #uf_acidente
    document.write_text(dict_especifico['municipio_ocorr'], (95, 538),font_size=12) #municipio_acidente
    document.write_code(dict_especifico['cod_ibge_ocorr'], (264, 537),space=2) #cod_ibge_acidente
    document.write_text(dict_especifico['local_ocorr'], (365, 538)) #local_acidente
    document.write_mini(dict_especifico['zona_ocorr'], (230, 551)) #zona_acidente
    document.write_mini(dict_especifico['tempo_picada'], (553, 553)) #tempo_decorrido
    document.write_code(dict_especifico['local_picada'], (139, 587), space=1) #local_picada
    document.write_mini(dict_especifico['manif_local'], (177, 610)) #manifes_locais
    document.write_mini(dict_especifico['manif_dor'], (212, 625)) #manifes_dor
    document.write_mini(dict_especifico['manif_edema'], (252, 626)) #manifes_edema
    document.write_mini(dict_especifico['manif_equimose'], (306, 625)) #manifes_equimose
    document.write_mini(dict_especifico['manif_necrose'], (364, 626)) #manifes_necrose
    document.write_mini(dict_especifico['manif_outro'], (428, 627)) #manifes_outras
    document.write_mini(dict_especifico['manif_outro_descricao'], (500, 626)) #manifes_text
    document.write_mini(dict_especifico['manif_sistemica'], (123, 666)) #manifes_sistemica
    document.write_mini(dict_especifico['manif_sist_neurop'], (155, 672)) #neuroparaliticas
    document.write_mini(dict_especifico['manif_sist_miolit'], (155, 693)) #mioliticas
    document.write_mini(dict_especifico['manif_sist_hemorr'], (289, 664)) #hemorragicas
    document.write_mini(dict_especifico['manif_sist_renais'], (291, 687)) #renais
    document.write_mini(dict_especifico['manif_sist_vagais'], (410, 665)) #vagais
    document.write_mini(dict_especifico['manif_sist_outra'], (410, 685)) #sistemic_outras
    document.write_mini(dict_especifico['manif_sist_outra_descricao'], (426, 693)) #sistemic_text
    document.write_mini(dict_especifico['tempo_coagulacao'], (555, 670)) #tempo_coagular
    document.write_mini(dict_especifico['tipo_acidente'], (288, 716)) #tipo_acidente
    document.write_mini(dict_especifico['tipo_acidente_outro'], (175, 732)) #acidente_text
    document.write_mini(dict_especifico['serp_tipo_acid'], (539, 715)) #serpe_tipo
    document.write_mini(dict_especifico['aran_tipo_acid'], (286, 751)) #aranha_tipo
    document.write_mini(dict_especifico['lagar_tipo_acid'], (544, 753)) #lagarta_tipo
    ####### fim da pagina 1######################
    document.write_mini(dict_especifico['classif_caso'], (335, 45),pg=1) #class_caso
    document.write_mini(dict_especifico['soroterapia'], (549, 44),pg=1) #soroterapia
    document.write_code(dict_especifico['soroterapia_sab'], (187, 80),pg=1,space=2) #SAB
    document.write_code(dict_especifico['soroterapia_sabl'], (187, 97),pg=1,space=2) #SABL
    document.write_code(dict_especifico['soroterapia_sabc'], (187, 114),pg=1,space=2) #SABC
    document.write_code(dict_especifico['soroterapia_sac'], (355, 76),pg=1,space=2) #SAC
    document.write_code(dict_especifico['soroterapia_sae'], (355, 96),pg=1,space=2) #SAE
    document.write_code(dict_especifico['soroterapia_saes'], (355, 113),pg=1,space=2) #SAEs
    document.write_code(dict_especifico['soroterapia_saar'], (523, 76),pg=1,space=2) #SAAr
    document.write_code(dict_especifico['soroterapia_salox'], (525, 95),pg=1,space=2) #SALox
    document.write_code(dict_especifico['soroterapia_salon'], (526, 112),pg=1,space=2) #SALon
    document.write_mini(dict_especifico['comp_locais'], (163, 135),pg=1) #complica_locais
    document.write_mini(dict_especifico['comp_loc_infec'], (188, 150),pg=1) #infec_secundaria
    document.write_mini(dict_especifico['comp_loc_necrose'], (263, 150),pg=1) #necrose_extensa
    document.write_mini(dict_especifico['comp_loc_sindrome'], (328, 150),pg=1) #sindrome_compartimental
    document.write_mini(dict_especifico['comp_loc_deficit'], (422, 151),pg=1) #deficit_funcional
    document.write_mini(dict_especifico['comp_loc_amputacao'], (506, 150),pg=1) #amputacao
    document.write_mini(dict_especifico['comp_sistemica'], (178, 171),pg=1) #complica_sistemica
    document.write_mini(dict_especifico['comp_sist_renal'], (208, 185),pg=1) #sist_insuf_renal
    document.write_mini(dict_especifico['comp_sist_edema'], (286, 186),pg=1) #sist_edema_pulmonar
    document.write_mini(dict_especifico['comp_sist_septi'], (416, 186),pg=1) #sist_sepicemia
    document.write_mini(dict_especifico['comp_sist_choque'], (515, 185),pg=1) #sist_choque
    document.write_mini(dict_especifico['doenca_rel_trab'], (139, 214),pg=1) #acidente_trabalho
    document.write_mini(dict_especifico['evolucao_caso'], (279, 205),pg=1) #evolucao_caso
    document.write_date(dict_especifico['dt_obito'], (330, 233),pg=1,spacing=2) #data_obito
    document.write_date(dict_especifico['dt_encerramento'], (460, 233),pg=1,spacing=2) #data_encerramento
    document.write_box(dict_especifico['obs_adicionais'], 1,(32, 680, 568,740)) #observacoes
    document.write_text(dict_especifico['municipio_us_investigador'], (60, 745),pg=1) #municipio_investigador
    document.write_code(dict_especifico['cod_us_investigador'], (471, 745),pg=1,space=2) #cod_unid_investigador
    document.write_text(dict_especifico['nome_investigador'], (60, 768),pg=1) #nome_investigador
    document.write_text(dict_especifico['funcao_investigador'], (260, 768),pg=1) #funcao_investigador
    document.write_text(dict_especifico['assinatura_investigador'], (472, 768),pg=1) #assign_investigador

    document.save(nome_arquivo, path_pdf_gerado, notificatoriaCSV, modelo_pdf_base)