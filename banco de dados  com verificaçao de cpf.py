import sqlite3

conn = sqlite3.connect("db_teste.db")
cursor = conn.cursor()


cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS clientes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf INTEGER
    )"""
)

print("--- adicione cliente ---")
clientes = input("Entre com o nome do cliente: ")

while True:
    try:
        cpf_input = input("Entre com o cpf do cliente: ")
        if cpf_input.isdigit() and len(cpf_input) == 11:
            cpf = int(cpf_input)
            break
        else:
            print("CPF inválido! Digite exatamente 11 números.")
    
    except ValueError:
        print("Digite apenas numeros!!!")


cursor.execute(
    "INSERT INTO clientes (nome, cpf) VALUES (?, ?)",
    (clientes, cpf)
)

conn.commit()

print(f"O cliente {clientes} com o cpf {cpf} foi registrado com sucesso")

print("=== dados da tabela (sem ordem) ===\n")

cursor.execute("SELECT * FROM clientes")
clientes = cursor.fetchall()

for clientes in clientes:
    print(clientes)

print("\n" + "="*20)
