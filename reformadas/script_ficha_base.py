def generateFicha(dictcsv=0):
  pdf = 'FichaNotificacao.pdf'
  try:
    from pdfWritter import PDFWriter
    document = PDFWriter(pdf)
    dict_geral = dictcsv
    #ficha geral
    document.write_text(dict_geral['numero_ficha'],(465,42))
    document.write_mini(dict_geral['tipo_notificacao'],(536,70))
    document.write_text(dict_geral['agravoDoenca'],(90,94))
    document.write_date(dict_geral['dt_notificacao'], (443, 97),spacing=2) #data-notificacao
    document.write_uf(dict_geral['uf_notificacao'], (66, 119),0) #uf-notificacao
    document.write_text(dict_geral['municipio_notificacao'], (97, 120),0) #municipio-notificacao --unid-saude 55,220
    document.write_code(dict_geral['cod_ibge_notificacao'], (470, 122),0,2) #cod-ibge
    document.write_text(dict_geral['unidade_saude'], (70, 142),0) #cod-unid-saude
    document.write_code(dict_geral['cod_unidade_saude'], (336, 144),0,2) #cod-unid-saude
    document.write_date(dict_geral['dt_sintomas'], (439, 145),spacing=2,font_size=13) #data-diagnostico
    ##############################################
    #####          NOTIFICACAO INDIVIDUAL     ####
    ##############################################
    document.write_text(dict_geral['nome_paciente'], (75, 167),0) #nome
    document.write_date(dict_geral['dt_nascimento'], (443, 169),spacing=2,font_size=13) #data-nascimento
    document.write_code(dict_geral['idade'], (73, 192),0,2) #idade
    document.write_mini(dict_geral['tipo_idade'], (118, 186),0) #tipo-idade
    document.write_mini(dict_geral['sexo'], (237, 181),0) #sexo
    document.write_mini(dict_geral['gestante'], (424, 182),0) #gestante
    document.write_mini(dict_geral['raca'], (544, 183),0) #raça/cor
    document.write_mini(dict_geral['escolaridade'], (544, 207),0) #escolaridade
    document.write_code(dict_geral['numero_sus'], (62, 242),0,1) #cartao-sus
    document.write_text(dict_geral['nome_mae'], (250, 241),0) #nome-mae
    document.write_date(dict_geral['dt_primeiro_sintoma'],(75, 267),font_size=12, spacing=2) #data-1-sintoma
    document.write_code(dict_geral['numero_casos_suspeitos'],(114, 293), space=2)
    document.write_mini(dict_geral['local_inicial_ocorrencia'],(529,261),spacing=2)
    document.write_mini(dict_geral['local_inicial_ocorrencia_outro'],(458,295), font_size=12)

    document.write_uf(dict_geral['uf_residencia'], (67, 320),0) #uf-residencia
    document.write_text(dict_geral['municipio_residencia'], (105, 320),0) #municipio-residencia
    document.write_code(dict_geral['cod_ibge_residencia'], (322, 320),space=2, font_size=13) #cod-ibge-residencia
    document.write_text(dict_geral['distrito_residencia'], (424, 321),0) #endereco
    document.write_text(dict_geral['bairro_residencia'], (75, 340),0) #bairro
    document.write_text(dict_geral['logradouro_residencia'], (210, 341),0) #logradouro
    document.write_code(dict_geral['codigo_residencia'], (473, 342),space=2,font_size=13) #cod-logradouro
    document.write_text(dict_geral['numero_residencia'], (69, 360),0) #numero
    document.write_text(dict_geral['complemento_residencia'], (130, 360),0) #complemento
    document.write_text(dict_geral['geo_campo1'], (415, 362),0) #geo-campo-1
    document.write_text(dict_geral['geo_campo2'], (70, 380),0) #geo-campo-2
    document.write_text(dict_geral['ponto_ref_residencia'], (230, 382),0) #ponto-ref
    document.write_code(dict_geral['cep_residencia'], (451, 384),space=2,font_size=11) #cep
    document.write_telefone(dict_geral['telefone_residencia'], (66, 403), space=2, font_size=12) #telefone
    document.write_mini(dict_geral['zona_residencia'], (331, 395),0) #zona
    document.write_text(dict_geral['pais_residencia'], (370, 403),0) #pais
    document.write_text(dict_geral['municipio_us_notificante'],(70,430)) #municipio hospital / unid saude
    document.write_text(dict_geral['nome_notificante'],(70,457)) #nome hospital
    document.write_text(dict_geral['funcao_notificante'],(255,458))
    document.write_text(dict_geral['assinatura_notificante'],(465,458))

    ##############################################
    #####          DADOS COMPLEMENTARES       ####
    ##############################################

    document.write_date(dict_geral['dt_amostra_sorologia'],(63, 550),spacing=2)
    document.write_date(dict_geral['dt_amostra_sorologia'],(176, 552),spacing=2)
    document.write_text(dict_geral['tipo_exame'],(300,551))
    document.write_mini(dict_geral['obito'],(272,566))
    document.write_mini(dict_geral['caso_semelhante'],(531,567))
    document.write_mini(dict_geral['exantema'],(213,590))
    document.write_date(dict_geral['dt_inicio_exantema'],(248, 606),spacing=2)
    document.write_mini(dict_geral['petequiaSufusao'],(539,595))
    document.write_mini(dict_geral['liquor'],(192,617))
    document.write_text(dict_geral['bacterioscopia'],(220, 630))
    document.write_mini(dict_geral['tomou_vacina'],(195,645))
    document.write_date(dict_geral['dt_ultima_dose_tomada'], (211, 661), spacing=2)
    document.write_mini(dict_geral['hospitalizacao'],(429, 647))
    document.write_date(dict_geral['dt_hospitalizacao'],(443, 664), spacing=2)
    document.write_uf(dict_geral['uf_hospital'], (65, 684))
    document.write_text(dict_geral['municipio_hospital'],(95, 686))
    document.write_code(dict_geral['cod_ibge_hospital'],(216, 688),space=2, font_size=13)
    document.write_text(dict_geral['nome_hospital'],(320, 688))
    document.write_code(dict_geral['cod_hospital'],(457,690), space=2, font_size=13)
    document.write_text(dict_geral['hipotese_diagnostica1'],(190, 714))
    document.write_text(dict_geral['hipotese_diagnostica2'],(190, 736))
    document.write_text(dict_geral['pais_infeccao'],(100, 769))
    document.write_text(dict_geral['distrito_infeccao'],(110, 790))
    document.write_uf(dict_geral['uf_infeccao'],(305,772))
    document.write_text(dict_geral['municipio_infeccao'],(385, 770))
    document.write_text(dict_geral['bairro_infeccao'],(375, 791))

    if __name__ == '__main__':
      document.save('ficha_base.pdf')
    return document
  except Exception as e:
    print('Erro ao gerar ficha geral.')
    print(e)




if __name__ == '__main__':
  dict_geral= {
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
  generateFicha(dict_geral)