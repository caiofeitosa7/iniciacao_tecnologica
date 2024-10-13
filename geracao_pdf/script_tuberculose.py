from .pdfWritter import PDFWriter


def gerar_pdf_tuberculose(notificatoriaCSV: dict, dict_especifico: dict, modelo_pdf: str, modelo_pdf_base: str, path_pdf_gerado: str, nome_arquivo: str):
    document = PDFWriter(modelo_pdf)
    
    ##############################################
    #####          DADOS GERAIS               ####
    ##############################################

    document.write_text(dict_especifico["numero_ficha2"],(470, 30),0)
    document.write_date(dict_especifico['dt_notificacao2'], (442, 135),0,spacing=2) #data-notificacao
    document.write_uf(dict_especifico['uf_notificacao2'], (55, 167),0) #uf-notificacao
    document.write_text(dict_especifico['municipio_notificacao2'], (90, 167),0) #municipio-notificacao --unid-saude 55,220
    document.write_code(dict_especifico['cod_ibge_notificacao2'], (475, 167),0,2) #cod-ibge
    document.write_text(dict_especifico['unidade_saude2'], (67, 193),0) #cod-unid-saude
    document.write_code(dict_especifico['cod_unidade_saude2'], (334, 193), space=2) #cod-unid-saude
    document.write_date(dict_especifico['dt_diagnostico'], (440, 193),spacing=2) #data-diagnostico

    ##############################################
    #####          NOTIFICACAO INDIVIDUAL     ####
    ##############################################

    document.write_text(dict_especifico['nome_paciente2'], (55, 223),0) #nome
    document.write_date(dict_especifico['dt_nascimento2'], (444, 224),spacing=2) #data-nascimento
    document.write_code(dict_especifico['idade2'], (63, 253),0,2) #idade
    document.write_mini(dict_especifico['tipo_idade2'], (111, 246),0) #tipo-idade
    document.write_mini(dict_especifico['sexo2'], (228, 240),0) #sexo
    document.write_mini(dict_especifico['gestante2'], (424, 240),0) #gestante
    document.write_mini(dict_especifico['raca2'], (548, 240),0) #raça/cor
    document.write_mini(dict_especifico['escolaridade2'], (547, 269),0) #escolaridade
    document.write_code(dict_especifico['numero_sus2'], (53, 315), space=1, font_size=14) #cartao-sus
    document.write_text(dict_especifico['nome_mae2'], (235, 315),0) #nome-mae

    ##############################################
    #####          DADOS DE RESIDENCIA        ####
    ##############################################

    document.write_uf(dict_especifico['uf_residencia2'], (56, 345),0) #uf-residencia
    document.write_text(dict_especifico['municipio_residencia2'], (87, 344),0) #municipio-residencia
    document.write_code(dict_especifico['cod_ibge_residencia2'], (323, 344),0,2) #cod-ibge-residencia
    document.write_text(dict_especifico['distrito_residencia2'], (416, 344),0) #distrito
    document.write_text(dict_especifico['bairro_residencia2'], (64, 367),0) #bairro
    document.write_text(dict_especifico['logradouro_residencia2'], (206, 369),0) #logradouro
    document.write_code(dict_especifico['codigo_residencia2'], (476, 369),0,2) #cod-logradouro
    document.write_text(dict_especifico['numero_residencia2'], (65, 393),0) #numero da residencia
    document.write_text(dict_especifico['complemento_residencia2'], (120, 393),0) #complemento
    document.write_text(dict_especifico['geo_campo1_2'], (416, 395),0) #geo-campo-1
    document.write_text(dict_especifico['geo_campo2_2'], (58, 418),0) #geo-campo-2
    document.write_text(dict_especifico['ponto_ref_residencia2'], (225, 418),0) #ponto-ref
    document.write_cep(dict_especifico['cep_residencia2'], (457 , 421),space=2,font_size=12) #cep
    document.write_telefone(dict_especifico['telefone_residencia2'], (59, 446), space=2) #telefone
    document.write_mini(dict_especifico['zona_residencia2'], (329, 434)) #zona
    document.write_text(dict_especifico['pais_residencia2'], (368, 445)) #pais

    ##############################################
    #####          DADOS COMPLEMENTARES       ####
    ##############################################

    document.write_telefone(dict_especifico['num_prontuario'], (59, 488), space=2) #numero do prontuario
    document.write_mini(dict_especifico['tipo_entrada'], (547, 476 )) #tipo de entrada
    document.write_mini(dict_especifico['pop_priv_liberdade'], (177, 502)) #pop_priv_liberdade
    document.write_mini(dict_especifico['pop_situacao_rua'], (177, 514)) #pop_situacao_rua
    document.write_mini(dict_especifico['pop_prof_saude'], (310, 503)) #pop_prof_saude
    document.write_mini(dict_especifico['pop_imigrante'], (330, 514)) #pop_imigrante
    document.write_mini(dict_especifico['transf_renda'], (551, 504)) #tipo de entrada
    document.write_mini(dict_especifico['forma'], (224, 534)) #forma
    document.write_mini(dict_especifico['se_extrapulmonar'], (546, 534)) #se_extrapulmonar
    document.write_mini(dict_especifico['se_extrapulmonar_outra'], (508, 550)) #se_extrapulmonar_outra
    document.write_mini(dict_especifico['agravo_aids'], (197, 571)) #agravo_aids
    document.write_mini(dict_especifico['agravo_alcool'], (242, 572)) #agravo_alcool
    document.write_mini(dict_especifico['agravo_diabetes'], (310, 572)) #agravo_diabetes
    document.write_mini(dict_especifico['agravo_mental'], (373, 572)) #agravo_mental
    document.write_mini(dict_especifico['agravo_droga'], (196, 586)) #agravo_droga
    document.write_mini(dict_especifico['agravo_tabagismo'], (329, 586)) #agravo_tabagismo
    document.write_mini(dict_especifico['agravo_outras'], (393, 586)) #agravo_outras
    document.write_mini(dict_especifico['agravo_outras_descricao'], (428, 586)) #agravo_outras_descricao
    document.write_mini(dict_especifico['bacilo_escarro'], (209, 603)) #bacilo_escarro
    document.write_mini(dict_especifico['radio_torax'], (386, 605)) #radio_torax
    document.write_mini(dict_especifico['teste_hiv'], (542, 604)) #teste_hiv
    document.write_mini(dict_especifico['terapia_tb'], (236, 656)) #terapia_tb
    document.write_mini(dict_especifico['histopatologia'], (534, 638)) #histopatologia
    document.write_mini(dict_especifico['cultura'], (136, 679)) #cultura
    document.write_mini(dict_especifico['teste_molec_tmr'], (319, 678)) #teste_molec_tmr
    document.write_mini(dict_especifico['teste_sensibilidade'], (536, 681)) #teste_sensibilidade
    document.write_date(dict_especifico['dt_tratamento_atual'], (85,755), spacing=2) #dt_tratamento_atual
    document.write_code(dict_especifico['total_contatos'], (310, 752), 0, 2) #total_contatos
    document.write_text(dict_especifico['municipio_us_investigador'], (58, 782),pg=0) #municipio_investigador
    document.write_code(dict_especifico['cod_us_investigador'], (452, 782), pg=0,space=2) #cod_unid_saude
    document.write_mini(dict_especifico['nome_investigador'], (55, 808),0, font_size=8) #nome-investigador
    document.write_mini(dict_especifico['funcao_investigador'], (250, 810),0) #func-investigador 
    document.write_mini(dict_especifico['assinatura_investigador'], (455, 810),0, font_size=8) #assign-investigador

    document.save(nome_arquivo, path_pdf_gerado, notificatoriaCSV, modelo_pdf_base)