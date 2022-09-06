from constantes.constantes import BRANCO
from tkinter import Tk, Message


class JanelaSobre:
    """Janela com as informações dos Alunos que 
       desenvolveram o programa
    """

    def __init__(self):
        self.carregar_janela_sobre()

    def carregar_janela_sobre(self):
        janela_sobre = Tk()
        janela_sobre.title('Sobre')
        largura_janela = 500
        altuta_janela = 300
        largura_screen = janela_sobre.winfo_screenwidth()
        altura_screen = janela_sobre.winfo_screenheight()
        posx = largura_screen/2 - largura_janela/2
        posy = altura_screen/2 - altuta_janela/2
        janela_sobre.geometry('%dx%d+%d+%d' %
                              (largura_janela, altuta_janela, posx, posy))
        janela_sobre.resizable(False, False)
        janela_sobre.configure(bg=BRANCO)

        msg_linha_1 = "Trabalho acadêmico para atender a Missão Certificadora"
        msg_linha_2 = "Mundo 1 do Curso Desenvolvimento Full Stack"
        msg_linha_3 = "pela instituíção de ensino Estacio. \n\n"
        msg_linha_4 = "                               GRUPO 4 \n\n"
        msg_linha_5 = " Allan Eduardo da Conceição Fortes(202205187391)\n"
        msg_linha_6 = "Jards de Oliveira Guimarães(202205003922) \n"
        mgs_linha_7 = "Rafael Vilarinho Dias Jacob(202205050289) \n"
        mgs_linha_8 = "Raferson Neres Faustino da Silva(202205216594) \n"

        menssagem = (f'{msg_linha_1} {msg_linha_2} {msg_linha_3} {msg_linha_4}'
                     f'{msg_linha_5} {msg_linha_6} {mgs_linha_7} {mgs_linha_8}')

        msg = Message(janela_sobre, text=menssagem)
        msg.configure(bg=BRANCO,font='Ivy 16', width=500)
        msg.pack()
