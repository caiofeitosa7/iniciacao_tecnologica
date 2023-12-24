function abrirMenuTiposDeFicha() {
    toggleModalTiposDeFicha()
    $(".modal-backdrop").css("z-index", 0);
}

function abrirFichaEscolhida(urlAbrirFicha) {
    let csrfToken = getCookie('csrftoken');
    let idFichaEscolhida = $("#selectTipoFicha")[0].value;

    toggleModalTiposDeFicha();
    fetch(urlAbrirFicha, {
        method: "POST",
        headers: {
            "Content-type": "application/json;charset=UTF-8",
            "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify({
            idFicha: idFichaEscolhida
        })
    })
        .then(response => response.json())
        .then(
            data => {
                $('#conteudo')[0].innerHTML = data.html[0];
            })
        .catch(err => console.log(err));
}

function toggleModalTiposDeFicha() {
    $('#modalTiposFicha').modal("toggle");
}