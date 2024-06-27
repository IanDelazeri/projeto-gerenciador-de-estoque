from dataclasses import dataclass
from typing import List, Optional
import sqlite3

@dataclass
class Cadastro:
    id: int
    NomeProduto: str
    Cod: int
    quantidade: int = 0

    def exibir(self):
        print(f"id: {self.id} | Produto: {self.NomeProduto} | Codigo: {self.Cod} | Quantidade: {self.quantidade}")

    def editar(self, NomeProduto: Optional[str] = None, Cod: Optional[int] = None):
        if NomeProduto is not None:
            self.NomeProduto = NomeProduto
        if Cod is not None:
            self.Cod = Cod

    def adicionar_estoque(self, quantidade: int):
        self.quantidade += quantidade

    def remover_estoque(self, quantidade: int):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
        else:
            print(f"Erro: Não é possível remover {quantidade} itens. Quantidade em estoque insuficiente.")

# Funções de manipulação do banco de dados
def adicionar_cadastro(NomeProduto: str, Cod: int, quantidade: int = 0):
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO produtos (NomeProduto, Cod, quantidade)
        VALUES (?, ?, ?)
    ''', (NomeProduto, Cod, quantidade))
    conn.commit()
    conn.close()
    print(f"Produto '{NomeProduto}' adicionado com sucesso.")

def exibir_cadastros():
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    conn.close()
    for prod in produtos:
        cadastro = Cadastro(id=prod[0], NomeProduto=prod[1], Cod=prod[2], quantidade=prod[3])
        cadastro.exibir()
    
    # Pausa para permitir que o usuário veja os cadastros
    input("Pressione Enter para continuar...")

def editar_cadastro(id: int, NomeProduto: Optional[str] = None, Cod: Optional[int] = None):
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    if NomeProduto:
        cursor.execute('UPDATE produtos SET NomeProduto = ? WHERE id = ?', (NomeProduto, id))
    if Cod:
        cursor.execute('UPDATE produtos SET Cod = ? WHERE id = ?', (Cod, id))
    conn.commit()
    conn.close()
    print(f"Cadastro com id {id} editado com sucesso.")

def excluir_cadastro(id: int):
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM produtos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    print(f"Cadastro com id {id} excluído com sucesso.")

def adicionar_estoque(id: int, quantidade: int):
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE produtos SET quantidade = quantidade + ? WHERE id = ?', (quantidade, id))
    conn.commit()
    conn.close()
    print(f"Adicionado {quantidade} unidades ao estoque do produto com id {id}.")

def remover_estoque(id: int, quantidade: int):
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT quantidade FROM produtos WHERE id = ?', (id,))
    current_quantity = cursor.fetchone()[0]
    if quantidade <= current_quantity:
        cursor.execute('UPDATE produtos SET quantidade = quantidade - ? WHERE id = ?', (quantidade, id))
        conn.commit()
        print(f"Removido {quantidade} unidades do estoque do produto com id {id}.")
    else:
        print(f"Erro: Não é possível remover {quantidade} itens. Quantidade em estoque insuficiente.")
    conn.close()
