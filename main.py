#importação da biblioteca tkinter
import tkinter as tk

#Função para executar quando o botão for clicado
def celcius():
    janelacel = tk.Tk()
    janelacel.title("Conversão de Celcius para Fahrenheit")
    janelacel.geometry("300x250")

    campo_de_texto = tk.Entry(janelacel)
    campo_de_texto.pack()

    buttom1 = tk.Button(janelacel, text="Converter", command= lambda: receber_valor_celcius(campo_de_texto, janelacel))
    buttom1.pack(padx=20, pady=20) #Adiciona o botão na interface


def receber_valor_celcius(campo_de_texto, janelacel):
    num1 = campo_de_texto.get()
    num1 = float(num1)

    conta = (num1 * (9/5)) + 32

    resultado = tk.Label(janelacel, text=f"A conversão de celcius para fahrenheit, será de {conta}f")
    resultado.pack()

def fahrenheit():
    janelafah = tk.Tk()
    janelafah.title("Conversão de Fahrenheit para Celcius")
    janelafah.geometry("300x250")

    campo_de_texto1 = tk.Entry(janelafah)
    campo_de_texto1.pack()


    buttom2 = tk.Button(janelafah, text="Converter", command= lambda: receber_valor_fahrenheit(campo_de_texto1, janelafah))
    buttom2.pack(padx=20, pady=20) #Adiciona o botão na interface
    

def receber_valor_fahrenheit(campo_de_texto1, janelafah):
    num2 = campo_de_texto1.get()
    num2 = float(num2)

    resolução = (num2 - 32) * (5/9)

    resultado = tk.Label(janelafah, text=f"A conversão de fahrenheit para celcius, será de {resolução}c")
    resultado.pack()

#Criação da Janela 
janela = tk.Tk()
janela.title("Interface de Entrada") #Adiciona um titulo a Interface 

#Cria um rotulo para criar uma mensagem
mensagem_label = tk.Label(janela, text="Escolha uma das duas opções")
mensagem_label.pack(padx=20, pady=20) #Adiciona o Rotulo na interface


#Criação do Botão
buttomcel = tk.Button(janela, text="Conversão de Celcius", command=celcius)
buttomcel.pack(padx=20, pady=20) #Adiciona o botão na interface

buttomfah = tk.Button(janela, text="Conversão de Fahrenheit", command=fahrenheit)
buttomfah.pack(padx=20, pady=20) #Adiciona o botão na interface

#Loop para a Janela
janela.mainloop()
