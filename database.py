import sqlite3

# Nom del fitxer de la base de dades
DB_NAME = "grup.db"

def get_connection():
    # Obrim una connexio amb SQLite
    return sqlite3.connect(DB_NAME)

def init_db():
    # Creem la taula si encara no existeix
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS grup (id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT NOT NULL)"""
    )
    conn.commit()
    conn.close()

def guardar_grup(noms):
    # Guardem els noms rebuts a la taula
    conn = get_connection()
    cursor = conn.cursor()

    # Esborrem el contingut anterior
    cursor.execute("DELETE FROM grup")

    # Inserim cada nom per separat
    for nom in noms:
        cursor.execute("INSERT INTO grup (nom) VALUES (?)", (nom,))

    conn.commit()
    conn.close()

def carregar_grup():
    # Llegim tots els noms guardats
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nom FROM grup")
    resultats = cursor.fetchall()
    conn.close()

    # Retornem nomes el text de cada nom
    return [fila[0] for fila in resultats]
