from constantes.constantes import AZUL, BRANCO, VERMELHO, VERDE, PRETO
from view.janela import Janela
from tkinter import Button, IntVar, Label, LabelFrame, Entry, Radiobutton, ttk


class JanelaTecnico(Janela):

    def __init__(self, janela_principal):
        super().__init__(janela_principal)
        self.carregar_frame_cima()
        self.carregar_frame_baixo()
        self.carregar_frame_direita()

    def carregar_frame_cima(self):
        lb_titulo = Label(self.frame_cima, text='Tecnico', font='Ivy 13 bold',
                          fg=BRANCO, bg=VERDE, relief='flat')
        lb_titulo.place(x=10, y=10)

    def carregar_frame_baixo(self):
        pass

    def carregar_frame_direita(self):
        pass
