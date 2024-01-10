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