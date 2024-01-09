function cadastrarFichaNotificacao(urlSetFichaNotificacao, urlHome) {
    let csrfToken = getCookie("csrftoken");
    let ficha = document.getElementById("fichaNotificacao");
    let cod_formulario = document.getElementById("cod-formulario").value;
    let prontuario = document.getElementById("prontuario").value;
    let setor = document.getElementById("setor").value;

    let camposNumeros = document.querySelectorAll('input[type="number"]');
    camposNumeros.forEach(function(campo) {
        if (campo.value === "")
          campo.value = 0;
    });

    let camposInput = ficha.querySelectorAll("input");
    let dicionario = {};
    camposInput.forEach(function(campo) {
        if (campo.id) {
            if (campo.type === 'number')
                dicionario[campo.id] = parseInt(campo.value, 10);
            else
                dicionario[campo.id] = campo.value;
        }
    });

    dicionario['setor'] = setor;
    dicionario['prontuario'] = parseInt(prontuario, 10);
    dicionario['cod_formulario'] = parseInt(cod_formulario, 10);

    if (!dicionario['campo-dt-notificacao']) {
        let dataAtual = new Date();
        let options = { year: 'numeric', month: '2-digit', day: '2-digit', timeZone: 'America/Fortaleza' };
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
