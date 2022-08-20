from tkinter import Tk, LabelFrame

janela = Tk()
janela.geometry('200x200')
teste = LabelFrame(janela, text='Teste', width=100, height=100, border=1)
teste.pack()

try:
    if isinstance(teste):
        print('Frame Criado')
    else:
        print('Ainda não criado no else')
except (Exception):
    print('Ainda não criado')

janela.mainloop()