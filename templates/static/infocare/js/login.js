function logarUsuario(urlLogarUsuario, urlHome) {
    let usuario = document.getElementById('usuario').value;
    let senha = document.getElementById('senha').value;
    let csrfToken = getCookie('csrftoken');

    urlHome = escaparCaracteresEspeciaisHTML(urlHome);
    urlLogarUsuario = escaparCaracteresEspeciaisHTML(urlLogarUsuario);

    fetch(urlLogarUsuario, {
        method: "POST",
        headers: {
            "Content-type": "application/json;charset=UTF-8",
            "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify({
            usuario: usuario,
            senha: senha
        })
    })
        .then(response => response.json())
        .then(
            function (json) {
                if (json["status"] === 'success') {
                    window.location.href = urlHome;
                } else {
                    $('#mensagem-retorno .modal-title').html("Algo deu errado!");
                    $('#mensagem-retorno .modal-body').html("Usuário ou senha incorretos");
                    $('#mensagem-retorno').modal("toggle");
                }
            }
        )
        .catch(err => console.log(err));
}

function checkEnter(event) {
    if (event.keyCode === 13) { // Se o código da tecla for 13 (Enter)
        document.querySelector('.login-form-btn').click();
    }
}