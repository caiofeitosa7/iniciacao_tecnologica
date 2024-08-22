from .pdfWritter import PDFWriter

"""
Pra preencher os dicionarios abaixo com os dados do CSV, apos ler os dados salvar em um dicionario
primeiro tendo os 70 primeiros atributos
eu testei este comando para unir dicionarios:
dic_A = {'a': 1, 'b': 2, 'c': 3}
dic_B = {'a': 'aaaaaa', 'b': 'bbbbb, 'c': 'ccccccc'}
dic_A.update(dic_B) # {'a': 'aaaaaa', 'b': 'bbbbb, 'c': 'ccccccc'} 
chaves iguais ele atualiza o valor, se tiver chave a mais ele adiciona
"""

#dicionario notificatoria
notificatoriaCSV = {
    "numero_ficha": "abcdefg",
    "tipo_notificacao": "1",
    "agravoDoenca": "abcdefg",
    "dt_notificacao": "15/12/2021",
    "uf_notificacao": "PI",
    "municipio_notificacao": "abcdefg",
    "cod_ibge_notificacao": "123456",
    "unidade_saude": "abcdefg",
    "cod_unidade_saude": "1234567",
    "dt_sintomas": "15/12/2021",
    "nome_paciente": "abcdefg",
    "dt_nascimento": "15/12/2021",
    "idade": "25",
    "tipo_idade": "1",
    "sexo": "4",
    "gestante": "2",
    "raca": "9",
    "escolaridade": "9",
    "numero_sus": "123564879563245",
    "nome_mae": "abcdefg",
    "dt_primeiro_sintoma": "15/12/2021",
    "numero_casos_suspeitos": "10",
    "local_inicial_ocorrencia": "99",
    "local_inicial_ocorrencia_outro": "abcdefg",
    "uf_residencia": "PI",
    "municipio_residencia": "abcdefg",
    "cod_ibge_residencia": "123456",
    "distrito_residencia": "abcdefg",
    "bairro_residencia": "abcdefg",
    "logradouro_residencia": "abcdefg",
    "codigo_residencia": "123456",
    "numero_residencia": "3678",
    "complemento_residencia": "abcdefg",
    "geo_campo1": "abcdefg",
    "geo_campo2": "abcdefg",
    "ponto_ref_residencia": "abcdefg",
    "cep_residencia": "64016-630",
    "telefone_residencia": "86988256784",
    "zona_residencia": "9",
    "pais_residencia": "abcdefg",
    "municipio_us_notificante": "abcdefg",
    "nome_notificante": "abcdefg",
    "funcao_notificante": "abcdefg",
    "assinatura_notificante": "abcdefg",
    "dt_amostra_sorologia": "15/12/2021",
    "dt_outra_amostra": "15/12/2021",
    "tipo_exame": "abcdefg",
    "obito": "2",
    "caso_semelhante": "9",
    "exantema": "9",
    "dt_inicio_exantema": "15/12/2021",
    "petequiaSufusao": "9",
    "liquor": "9",
    "bacterioscopia": "abcdefg",
    "tomou_vacina": "9",
    "dt_ultima_dose_tomada": "15/12/2021",
    "hospitalizacao": "9",
    "dt_hospitalizacao": "15/12/2021",
    "uf_hospital": "PI",
    "municipio_hospital": "abcdefg",
    "cod_ibge_hospital": "1234567",
    "nome_hospital": "abcdefg",
    "cod_hospital": "1234567",
    "hipotese_diagnostica1": "abcdefg",
    "hipotese_diagnostica2": "abcdefg",
    "pais_infeccao": "abcdefg",
    "distrito_infeccao": "abcdefg",
    "uf_infeccao": "PI",
    "municipio_infeccao": "abcdefg",
    "bairro_infeccao": "abcdefg"
}

