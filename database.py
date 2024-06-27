import sqlite3

def create_table():
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            NomeProduto TEXT NOT NULL,
            Cod INTEGER NOT NULL,
            quantidade INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Chamar a função create_table para garantir que a tabela é criada ao importar o módulo
create_table()
