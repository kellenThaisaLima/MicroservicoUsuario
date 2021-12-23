
# MicroservicoUsuario

Desenvolvimento de uma API REST com Python e Flask para inclusão de usuários


## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

A tabela usuário é composta por 5 colunas:

ID, CPF, NOME, DATA_DE_NASCIMENTO, DATA_DE_CRIAÇÃO e DATA_DE_ATUALIZAÇÃO


### 📦 Desenvolvimento

Para iniciar o projeto, acesse a pasta main e execute:

```http
  python main.py
```

### Instalar os pacotes

Python:

```http
  sudo apt-get install python3-werkzeug 
```
Pip

```http
  sudo apt install pip 
```

Flask

```http
  pip install flask
```

Flask Restx

```http
  pip install flask-restx
```

Werkzeug:

```http
  pip install Werkzeug==0.16.0
```

    
### Para rodar localmente



Clone o projeto

```bash
  git clone https://github.com/kellenThaisaLima/MicroservicoUsuario.git
```

Acesse a pasta do projeto

```bash
  cd MicroservicoUsuario
```

Instale as dependencias

```bash
  consulta a seção **Instalar pacotes**
```

Inicie o servidor 

```bash
  python main.py
```


### Deployment

Tentei fazer o deploy no heroku mas não consegui, não encontrei um tutorial para fazer deploy com o makefile

```bash
  npm run deploy
```


### Documentação

[Documentation](http://127.0.0.1:5000/docs)


### Rotas API

GET
http://127.0.0.1:5000/usuarios

POST
http://127.0.0.1:5000/usuarios


As rotas put e delete não estão funcionais, pois não consegui concluir

DELETE
http://127.0.0.1:5000/

PUT
http://127.0.0.1:5000/


### Demo

Rota GET no Insomnia

https://uploaddeimagens.com.br/imagens/ZiveFXs


### Deseafios a serem superados

**Deploy**


Concluir o deploy no heroku, pois não consegui achar um tutorial que ensinasse a fazer deploy makefile.

**Rotas**


Concluir as rotas delete e put


**Testes**


Fazer testes unitários, validações de campo de entrada de dados


**Banco de Dados**


Conseguir criar o banco de dados Sqlite, pois precisei utilizar dados mocados para facilitar meu desenvolvimento.


**Segunda API de Microserviço**


Conseguir fazer uma segunda API que consuma dados desta

### Authors

- [@kellenThaisaLima](https://github.com/kellenThaisaLima)


### Lições Aprendidas

Criação de rotas de API REST com padrão CRUD com tecnologia PYTHON;
Configuração de ambiente Flask;
Que o Flask gera uma documentação automatica;
Conseguir fazer o readme do git;
Utilização de banco de dados Sqlite;

## 🛠️ Construído com

Mencione as ferramentas que você usou para criar seu projeto

* [Python]- Linguagem utilizada
* [Flask] - MicroBiblioteca utilizada para criar as APIs
* [Heroku] - Ferramenta utilizada para fazer deploy
* [Insomnia] - Ferramenta utilizada para fazer o teste de rotas
* [Sqlite3] - Ferramenta utilizada para criação de banco de dados
* [Linux] - Sistema operacional utilizado

## Contribuindo

As constribuições são sempre bem vindas!

Os vídeos de Pedro Impulcetto me ajudaram no desenvolvimento https://www.youtube.com/watch?v=levz4eumJ98


## 🔗 Links
[![portfolio](https://github.com/kellenThaisaLima)
[![linkedin](https://www.linkedin.com/in/kellenthaisadelima/)


## 🎁 Expressões de gratidão

* Eu amei fazer esse projeto e aprendi muito 📢
* Me ajudem a melhorar esse projeto pessoal, experiência enriquecedora 🍺 
* Obrigado QuiteJá pela oportunidade🤓.


---
⌨️ com ❤️ por [Kellen Thaisa de Lima](https://github.com/kellenThaisaLima) 😊
