from webbrowser import BackgroundBrowser
from view.janela import Janela
from constantes.constantes import AZUL, BRANCO, PRETO, VERDE, VERMELHO, LISTA_HORARIOS
from controller.controller_ferramentaria import ControllerFerramentaria
from tkinter import Entry, Label, Button, PhotoImage, ttk
# from tkinter import Radiobutton, messagebox, ttk
from tkinter.constants import NW
from tkcalendar import DateEntry


class JanelaReserva(Janela):

    def __init__(self, janela_principal, local_imagens):
        super().__init__(janela_principal)
        self.pasta_app = local_imagens
        self.controller = ControllerFerramentaria()
        self.nome_tecnico = 'Jards de Oliveira Gumaraes de Albuquerque'
        self.nome_ferramenta = 'Chave de Boca'
        self.carrega_frame_cima()
        self.carrega_frame_baixo()
        self.carrega_frame_direita()

    def carrega_frame_cima(self):
        lb_titulo = Label(self.frame_cima, text='Reserva:', font='Ivy 13 bold',
                          fg=BRANCO, bg=VERDE, relief='flat')
        lb_titulo.place(x=10, y=10)

    def carrega_frame_baixo(self):

        def botao_inserir():
            pass

        def botao_atualizar():
            pass

        def botao_deletar():
            pass

        def botao_pesquisar_tecnico():
            print('Pesquisar Tecnico')

        def botao_pesquisar_ferramenta():
            print('Pesquisar Tecnico')

        # ID
        lb_id = Label(self.frame_baixo, text='ID:', anchor=NW, font='Ivy 13 bold',
                      bg=BRANCO, fg=PRETO, relief='flat')
        lb_id.place(x=10, y=10)
        self.ent_id = Entry(self.frame_baixo, width=15, justify='left',
                            relief='solid')
        self.ent_id.place(x=40, y=10)

        # ID Tecnico
        lb_id_tecnico = Label(self.frame_baixo, text='ID Tecnico:', anchor=NW,
                              font=('Ivy 13 bold'), fg=PRETO, bg=BRANCO,
                              relief='flat')
        lb_id_tecnico.place(x=10, y=40)
        self.ent_id_tecnico = Entry(self.frame_baixo, width=15,
                                    justify='left', relief='solid')
        self.ent_id_tecnico.place(x=105, y=40)
        self.btn_lupa_tecnico = Button(self.frame_baixo, text='Pesquisar', width=8,
                                       font=('Ivy 7 bold'), relief='raised',
                                       overrelief='ridge',
                                       command=botao_pesquisar_tecnico)
        self.btn_lupa_tecnico.place(x=205, y=40)
        self.lb_nome_tecnico = Label(self.frame_baixo, text=self.nome_tecnico, anchor=NW,
                                     font='Times 10', fg=PRETO, bg=BRANCO,
                                     relief='flat')
        self.lb_nome_tecnico.place(x=15, y=60)

        # ID Ferramenta
        lb_id_ferramenta = Label(self.frame_baixo, text='ID Ferramenta:', anchor=NW,
                                 font=('Ivy 13 bold'), fg=PRETO, bg=BRANCO,
                                 relief='flat')
        lb_id_ferramenta.place(x=10, y=90)
        self.ent_id_ferramenta = Entry(self.frame_baixo, width=15,
                                       justify='left', relief='solid')
        self.ent_id_ferramenta.place(x=135, y=90)
        self.btn_lupa_ferramenta = Button(self.frame_baixo, text='Pesquisar', width=8,
                                          font=('Ivy 7 bold'), relief='raised',
                                          overrelief='ridge',
                                          command=botao_pesquisar_ferramenta)
        self.btn_lupa_ferramenta.place(x=235, y=90)
        self.lb_nome_ferramenta = Label(self.frame_baixo, text=self.nome_ferramenta,
                                        anchor=NW, font='Times 10', fg=PRETO,
                                        bg=BRANCO, relief='flat')
        self.lb_nome_ferramenta.place(x=15, y=110)

        # ID Devolução
        lb_id_devolucao = Label(self.frame_baixo, text='Devolução:', anchor=NW,
                                font=('Ivy 13 bold'), fg=PRETO, bg=BRANCO,
                                relief='flat')
        lb_id_devolucao.place(x=10, y=140)
        lb_data_devolucao = Label(self.frame_baixo, text='Data: ', anchor=NW,
                                  font=('Ivy 13 bold'), fg=PRETO, bg=BRANCO,
                                  relief='flat')
        lb_data_devolucao.place(x=15, y=165)
        self.ent_devolucao = DateEntry(self.frame_baixo, width=15, background=AZUL,
                                       foreground=BRANCO, borderwidth=2, year=2022,
                                       locate='pt_br')
        self.ent_devolucao.place(x=65, y=165)
        lb_hora_devolucao = Label(self.frame_baixo, text='Hora: ', anchor=NW,
                                  font=('Ivy 13 bold'), fg=PRETO, bg=BRANCO,
                                  relief='flat')
        lb_hora_devolucao.place(x=185, y=165)
        self.cbx_hora_devolucao = ttk.Combobox(self.frame_baixo, values=LISTA_HORARIOS,
                                               width=6)
        self.cbx_hora_devolucao.place(x=235, y=165)
        self.cbx_hora_devolucao.set('00:00')
        # self.ent_hora_devolucao = Entry(self.frame_baixo, width=10,
        #                                justify='left', relief='solid')
        # self.ent_hora_devolucao.place(x=235, y=165)

        # Botão Inserir
        btn_inserir = Button(self.frame_baixo, text='Inserir', width=8,
                             font=('Ivy 10 bold'), bg=AZUL, fg=BRANCO,
                             relief='raised', overrelief='ridge',
                             command=botao_inserir)
        btn_inserir.place(x=15, y=200)

        # Botão Atualizar
        btn_atualizar = Button(self.frame_baixo, text='Atualizar', width=8,
                               font=('Ivy 10 bold'), bg=VERDE, fg=BRANCO,
                               relief='raised', overrelief='ridge',
                               command=botao_atualizar)
        btn_atualizar.place(x=115, y=200)

        # Botão Deletar
        btn_deletar = Button(self.frame_baixo, text='Deletar', width=8,
                             font=('Ivy 10 bold'), bg=VERMELHO, fg=BRANCO,
                             relief='raised', overrelief='ridge',
                             command=botao_deletar)
        btn_deletar.place(x=215, y=200)

    def carrega_frame_direita(self):
        pass
