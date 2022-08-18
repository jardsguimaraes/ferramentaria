from constantes.constantes import AZUL, BRANCO, VERDE, VERMELHO
from tkinter import Frame
from tkinter.constants import NSEW


class Janela:

    def __init__(self, janela_principal):
        self.janela_principal = janela_principal
        self.criar_frames()

    def criar_frames(self):
        self.frame_cima = Frame(self.janela_principal, width=310, height=50,
                                relief='flat', bg=VERDE)
        self.frame_cima.grid(row=0, column=0)

        self.frame_baixo = Frame(self.janela_principal, width=310, height=500,
                                relief='flat', bg=AZUL)
        self.frame_baixo.grid(row=1, column=0, padx=0, pady=1, sticky=NSEW)

        self.frame_direita = Frame(self.janela_principal, width=729, height=550,
                                relief='flat', bg=VERMELHO)
        self.frame_direita.grid(row=0, column=1, rowspan=2, sticky=NSEW)


        