#dicionario da ficha
dict_espec = {
    "numero_ficha2": "18754",
    "dt_notificacao2": "15/12/2021",
    "uf_notificacao2": "PI",
    "municipio_notificacao2": "abcdefg",
    "cod_ibge_notificacao2": "123456",
    "unidade_saude2": "abcdefg",
    "cod_unidade_saude2": "1234567",
    "dt_diagnostico": "15/12/2021",
    "nome_paciente2": "abcdefg",
    "dt_nascimento2": "15/12/2021",
    "idade2": "25",
    "tipo_idade2": "9",
    "sexo2": "9",
    "gestante2": "9",
    "raca2": "9",
    "escolaridade2": "9",
    "numero_sus2": "123564879563245",
    "nome_mae2": "abcdefg",
    "uf_residencia2": "PI",
    "municipio_residencia2": "abcdefg",
    "cod_ibge_residencia2": "123456",
    "distrito_residencia2": "abcdefg",
    "bairro_residencia2": "abcdefg",
    "logradouro_residencia2": "abcdefg",
    "codigo_residencia2": "1234567",
    "numero_residencia2": "3678",
    "complemento_residencia2": "abcdefg",
    "geo_campo1_2": "abcdefg",
    "geo_campo2_2": "abcdefg",
    "ponto_ref_residencia2": "abcdefg",
    "cep_residencia2": "64016-630",
    "telefone_residencia2": "86988888888",
    "zona_residencia2": "1",
    "pais_residencia2": "abcdefg",
    "ocupacao": "abcdefg",
    "trans_vertical": "9",
    "trans_sexual": "9",
    "trans_droga_injetavel": "9",
    "trans_hemotransfusao": "9",
    "trans_transfusao": "9",
    "trans_mat_biologico": "9",
    "dt_transfusao": "15/12/2021",
    "uf_transfusao": "PI",
    "municipio_transfusao": "abcdefg",
    "cod_ibge_transfusao": "1234567",
    "instituicao_transfusao": "abcdefg",
    "cod_instit_transfusao": "1234567",
    "causa_infeccao": "8",
    "test_triagem_hiv": "8",
    "dt_coleta_triagem": "15/12/2021",
    "test_confirmatorio": "8",
    "dt_coleta_confirm": "15/12/2021",
    "test_rapido1": "9",
    "test_rapido2": "9",
    "test_rapido3": "9",
    "dt_coleta_rapida": "15/12/2021",
    "crit_kaposi": "9",
    "crit_tb_disseminada": "9",
    "crit_candidose": "9",
    "crit_tb_pulmonar": "9",
    "crit_herpes_zoster": "9",
    "crit_disf_snc": "9",
    "crit_diarreia": "9",
    "crit_febre": "9",
    "crit_caquexia": "9",
    "crit_astenia": "9",
    "crit_dermatite": "9",
    "crit_anemia": "9",
    "crit_tosse": "9",
    "crit_linfadeno": "9",
    "crit_cdc_ca_cervical": "9",
    "crit_cdc_candidose_eso": "9",
    "crit_cdc_candidose_traq": "9",
    "crit_cdc_citomegalovirose": "9",
    "crit_cdc_criptococose": "9",
    "crit_cdc_criptosporidiose": "9",
    "crit_cdc_herpes": "9",
    "crit_cdc_histoplasmose": "9",
    "crit_cdc_isosporidiose": "9",
    "crit_cdc_leucoencefalopatia": "9",
    "crit_cdc_linf_nao_hodgkin": "9",
    "crit_cdc_linf_cerebro": "9",
    "crit_cdc_micobacteriose": "9",
    "crit_cdc_pneumonia": "9",
    "crit_cdc_chagas": "9",
    "crit_cdc_salmonelose": "9",
    "crit_cdc_toxoplasmose": "9",
    "crit_cdc_linfocito": "9",
    "criterio_obito": "9",
    "uf_tratamento": "PI",
    "municipio_tratamento": "abcdefg",
    "cod_ibge_tratamento": "1234567",
    "us_tratamento": "abcdefg",
    "cod_ibge_us_tratamento": "1234567",
    "evolucao_caso": "9",
    "dt_obito": "15/12/2021",
    "nome_investigador": "abcdefg",
    "funcao_investigador": "abcdefg",
    "assinatura_investigador": "abcdefg"
}


