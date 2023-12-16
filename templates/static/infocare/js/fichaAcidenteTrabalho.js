// function submit_info() {
//     let csrfToken = getCookie("csrftoken")
//     let cod_ficha = document.getElementById("numero-ficha").value
//     let campo_dt_notificacao = document.getElementById("campo-dt-notificacao").value
//     let campo_uf_notificacao = document.getElementById("campo-uf-notificacao").value
//     let campo_municipio_notificacao = document.getElementById("campo-municipio-notificacao").value
//     let campo_cod_ibge_notificacao = document.getElementById("campo-cod-ibge-notificacao").value
//     let campo_unidade_saude = document.getElementById("campo-unidade-saude").value
//     let campo_codigo_unidade_saude = document.getElementById("campo-codigo-unidade-saude").value
//     let campo_dt_acidente = document.getElementById("campo-dt-acidente").value
//     let campo_nome_paciente = document.getElementById("campo-nome-paciente").value
//     let campo_dt_nascimento = document.getElementById("campo-dt-nascimento").value
//     let campo_idade = document.getElementById("campo-idade").value
//     let campo_tipo_idade = document.getElementById("campo-tipo-idade").value
//     let campo_sexo = document.getElementById("campo-sexo").value
//     let campo_gestante = document.getElementById("campo-gestante").value
//     let campo_raca = document.getElementById("campo-raca").value
//     let campo_escolaridade = document.getElementById("campo-escolaridade").value
//     let campo_numero_sus = document.getElementById("campo-numero-sus").value
//     let campo_nome_mae = document.getElementById("campo-nome-mae").value
//     let campo_uf_residencia = document.getElementById("campo-uf-residencia").value
//     let campo_municipio_residencia = document.getElementById("campo-municipio-residencia").value
//     let campo_cod_ibge_residencia = document.getElementById("campo-cod-ibge-residencia").value
//     let campo_distrito_residencia = document.getElementById("campo-distrito-residencia").value
//     let campo_bairro_residencia = document.getElementById("campo-bairro-residencia").value
//     let campo_logradouro_residencia = document.getElementById("campo-logradouro-residencia").value
//     let campo_codigo_residencia = document.getElementById("campo-codigo-residencia").value
//     let campo_numero_residencia = document.getElementById("campo-numero-residencia").value
//     let campo_complemento_residencia = document.getElementById("campo-complemento-residencia").value
//     let campo_geo_campo1 = document.getElementById("campo-geo-campo1").value
//     let campo_geo_campo2 = document.getElementById("campo-geo-campo2").value
//     let campo_ponto_ref_residencia = document.getElementById("campo-ponto-ref-residencia").value
//     let campo_cep_residencia = document.getElementById("campo-cep-residencia").value
//     let campo_telefone_residencia = document.getElementById("campo-telefone-residencia").value
//     let campo_zona_residencia = document.getElementById("campo-zona-residencia").value
//     let campo_pais_residencia = document.getElementById("campo-pais-residencia").value
//     let campo_ocupacao = document.getElementById("campo-ocupacao").value
//     let campo_situacao_mercado_trabalho = document.getElementById("campo-situacao-mercado-trabalho").value
//     let campo_tempo_trabalho = document.getElementById("campo-tempo-trabalho").value
//     let campo_tipo_tempo_trabalho = document.getElementById("campo-tipo-tempo-trabalho").value
//     let campo_local_acidente = document.getElementById("campo-local-acidente").value
//     let campo_cnpj_contratante = document.getElementById("campo-cnpj-contratante").value
//     let campo_nome_contratante = document.getElementById("campo-nome-contratante").value
//     let campo_atividade_contratante = document.getElementById("campo-atividade-contratante").value
//     let campo_uf_contratante = document.getElementById("campo-uf-contratante").value
//     let campo_municipio_contratante = document.getElementById("campo-municipio-contratante").value
//     let campo_cod_ibge_contratante = document.getElementById("campo-cod-ibge-contratante").value
//     let campo_distrito_contratante = document.getElementById("campo-distrito-contratante").value
//     let campo_bairro_contratante = document.getElementById("campo-bairro-contratante").value
//     let campo_endereco_contratante = document.getElementById("campo-endereco-contratante").value
//     let campo_numero_contratante = document.getElementById("campo-numero-contratante").value
//     let campo_ponto_ref_contratante = document.getElementById("campo-ponto-ref-contratante").value
//     let campo_telefone_contratante = document.getElementById("campo-telefone-contratante").value
//     let campo_empresa_terceirizada_contratante = document.getElementById("campo-empresa-terceirizada-contratante").value
//     let campo_cnae_emp_principal_contratante = document.getElementById("campo-cnae-emp-principal-contratante").value
//     let campo_cnpj_emp_principal_contratante = document.getElementById("campo-cnpj-emp-principal-contratante").value
//     let campo_razao_social_contratante = document.getElementById("campo-razao-social-contratante").value
//     let campo_hora_acidente = document.getElementById("campo-hora-acidente").value
//     let campo_minuto_acidente = document.getElementById("campo-minuto-acidente").value
//     let campo_hora_apos_inicio_jornada = document.getElementById("campo-hora-apos-inicio-jornada").value
//     let campo_minuto_apos_inicio_jornada = document.getElementById("campo-minuto-apos-inicio-jornada").value
//     let campo_uf_acidente = document.getElementById("campo-uf-acidente").value
//     let campo_municipio_acidente = document.getElementById("campo-municipio-acidente").value
//     let campo_codigo_acidente = document.getElementById("campo-codigo-acidente").value
//     let campo_cod_causa_acidente = document.getElementById("campo-cod-causa-acidente").value
//     let campo_tipo_acidente = document.getElementById("campo-tipo-acidente").value
//     let campo_outros_trabalhadores_acidente = document.getElementById("campo-outros-trabalhadores-acidente").value
//     let campo_quantos_trabalhadores_acidente = document.getElementById("campo-quantos-trabalhadores-acidente").value
//     let campo_ocorreu_atendimento = document.getElementById("campo-ocorreu-atendimento").value
//     let campo_dt_atendimento = document.getElementById("campo-dt-atendimento").value
//     let campo_uf_atendimento = document.getElementById("campo-uf-atendimento").value
//     let campo_municipio_atendimento = document.getElementById("campo-municipio-atendimento").value
//     let campo_cod_ibge_atendimento = document.getElementById("campo-cod-ibge-atendimento").value
//     let campo_nome_us_atendimento = document.getElementById("campo-nome-us-atendimento").value
//     let campo_cod_us_atendimento = document.getElementById("campo-cod-us-atendimento").value
//     let campo_partes_corpo_atendimento1 = document.getElementById("campo-partes-corpo-atendimento1").value
//     let campo_partes_corpo_atendimento2 = document.getElementById("campo-partes-corpo-atendimento2").value
//     let campo_partes_corpo_atendimento3 = document.getElementById("campo-partes-corpo-atendimento3").value
//     let campo_diagnostico_atendimento = document.getElementById("campo-diagnostico-atendimento").value
//     let campo_regime_tratamento_atendimento = document.getElementById("campo-regime-tratamento-atendimento").value
//     let campo_evolucao_caso = document.getElementById("campo-evolucao-caso").value
//     let campo_dt_obito = document.getElementById("campo-dt-obito").value
//     let campo_comunicacao_acidente_trabalho = document.getElementById("campo-comunicacao-acidente-trabalho").value
//     let campo_municipio_us_investigador = document.getElementById("campo-municipio-us-investigador").value
//     let campo_cod_us_investigador = document.getElementById("campo-cod-us-investigador").value
//     let campo_nome_investigador = document.getElementById("campo-nome-investigador").value
//     let campo_funcao_investigador = document.getElementById("campo-funcao-investigador").value
//     let campo_assinatura_investigador = document.getElementById("campo-assinatura-investigador").value
// }

