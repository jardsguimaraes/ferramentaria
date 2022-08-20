from constantes.constantes import BRANCO
from view.janela_tecnico import JanelaTecnico
from view.janela_sobre import JanelaSobre
from tkinter import Tk, Menu, Label, PhotoImage

import sys


class JanelaPrincipal:
    """Classe da Jenela Principal do Programa
    """

    def __init__(self, local_magens):
        self.pasta_app = local_magens
        self.carregar_janela_principal()

    def limpar_logo(self):
        """Limpa as logos da tela para a inserção dos componentes 
           da próxima janela"""
        self.lb_logo_ferramentaria.destroy()
        self.lb_logo_estacio.destroy()
    
    def janela_tecnico(self):
        """Chama a Janela Tecnico
        """
        self.limpar_logo()
        JanelaTecnico(self.janela)

    def janela_ferramenta(self):
        """Chama a Janela Ferramenta
        """
        pass

    def janela_reserva(self):
        """Chama a Janela Reserva
        """
        pass

    def janela_sobre(self):
        """Chama a Janela Sobre
        """
        JanelaSobre()

    def sair(self):
        """Fecha o Programa
        """
        sys.exit(0)

    def carregar_janela_principal(self):
        """Carrega os componentes da Janela Principal
        """
        self.janela = Tk()
        self.janela.title('Ferramentaria')
        largura_janela = 1043
        altura_janela = 553
        largura_screen = self.janela.winfo_screenwidth()
        altura_screen = self.janela.winfo_screenheight()
        posx = largura_screen/2 - largura_janela/2
        posy = altura_screen/2 - altura_janela/2
        self.janela.geometry('%dx%d%+d+%d' %
                             (largura_janela, altura_janela, posx, posy))
        self.janela.resizable(False, False)

        # Menu
        barra_menu = Menu(self.janela)

        barra_menu.add_command(label='Tecnico', command=self.janela_tecnico)
        barra_menu.add_command(
            label='Ferramenta', command=self.janela_ferramenta)
        barra_menu.add_command(label='Reserva', command=self.janela_reserva)
        barra_menu.add_command(label='Sobre', command=self.janela_sobre)
        barra_menu.add_command(label='Sair', command=self.sair)

        self.janela.configure(menu=barra_menu, background=BRANCO)

        # Imagens Janela Principal
        img_logo_ferramentaria = PhotoImage(
            file=self.pasta_app + '\\imagens\\logo1.png')
        img_logo_estacio = PhotoImage(
            file=self.pasta_app + '\\imagens\\estacio.png')

        self.lb_logo_ferramentaria = Label(
            self.janela, image=img_logo_ferramentaria, border=0)
        self.lb_logo_ferramentaria.pack()

        self.lb_logo_estacio = Label(self.janela, image=img_logo_estacio, border=0)
        self.lb_logo_estacio.pack()

        self.janela.mainloop()