def gerar_pdf_hiv(notificatoriaCSV: dict, dict_espec: dict, modelo_pdf: str, modelo_pdf_base: str, path_pdf_gerado: str, nome_arquivo: str):
    document = PDFWriter(modelo_pdf)

    ##############################################
    #####            DADOS GERAIS             ####
    ##############################################
    document.write_text(dict_espec["numero_ficha2"], (475, 44), 0)
    document.write_date(dict_espec['dt_notificacao2'], (448, 162), 0, spacing=2)  #data-notificacao
    document.write_uf(dict_espec['uf_notificacao2'], (55, 191), 0)  #uf-notificacao
    document.write_text(dict_espec['municipio_notificacao2'], (90, 191), 0)  #municipio-notificacao --unid-saude 55,220
    document.write_code(dict_espec['cod_ibge_notificacao2'], (477, 191), 0, 2)  #cod-ibge
    document.write_text(dict_espec['unidade_saude2'], (70, 220), 0)  #cod-unid-saude
    document.write_code(dict_espec['cod_unidade_saude2'], (340, 220), space=2)  #cod-unid-saude
    document.write_date(dict_espec['dt_diagnostico'], (448, 218), spacing=2)  #data-diagnostico
    ##############################################
    #####          NOTIFICACAO INDIVIDUAL     ####
    ##############################################
    document.write_text(dict_espec['nome_paciente2'], (55, 250), 0)  #nome
    document.write_date(dict_espec['dt_nascimento2'], (450, 249), spacing=2)  #data-nascimento
    document.write_code(dict_espec['idade2'], (65, 278), 0, 2)  #idade
    document.write_mini(dict_espec['tipo_idade2'], (112, 271), 0)  #tipo-idade
    document.write_mini(dict_espec['sexo2'], (234, 265), 0)  #sexo
    document.write_mini(dict_espec['gestante2'], (430, 265), 0)  #gestante
    document.write_mini(dict_espec['raca2'], (555, 265), 0)  #raça/cor
    document.write_mini(dict_espec['escolaridade2'], (555, 294), 0)  #escolaridade
    document.write_code(dict_espec['numero_sus2'], (53, 340), space=1, font_size=14)  #cartao-sus
    document.write_text(dict_espec['nome_mae2'], (240, 338), 0)  #nome-mae
    ##############################################
    #####          DADOS DE RESIDENCIA        ####
    ##############################################

    document.write_uf(dict_espec['uf_residencia2'], (56, 371), 0)  #uf-residencia
    document.write_text(dict_espec['municipio_residencia2'], (95, 371), 0)  #municipio-residencia
    document.write_code(dict_espec['cod_ibge_residencia2'], (327, 370), 0, 2)  #cod-ibge-residencia
    document.write_text(dict_espec['distrito_residencia2'], (424, 370), 0)  #endereco
    document.write_text(dict_espec['bairro_residencia2'], (64, 393), 0)  #bairro
    document.write_text(dict_espec['logradouro_residencia2'], (210, 395), 0)  #logradouro
    document.write_code(dict_espec['codigo_residencia2'], (480, 395), 0, 2)  #cod-logradouro
    document.write_text(dict_espec['numero_residencia2'], (60, 420), 0)  #numero
    document.write_text(dict_espec['complemento_residencia2'], (120, 420), 0)  #complemento
    document.write_text(dict_espec['geo_campo1_2'], (418, 422), 0)  #geo-campo-1
    document.write_text(dict_espec['geo_campo2_2'], (60, 445), 0)  #geo-campo-2
    document.write_text(dict_espec['ponto_ref_residencia2'], (230, 445), 0)  #ponto-ref
    document.write_cep(dict_espec['cep_residencia2'], (459, 449), space=2, font_size=12)  #cep
    document.write_telefone(dict_espec['telefone_residencia2'], (59, 472), space=2)  #telefone
    document.write_mini(dict_espec['zona_residencia2'], (335, 460))  #zona
    document.write_text(dict_espec['pais_residencia2'], (380, 472))  #pais

    ##############################################
    #####          DADOS COMPLEMENTARES       ####
    ##############################################
    document.write_text(dict_espec['ocupacao'], (70, 524))  #ocupacao
    document.write_mini(dict_espec['trans_vertical'], (238, 552))  #transmissao
    document.write_mini(dict_espec['trans_sexual'], (552, 548))  #orientacao-sexual
    document.write_mini(dict_espec['trans_droga_injetavel'], (287, 594))  #uso-drogas
    document.write_mini(dict_espec['trans_hemotransfusao'], (287, 613))  #tratamento-hemotransfusao
    document.write_mini(dict_espec['trans_transfusao'], (486, 594))  #transfussao
    document.write_mini(dict_espec['trans_mat_biologico'], (486, 612))  #acidente-biologico
    document.write_date(dict_espec['dt_transfusao'], (68, 652), spacing=2)  #data-transfussao
    document.write_uf(dict_espec['uf_transfusao'], (186, 652))  #uf-transfussao
    document.write_text(dict_espec['municipio_transfusao'], (230, 652))  #municipio-transfussao
    document.write_code(dict_espec['cod_ibge_transfusao'], (482, 652), space=2)  #ibge-transfussao
    document.write_text(dict_espec['instituicao_transfusao'], (70, 680))  #instituicao-transfussao
    document.write_code(dict_espec['cod_instit_transfusao'], (468, 680), space=2)  #cod-instituicao-transfussao
    document.write_mini(dict_espec['causa_infeccao'], (545, 700))  #resultado-invest-aids
    ##############################################
    #####          DADOS COMPLEMENTARES LAB   ####
    ##############################################
    document.write_date(dict_espec['dt_coleta_triagem'], (164, 770), spacing=2)  #data-coleta-1
    document.write_date(dict_espec['dt_coleta_confirm'], (387, 770), spacing=2)  #data-coleta-2
    document.write_date(dict_espec['dt_coleta_rapida'], (368, 805), spacing=2)  #data-coleta-3
    document.write_mini(dict_espec['test_triagem_hiv'], (114, 761), 0)  #triagem
    document.write_mini(dict_espec['test_confirmatorio'], (312, 763), 0)  #confirmatorio
    document.write_mini(dict_espec['test_rapido1'], (157, 794), 0)  #rapido-1
    document.write_mini(dict_espec['test_rapido2'], (237, 795), 0)  #rapido-2
    document.write_mini(dict_espec['test_rapido3'], (315, 795), 0)  #rapido-3
    ##############################################
    #####        DOS COMPLEMENTARES DEF AIDS  ####
    ##############################################
    #COLUNA 1
    document.write_mini(dict_espec['crit_kaposi'], (70, 50), 1)  #sarcoma-de-kaposi
    document.write_mini(dict_espec['crit_tb_disseminada'], (70, 65), 1)  #tuberculose-ncavitaria
    document.write_mini(dict_espec['crit_candidose'], (70, 79), 1)  #candidose-oral-ou-leucoplasia
    document.write_mini(dict_espec['crit_tb_pulmonar'], (70, 94), 1)  #turbeculose-cavitaria
    document.write_mini(dict_espec['crit_herpes_zoster'], (70, 108), 1)  #herpes-zoster-menor-60
    document.write_mini(dict_espec['crit_disf_snc'], (70, 123), 1)  #disf-sist-nerv-central
    document.write_mini(dict_espec['crit_diarreia'], (70, 137), 1)  #diarreia-cronica
    document.write_mini(dict_espec['crit_febre'], (70, 151), 1)  #febre-maior-1-mes

    #COLUNA 2
    document.write_mini(dict_espec['crit_caquexia'], (304, 50), 1)  #perda-10-peso-1-mes
    document.write_mini(dict_espec['crit_astenia'], (304, 65), 1)  #astenia-maior-1-mes
    document.write_mini(dict_espec['crit_dermatite'], (304, 79), 1)  #dermatite-persistente
    document.write_mini(dict_espec['crit_anemia'], (304, 94), 1)  #anemia-linfopenia-trombocitopenia
    document.write_mini(dict_espec['crit_tosse'], (304, 108), 1)  #tosse-cronica-ou-pneumonia
    document.write_mini(dict_espec['crit_linfadeno'], (304, 123), 1)  #linfadenopatia->1-tempo->1-mes

    # CDC ADAPTADO
    #COLUNA 1
    document.write_mini(dict_espec['crit_cdc_ca_cervical'], (69, 182), 1)  #cancer-cervical-inv
    document.write_mini(dict_espec['crit_cdc_candidose_eso'], (69, 196), 1)  #candidose-esofago
    document.write_mini(dict_espec['crit_cdc_candidose_traq'], (69, 211), 1)  #candidose-traqueia-pulmao
    document.write_mini(dict_espec['crit_cdc_citomegalovirose'], (69, 225), 1)  #citomegalovirose
    document.write_mini(dict_espec['crit_cdc_criptococose'], (69, 240), 1)  #criptococose-extrapulmonar
    document.write_mini(dict_espec['crit_cdc_criptosporidiose'], (69, 254), 1)  #criptosporidiose-cronica
    document.write_mini(dict_espec['crit_cdc_herpes'], (69, 269), 1)  #herpes-simples
    document.write_mini(dict_espec['crit_cdc_histoplasmose'], (69, 285), 1)  #histoplasmose-disseminada
    document.write_mini(dict_espec['crit_cdc_isosporidiose'], (69, 299), 1)  #isossporidiose

    #COLUNA 2
    document.write_mini(dict_espec['crit_cdc_leucoencefalopatia'], (302, 181), 1)  #leucoencefalopatia
    document.write_mini(dict_espec['crit_cdc_linf_nao_hodgkin'], (302, 198), 1)  #linfoma-n-hodgkin
    document.write_mini(dict_espec['crit_cdc_linf_cerebro'], (302, 212), 1)  #linfoma-prim-cerebro
    document.write_mini(dict_espec['crit_cdc_micobacteriose'], (302, 226), 1)  #micobacteriose-disseminada
    document.write_mini(dict_espec['crit_cdc_pneumonia'], (302, 242), 1)  #pneumonia-pneumocystis
    document.write_mini(dict_espec['crit_cdc_chagas'], (302, 256), 1)  #reativacao-chagas
    document.write_mini(dict_espec['crit_cdc_salmonelose'], (302, 270), 1)  #salmonelose
    document.write_mini(dict_espec['crit_cdc_toxoplasmose'], (302, 285), 1)  #toxoplasmose-cerebral
    document.write_mini(dict_espec['crit_cdc_linfocito'], (302, 299), 1)  #cont-linfocito-T-baixa

    ##############################################
    #####          RESULTADO TRATAMENTO       ####
    ##############################################
    document.write_mini(dict_espec['criterio_obito'], (507, 328), 1)  #obito
    document.write_uf(dict_espec['uf_tratamento'], (56, 377), 1)  #uf-tratamento
    document.write_text(dict_espec['municipio_tratamento'], (95, 377), 1)  #municipio-tratamento
    document.write_code(dict_espec['cod_ibge_tratamento'], (252, 377), 1, 2)  #ibge-tratamento
    document.write_text(dict_espec['us_tratamento'], (350, 377), 1)  #instituicao-tratamento
    document.write_code(dict_espec['cod_ibge_us_tratamento'], (467, 377), 1, 2)  #cod-instituicao-tratamento
    document.write_mini(dict_espec['evolucao_caso'], (428, 392), 1)  #evolucao
    document.write_date(dict_espec['dt_obito'], (452, 410), pg=1, spacing=2)  #data-obito
    document.write_text(dict_espec['nome_investigador'], (70, 440), 1)  #nome-investigador
    document.write_text(dict_espec['funcao_investigador'], (380, 440), 1)  #func-investigador
    document.write_text(dict_espec['assinatura_investigador'], (70, 470), 1)  #assign-investigador
    document.save(nome_arquivo, path_pdf_gerado, notificatoriaCSV, modelo_pdf_base)