from view.janela import Janela
from constantes.constantes import AZUL, BRANCO, VERDE_CLARO, VERDE, VERMELHO, PRETO
from controller.controller_ferramentaria import ControllerFerramentaria
from tkinter import Button, Frame, IntVar, Label, LabelFrame, Entry, Scrollbar
from tkinter import Radiobutton, messagebox, ttk
from tkinter.constants import END, NW, N
from tkcalendar import DateEntry


class JanelaFerramenta(Janela):
    """Classe da Jenela Ferramenta
    """

    def __init__(self, janela_principal):
        super().__init__(janela_principal)
        self.carrega_frame_cima()
        self.carrega_frame_baixo()
        self.carrega_frame_direita()
        self.ent_id.focus()

    def carrega_frame_cima(self):
        """Carrega os componentes do Frame Titulo
        """
        lb_titulo = Label(self.frame_cima, text='Ferramenta', font='Ivy 13 bold',
                          fg=BRANCO, bg=VERDE, relief='flat')
        lb_titulo.place(x=10, y=10)

    def carrega_frame_baixo(self):
        """Carrega os componentes do Frame Formulário
        """

        def valida_formaulario():
            pass

        def botao_inserir():
            pass

        def botao_atualizar():
            pass

        def botao_deletar():
            pass

        # ID
        lb_id = Label(self.frame_baixo, text='ID', anchor=NW,
                      font=('Ivy 13 bold'), fg=PRETO, bg=BRANCO,
                      relief='flat')
        lb_id.place(x=10, y=10)
        self.ent_id = Entry(self.frame_baixo, width=15,
                            justify='left', relief='solid')
        self.ent_id.place(x=40, y=10)

        # Descrição
        lb_descricao = Label(self.frame_baixo, text='Descrição: ', anchor=N,
                             font=('Ivy 13 bold'), fg=PRETO, bg=BRANCO,
                             relief='flat')
        lb_descricao.place(x=10, y=40)
        self.ent_descricaoricao = Entry(self.frame_baixo, width=45, justify='left',
                                        relief='solid')
        self.ent_descricaoricao.place(x=15, y=65)

        # Fabricante
        lb_fabricante = Label(self.frame_baixo, text='Fabricante: ', anchor=N,
                              font=('Ivy 13 bold'), fg=PRETO, bg=BRANCO,
                              relief='flat')
        lb_fabricante.place(x=10, y=95)
        self.ent_fabricante = Entry(self.frame_baixo, width=45, justify='left',
                                    relief='solid')
        self.ent_fabricante.place(x=15, y=120)

        # Voltagem
        lb_voltagem = Label(self.frame_baixo, text='Voltagem: ', anchor=N,
                            font=('Ivy 13 bold'), fg=PRETO, bg=BRANCO,
                            relief='flat')
        lb_voltagem.place(x=10, y=150)
        self.ent_voltagem = Entry(self.frame_baixo, width=15, justify='left',
                                  relief='solid')
        self.ent_voltagem.place(x=15, y=175)

        # Serial
        lb_serial = Label(self.frame_baixo, text='Serial: ', anchor=N,
                          font=('Ivy 13 bold'), fg=PRETO, bg=BRANCO,
                          relief='flat')
        lb_serial.place(x=130, y=150)
        self.ent_serial = Entry(self.frame_baixo, width=25, justify='left',
                                relief='solid')
        self.ent_serial.place(x=135, y=175)

        # Tamanho
        lb_tamanho = Label(self.frame_baixo, text='Tamanho: ', anchor=N,
                           font=('Ivy 13 bold'), fg=PRETO, bg=BRANCO,
                           relief='flat')
        lb_tamanho.place(x=10, y=205)
        self.ent_tamanho = Entry(self.frame_baixo, width=15, justify='left',
                                 relief='solid')
        self.ent_tamanho.place(x=15, y=230)

        # Medida
        lb_medida = Label(self.frame_baixo, text='Medida: ', anchor=N,
                          font=('Ivy 13 bold'), fg=PRETO, bg=BRANCO,
                          relief='flat')
        lb_medida.place(x=130, y=205)
        self.ent_medida = Entry(self.frame_baixo, width=25, justify='left',
                                relief='solid')
        self.ent_medida.place(x=135, y=230)

        # Manutenção
        lb_manutencao = Label(self.frame_baixo, text='Manutenção: ', anchor=N,
                              font=('Ivy 13 bold'), fg=PRETO, bg=BRANCO,
                              relief='flat')
        lb_manutencao.place(x=10, y=260)
        self.ent_manutencao = DateEntry(self.frame_baixo, width=15, background=AZUL,
                               foreground=BRANCO, borderwidth=2, year=2022,
                               locate='pt_br')
        self.ent_manutencao.place(x=15, y=285)

        # Tipo
        lb_tipo = Label(self.frame_baixo, text='Tipo: ', anchor=N,
                        font=('Ivy 13 bold'), fg=PRETO, bg=BRANCO,
                        relief='flat')
        lb_tipo.place(x=10, y=315)
        self.ent_tipo = Entry(self.frame_baixo, width=45, justify='left',
                              relief='solid')
        self.ent_tipo.place(x=15, y=340)

        # Botão Inserir
        btn_inserir = Button(self.frame_baixo, text='Inserir', width=8,
                             font=('Ivy 10 bold'), bg=AZUL, fg=BRANCO,
                             relief='raised', overrelief='ridge',
                             command=botao_inserir)
        btn_inserir.place(x=15, y=385)

        # Botão Atualizar
        btn_atualizar = Button(self.frame_baixo, text='Atualizar', width=8,
                               font=('Ivy 10 bold'), bg=VERDE, fg=BRANCO,
                               relief='raised', overrelief='ridge',
                               command=botao_atualizar)
        btn_atualizar.place(x=115, y=385)

        # Botão Deletar
        btn_deletar = Button(self.frame_baixo, text='Deletar', width=8,
                             font=('Ivy 10 bold'), bg=VERMELHO, fg=BRANCO,
                             relief='raised', overrelief='ridge',
                             command=botao_deletar)
        btn_deletar.place(x=215, y=385)

    def carrega_frame_direita(self):
        """Carrega os componentes do Frame da Direita
        """

        def apresentar_dados_selecionados(event):
            """Retonra a Ferramenta selecionada no Treeview

            Args:
                event (tuple): Tupla com a Ferramenta selecionada
            """

            pass

        def botao_pesquisar():
            """Verifica qual Opção do RadioButton esta selecionada e 
               chama a função correta
            """
            pass

        def limpar_entry_pesquisar():
            """Limpa o Campo de Pesquisa
            """
            pass

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

        rb_id = Radiobutton(fr_pesquisar, text='ID', variable=grupo_rb,
                             value=1, bg=BRANCO,
                             command=limpar_entry_pesquisar)
        rb_id.place(x=70, y=2)

        rb_descricao = Radiobutton(fr_pesquisar, text='Descricão', variable=grupo_rb,
                              value=2, bg=BRANCO,
                              command=limpar_entry_pesquisar)
        rb_descricao.place(x=115, y=2)

        rb_fabricante = Radiobutton(fr_pesquisar, text='Fabricante', variable=grupo_rb,
                              value=3, bg=BRANCO,
                              command=limpar_entry_pesquisar)
        rb_fabricante.place(x=200, y=2)

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

        self.tv_tecnico = ttk.Treeview(fr_treeview, columns=('ID', 'DESCRICAO', 'FABRICANTE',
                                                             'VOLTAGEM', 'SERIAL', 'TAMANHO',
                                                             'MANUTENCAO', 'MEDIDA', 'TIPO',
                                                             'MATERIAL'),
                                       show='headings')

        self.tv_tecnico.column('ID', minwidth=0, width=30)
        self.tv_tecnico.column('DESCRICAO', minwidth=0, width=220)
        self.tv_tecnico.column('FABRICANTE', minwidth=0, width=95)
        self.tv_tecnico.column('VOLTAGEM', minwidth=0, width=15)
        self.tv_tecnico.column('SERIAL', minwidth=0, width=50)
        self.tv_tecnico.column('TAMANHO', minwidth=0, width=50)
        self.tv_tecnico.column('MANUTENCAO', minwidth=0, width=50)
        self.tv_tecnico.column('MEDIDA', minwidth=0, width=50)
        self.tv_tecnico.column('TIPO', minwidth=0, width=50)
        self.tv_tecnico.column('MATERIAL', minwidth=0, width=50)

        self.tv_tecnico.heading('ID', text='ID')
        self.tv_tecnico.heading('DESCRICAO', text='DESCRICAO')
        self.tv_tecnico.heading('FABRICANTE', text='FABRICANTE')
        self.tv_tecnico.heading('VOLTAGEM', text='VOLTAGEM')
        self.tv_tecnico.heading('SERIAL', text='SERIAL')
        self.tv_tecnico.heading('TAMANHO', text='TAMANHO')
        self.tv_tecnico.heading('MANUTENCAO', text='MANUTENCAO')
        self.tv_tecnico.heading('MEDIDA', text='MEDIDA')
        self.tv_tecnico.heading('TIPO', text='TIPO')
        self.tv_tecnico.heading('MATERIAL', text='MATERIAL')

        self.tv_tecnico.place(relx=0.01, rely=0.01,
                              relwidth=0.96, relheight=0.96)
        self.tv_tecnico.bind('<<TreeviewSelect>>',
                             apresentar_dados_selecionados)

        sbv = Scrollbar(fr_treeview, orient='vertical',
                        command=self.tv_tecnico.yview)
        self.tv_tecnico.configure(yscrollcommand=sbv.set)

        sbv.place(relx=0.97, rely=0.01, relwidth=0.03, relheight=0.96)
