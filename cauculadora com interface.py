import tkinter as tk

def somar():
    num1 = float(entrada.get())
    num2 = float(entrada2.get())
    resultado = num1 + num2
    label_resultado.config(text=f"{resultado}")

def subtrair():
    num1 = float(entrada.get())
    num2 = float(entrada2.get())
    resultado = num1 - num2
    label_resultado.config(text=f"{resultado}")

def dividir():
    num1 = float(entrada.get())
    num2 = float(entrada2.get())
    if num2 == 0:
        label_resultado.config(text="Erro")
    else:
        resultado = num1 / num2
        label_resultado.config(text=f"{resultado}")

def multiplicar():
    num1 = float(entrada.get())
    num2 = float(entrada2.get())
    resultado = num1 * num2
    label_resultado.config(text=f"{resultado}")

# Janela
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x260")

# Entradas
entrada = tk.Entry(janela, width=20)
entrada.grid(row=0, column=0, padx=10, pady=10)

entrada2 = tk.Entry(janela, width=20)
entrada2.grid(row=0, column=1, padx=10, pady=10)

# Botões (fileira)
tk.Button(janela, text=" Somar", width=12, command=somar).grid(row=1, column=0, padx=5, pady=10)
tk.Button(janela, text=" Subtrair", width=12, command=subtrair).grid(row=1, column=1, padx=5, pady=10)
tk.Button(janela, text=" Dividir", width=12, command=dividir).grid(row=2, column=0, padx=5, pady=5)
tk.Button(janela, text=" Multiplicar", width=12, command=multiplicar).grid(row=2, column=1, padx=5, pady=5)

# Resultado GRANDE embaixo
label_resultado = tk.Label(janela, text="", font=("Arial", 24))
label_resultado.grid(row=3, column=0, columnspan=2, pady=20)

janela.mainloop()