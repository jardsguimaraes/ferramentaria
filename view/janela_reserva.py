from view.janela import Janela
from view.janela_reserva_pesq_tecnico import JanelaReservaPesqTecnico
from constantes.constantes import AZUL, BRANCO, PRETO, VERDE, VERMELHO
from constantes.constantes import VERDE_CLARO, LISTA_HORARIOS
from controller.controller_ferramentaria import ControllerFerramentaria
from tkinter import SEL, Entry, IntVar, Label, Button, LabelFrame, Frame, StringVar
from tkinter import Radiobutton, messagebox, ttk, Scrollbar
from tkinter.constants import NW, END
from tkcalendar import DateEntry


class JanelaReserva(Janela):

    def __init__(self, janela_principal, local_imagens):
        super().__init__(janela_principal)
        self.pasta_app = local_imagens
        self.controller = ControllerFerramentaria()
        self.nome_tecnico = StringVar()
        self.nome_ferramenta = StringVar()
        self.carrega_frame_cima()
        self.carrega_frame_baixo()
        self.carrega_frame_direita()

    def limpar_campos(self):
        self.ent_id.delete(0, END)
        self.ent_id_tecnico.delete(0, END)
        self.ent_id_ferramenta.delete(0, END)

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
            JanelaReservaPesqTecnico(self.ent_id_tecnico,
                                     self.nome_tecnico)

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
        self.lb_nome_tecnico = Label(self.frame_baixo, textvariable=self.nome_tecnico, anchor=NW,
                                     font='Times 10', fg=AZUL, bg=BRANCO,
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
        self.lb_nome_ferramenta = Label(self.frame_baixo, textvariable=self.nome_ferramenta,
                                        anchor=NW, font='Times 10', fg=AZUL,
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

        def apresentar_dados_selecionados(event):
            reserva_selecionada = self.tv_reserva.selection()
            valores = self.tv_reserva.item(reserva_selecionada, 'values')
            tecnico_cpf, ferramenta_id = self.controller.pesquisar_reserva(
                valores[0])

            self.limpar_campos()

            self.ent_id.insert(0, valores[0])
            self.ent_id_tecnico.insert(0, tecnico_cpf)
            self.nome_tecnico.set(valores[1])
            self.ent_id_ferramenta.insert(0, ferramenta_id)
            self.nome_ferramenta.set(valores[2])
            self.ent_devolucao.set_date(valores[3])
            self.cbx_hora_devolucao.set(valores[4])

        def limpar_entry_pesquisar():
            """Limpa o Campo de Pesquisa
            """
            self.ent_pesquisar.delete(0, END)
            self.ent_pesquisar.focus()

        def botao_pesquisar():
            """Verifica qual Opção do RadioButton esta selecionada e 
               chama a função correta
            """
            if grupo_rb.get() == 0:
                self.controller.preencher_treeview(
                    self.tv_reserva, 'reserva')
                limpar_entry_pesquisar()
            elif grupo_rb.get() == 1:
                try:
                    tecnico_informado = self.ent_pesquisar.get()
                    self.controller.pesquisar_reserva_tecnico(
                        tecnico_informado, self.tv_reserva)
                except (Exception):
                    messagebox.showinfo(title='Tecnico não encontrado',
                                        message='Tecnico não encontrado. '
                                        'Valide o nome do Tecnico!!!')
                finally:
                    self.ent_pesquisar.delete(0, END)
                    self.ent_pesquisar.focus()
            elif grupo_rb.get() == 2:
                try:
                    ferramenta_informada = self.ent_pesquisar.get()
                    self.controller.pesquisar_reserva_ferramenta(
                        ferramenta_informada, self.tv_reserva)
                except (Exception):
                    messagebox.showinfo(title='Ferramenta não encontrada',
                                        message='Ferramenta não encontrada. '
                                        'Valide o nome da Ferramenta!!!')
                finally:
                    self.ent_pesquisar.delete(0, END)
                    self.ent_pesquisar.focus()

        # Frame Pesquisar
        fr_pesquisar = LabelFrame(self.frame_direita, text='Pesquisar',
                                  width=730, height=82, relief='solid',
                                  bg=BRANCO, border=1)
        fr_pesquisar.grid(column=0, row=0)

        self.ent_pesquisar = Entry(fr_pesquisar, width=95, justify='left',
                                   relief='solid')
        self.ent_pesquisar.place(x=5, y=30)

        # RadioButton
        grupo_rb = IntVar()

        rb_todos = Radiobutton(fr_pesquisar, text='Todos', variable=grupo_rb,
                               value=0, bg=BRANCO, command=botao_pesquisar)
        rb_todos.place(x=5, y=2)

        rb_tecnico = Radiobutton(fr_pesquisar, text='Tecnico', variable=grupo_rb,
                                 value=1, bg=BRANCO,
                                 command=limpar_entry_pesquisar)
        rb_tecnico.place(x=70, y=2)

        rb_ferramenta = Radiobutton(fr_pesquisar, text='Ferramenta', variable=grupo_rb,
                                    value=2, bg=BRANCO,
                                    command=limpar_entry_pesquisar)
        rb_ferramenta.place(x=150, y=2)

        rb_todos.select()

        # Botão pesquisar
        btn_pesquisar = Button(fr_pesquisar, text='Pesquisar', width=8,
                               font='Ivy 13 bold', bg=VERDE_CLARO, fg=BRANCO,
                               relief='raised', overrelief='ridge',
                               command=botao_pesquisar)
        btn_pesquisar.place(x=585, y=21)

        # Frame Treeview
        fr_treeview = Frame(self.frame_direita, width=730, height=460,
                            relief='solid', bg=BRANCO, border=1)
        fr_treeview.grid(column=0, row=1, pady=5)

        self.tv_reserva = ttk.Treeview(fr_treeview, columns=('ID', 'TECNICO', 'FERRAMENTA',
                                                             'DATA_DEVOLUCAO', 'HORA_DEVOLUCAO'),
                                       show='headings')

        self.tv_reserva.column('ID', minwidth=10, width=20)
        self.tv_reserva.column('TECNICO', minwidth=0, width=220)
        self.tv_reserva.column('FERRAMENTA', minwidth=50, width=150)
        self.tv_reserva.column('DATA_DEVOLUCAO', minwidth=80, width=100)
        self.tv_reserva.column('HORA_DEVOLUCAO', minwidth=80, width=100)

        self.tv_reserva.heading('ID', text='ID')
        self.tv_reserva.heading('TECNICO', text='TECNICO')
        self.tv_reserva.heading('FERRAMENTA', text='FERRAMENTA')
        self.tv_reserva.heading('DATA_DEVOLUCAO', text='DATA DEVOLUCAO')
        self.tv_reserva.heading('HORA_DEVOLUCAO', text='HORA DEVOLUCAO')

        self.tv_reserva.place(relx=0.01, rely=0.01,
                              relwidth=0.96, relheight=0.96)
        self.tv_reserva.bind('<<TreeviewSelect>>',
                             apresentar_dados_selecionados)

        sbv = Scrollbar(fr_treeview, orient='vertical',
                        command=self.tv_reserva.yview)
        sbh = Scrollbar(fr_treeview, orient='horizontal',
                        command=self.tv_reserva.xview)
        self.tv_reserva.configure(yscrollcommand=sbv.set,
                                  xscrollcommand=sbh.set)

        sbv.place(relx=0.97, rely=0.01, relwidth=0.03, relheight=0.96)
        sbh.place(relx=0.01, rely=0.97, relwidth=0.96, relheight=0.03)

        self.controller.preencher_treeview(self.tv_reserva, 'reserva')
