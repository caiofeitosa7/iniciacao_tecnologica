function cadastrarUsuario(url, idForm){
    let csrfToken = getCookie("csrftoken");
    let form = document.getElementById(idForm);
    let dicionario = {};
    
    let camposInput = form.querySelectorAll("input, select");
    camposInput.forEach(function(campo) {
        if (campo.id) {    // Exclui o campo do csrf_token
            switch (campo.type) {
                case 'number':
                    dicionario[campo.id] = parseInt(campo.value, 10);
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
    .then(
        function (json) {
            if (json["status"] === 'success') {
                $('#conteudo')[0].innerHTML = json.html[0];
                $('#mensagem-retorno .modal-title').html("Sucesso!");
                $('#mensagem-retorno .modal-body').html("Dados atualizados com sucesso.");
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
