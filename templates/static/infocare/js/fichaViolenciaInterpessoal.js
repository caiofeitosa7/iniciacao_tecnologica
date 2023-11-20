function submit_info() {
  let csrfToken = getCookie("csrftoken")
  let cod_ficha = document.getElementById("cod-ficha").value
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
  let campo_unidade_notificadora = document.getElementById(
    "campo-unidade-notificadora"
  ).value
  let campo_nome_un_notificadora = document.getElementById(
    "campo-nome-un-notificadora"
  ).value
  let campo_codigo_unidade_saude = document.getElementById(
    "campo-codigo-unidade-saude"
  ).value
  let campo_unidade_saude = document.getElementById("campo-unidade-saude").value
  let campo_cod_cnes_unidade_saude = document.getElementById(
    "campo-cod-cnes-unidade-saude"
  ).value
  let campo_dt_violencia = document.getElementById("campo-dt-violencia").value
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
  let campo_uf_residencia = document.getElementById("campo-uf-residencia").value
  let campo_municipio_residencia = document.getElementById(
    "campo-municipio-residencia"
  ).value
  let campo_cod_ibge_residencia = document.getElementById(
    "campo-cod-ibge-residencia"
  ).value
  let campo_distrito = document.getElementById("campo-distrito").value
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
  let campo_nome_social = document.getElementById("campo-nome-social").value
  let campo_ocupacao = document.getElementById("campo-ocupacao").value
  let campo_estado_civil = document.getElementById("campo-estado-civil").value
  let campo_orientacao_sexual = document.getElementById(
    "campo-orientacao-sexual"
  ).value
  let campo_identidade_genero = document.getElementById(
    "campo-identidade-genero"
  ).value
  let campo_possui_deficiencia = document.getElementById(
    "campo-possui-deficiencia"
  ).value
  let opcao_deficiencia_fisica = document.getElementById(
    "opcao-deficiencia-fisica"
  ).value
  let opcao_deficiencia_intelectual = document.getElementById(
    "opcao-deficiencia-intelectual"
  ).value
  let opcao_deficiencia_visual = document.getElementById(
    "opcao-deficiencia-visual"
  ).value
  let opcao_deficiencia_auditiva = document.getElementById(
    "opcao-deficiencia-auditiva"
  ).value
  let opcao_deficiencia_mental = document.getElementById(
    "opcao-deficiencia-mental"
  ).value
  let opcao_deficiencia_comportamento = document.getElementById(
    "opcao-deficiencia-comportamento"
  ).value
  let opcao_deficiencia_outro = document.getElementById(
    "opcao-deficiencia-outro"
  ).value
  let descricao_deficiencia_outro = document.getElementById(
    "descricao-deficiencia-outro"
  ).value
  let campo_uf_ocorrencia = document.getElementById("campo-uf-ocorrencia").value
  let campo_municipio_ocorrencia = document.getElementById(
    "campo-municipio-ocorrencia"
  ).value
  let campo_cod_ibge_ocorrencia = document.getElementById(
    "campo-cod-ibge-ocorrencia"
  ).value
  let campo_distrito_ocorrencia = document.getElementById(
    "campo-distrito-ocorrencia"
  ).value
  let campo_bairro_ocorrencia = document.getElementById(
    "campo-bairro-ocorrencia"
  ).value
  let campo_logradouro_ocorrencia = document.getElementById(
    "campo-logradouro-ocorrencia"
  ).value
  let campo_codigo_ocorrencia = document.getElementById(
    "campo-codigo-ocorrencia"
  ).value
  let campo_numero_ocorrencia = document.getElementById(
    "campo-numero-ocorrencia"
  ).value
  let campo_complemento_ocorrencia = document.getElementById(
    "campo-complemento-ocorrencia"
  ).value
  let campo_geo_campo3 = document.getElementById("campo-geo-campo3").value
  let campo_geo_campo4 = document.getElementById("campo-geo-campo4").value
  let campo_ponto_ref_ocorrencia = document.getElementById(
    "campo-ponto-ref-ocorrencia"
  ).value
  let campo_zona_ocorrencia = document.getElementById(
    "campo-zona-ocorrencia"
  ).value
  let campo_hora_ocorrencia = document.getElementById(
    "campo-hora-ocorrencia"
  ).value
  let campo_local_ocorrencia = document.getElementById(
    "campo-local-ocorrencia"
  ).value
  let descricao_local_outro = document.getElementById(
    "descricao-local-outro"
  ).value
  let campo_outras_vezes_ocorrencia = document.getElementById(
    "campo-outras-vezes-ocorrencia"
  ).value
  let campo_autoprovocada_ocorrencia = document.getElementById(
    "campo-autoprovocada-ocorrencia"
  ).value
  let campo_motivacao_violencia = document.getElementById(
    "campo-motivacao-violencia"
  ).value
  let descricao_violencia_outro = document.getElementById(
    "descricao-violencia-outro"
  ).value
  let opcao_violencia_fisica = document.getElementById(
    "opcao-violencia-fisica"
  ).value
  let opcao_violencia_psicologica = document.getElementById(
    "opcao-violencia-psicologica"
  ).value
  let opcao_violencia_tortura = document.getElementById(
    "opcao-violencia-tortura"
  ).value
  let opcao_violencia_sexual = document.getElementById(
    "opcao-violencia-sexual"
  ).value
  let opcao_violencia_trafico_humano = document.getElementById(
    "opcao-violencia-trafico-humano"
  ).value
  let opcao_violencia_financeira = document.getElementById(
    "opcao-violencia-financeira"
  ).value
  let opcao_violencia_abandono = document.getElementById(
    "opcao-violencia-abandono"
  ).value
  let opcao_violencia_trabalho_infantil = document.getElementById(
    "opcao-violencia-trabalho-infantil"
  ).value
  let opcao_violencia_intervencao_legal = document.getElementById(
    "opcao-violencia-intervencao-legal"
  ).value
  let opcao_violencia_outros = document.getElementById(
    "opcao-violencia-outros"
  ).value
  let descricao_violencia_outros = document.getElementById(
    "descricao-violencia-outros"
  ).value
  let opcao_meio_agressao_espancamento = document.getElementById(
    "opcao-meio-agressao-espancamento"
  ).value
  let opcao_meio_agressao_enforcamento = document.getElementById(
    "opcao-meio-agressao-enforcamento"
  ).value
  let opcao_meio_agressao_objContundente = document.getElementById(
    "opcao-meio-agressao-objContundente"
  ).value
  let opcao_meio_agressao_objPerfurocortante = document.getElementById(
    "opcao-meio-agressao-objPerfurocortante"
  ).value
  let opcao_meio_agressao_objQuente = document.getElementById(
    "opcao-meio-agressao-objQuente"
  ).value
  let opcao_meio_agressao_envenenamento = document.getElementById(
    "opcao-meio-agressao-envenenamento"
  ).value
  let opcao_meio_agressao_armaFogo = document.getElementById(
    "opcao-meio-agressao-armaFogo"
  ).value
  let opcao_meio_agressao_ameaca = document.getElementById(
    "opcao-meio-agressao-ameaca"
  ).value
  let opcao_meio_agressao_outro = document.getElementById(
    "opcao-meio-agressao-outro"
  ).value
  let descricao_meio_agressao_outro = document.getElementById(
    "descricao-meio-agressao-outro"
  ).value
  let opcao_violencia_sexual_assedio = document.getElementById(
    "opcao-violencia-sexual-assedio"
  ).value
  let opcao_violencia_sexual_estupro = document.getElementById(
    "opcao-violencia-sexual-estupro"
  ).value
  let opcao_violencia_sexual_pornInfatil = document.getElementById(
    "opcao-violencia-sexual-pornInfatil"
  ).value
  let opcao_violencia_sexual_exploracaoSexual = document.getElementById(
    "opcao-violencia-sexual-exploracaoSexual"
  ).value
  let opcao_violencia_sexual_outros = document.getElementById(
    "opcao-violencia-sexual-outros"
  ).value
  let descricao_violencia_sexual_outros = document.getElementById(
    "descricao-violencia-sexual-outros"
  ).value
  let opcao_procedimento_dst = document.getElementById(
    "opcao-procedimento-dst"
  ).value
  let opcao_procedimento_hiv = document.getElementById(
    "opcao-procedimento-hiv"
  ).value
  let opcao_procedimento_hepatiteB = document.getElementById(
    "opcao-procedimento-hepatiteB"
  ).value
  let opcao_procedimento_sangue = document.getElementById(
    "opcao-procedimento-sangue"
  ).value
  let opcao_procedimento_semen = document.getElementById(
    "opcao-procedimento-semen"
  ).value
  let opcao_procedimento_secrecaoVaginal = document.getElementById(
    "opcao-procedimento-secrecaoVaginal"
  ).value
  let opcao_procedimento_contracepcao = document.getElementById(
    "opcao-procedimento-contracepcao"
  ).value
  let opcao_procedimento_aborto = document.getElementById(
    "opcao-procedimento-aborto"
  ).value
  let campo_numero_envolvidos = document.getElementById(
    "campo-numero-envolvidos"
  ).value
  let opcao_1_vinculo_pai = document.getElementById("opcao-1-vinculo-pai").value
  let opcao_2_vinculo_mae = document.getElementById("opcao-2-vinculo-mae").value
  let opcao_3_vinculo_padrasto = document.getElementById(
    "opcao-3-vinculo-padrasto"
  ).value
  let opcao_4_vinculo_madrasta = document.getElementById(
    "opcao-4-vinculo-madrasta"
  ).value
  let opcao_5_vinculo_conjuge = document.getElementById(
    "opcao-5-vinculo-conjuge"
  ).value
  let opcao_6_vinculo_ex_conjuge = document.getElementById(
    "opcao-6-vinculo-ex-conjuge"
  ).value
  let opcao_7_vinculo_namorad = document.getElementById(
    "opcao-7-vinculo-namorad"
  ).value
  let opcao_8_vinculo_ex_namorad = document.getElementById(
    "opcao-8-vinculo-ex-namorad"
  ).value
  let opcao_9_vinculo_filho = document.getElementById(
    "opcao-9-vinculo-filho"
  ).value
  let opcao_10_vinculo_irmao = document.getElementById(
    "opcao-10-vinculo-irmao"
  ).value
  let opcao_11_vinculo_amigos_conhecidos = document.getElementById(
    "opcao-11-vinculo-amigos-conhecidos"
  ).value
  let opcao_12_vinculo_desconhecido = document.getElementById(
    "opcao-12-vinculo-desconhecido"
  ).value
  let opcao_13_vinculo_cuidador = document.getElementById(
    "opcao-13-vinculo-cuidador"
  ).value
  let opcao_14_vinculo_patrao = document.getElementById(
    "opcao-14-vinculo-patrao"
  ).value
  let opcao_15_vinculo_relacao_institucional = document.getElementById(
    "opcao-15-vinculo-relacao-institucional"
  ).value
  let opcao_16_vinculo_policial = document.getElementById(
    "opcao-16-vinculo-policial"
  ).value
  let opcao_17_vinculo_propria_pessoa = document.getElementById(
    "opcao-17-vinculo-propria-pessoa"
  ).value
  let opcao_18_vinculo_outros = document.getElementById(
    "opcao-18-vinculo-outros"
  ).value
  let descricao_vinculo_grau_parentesco = document.getElementById(
    "descricao-vinculo-grau-parentesco"
  ).value
  let campo_sexo_autor = document.getElementById("campo-sexo-autor").value
  let campo_alcool_autor = document.getElementById("campo-alcool-autor").value
  let campo_ciclo_vida_autor = document.getElementById(
    "campo-ciclo-vida-autor"
  ).value
  let opcao_encaminhamento_redeSaude = document.getElementById(
    "opcao-encaminhamento-redeSaude"
  ).value
  let opcao_encaminhamento_redeAssistencial = document.getElementById(
    "opcao-encaminhamento-redeAssistencial"
  ).value
  let opcao_encaminhamento_redeEducacao = document.getElementById(
    "opcao-encaminhamento-redeEducacao"
  ).value
  let opcao_encaminhamento_atendimentoMulher = document.getElementById(
    "opcao-encaminhamento-atendimentoMulher"
  ).value
  let opcao_encaminhamento_conselhoTutelar = document.getElementById(
    "opcao-encaminhamento-conselhoTutelar"
  ).value
  let opcao_encaminhamento_conselhoIdoso = document.getElementById(
    "opcao-encaminhamento-conselhoIdoso"
  ).value
  let opcao_encaminhamento_delegaciaIdoso = document.getElementById(
    "opcao-encaminhamento-delegaciaIdoso"
  ).value
  let opcao_encaminhamento_direitosHumanos = document.getElementById(
    "opcao-encaminhamento-direitosHumanos"
  ).value
  let opcao_encaminhamento_ministerioPublico = document.getElementById(
    "opcao-encaminhamento-ministerioPublico"
  ).value
  let opcao_encaminhamento_delegaciaCrianca = document.getElementById(
    "opcao-encaminhamento-delegaciaCrianca"
  ).value
  let opcao_encaminhamento_delegaciaMulher = document.getElementById(
    "opcao-encaminhamento-delegaciaMulher"
  ).value
  let opcao_encaminhamento_outrasDelegacias = document.getElementById(
    "opcao-encaminhamento-outrasDelegacias"
  ).value
  let opcao_encaminhamento_justicaInfancia = document.getElementById(
    "opcao-encaminhamento-justicaInfancia"
  ).value
  let opcao_encaminhamento_defensoriaPublica = document.getElementById(
    "opcao-encaminhamento-defensoriaPublica"
  ).value
  let campo_violencia_relacionada = document.getElementById(
    "campo-violencia-relacionada"
  ).value
  let campo_emitida_CAT = document.getElementById("campo-emitida-CAT").value
  let campo_circusntancia_lesao = document.getElementById(
    "campo-circusntancia-lesao"
  ).value
  let campo_dt_encerramento = document.getElementById(
    "campo-dt-encerramento"
  ).value
  let campo_nome_acompanhante = document.getElementById(
    "campo-nome-acompanhante"
  ).value
  let campo_grau_parentesco = document.getElementById(
    "campo-grau-parentesco"
  ).value
  let campo_telefone_acompanhate = document.getElementById(
    "campo-telefone-acompanhate"
  ).value
  let campo_municipio_us_investigador = document.getElementById(
    "campo-municipio-us-investigador"
  ).value
  let campo_cod_us_investigador = document.getElementById(
    "campo-cod-us-investigador"
  ).value
  let campo_nome_investigador = document.getElementById(
    "campo-nome-investigador"
  ).value
  let campo_funcao_investigador = document.getElementById(
    "campo-funcao-investigador"
  ).value
  let campo_assinatura_investigador = document.getElementById(
    "campo-assinatura-investigador"
  ).value
}
