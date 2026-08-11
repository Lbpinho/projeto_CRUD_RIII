#importação do flask, do sqlite3 e data
from flask import Flask, request, render_template, redirect
import sqlite3
from datetime import date 
app = Flask(__name__)

#tabelas 
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        cpf TEXT NOT NULL UNIQUE,
        telefone TEXT NOT NULL,
        data_nascimento TEXT NOT NULL,
        data_cadastro TEXT NOT NULL
    )
""")
conexao.commit()
conexao.close()

#página inicial
@app.route("/")
def home():
    return render_template("index.html")

#cadastro
@app.route("/cadastrar", methods= ["POST"])
def cadastrar():
    nome = request.form["nome"]
    email = request.form["email"]
    cpf = request.form["cpf"]
    telefone = request.form["telefone"]
    data_nascimento = request.form["data_nascimento"]
    data_cadastro = str(date.today()) 
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email, cpf, telefone, data_nascimento, data_cadastro) VALUES (?, ?, ?, ?, ?, ?)", (nome, email, cpf, telefone, data_nascimento, data_cadastro))
    conexao.commit()
    conexao.close()
    return "Cadastro realizado com sucesso!"

#lista de usuarios
@app.route("/usuarios")
def listar():
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conexao.close()
    return render_template("usuarios.html", usuarios=usuarios)

#editar usuario
@app.route("/editar/<int:id>")
def editar(id):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
    usuario = cursor.fetchone()
    conexao.close()
    return render_template("editar.html", usuario=usuario)


#atualizar usuario (corrigi com i.a pq toda hora dava erro)
@app.route("/atualizar/<int:id>", methods=["POST"])
def atualizar(id):
    nome = request.form["nome"]
    email = request.form["email"]
    cpf = request.form["cpf"]
    telefone = request.form["telefone"]
    data_nascimento = request.form["data_nascimento"]
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("UPDATE usuarios SET nome = ?, email = ?, cpf = ?, telefone = ?, data_nascimento = ? WHERE id = ?", (nome, email, cpf, telefone, data_nascimento, id))
    conexao.commit()
    conexao.close()
    return redirect("/usuarios")

#deletar 
@app.route("/deletar/<int:id>")
def deletar(id):
    conexao = sqlite3.connect("banco.db") 
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()
    return redirect("/usuarios")
  
if __name__ == "__main__":
    app.run(debug=True)
