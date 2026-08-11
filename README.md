# CRUD de cadastro de usuários
Sistema de gerenciamento de usuários (cadastrar, listar, editar e apagar), desenvolvido como atividade prática integrando Front-End, Back-End e Banco de Dados.

## Tecnologias Utilizadas:
-- Python 3;
-- HTML e CSS;
-- Flask;
-- SQLite;

## Como executar?

1. Clone o repositorio ou baixe os arquivos;
2. Instale o Flask, caso não tenha;
3. Execute o arquivo principal: python app.py
4. Acesse no navegador:  http://127.0.0.1:5000

### O front-end (formulários e páginas) é servido diretamente pelo Flask através de templates HTML — não é necessário rodar nenhum projeto separado para visualizar a interface.

## Estrutura da aplicação:

back/
├── app.py           → backend (rotas Flask e lógica de acesso ao banco)
├── banco.sql        → script de criação da tabela do banco de dados
├── banco.db          → arquivo do banco de dados SQLite (gerado automaticamente)
├── templates/
│   ├── index.html    → formulário de cadastro;
│   ├── usuarios.html → listagem de usuários cadastrados;
│   └── editar.html   → formulário de edição de usuário;
└── static/
    └── style.css      → estilização das páginas.