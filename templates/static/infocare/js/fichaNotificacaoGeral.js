function submitInfo() {
  let csrfToken = getCookie("csrftoken")
  let cod_ficha = document.getElementById("cod-ficha").value
  let campo_tipo_notificacao = document.getElementById(
    "campo-tipo-notificacao"
  ).value
  let campo_agravoDoenca = document.getElementById("campo-agravoDoenca").value
  let campo_dt_notificacao = document.getElementById(
    "campo-dt-notificacao"
  ).value
  let campo_uf_notificacao = document.getElementById(
    "campo-uf-notificacao"
  ).value
  let campo_municipio_notificacao = document.getElementById(
    "campo-municipio-notificacao"
  ).value
  let campo_cod_ibge_notificacao = document.getElementById(
    "campo-cod-ibge-notificacao"
  ).value
  let campo_unidade_saude = document.getElementById("campo-unidade-saude").value
  let campo_codigo_unidade_saude = document.getElementById(
    "campo-codigo-unidade-saude"
  ).value
  let campo_dt_sintomas = document.getElementById("campo-dt-sintomas").value
  let campo_nome_paciente = document.getElementById("campo-nome-paciente").value
  let campo_dt_nascimento = document.getElementById("campo-dt-nascimento").value
  let campo_idade = document.getElementById("campo-idade").value
  let campo_tipo_idade = document.getElementById("campo-tipo-idade").value
  let campo_sexo = document.getElementById("campo-sexo").value
  let campo_gestante = document.getElementById("campo-gestante").value
  let campo_raca = document.getElementById("campo-raca").value
  let campo_escolaridade = document.getElementById("campo-escolaridade").value
  let campo_numero_sus = document.getElementById("campo-numero-sus").value
  let campo_nome_mae = document.getElementById("campo-nome-mae").value
  let campo_dt_primeiro_sintoma = document.getElementById(
    "campo-dt-primeiro-sintoma"
  ).value
  let campo_numero_casos_suspeitos = document.getElementById(
    "campo-numero-casos-suspeitos"
  ).value
  let campo_local_inicial_ocorrencia = document.getElementById(
    "campo-local-inicial-ocorrencia"
  ).value
  let campo_local_especificar_ocorrencia = document.getElementById(
    "campo-local-especificar-ocorrencia"
  ).value
  let campo_uf_residencia = document.getElementById("campo-uf-residencia").value
  let campo_municipio_residencia = document.getElementById(
    "campo-municipio-residencia"
  ).value
  let campo_cod_ibge_residencia = document.getElementById(
    "campo-cod-ibge-residencia"
  ).value
  let campo_distrito_residencia = document.getElementById("campo-distrito-residencia").value
  let campo_bairro_residencia = document.getElementById(
    "campo-bairro-residencia"
  ).value
  let campo_logradouro_residencia = document.getElementById(
    "campo-logradouro-residencia"
  ).value
  let campo_codigo_residencia = document.getElementById(
    "campo-codigo-residencia"
  ).value
  let campo_numero_residencia = document.getElementById(
    "campo-numero-residencia"
  ).value
  let campo_complemento_residencia = document.getElementById(
    "campo-complemento-residencia"
  ).value
  let campo_geo_campo1 = document.getElementById("campo-geo-campo1").value
  let campo_geo_campo2 = document.getElementById("campo-geo-campo2").value
  let campo_ponto_ref_residencia = document.getElementById(
    "campo-ponto-ref-residencia"
  ).value
  let campo_cep_residencia = document.getElementById(
    "campo-cep-residencia"
  ).value
  let campo_telefone_residencia = document.getElementById(
    "campo-telefone-residencia"
  ).value
  let campo_zona_residencia = document.getElementById(
    "campo-zona-residencia"
  ).value
  let campo_pais_residencia = document.getElementById(
    "campo-pais-residencia"
  ).value
  let campo_municipio_us_notificante = document.getElementById(
    "campo-municipio-us-notificante"
  ).value
  let campo_nome_notificante = document.getElementById(
    "campo-nome-notificante"
  ).value
  let campo_funcao_notificante = document.getElementById(
    "campo-funcao-notificante"
  ).value
  let campo_assinatura_notificante = document.getElementById(
    "campo-assinatura-notificante"
  ).value
  let campo_dt_amostra_sorologia = document.getElementById(
    "campo-dt-amostra-sorologia"
  ).value
  let campo_dt_outra_amostra = document.getElementById(
    "campo-dt-outra-amostra"
  ).value
  let campo_tipo_exame = document.getElementById("campo-tipo-exame").value
  let campo_obito = document.getElementById("campo-obito").value
  let campo_caso_semelhante = document.getElementById(
    "campo-caso-semelhante"
  ).value
  let campo_exantema = document.getElementById("campo-exantema").value
  let campo_dt_inicio_exatema = document.getElementById(
    "campo-dt-inicio-exatema"
  ).value
  let campo_petequiaSufusao = document.getElementById(
    "campo-petequiaSufusao"
  ).value
  let campo_liquor = document.getElementById("campo-liquor").value
  let campo_bacterioscopia = document.getElementById(
    "campo-bacterioscopia"
  ).value
  let campo_tomou_vacina = document.getElementById("campo-tomou-vacina").value
  let campo_dt_ultima_dose_tomada = document.getElementById(
    "campo-dt-ultima-dose-tomada"
  ).value
  let campo_hospitalizacao = document.getElementById(
    "campo-hospitalizacao"
  ).value
  let campo_dt_hospitalizacao = document.getElementById(
    "campo-dt-hospitalizacao"
  ).value
  let campo_uf_hospital = document.getElementById("campo-uf-hospital").value
  let campo_municipio_hospital = document.getElementById(
    "campo-municipio-hospital"
  ).value
  let campo_cod_ibge_hospital = document.getElementById(
    "campo-cod-ibge-hospital"
  ).value
  let campo_nome_hospital = document.getElementById("campo-nome-hospital").value
  let campo_cod_hospital = document.getElementById("campo-cod-hospital").value
  let campo_hipotese_diagnostica1 = document.getElementById(
    "campo-hipotese-diagnostica1"
  ).value
  let campo_hipotese_diagnostica2 = document.getElementById(
    "campo-hipotese-diagnostica2"
  ).value
  let campo_pais_infeccao = document.getElementById("campo-pais-infeccao").value
  let campo_distrito_infeccao = document.getElementById(
    "campo-distrito-infeccao"
  ).value
  let campo_uf_infeccao = document.getElementById("campo-uf-infeccao").value
  let campo_municipio_infeccao = document.getElementById(
    "campo-municipio-infeccao"
  ).value
  let campo_bairro_infeccao = document.getElementById(
    "campo-bairro-infeccao"
  ).value
}
