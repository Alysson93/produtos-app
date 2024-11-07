# Catálogo de produtos

Olá! Este é um simples projeto web de catálogo de produtos, onde o usuário pode fazer interações básicas como criar, visualizar, editar e deletar produtos.


# Sobre o projeto

Implementado em Python com FastAPI e SQLAlchemy, o **Catálogo de Produtos** foi criado para fins educacionais, simulando os possíveis problemas que podemos encontrar em um projeto em produção. A ideia é que você possa contribuir com o projeto, propondo melhorias, manutenções e concertos de bugs.
O projeto conta inicialmente com a implementação tando de uma aplicação de páginas web, quanto uma API rest, ambos implementados no projeto FastAPI.
Esperamos que este projeto possa contribuir com o seu aprendizado!

## Requisitos para executar o projeto na minha máquina

Primeiro, cerifique-se de ter no mínimo, o python3.10 (linguagem de programação) instalado em seu computador. Você pode checar esta informação com o comando:
python3 -- version
No windows, este comando pode variar como 'python --version' ou 'py --version' 

## Criando ambiente virtual

Com o python instalado, execute o comando:
**python3 -m venv venv**
Isto criará um ambiente virtual isolado para que as dependências instaladas sejam próprias do projeto (não havendo a necessidade de instalar as dependências globalmente em sua máquina).
Uma vez criado o ambiente, acesse-o com o comando:
**source venv/bin/activate** (no Linux)
**venv\Scripts\activate** (no windows)
Certifique-se de instalar as dependências apenas quando o ambiente virtual estiver ativo.
Caso queira desativar o ambiente, use o comando:
**deactivate**


## Instalando as dependências

Agora que acessamos nosso ambiente virtual, instale as dependências do projeto usando o comando:
**pip install -r requirements.txt**
Este comando lê as dependências listadas no arquivo requirements.txt e as instala no seu ambiente virtual.
Você pode notar que também temos um arquivo chamado **requirements-dev.txt**. Este arquivo lista dependências de desenvolvimento, ou seja, que não são esOsenciais para o funcionamento do projeto em produção, mas são úteis durante o desenvolvimento. Você também pode instalá-las com o comando:
**pip install -r requirements-dev.txt**

## Variáveis de ambiente e banco de dados

O sistema conta com um banco de dados sqlite para fins de desenvolvimento. Você pode substituílo pelo SGBD de sua preferência, porém, as informações do banco não podem estar dispostas no código, já que usuários e senhas de banco são constantes alvos de ataque. Para evitar esta falha de segurança, usamos o arquivo **.env**
É apenas nele que colocamos informações sensíveis. Este é um arquivo que não deve ser rastreado pelo repositório, por isso ele está listado entre os arquivos e diretórios que devem ser ignorados no **.gitignore**.
Porém, temos um **.env.example** para ajudar o desenvolvedor a criar o seu .env local.
 

## Executando o projeto

Pronto! Agora temos nossa máquina totalmente configurada para executar o projeto, o arquivo **'main.py** é o coração da aplicação. Ele é quem chama todos os módulos e rotas do projeto. Logo, executamos a aplicação com o comando:
**python main.py**

## Organização do código

A medida que formos implementando novas features na aplicação, o código pode ficar um tanto complexo, e se não bem organizado, pode dificultar a nossa leitura. Para isso, temos duas dependências de desenvolvimento que nos ajuda a organizar o código. Elas podem ser executadas com os comandos:
**blue .** (cuida da identação e estrutura correta de um código python)
**isort .** (organiza os imports dos arquivos)
