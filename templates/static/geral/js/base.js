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


function abrirOpcaoMenu(url, numeroOpcao){
    if (sidebar.classList.contains("open"))
        abreFechaMenu();

    localStorage.setItem('opcaoSelecionada', numeroOpcao)
    requisicaoGetPadrao(url);
}

function abrirOpcaoPaginaInicial() {
    abrirOpcaoMenu('pagina_inicial/', 1);
}

function abrirOpcaoFichasDescartadas(){
    if (sidebar.classList.contains("open"))
        abreFechaMenu();

    localStorage.setItem('opcaoSelecionada', 2)
    abrirOpcaoMenu('fichas_descartadas/', 2);
}

function abrirOpcaoUsuarios() {
    if (sidebar.classList.contains("open"))
        abreFechaMenu();

    localStorage.setItem('opcaoSelecionada', 4)
    requisicaoGetPadrao('usuarios/');
}


document.addEventListener('DOMContentLoaded', function () {
    let opMenu = parseInt(localStorage.getItem('opcaoSelecionada'))

    switch (opMenu) {
        case 1:
            abrirOpcaoPaginaInicial();
            break;
        case 2:
            abrirOpcaoFichasDescartadas();
            break;
        case 4:
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

function autoPreenchimento(url, prontuario) {
    let parts = url.split('/');
    parts[parts.length - 1] = prontuario;
    url = parts.join('/');

    fetch(url, {
        method: 'GET',
        headers: {
            "Content-type": "application/json;charset=UTF-8"
        },
    })
        .then(response => response.json())
        .then(json => {
            if (json.status == "success") {
                dados = json.dados;
                document.getElementById("setor").value = dados.posto_nome;

                let nomePaciente = document.getElementById("campo-nome-paciente");
                let nomePaciente2 = document.getElementById("campo-nome-paciente2");
                let dtNascimento = document.getElementById("campo-dt-nascimento");
                let dtNascimento2 = document.getElementById("campo-dt-nascimento2");
                let sexo = document.getElementById("campo-sexo");
                let sexo2 = document.getElementById("campo-sexo2");
                let numeroSus = document.getElementById("campo-numero-sus");
                let numeroSus2 = document.getElementById("campo-numero-sus2");
                let nomeMae = document.getElementById("campo-nome-mae");
                let nomeMae2 = document.getElementById("campo-nome-mae2");
                let ufResidencia = document.getElementById("campo-uf-residencia");
                let ufResidencia2 = document.getElementById("campo-uf-residencia2");
                let municipioResidencia = document.getElementById("campo-municipio-residencia");
                let municipioResidencia2 = document.getElementById("campo-municipio-residencia2");
                let codIbgeResidencia = document.getElementById("campo-cod-ibge-residencia");
                let codIbgeResidencia2 = document.getElementById("campo-cod-ibge-residencia2");
                let bairroResidencia = document.getElementById("campo-bairro-residencia");
                let bairroResidencia2 = document.getElementById("campo-bairro-residencia2");
                let logradouroResidencia = document.getElementById("campo-logradouro-residencia");
                let logradouroResidencia2 = document.getElementById("campo-logradouro-residencia2");
                let numeroResidencia = document.getElementById("campo-numero-residencia");
                let numeroResidencia2 = document.getElementById("campo-numero-residencia2");
                let telefoneResidencia = document.getElementById("campo-telefone-residencia");
                let telefoneResidencia2 = document.getElementById("campo-telefone-residencia2");
                let endereco = document.getElementById("endereco-residencia");

                if (nomePaciente != null) nomePaciente.value = dados.nome;
                if (nomePaciente2 != null) nomePaciente2.value = dados.nome;
                if (dtNascimento != null) dtNascimento.value = dados.data_nascimento;
                if (dtNascimento2 != null) dtNascimento2.value = dados.data_nascimento;
                if (sexo != null) sexo.value = dados.paciente_sexo;
                if (sexo2 != null) sexo2.value = dados.paciente_sexo;
                if (numeroSus != null) numeroSus.value = dados.cartao_sus;
                if (numeroSus2 != null) numeroSus2.value = dados.cartao_sus;
                if (nomeMae != null) nomeMae.value = dados.nome_mae;
                if (nomeMae2 != null) nomeMae2.value = dados.nome_mae;
                if (ufResidencia != null) ufResidencia.value = dados.endereco_uf;
                if (ufResidencia2 != null) ufResidencia2.value = dados.endereco_uf;
                if (municipioResidencia != null) municipioResidencia.value = dados.endereco_municipio;
                if (municipioResidencia2 != null) municipioResidencia2.value = dados.endereco_municipio;
                if (codIbgeResidencia != null) codIbgeResidencia.value = dados.endereco_municipio_codigo;
                if (codIbgeResidencia2 != null) codIbgeResidencia2.value = dados.endereco_municipio_codigo;
                if (bairroResidencia != null) bairroResidencia.value = dados.endereco_bairro;
                if (bairroResidencia2 != null) bairroResidencia2.value = dados.endereco_bairro;
                if (logradouroResidencia != null) logradouroResidencia.value = dados.endereco_logradouro;
                if (logradouroResidencia2 != null) logradouroResidencia2.value = dados.endereco_logradouro;
                if (numeroResidencia != null) numeroResidencia.value = dados.endereco_numero;
                if (numeroResidencia2 != null) numeroResidencia2.value = dados.endereco_numero;
                if (telefoneResidencia != null) telefoneResidencia.value = dados.telefones;
                if (telefoneResidencia2 != null) telefoneResidencia2.value = dados.telefones;
                if (endereco != null) endereco.value = dados.endereco_completo;

            } else {
                console.log('Não encontrou nada')
            }
        })
        .catch(error => {
            console.error('Erro na requisição:', error);
        });
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
    abrirTelaCarregamento();

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
            fecharTelaCarregamento();
            $('#conteudo')[0].innerHTML = data.html[0];
        })
        .catch(error => {
            console.error('Erro na requisição:', error);
        });
}

function requisicaoPostPadrao(url, idForm) {
    let csrfToken = getCookie("csrftoken");
    let formulario = document.getElementById(idForm);
    let camposInput = formulario.querySelectorAll("input, select, textarea");

    let dicionario = {};
    camposInput.forEach(function (campo) {
        if (campo.id)
            if (campo.type === 'number')
                dicionario[campo.id] = parseInt(campo.value, 10);
            else
                dicionario[campo.id] = campo.value;
    });

    abrirTelaCarregamento();

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
                fecharTelaCarregamento();
                // retirarTelaCarregamento();
                // if (json["status"] === 'success') {
                //     $('#conteudo')[0].innerHTML = json.html[0];
                // }

                console.log(dicionario);
            }
        )
        .catch(err => console.log(err));
}

function retornoListaFichas() {
    let ultimaListaSelecionada = parseInt(localStorage.getItem('opcaoSelecionada'));

    switch (ultimaListaSelecionada) {
        case 2:
            abrirOpcaoFichasDescartadas();
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
}


function abrirTelaCarregamento() {
    let tela_carregamento = document.getElementById("tela-carregamento");
    let tela_conteudo = document.getElementById("conteudo");

    tela_carregamento.classList.remove("d-none");
    tela_carregamento.classList.add("d-flex");
    tela_conteudo.classList.remove("d-block");
    tela_conteudo.classList.add("d-none");
}

function fecharTelaCarregamento() {
    let tela_carregamento = document.getElementById("tela-carregamento");
    let tela_conteudo = document.getElementById("conteudo");

    tela_carregamento.classList.remove("d-flex");
    tela_carregamento.classList.add("d-none");
    tela_conteudo.classList.remove("d-none");
    tela_conteudo.classList.add("d-block");
}