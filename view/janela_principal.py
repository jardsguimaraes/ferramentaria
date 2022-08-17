from constantes.constantes import BRANCO
from tkinter import Tk, Menu, Label, PhotoImage

import sys


class JanelaPrincipal:

    def __init__(self, local_magens):
        self.pasta_app =local_magens
        self.carregar_janela_principal()

    def janela_tecnico(self):
        pass

    def janela_ferramenta(self):
        pass

    def janela_reserva(self):
        pass

    def janela_sobre(self):
        pass

    def sair(self):
        sys.exit(0)

    def carregar_janela_principal(self):
        self.janela = Tk()
        self.janela.title('Ferramentaria')
        largura_janela = 1043
        altura_janela = 553
        largura_screen = self.janela.winfo_screenwidth()
        altura_screen = self.janela.winfo_screenheight()
        posx = largura_screen/2 - largura_janela/2
        posy = altura_screen/2 - altura_janela/2
        self.janela.geometry('%dx%d%+d+%d' % (largura_janela, altura_janela, posx, posy))
        self.janela.resizable(False, False)

        # Menu
        barra_menu = Menu(self.janela)

        barra_menu.add_command(label='Tecnico', command=self.janela_tecnico)
        barra_menu.add_command(label='Ferramenta', command=self.janela_ferramenta)
        barra_menu.add_command(label='Reserva', command=self.janela_reserva)
        barra_menu.add_command(label='Sobre', command=self.janela_sobre)
        barra_menu.add_command(label='Sair', command=self.sair)

        self.janela.configure(menu=barra_menu, background=BRANCO)

        # Imagens Janela Principal
        print(self.pasta_app)
        img_logo_ferramentaria = PhotoImage(file=self.pasta_app + '\\imagens\\logo1.png')
        img_logo_estacio = PhotoImage(file=self.pasta_app + '\\imagens\\estacio.png')

        lb_logo_ferramentaria = Label(self.janela, image=img_logo_ferramentaria, border=0)
        lb_logo_ferramentaria.pack()

        lb_logo_estacio = Label(self.janela, image=img_logo_estacio, border=0)
        lb_logo_estacio.pack()

        self.janela.mainloop()
        

