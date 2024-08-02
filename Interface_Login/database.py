import sqlite3

conn = sqlite3.connect("Login.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Username TEXT NOT NULL,
    Email TEXT NOT NULL,
    Passowrd TEXT NOT NULL,
    confPassword TEXT NOT NULL                          
)""")

print("Conexao ao Banco de Dados realizada com sucesso!")