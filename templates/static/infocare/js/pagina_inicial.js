function abrirMenuTiposDeFormulario() {
    toggleModalTiposDeFormulario()
    $(".modal-backdrop").css("z-index", 0);
}

function abrirFormularioEscolhido(url) {
    toggleModalTiposDeFormulario();
    requisicaoGetPadrao(url);
}

function toggleModalTiposDeFormulario() {
    $('#modalTiposFormulario').modal("toggle");
}

function abrirOpcaoColorida(url) {
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



















