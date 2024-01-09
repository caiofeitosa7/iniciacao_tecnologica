function cadastrarFichaNotificacao(urlSetFichaNotificacao, urlHome) {
    let camposNumeros = document.querySelectorAll('input[type="number"]');
    camposNumeros.forEach(function(campo) {
        if (campo.value === "")
          campo.value = 0;
    });
    let csrfToken = getCookie("csrftoken");
    let cod_formulario = document.getElementById("cod-formulario").value;
    let prontuario = document.getElementById("prontuario").value;
    let setor = document.getElementById("setor").value;
    let numero_ficha = document.getElementById("numero-ficha").value;
    let campo_tipo_notificacao = document.getElementById("campo-tipo-notificacao").value;
    let campo_agravoDoenca = document.getElementById("campo-agravoDoenca").value;
    let campo_dt_notificacao = document.getElementById("campo-dt-notificacao").value;
    let campo_uf_notificacao = document.getElementById("campo-uf-notificacao").value;
    let campo_municipio_notificacao = document.getElementById("campo-municipio-notificacao").value;
    let campo_cod_ibge_notificacao = document.getElementById("campo-cod-ibge-notificacao").value;
    let campo_unidade_saude = document.getElementById("campo-unidade-saude").value
    let campo_cod_unidade_saude = document.getElementById("campo-cod-unidade-saude").value;
    let campo_dt_sintomas = document.getElementById("campo-dt-sintomas").value;
    let campo_nome_paciente = document.getElementById("campo-nome-paciente").value;
    let campo_dt_nascimento = document.getElementById("campo-dt-nascimento").value;
    let campo_idade = document.getElementById("campo-idade").value;
    let campo_tipo_idade = document.getElementById("campo-tipo-idade").value;
    let campo_sexo = document.getElementById("campo-sexo").value;
    let campo_gestante = document.getElementById("campo-gestante").value;
    let campo_raca = document.getElementById("campo-raca").value;
    let campo_escolaridade = document.getElementById("campo-escolaridade").value;
    let campo_numero_sus = document.getElementById("campo-numero-sus").value;
    let campo_nome_mae = document.getElementById("campo-nome-mae").value;
    let campo_dt_primeiro_sintoma = document.getElementById("campo-dt-primeiro-sintoma").value;
    let campo_numero_casos_suspeitos = document.getElementById("campo-numero-casos-suspeitos").value;
    let campo_local_inicial_ocorrencia = document.getElementById("campo-local-inicial-ocorrencia").value;
    let campo_local_especificar_ocorrencia = document.getElementById("campo-local-especificar-ocorrencia").value;
    let campo_uf_residencia = document.getElementById("campo-uf-residencia").value;
    let campo_municipio_residencia = document.getElementById("campo-municipio-residencia").value;
    let campo_cod_ibge_residencia = document.getElementById("campo-cod-ibge-residencia").value;
    let campo_distrito_residencia = document.getElementById("campo-distrito-residencia").value;
    let campo_bairro_residencia = document.getElementById("campo-bairro-residencia").value;
    let campo_logradouro_residencia = document.getElementById("campo-logradouro-residencia").value;
    let campo_codigo_residencia = document.getElementById("campo-codigo-residencia").value;
    let campo_numero_residencia = document.getElementById("campo-numero-residencia").value;
    let campo_complemento_residencia = document.getElementById("campo-complemento-residencia").value;
    let campo_geo_campo1 = document.getElementById("campo-geo-campo1").value;
    let campo_geo_campo2 = document.getElementById("campo-geo-campo2").value;
    let campo_ponto_ref_residencia = document.getElementById("campo-ponto-ref-residencia").value;
    let campo_cep_residencia = document.getElementById("campo-cep-residencia").value;
    let campo_telefone_residencia = document.getElementById("campo-telefone-residencia").value;
    let campo_zona_residencia = document.getElementById("campo-zona-residencia").value;
    let campo_pais_residencia = document.getElementById("campo-pais-residencia").value;
    let campo_municipio_us_notificante = document.getElementById("campo-municipio-us-notificante").value;
    let campo_nome_notificante = document.getElementById("campo-nome-notificante").value;
    let campo_funcao_notificante = document.getElementById("campo-funcao-notificante").value;
    let campo_assinatura_notificante = document.getElementById("campo-assinatura-notificante").value;
    let campo_dt_amostra_sorologia = document.getElementById("campo-dt-amostra-sorologia").value;
    let campo_dt_outra_amostra = document.getElementById("campo-dt-outra-amostra").value;
    let campo_tipo_exame = document.getElementById("campo-tipo-exame").value;
    let campo_obito = document.getElementById("campo-obito").value;
    let campo_caso_semelhante = document.getElementById("campo-caso-semelhante").value;
    let campo_exantema = document.getElementById("campo-exantema").value;
    let campo_dt_inicio_exantema = document.getElementById("campo-dt-inicio-exatema").value;
    let campo_petequiaSufusao = document.getElementById("campo-petequiaSufusao").value;
    let campo_liquor = document.getElementById("campo-liquor").value;
    let campo_bacterioscopia = document.getElementById("campo-bacterioscopia").value;
    let campo_tomou_vacina = document.getElementById("campo-tomou-vacina").value;
    let campo_dt_ultima_dose_tomada = document.getElementById("campo-dt-ultima-dose-tomada").value;
    let campo_hospitalizacao = document.getElementById("campo-hospitalizacao").value;
    let campo_dt_hospitalizacao = document.getElementById("campo-dt-hospitalizacao").value;
    let campo_uf_hospital = document.getElementById("campo-uf-hospital").value;
    let campo_municipio_hospital = document.getElementById("campo-municipio-hospital").value;
    let campo_cod_ibge_hospital = document.getElementById("campo-cod-ibge-hospital").value;
    let campo_nome_hospital = document.getElementById("campo-nome-hospital").value;
    let campo_cod_hospital = document.getElementById("campo-cod-hospital").value;
    let campo_hipotese_diagnostica1 = document.getElementById("campo-hipotese-diagnostica1").value;
    let campo_hipotese_diagnostica2 = document.getElementById("campo-hipotese-diagnostica2").value;
    let campo_pais_infeccao = document.getElementById("campo-pais-infeccao").value;
    let campo_distrito_infeccao = document.getElementById("campo-distrito-infeccao").value;
    let campo_uf_infeccao = document.getElementById("campo-uf-infeccao").value;
    let campo_municipio_infeccao = document.getElementById("campo-municipio-infeccao").value;
    let campo_bairro_infeccao = document.getElementById("campo-bairro-infeccao").value;

    if (!campo_dt_notificacao) {
        let dataAtual = new Date();
        let options = { year: 'numeric', month: '2-digit', day: '2-digit', timeZone: 'America/Fortaleza' };
        campo_dt_notificacao = dataAtual.toLocaleDateString('pt-BR', options).split('/').reverse().join('-');
    }

    fetch(urlSetFichaNotificacao, {
        method: "POST",
        credentials: 'include',
        headers: {
            "Content-type": "application/json;charset=UTF-8",
            "X-CSRFToken": csrfToken
        },
        body: JSON.stringify({
            numero_ficha: numero_ficha,
            tipo_notificacao: campo_tipo_notificacao,
            agravoDoenca: campo_agravoDoenca,
            dt_notificacao: campo_dt_notificacao,
            uf_notificacao: campo_uf_notificacao,
            municipio_notificacao: campo_municipio_notificacao,
            cod_ibge_notificacao: campo_cod_ibge_notificacao,
            unidade_saude: campo_unidade_saude,
            cod_unidade_saude: campo_cod_unidade_saude,
            dt_sintomas: campo_dt_sintomas,
            nome_paciente: campo_nome_paciente,
            dt_nascimento: campo_dt_nascimento,
            idade: campo_idade,
            tipo_idade: campo_tipo_idade,
            sexo: campo_sexo,
            gestante: campo_gestante,
            raca: campo_raca,
            escolaridade: campo_escolaridade,
            numero_sus: campo_numero_sus,
            nome_mae: campo_nome_mae,
            dt_primeiro_sintoma: campo_dt_primeiro_sintoma,
            numero_casos_suspeitos: campo_numero_casos_suspeitos,
            local_inicial_ocorrencia: campo_local_inicial_ocorrencia,
            local_inicial_ocorrencia_outro: campo_local_especificar_ocorrencia,
            uf_residencia: campo_uf_residencia,
            municipio_residencia: campo_municipio_residencia,
            cod_ibge_residencia: campo_cod_ibge_residencia,
            distrito_residencia: campo_distrito_residencia,
            bairro_residencia: campo_bairro_residencia,
            logradouro_residencia: campo_logradouro_residencia,
            codigo_residencia: campo_codigo_residencia,
            numero_residencia: campo_numero_residencia,
            complemento_residencia: campo_complemento_residencia,
            geo_campo1: campo_geo_campo1,
            geo_campo2: campo_geo_campo2,
            ponto_ref_residencia: campo_ponto_ref_residencia,
            cep_residencia: campo_cep_residencia,
            telefone_residencia: campo_telefone_residencia,
            zona_residencia: campo_zona_residencia,
            pais_residencia: campo_pais_residencia,
            municipio_us_notificante: campo_municipio_us_notificante,
            nome_notificante: campo_nome_notificante,
            funcao_notificante: campo_funcao_notificante,
            assinatura_notificante: campo_assinatura_notificante,
            dt_amostra_sorologia: campo_dt_amostra_sorologia,
            dt_outra_amostra: campo_dt_outra_amostra,
            tipo_exame: campo_tipo_exame,
            obito: campo_obito,
            caso_semelhante: campo_caso_semelhante,
            exantema: campo_exantema,
            dt_inicio_exantema: campo_dt_inicio_exantema,
            petequiaSufusao: campo_petequiaSufusao,
            liquor: campo_liquor,
            bacterioscopia: campo_bacterioscopia,
            tomou_vacina: campo_tomou_vacina,
            dt_ultima_dose_tomada: campo_dt_ultima_dose_tomada,
            hospitalizacao: campo_hospitalizacao,
            dt_hospitalizacao: campo_dt_hospitalizacao,
            uf_hospital: campo_uf_hospital,
            municipio_hospital: campo_municipio_hospital,
            cod_ibge_hospital: campo_cod_ibge_hospital,
            nome_hospital: campo_nome_hospital,
            cod_hospital: campo_cod_hospital,
            hipotese_diagnostica1: campo_hipotese_diagnostica1,
            hipotese_diagnostica2: campo_hipotese_diagnostica2,
            pais_infeccao: campo_pais_infeccao,
            distrito_infeccao: campo_distrito_infeccao,
            uf_infeccao: campo_uf_infeccao,
            municipio_infeccao: campo_municipio_infeccao,
            bairro_infeccao: campo_bairro_infeccao,
            setor: setor,
            prontuario: prontuario,
            cod_formulario: cod_formulario,
        })
    })
        .then(response => response.json())
        .then(
            function (json) {
                if (json["status"] === 'success') {
                    // abrirOpcaoPaginaInicial()
                } else {
                    $('#mensagem-retorno .modal-title').html("Cadastro não efetuado!");
                    $('#mensagem-retorno .modal-body').html("Algo deu errado ao salvar as informações.");
                    $('#mensagem-retorno').modal("toggle");
                }
            }
        )
        .catch(err => console.log(err));
}
