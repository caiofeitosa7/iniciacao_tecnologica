function escaparCaracteresEspeciaisHTML(input) {
    return input.replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#x27;')
}

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

function atribuirValor(elementId) {
    let valorDoCampo = document.getElementById(elementId).value;
    let novoElementId = elementId + "2";

    document.getElementById(novoElementId).value = valorDoCampo;
}

function pesquisaCep(elemento) {
    let cep = elemento.value.replace(/\D/g, '');  // somente numeros

    if (cep != "") {
        let validacep = /^[0-9]{8}$/;

        if (validacep.test(cep)) {
            let apiUrl = 'https://viacep.com.br/ws/'+ cep + '/json/';

            fetch(apiUrl)
                .then(response => {
                    if (!response.ok)
                        console.log('Erro ao consultar o CEP');
                    return response.json();
                })
                .then(data => {
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
        }
        else {
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



















