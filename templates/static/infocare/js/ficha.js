function cadastrarFichaNotificacao(urlSetFichaNotificacao) {
    let csrfToken = getCookie("csrftoken");
    let cod_formulario = document.getElementById("cod_formulario").value;
    let prontuario = document.getElementById("prontuario").value;
    let setor = document.getElementById("setor").value;

    let camposNumericos = document.querySelectorAll('input[type="number"]');
    camposNumericos.forEach(function (campo) {
        if (campo.value === "")
            campo.value = 0;
    });

    let fichas = document.getElementsByClassName("ficha");
    let dicionario = {};

    Array.from(fichas).forEach(function(ficha) {
        let camposInput = ficha.querySelectorAll("input, textarea");

        // camposInput.forEach(function(campo) {
        //     if (campo.id) { // Exclui o campo do csrf_token
        //         if (campo.type === 'number') {
        //             dicionario[campo.id] = parseInt(campo.value, 10);
        //         } else {
        //             if (campo.type === 'date' && campo.value === '') {
        //                 dicionario[campo.id] = null;
        //             } else {
        //                 dicionario[campo.id] = campo.value;
        //             }
        //         }
        //     }
        // });

        camposInput.forEach(function(campo) {
            if (campo.id) {    // Exclui o campo do csrf_token
                switch (campo.type) {
                    case 'number':
                        dicionario[campo.id] = parseInt(campo.value, 10);
                        break;
                    case 'checkbox':
                        dicionario[campo.id] = campo.checked ? 1 : 0;
                        break;
                    case 'radio':
                        if (campo.checked) {
                            dicionario[campo.name] = campo.value;
                        } else {
                            if (!dicionario.hasOwnProperty(campo.name))
                                dicionario[campo.name] = "";
                        }
                        break;
                    case 'date':
                        dicionario[campo.id] = campo.value === "" ? null : campo.value;
                        break;
                    default:
                        dicionario[campo.id] = campo.value;
                        break;
                }
            }
        });
    });

    dicionario['setor'] = setor;
    dicionario['prontuario'] = parseInt(prontuario, 10);
    dicionario['cod_tipo_ficha'] = parseInt(cod_formulario, 10);

    if (!dicionario['campo-dt-notificacao']) {
        let dataAtual = new Date();
        let options = {year: 'numeric', month: '2-digit', day: '2-digit', timeZone: 'America/Fortaleza'};
        dicionario['campo-dt-notificacao'] = dataAtual.toLocaleDateString('pt-BR', options).split('/').reverse().join('-');
    }

    fetch(urlSetFichaNotificacao, {
        method: "POST",
        credentials: 'include',
        headers: {
            "Content-type": "application/json;charset=UTF-8",
            "X-CSRFToken": csrfToken
        },
        body: JSON.stringify(dicionario)
    })
    .then(response => response.json())
    .then(
        function (json) {
            if (json["status"] === 'success') {
                let uploadForm = document.getElementById('uploadForm');
                let parts = uploadForm.action.split('/');
                
                parts[parts.length - 1] = json["cod_ficha"];
                uploadForm.action = parts.join('/');
                uploadForm.submit();

                $('#conteudo')[0].innerHTML = json.html[0];
                $('#mensagem-retorno .modal-title').html("Sucesso!");
                $('#mensagem-retorno .modal-body').html("Dados cadastrados com sucesso.");
                $('#mensagem-retorno').modal("toggle");
            } else {
                $('#mensagem-retorno .modal-title').html("Cadastro não efetuado!");
                $('#mensagem-retorno .modal-body').html("Algo deu errado ao salvar as informações.");
                $('#mensagem-retorno').modal("toggle");
            }
        }
    )
    .catch(err => console.log(err));
}

function addInputFile() {
    let containerInputs = document.getElementById("containerInputsPDF");
    let proxInputs = containerInputs.querySelectorAll('input').length + 1;

    let inputFile = document.createElement('input');
    inputFile.classList.add('form-control', 'mt-2');
    inputFile.setAttribute('name', 'file' + proxInputs);
    inputFile.setAttribute('id', 'file' + proxInputs);
    inputFile.setAttribute('accept', '.pdf');
    inputFile.setAttribute('type', 'file');

    containerInputs.appendChild(inputFile);
}

function verificarMudancaEstadoFicha(url) {
    let quantPendenciaAbertas = 0
    document.querySelectorAll('span.pendencia-aberta').forEach(function(span){
        quantPendenciaAbertas += 1
    });

    if (quantPendenciaAbertas > 0) {
        $('#mensagem-retorno .modal-title').html("Erro!");
        $('#mensagem-retorno .modal-body').html("Para enviar a ficha para análise, você precisa concluir todas as pendências.");
        $('#mensagem-retorno').modal("toggle");
    } else {
        requisicaoGetPadrao(url)
    }
}