function atribuirValor(elementId) {
    let valorDoCampo = document.getElementById(elementId).value;
    let novoElementId = elementId + "2";

    document.getElementById(novoElementId).value = valorDoCampo;
}

function pesquisaCep(elemento) {
    let cep = elemento.value.replace(/\D/g, ''); // somente numeros

    console.log(cep);

    if (cep != "") {
        let validacep = /^[0-9]{8}$/;

        if (validacep.test(cep)) {
            let apiUrl = 'https://viacep.com.br/ws/'+ cep + '/json/';

            fetch(apiUrl)
                .then(response => {
                    if (!response.ok)
                        throw new Error('Erro ao consultar o CEP');

                    return response.json();
                })
                .then(data => {
                    elemento.value = data["cep"];
                    document.getElementById(elemento.id + "2").value = data["cep"];
                    document.getElementById("campo-uf-residencia").value = data["uf"];
                    document.getElementById("campo-uf-residencia2").value = data["uf"];
                    document.getElementById("campo-municipio-residencia").value = data["localidade"];
                    document.getElementById("campo-municipio-residencia2").value = data["localidade"];
                    document.getElementById("campo-cod-ibge-residencia").value = data["ibge"];
                    document.getElementById("campo-cod-ibge-residencia2").value = data["ibge"];
                    document.getElementById("campo-bairro-residencia").value = data["bairro"];
                    document.getElementById("campo-bairro-residencia2").value = data["bairro"];
                    document.getElementById("campo-logradouro-residencia").value = data["logradouro"];
                    document.getElementById("campo-logradouro-residencia2").value = data["logradouro"];
                })
                .catch(error => {
                    console.error('Erro na requisição:', error);
                    elemento.value = "";
                    document.getElementById(elemento.id + "2").value = "";
                    document.getElementById("campo-uf-residencia").value = "";
                    document.getElementById("campo-uf-residencia2").value = "";
                    document.getElementById("campo-municipio-residencia").value = "";
                    document.getElementById("campo-municipio-residencia2").value = "";
                    document.getElementById("campo-cod-ibge-residencia").value = "";
                    document.getElementById("campo-cod-ibge-residencia2").value = "";
                    document.getElementById("campo-bairro-residencia").value = "";
                    document.getElementById("campo-bairro-residencia2").value = "";
                    document.getElementById("campo-logradouro-residencia").value = "";
                    document.getElementById("campo-logradouro-residencia2").value = "";
                });
        }
        else {
            console.error('Erro na requisição:', error);
            elemento.value = "";
            document.getElementById(elemento.id + "2").value = "";
            document.getElementById("campo-uf-residencia").value = "";
            document.getElementById("campo-municipio-residencia").value = "";
            document.getElementById("campo-cod-ibge-residencia").value = "";
            document.getElementById("campo-bairro-residencia").value = "";
            document.getElementById("campo-logradouro-residencia").value = "";
        }
    }
}
























