# Inteligência artificial aplicada a notificação de situações adversas de pacientes em ambiente hospitalar

<div>
  <p dir="auto" style="text-align:justify;">
    A vigilância epidemiológica no Hospital de Urgência de Teresina Prof. Zenon Rocha (HUT), assim como na maioria dos hospitais, é feita através do registro manual da Ficha Individual de Notificação (FIN), elaborada para cada paciente com suspeita de uma doença de notificação compulsória. Desse modo, o propósito desse projeto é implementar um sistema eletrônico de notificações, tendo o HUT como piloto, com o objetivo de automatizar esse fluxo. Adicionalmente, esse sistema incorporará a inteligência artificial para monitorar os dados de saúde dos pacientes, identificando anomalias e notificando imediatamente os profissionais de saúde pertinentes, possibilitando uma resposta preventiva ou corretiva ágil.
  </p>
</div>

## Como executar o projeto

### Pré-requisitos:

- [Python](https://www.python.org/)

### Ambiente Virtual Python:

Caso o 'pip', instalador de pacotes do python não esteja instalado.

- `$ sudo apt install python3-pip -y`

Instalar o pacote 'virtualenv'.

- `$ pip install virtualenv` ou
- `$ sudo apt install python3-virtualenv`


Criar um ambiente virtual para instalar as dependências do projeto.

- `$ virtualenv venv` (sendo o segundo venv o nome do ambiente virtual)
- `$ venv\Scripts\activate` (para ativar o ambiente virtual - WINDOWS)
- `$ source venv/bin/activate` (para ativar o ambiente virtual - LINUX)
- `$ deactivate` (para desativar o ambiente virtual)

OBS: Os passos seguintes devem ser executados com o ambiente virtual ativo.

### Instalar as dependencias do projeto:

- `$ pip install -r requirements.txt`

OBS: caso dê erro na instalação do mysqlclient. Execute: `sudo apt-get install python3-dev default-libmysqlclient-dev build-essential`

### Preparar arquivos estáticos:

- `$ python manage.py collectstatic` (WINDOWS)
- `$ python3 manage.py collectstatic` (LINUX)

### Executar o projeto:

- `$ python manage.py runserver 0.0.0.0:8000` (WINDOWS)
- `$ python3 manage.py runserver 0.0.0.0:8000` (LINUX)

### Acessar o projeto:

- No console aparecerá o endereço de acesso, normalmente fica no [localhost:8000](http://127.0.0.1:8000/), podendo variar dependendo das configurações da maquina.

- Para acessar de outros dispositivos (incluindo os tablets), a url difere do padrão 'http://127.0.0.1:8000/'. Ao invés de acessar o localhost, outro dispositivo que deseja entrar na aplicação deve acessar pelo IP do servidor do sistema. Isso é possível desde que esteja conectado à mesma rede do servidor.
