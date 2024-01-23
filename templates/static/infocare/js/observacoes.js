function enviarFichaParaConclusao(url) {
    let quantObsAbertas = 0
    document.querySelectorAll('span.obs-aberta').forEach(function(span){
        quantObsAbertas += 1
    });

    if (quantObsAbertas > 0) {
        $('#mensagem-retorno .modal-title').html("Erro!");
        $('#mensagem-retorno .modal-body').html("Para enviar a ficha para análise, você precisa terminar todas as observações.");
        $('#mensagem-retorno').modal("toggle");
    } else {
        requisicaoGetPadrao(url)
    }
}


function abrirModalNovaObservacao() {
    $('#modalNovaObservacao').modal("toggle");
    $(".modal-backdrop").css("display", 'none');
    $('#modal-title').html('Observação');
}

function salvarObservacao(url, idModal){
    let csrfToken = getCookie("csrftoken");
    let formulario = document.getElementById(idModal);
    let camposInput = formulario.querySelectorAll("input, textarea");

    let dicionario = {};
    camposInput.forEach(function (campo) {
        if (campo.id) {
            if (campo.type === 'number')
                dicionario[campo.id] = parseInt(campo.value, 10);
            else
                dicionario[campo.id] = escaparCaracteresEspeciaisHTML(campo.value);
        }
    });

    fetch(url, {
            method: "POST",
            credentials: 'include',
            headers: {
                "Content-type": "application/json;charset=UTF-8",
                "X-CSRFToken": csrfToken
            },
            body: JSON.stringify(dicionario)
        })
            .then(response => response.json())
            .then(function (json) {
                    if (json["status"] === 'success') {
                        // $('#mensagem-retorno .modal-title').html("Sucesso!");
                        // $('#mensagem-retorno .modal-body').html("Dados cadastrados com sucesso.");
                        // $('#mensagem-retorno').modal("toggle");
                        $(idModal).modal("toggle");
                        $('#conteudo')[0].innerHTML = json.html[0];
                    } else {
                        $('#mensagem-retorno .modal-title').html("Erro!");
                        $('#mensagem-retorno .modal-body').html("Você não tem permissão para acessar essa página.");
                        $('#mensagem-retorno').modal("toggle");
                        $(idModal).modal("toggle");
                    }
                }
            )
            .catch(err => console.log(err));
}



















