function abrirMenuTiposDeFicha() {
    toggleModalTiposDeFicha()
    $(".modal-backdrop").css("z-index", 0);
}

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



















