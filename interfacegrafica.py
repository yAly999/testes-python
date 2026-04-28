import urllib.request
from tkinter import *
import json

def pegar_cotacoes():                              ## codigo feito por hashtag proçramação para uso de aprender usar janela e botoes
    with urllib.request.urlopen("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL") as resposta:
        requisicao_dic = json.loads(resposta.read().decode())

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}
                        '''
  
    texto_das_cotacoes["text"] = texto          ## isso aqui troca o texto da ultima funçao apos clicar no botao==========



## Criando a interface gráfica

janela = Tk()         ## criar janela
janela.title("cotações")         # titulo
janela.geometry("300x300") ## tamanhp da janela

orientação_txt = Label(janela, text="Aperte no botão para ver a cotação das moedas")        ## isso ae cria um texto ======================
orientação_txt.grid(column=0, row=0, padx=10, pady= 10)                                      ## isso ae posiciona o texto na janela==========

button = Button(janela, text=" pressione para ver a cotação", command=pegar_cotacoes)        ##criar o bottao e atribuir um texto
button.grid(column=0, row=1,padx=10, pady= 10)                                              ## função pad ajuda a dar espaço entre as junçoes de texto


texto_das_cotacoes = Label(janela, text = (""))
texto_das_cotacoes.grid(column=0, row= 2,padx=10, pady= 10)              ##  isso aqui e o resultado das cotas atualizado


janela.mainloop()