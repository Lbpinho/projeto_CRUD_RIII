CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT;
    nome TEXT NOT NULL;
    email TEXT NOT NULL;
    cpf TEXT NOT NULL UNIQUE;
    telefone TEXT NOT NULL;
    data_nascimento TEXT NOT NULL;
    data_cadastro TEXT NOT NULL;
)
