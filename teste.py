import webbrowser
import os

## while pro loop
while True:
## entrada de dados
    print("="*37)
    print(" ")
    num1 = float(input("Primeiro numero: "))
    num2 = float(input("Segundo numero: "))
    print(" ")
    print("="*37)

## escolha da operação
    print(" 1 | soma \n 2 | subtração \n 3 | divisao \n 4 | multiplica \n 5 | para sair  ")
    print(" ")
    opr = int(input("Qual operação vocé deseja fazer: "))
    print("="*37)
    print(" ")

##if elif else para uso das operações
    soma = int()
    if opr == 1: ## soma------------------
        soma = num1 + num2
        print(f"A soma dos numeros é : {soma}")
        print(" ")
        print("="*37)
    elif opr == 2: ## subtração--------------
        soma = num1 - num2
        print(f"A subtração dos numeros é: {soma}")
        print(" ")
        print("="*37)
    elif opr == 3:    ## divisão-------------
        soma = num1 / num2
        print(f"a divisão dos numeros são: {soma}")
        print(" ")
        print("="*37)
    elif opr == 4:    ##multiplicação----------
        soma = num1 * num2
        print(f"a multiplicação dos numeros é: {soma}") 
        print(" ")
        print("="*37)
    elif opr == 5:      ## sair do loop------------
        print("obrigado por usar a calculadora")
        print(" ")
        print("="*37)
        webbrowser.open("https://www.youtube.com/watch?v=Anlzn2yqr9Y")
        break
    else:
        print("escolha de operação invalida")
        print(" ")
        print("="*37)

