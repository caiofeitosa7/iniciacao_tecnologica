var sidebar = document.querySelector(".sidebar");
var btnMenu = document.querySelector("#btnMenu");
var nomeLogo = document.getElementById("logo-name");
var menuLateral = document.getElementsByClassName("nav-list")[0];

menuLateral.style.display = "none";
nomeLogo.style.display = "none";

btnMenu.addEventListener("click", abreFechaMenu);

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function abreFechaMenu() {
    sidebar.classList.toggle("open");
    menuBtnChange();
}

function menuBtnChange() {
    if (sidebar.classList.contains("open")) {
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
    if (sidebar.classList.contains("open"))
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
    if (sidebar.classList.contains("open"))
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

document.addEventListener('DOMContentLoaded', function () {
    let opMenu = parseInt(localStorage.getItem('opcaoSelecionada'))

    switch (opMenu) {
        case 1:
            abrirOpcaoPaginaInicial();
            break;
        case 2:
            abrirOpcaoUsuarios();
            break;
        case 97:
            abrirOpcaoColorida('fichas_preliminares/');
            break;
        case 98:
            abrirOpcaoColorida('fichas_pendentes/');
            break;
        case 99:
            abrirOpcaoColorida('fichas_concluidas/');
            break;

        default:
            abrirOpcaoPaginaInicial();
    }
});

function atribuirValor(elementId) {
    let valorDoCampo = document.getElementById(elementId).value;
    let novoElementId = elementId + "2";

    document.getElementById(novoElementId).value = valorDoCampo;
}

function pesquisaCepComReplicacao(elemento) {
    let cep = elemento.value.replace(/\D/g, '');  // somente numeros

    if (cep !== "") {
        let validacep = /^[0-9]{8}$/;

        if (validacep.test(cep)) {
            let apiUrl = 'https://viacep.com.br/ws/' + cep + '/json/';

            fetch(apiUrl)
                .then(response => {
                    if (!response.ok)
                        console.log('Erro ao consultar o CEP');
                    return response.json();
                })
                .then(data => {
                    if (data["cep"] !== 'undefined') {
                        elemento.value = data["cep"];
                        document.getElementById(elemento.id + "2").value = data["cep"];
                        document.getElementById("campo-uf-residencia").value = data["uf"];
                        document.getElementById("campo-uf-residencia2").value = data["uf"];
                        document.getElementById("campo-municipio-residencia").value = data["localidade"];
                        document.getElementById("campo-municipio-residencia2").value = data["localidade"];
                        document.getElementById("campo-cod-ibge-residencia").value = data["ibge"];
                        document.getElementById("campo-cod-ibge-residencia2").value = data["ibge"];
                        document.getElementById("campo-bairro-residencia").value = data["bairro"];
                        document.getElementById("campo-bairro-residencia2").value = data["bairro"];
                        document.getElementById("campo-logradouro-residencia").value = data["logradouro"];
                        document.getElementById("campo-logradouro-residencia2").value = data["logradouro"];
                    }
                })
                .catch(error => {
                    console.error('Erro na requisição:', error);
                    elemento.value = "";
                    document.getElementById(elemento.id + "2").value = "";
                    document.getElementById("campo-uf-residencia").value = "";
                    document.getElementById("campo-uf-residencia2").value = "";
                    document.getElementById("campo-municipio-residencia").value = "";
                    document.getElementById("campo-municipio-residencia2").value = "";
                    document.getElementById("campo-cod-ibge-residencia").value = "";
                    document.getElementById("campo-cod-ibge-residencia2").value = "";
                    document.getElementById("campo-bairro-residencia").value = "";
                    document.getElementById("campo-bairro-residencia2").value = "";
                    document.getElementById("campo-logradouro-residencia").value = "";
                    document.getElementById("campo-logradouro-residencia2").value = "";
                });
        } else {
            console.error('CEP não passou no teste do regex');
            elemento.value = "";
            document.getElementById(elemento.id + "2").value = "";
            document.getElementById("campo-uf-residencia").value = "";
            document.getElementById("campo-municipio-residencia").value = "";
            document.getElementById("campo-cod-ibge-residencia").value = "";
            document.getElementById("campo-bairro-residencia").value = "";
            document.getElementById("campo-logradouro-residencia").value = "";
        }
    }
}

function pesquisaCepSemReplicacao(elemento) {
    let cep = elemento.value.replace(/\D/g, '');  // somente numeros

    if (cep !== "") {
        let validacep = /^[0-9]{8}$/;

        if (validacep.test(cep)) {
            let apiUrl = 'https://viacep.com.br/ws/' + cep + '/json/';

            fetch(apiUrl)
                .then(response => {
                    if (!response.ok)
                        console.log('Erro ao consultar o CEP');
                    return response.json();
                })
                .then(data => {
                    if (data["cep"] !== 'undefined') {
                        elemento.value = data["cep"];
                        document.getElementById("campo-uf-residencia").value = data["uf"];
                        document.getElementById("campo-municipio-residencia").value = data["localidade"];
                        document.getElementById("campo-cod-ibge-residencia").value = data["ibge"];
                        document.getElementById("campo-bairro-residencia").value = data["bairro"];
                        document.getElementById("campo-logradouro-residencia").value = data["logradouro"];
                    }
                })
                .catch(error => {
                    console.error('Erro na requisição:', error);
                    elemento.value = "";
                    document.getElementById("campo-uf-residencia").value = "";
                    document.getElementById("campo-municipio-residencia").value = "";
                    document.getElementById("campo-cod-ibge-residencia").value = "";
                    document.getElementById("campo-bairro-residencia").value = "";
                    document.getElementById("campo-logradouro-residencia").value = "";
                });
        } else {
            console.error('CEP não passou no teste do regex');
            elemento.value = "";
            document.getElementById("campo-uf-residencia").value = "";
            document.getElementById("campo-municipio-residencia").value = "";
            document.getElementById("campo-cod-ibge-residencia").value = "";
            document.getElementById("campo-bairro-residencia").value = "";
            document.getElementById("campo-logradouro-residencia").value = "";
        }
    }
}

function deslogarUsuario(url) {
    localStorage.clear();
    window.location.href = url;
}

// ------------------------------ Funcoes Auxiliares --------------------------------- //

function escaparCaracteresEspeciaisHTML(input) {
    return input.replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#x27;')
}

function requisicaoGetPadrao(url) {
    fetch(url, {
        method: 'GET',
        headers: {
            "Content-type": "application/json;charset=UTF-8"
        },
    })
        .then(response => response.json())
        .then(data => {
            // if (tituloAba)
            //     alterarTituloAba(tituloAba);
            $('#conteudo')[0].innerHTML = data.html[0];
        })
        .catch(error => {
            console.error('Erro na requisição:', error);
        });
}

function retornoListaFichas() {
    let ultimaListaSelecionada = parseInt(localStorage.getItem('opcaoSelecionada'));

    switch (ultimaListaSelecionada) {
        case 97:
            abrirOpcaoColorida('fichas_preliminares/');
            break;
        case 98:
            abrirOpcaoColorida('fichas_pendentes/');
            break;
        case 99:
            abrirOpcaoColorida('fichas_concluidas/');
            break;
        default:
            abrirOpcaoPaginaInicial();
    }
}


















