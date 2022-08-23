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
        self.controller = ControllerFerramentaria()
        self.carrega_frame_cima()
        self.carrega_frame_baixo()
        self.carrega_frame_direita()
        self.ent_id.focus()

    def limpar_campos(self):
        self.ent_id.delete(0, END)
        self.ent_descricao.delete(0, END)
        self.ent_fabricante.delete(0, END)
        self.ent_voltagem.delete(0, END)
        self.ent_serial.delete(0, END)
        self.ent_tamanho.delete(0, END)
        self.ent_medida.delete(0, END)
        self.ent_tipo.delete(0, END)
        self.ent_material.delete(0, END)

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
        self.ent_descricao = Entry(self.frame_baixo, width=45, justify='left',
                                   relief='solid')
        self.ent_descricao.place(x=15, y=65)

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

        # Material
        lb_material = Label(self.frame_baixo, text='Material: ', anchor=N,
                            font=('Ivy 13 bold'), fg=PRETO, bg=BRANCO,
                            relief='flat')
        lb_material.place(x=10, y=375)
        self.ent_material = Entry(self.frame_baixo, width=45, justify='left',
                                  relief='solid')
        self.ent_material.place(x=15, y=400)

        # Botão Inserir
        btn_inserir = Button(self.frame_baixo, text='Inserir', width=8,
                             font=('Ivy 10 bold'), bg=AZUL, fg=BRANCO,
                             relief='raised', overrelief='ridge',
                             command=botao_inserir)
        btn_inserir.place(x=15, y=445)

        # Botão Atualizar
        btn_atualizar = Button(self.frame_baixo, text='Atualizar', width=8,
                               font=('Ivy 10 bold'), bg=VERDE, fg=BRANCO,
                               relief='raised', overrelief='ridge',
                               command=botao_atualizar)
        btn_atualizar.place(x=115, y=445)

        # Botão Deletar
        btn_deletar = Button(self.frame_baixo, text='Deletar', width=8,
                             font=('Ivy 10 bold'), bg=VERMELHO, fg=BRANCO,
                             relief='raised', overrelief='ridge',
                             command=botao_deletar)
        btn_deletar.place(x=215, y=445)

    def carrega_frame_direita(self):
        """Carrega os componentes do Frame da Direita
        """

        def apresentar_dados_selecionados(event):
            """Retonra a Ferramenta selecionada no Treeview

            Args:
                event (tuple): Tupla com a Ferramenta selecionada
            """
            ferramenta_selecionada = self.tv_ferramenta.selection()
            valores = self.tv_ferramenta.item(ferramenta_selecionada, 'values')

            self.limpar_campos()

            self.ent_id.insert(0, valores[0])
            self.ent_descricao.insert(0, valores[1])
            self.ent_fabricante.insert(0, valores[2])
            self.ent_voltagem.insert(0, valores[3])
            self.ent_serial.insert(0, valores[4])
            self.ent_tamanho.insert(0, valores[5])
            self.ent_manutencao.set_date(valores[6])
            self.ent_medida.insert(0, valores[7])
            self.ent_tipo.insert(0, valores[8])
            self.ent_material.insert(0, valores[9])

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
                    self.tv_ferramenta, 'ferramenta')
                limpar_entry_pesquisar()
            elif grupo_rb.get() == 1:
                try:
                    id_informado = int(self.ent_pesquisar.get())
                    self.controller.pesquisar_ferramenta_id(
                        id_informado, self.tv_ferramenta)                    
                except (Exception):
                    messagebox.showinfo(title='Ferramenta não encontrada',
                                        message='Ferramenta não encontrada. '
                                        'Digite apenas números!!!')
                finally:
                    self.ent_pesquisar.delete(0, END)
                    self.ent_pesquisar.focus()
            elif grupo_rb.get() == 2:
                try:
                    descricao_informada = self.ent_pesquisar.get()
                    self.controller.pespesquisar_ferramenta_descricao(
                        descricao_informada, self.tv_ferramenta)                    
                except (Exception):
                    messagebox.showinfo(title='Ferramenta não encontrada',
                                        message='Ferramenta não encontrada. '
                                        'Valide o nome da Ferramenta!!!')
                finally:
                    self.ent_pesquisar.delete(0, END)
                    self.ent_pesquisar.focus()
            elif grupo_rb.get() == 3:
                try:
                    descricao_informada = self.ent_pesquisar.get()
                    self.controller.pespesquisar_ferramenta_fabricante(
                        descricao_informada, self.tv_ferramenta)                    
                except (Exception):
                    messagebox.showinfo(title='Ferramenta não encontrada',
                                        message='Ferramenta não encontrada. '
                                        'Valide o nome do Frabricante!!!')
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

        self.tv_ferramenta = ttk.Treeview(fr_treeview, columns=('ID', 'DESCRICAO', 'FABRICANTE',
                                                                'VOLTAGEM', 'SERIAL', 'TAMANHO',
                                                                'MANUTENCAO', 'MEDIDA', 'TIPO',
                                                                'MATERIAL'),
                                          show='headings')

        self.tv_ferramenta.column('ID', minwidth=10, width=20)
        self.tv_ferramenta.column('DESCRICAO', minwidth=50, width=150)
        self.tv_ferramenta.column('FABRICANTE', minwidth=50, width=95)
        self.tv_ferramenta.column('VOLTAGEM', minwidth=80, width=100)
        self.tv_ferramenta.column('SERIAL', minwidth=80, width=100)
        self.tv_ferramenta.column('TAMANHO', minwidth=30, width=70)
        self.tv_ferramenta.column('MANUTENCAO', minwidth=80, width=100)
        self.tv_ferramenta.column('MEDIDA', minwidth=80, width=100)
        self.tv_ferramenta.column('TIPO', minwidth=60, width=90)
        self.tv_ferramenta.column('MATERIAL', minwidth=60, width=120)

        self.tv_ferramenta.heading('ID', text='ID')
        self.tv_ferramenta.heading('DESCRICAO', text='DESCRICAO')
        self.tv_ferramenta.heading('FABRICANTE', text='FABRICANTE')
        self.tv_ferramenta.heading('VOLTAGEM', text='VOLTAGEM')
        self.tv_ferramenta.heading('SERIAL', text='SERIAL')
        self.tv_ferramenta.heading('TAMANHO', text='TAMANHO')
        self.tv_ferramenta.heading('MANUTENCAO', text='MANUTENCAO')
        self.tv_ferramenta.heading('MEDIDA', text='MEDIDA')
        self.tv_ferramenta.heading('TIPO', text='TIPO')
        self.tv_ferramenta.heading('MATERIAL', text='MATERIAL')

        self.tv_ferramenta.place(relx=0.01, rely=0.01,
                                 relwidth=0.96, relheight=0.96)
        self.tv_ferramenta.bind('<<TreeviewSelect>>',
                                apresentar_dados_selecionados)

        sbv = Scrollbar(fr_treeview, orient='vertical',
                        command=self.tv_ferramenta.yview)
        sbh = Scrollbar(fr_treeview, orient='horizontal',
                        command=self.tv_ferramenta.xview)
        self.tv_ferramenta.configure(yscrollcommand=sbv.set,
                                     xscrollcommand=sbh.set)

        sbv.place(relx=0.97, rely=0.01, relwidth=0.03, relheight=0.96)
        sbh.place(relx=0.01, rely=0.97, relwidth=0.96, relheight=0.03)

        self.controller.preencher_treeview(self.tv_ferramenta, 'ferramenta')
