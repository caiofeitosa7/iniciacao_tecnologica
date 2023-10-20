var sidebar = document.querySelector(".sidebar");
var btnMenu = document.querySelector("#btnMenu");
var nomeLogo = document.getElementById("logo-name");
var menuLateral = document.getElementsByClassName("nav-list")[0];

menuLateral.style.display = "none";
nomeLogo.style.display = "none";

btnMenu.addEventListener("click", abreFechaMenu);

function abreFechaMenu() {
    sidebar.classList.toggle("open");
    menuBtnChange();
}

function menuBtnChange() {
    if(sidebar.classList.contains("open")){
        menuLateral.style.display = "block";
        nomeLogo.style.display = "block";
        sidebar.style.left = "0";
    } else {
        menuLateral.style.display = "none";
        nomeLogo.style.display = "none";
        sidebar.style.left = "-28px";
    }
}

function abrirOpcaoPaginaInicial() {
    if(sidebar.classList.contains("open"))
        abreFechaMenu();

    fetch("pagina_inicial/", {
        method: 'GET',
        headers: {
            "Content-type": "application/json;charset=UTF-8"
        },
    })
    .then(response => response.json())
    .then(data => {
        localStorage.setItem('opcaoSelecionada', 1);
        document.getElementById('conteudo').innerHTML = data.html[0];
    })
    .catch(error => {
        console.error('Erro na requisição:', error);
    });
}

function abrirOpcaoUsuarios() {
    if(sidebar.classList.contains("open"))
        abreFechaMenu();

    fetch("usuarios/", {
        method: 'GET',
        headers: {
            "Content-type": "application/json;charset=UTF-8"
        },
    })
    .then(response => response.json())
    .then(data => {
        localStorage.setItem('opcaoSelecionada', 2)
        $('#conteudo')[0].innerHTML = data.html[0];
    })
    .catch(error => {
        console.error('Erro na requisição:', error);
    });
}

document.addEventListener('DOMContentLoaded', function() {
    let opMenu = parseInt(localStorage.getItem('opcaoSelecionada'))

    switch (opMenu) {
        case 1:
            abrirOpcaoPaginaInicial();
            break;
        case 2:
            abrirOpcaoUsuarios();
            break;
        default:
            abrirOpcaoPaginaInicial();
    }
});




















