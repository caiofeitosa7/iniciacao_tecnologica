function abrirMenuTiposDeFicha() {
  toggleModalTiposDeFicha()
  $(".modal-backdrop").css("z-index", 0)
}

<<<<<<< HEAD
function abrirFichaEscolhida(urlAbrirFicha) {
  let csrfToken = getCookie("csrftoken")
  let idFichaEscolhida = $("#selectTipoFicha")[0].value

  toggleModalTiposDeFicha()
  fetch(urlAbrirFicha, {
    method: "POST",
    headers: {
      "Content-type": "application/json;charset=UTF-8",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({
      idFicha: idFichaEscolhida,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      $("#conteudo")[0].innerHTML = data.html[0]
    })
    .catch((err) => console.log(err))
}
function abrirFichaDev(urlAbrirFicha) {
  let csrfToken = getCookie("csrftoken")
  let idFichaEscolhida = $("#devFichaVisualizacaoID")[0].value
  //let idFichaEscolhida = "4"

  fetch(urlAbrirFicha, {
    method: "POST",
    headers: {
      "Content-type": "application/json;charset=UTF-8",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({
      idFicha: idFichaEscolhida,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      $("#conteudo")[0].innerHTML = data.html[0]
    })
    .catch((err) => console.log(err))
}

function toggleModalTiposDeFicha() {
  $("#modalTiposFicha").modal("toggle")
}
=======
function abrirFichaEscolhida(url) {
    toggleModalTiposDeFicha();
    requisicaoGetPadrao(url);
}

function toggleModalTiposDeFicha() {
    $('#modalTiposFicha').modal("toggle");
}

function abrirOpcaoColorida(url) {
    console.log(url)

    if (url.includes('fichas_preliminares')) {
        localStorage['opcaoSelecionada'] = 97;
        requisicaoGetPadrao(url);
    }
    else {
        if (url.includes('fichas_pendentes')) {
            localStorage['opcaoSelecionada'] = 98;
            requisicaoGetPadrao(url);
        }
        else {
            localStorage['opcaoSelecionada'] = 99;
            requisicaoGetPadrao(url);
        }
    }
}



















>>>>>>> db60f451a36e8d5c456d5881f2f7c9684fa37955
