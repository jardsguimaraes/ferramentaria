from ast import Delete
from html import entities
from webbrowser import get
from constantes.constantes import AZUL, BRANCO, VERDE_CLARO, VERMELHO, VERDE, PRETO
from controller.controller_ferramentaria import ControllerFerramentaria
from view.janela import Janela
from tkinter import Button, Frame, IntVar, Label, LabelFrame, Entry, Scrollbar
from tkinter import Radiobutton, messagebox, ttk
from tkinter.constants import NW, END


class JanelaTecnico(Janela):

    def __init__(self, janela_principal):
        super().__init__(janela_principal)
        self.controller = ControllerFerramentaria()
        self.carregar_frame_cima()
        self.carregar_frame_baixo()
        self.carregar_frame_direita()
        self.ent_cpf.focus()

    def valida_formulario(self):
        retorno = True

        if not self.ent_cpf.get().split():
            retorno = False
        elif not self.ent_nome.get().split():
            retorno = False
        elif not self.ent_telefone.get().split():
            retorno = False
        elif not self.ent_equipe.get().split():
            retorno = False

        return retorno

    def limpar_campos(self):
        self.ent_cpf.delete(0, END)
        self.ent_nome.delete(0, END)
        self.ent_telefone.delete(0, END)
        self.ent_equipe.delete(0, END)

    def pega_formulario(self):
        parametros = (self.ent_cpf.get(), self.ent_nome.get(),
                      self.ent_telefone.get(), self.cbx_turno.get(),
                      self.ent_equipe.get().upper())
        return parametros

    def carregar_frame_cima(self):
        lb_titulo = Label(self.frame_cima, text='Tecnico', font='Ivy 13 bold',
                          fg=BRANCO, bg=VERDE, relief='flat')
        lb_titulo.place(x=10, y=10)

    def carregar_frame_baixo(self):

        def botao_inserir():
            if self.valida_formulario():
                parametros = self.pega_formulario()
                self.controller.inserir_tecnico(*parametros)
                self.tv_tecnico.delete(*self.tv_tecnico.get_children())
                self.controller.preencher_treeview(self.tv_tecnico)
                self.limpar_campos()
                messagebox.showinfo(title='Cadastrado!!!',
                                    message='Tecnico Cadastrado com Sucesso')
            else:
                messagebox.showerror(title='Error', message='Todos os campos '
                                                            'devem estar '
                                                            'preeenchidos!!!')
                self.ent_cpf.focus()

        def botao_atualizar():
            pass

        def botao_deletar():
            pass

        # CPF
        lb_cpf = Label(self.frame_baixo, text='CPF: ', anchor=NW,
                       font='Ivy 13 bold', fg=PRETO, bg=BRANCO,
                       relief='flat')
        lb_cpf.place(x=10, y=10)

        self.ent_cpf = Entry(self.frame_baixo, width=15, justify='left',
                             relief='solid')
        self.ent_cpf.place(x=15, y=35)

        # Nome
        lb_nome = Label(self.frame_baixo, text='Nome: ', anchor=NW,
                        font='Ivy 13 bold', fg=PRETO, bg=BRANCO,
                        relief='flat')
        lb_nome.place(x=10, y=65)

        self.ent_nome = Entry(self.frame_baixo, width=45, justify='left',
                              relief='solid')
        self.ent_nome.place(x=15, y=90)

        # Telefone
        lb_telefone = Label(self.frame_baixo, text='Telefone: ', anchor=NW,
                            font='Ivy 13 bold', fg=PRETO, bg=BRANCO,
                            relief='flat')
        lb_telefone.place(x=10, y=120)

        self.ent_telefone = Entry(self.frame_baixo, width=45, justify='left',
                                  relief='solid')
        self.ent_telefone.place(x=15, y=145)

        # Turno
        lista_turno = ['MANHA', 'TARDE', 'NOITE']

        lb_turno = Label(self.frame_baixo, text='Turno: ', anchor=NW,
                         font='Ivy 13 bold', fg=PRETO, bg=BRANCO,
                         relief='flat')
        lb_turno.place(x=10, y=175)

        self.cbx_turno = ttk.Combobox(self.frame_baixo, values=lista_turno,
                                      width=15)
        self.cbx_turno.place(x=15, y=200)

        self.cbx_turno.set('MANHA')

        # Equipe
        lb_equipe = Label(self.frame_baixo, text='Equipe: ', anchor=NW,
                          font='Ivy 13 bold', fg=PRETO, bg=BRANCO,
                          relief='flat')
        lb_equipe.place(x=10, y=230)

        self.ent_equipe = Entry(self.frame_baixo, width=45, justify='left',
                                relief='solid')
        self.ent_equipe.place(x=15, y=255)

        # Botão Inserir
        self.btn_inserir = Button(self.frame_baixo, text='Inserir', width=8,
                                  font='Ivy 13 bold', bg=AZUL, fg=BRANCO,
                                  relief='raised',
                                  overrelief='ridge', command=botao_inserir)
        self.btn_inserir.place(x=15, y=300)

        # Botão Atualizar
        self.btn_atualizar = Button(self.frame_baixo, text='Atualizar', width=8,
                                    font='Ivy 13 bold', bg=VERDE, fg=BRANCO,
                                    relief='raised',
                                    overrelief='ridge', command=botao_atualizar)
        self.btn_atualizar.place(x=115, y=300)

        # Botão Deletar
        self.btn_deletar = Button(self.frame_baixo, text='Deletar', width=8,
                                  font='Ivy 13 bold', bg=VERMELHO, fg=BRANCO,
                                  relief='raised',
                                  overrelief='ridge', command=botao_deletar)
        self.btn_deletar.place(x=215, y=300)

    def carregar_frame_direita(self):

        def apresentar_dados_selecionados(event):
            tecnico_selecionado = self.tv_tecnico.selection()[0]
            valores = self.tv_tecnico.item(tecnico_selecionado, 'values')

            self.limpar_campos()

            self.ent_cpf.insert(0, valores[0])
            self.ent_nome.insert(0, valores[1])
            self.ent_telefone.insert(0, valores[2])
            self.cbx_turno.set(valores[3])
            self.ent_equipe.insert(0, valores[4])

        def botao_pesquisar():
            if grupo_rb.get() == 0:
                self.controller.preencher_treeview(self.tv_tecnico)
                self.ent_pesquisar.delete(0, END)
                self.ent_pesquisar.focus()
            elif grupo_rb.get() == 1:
                try:
                    cpf_informado = int(self.ent_pesquisar.get())
                    tecnico_cpf = self.controller.pesquisar_tecnico_cpf(
                        cpf_informado)
                    self.tv_tecnico.delete(*self.tv_tecnico.get_children())
                    for (cpf, nome, telefone, turno, equipe) in tecnico_cpf:
                        self.tv_tecnico.insert('', 'end', values=(cpf, nome, telefone,
                                                                  turno, equipe))
                except (Exception):
                    messagebox.showinfo(title='Tecnico não encontrado',
                                        message='CPF não encontadro. '
                                        'Digite apenas números!!!')
                finally:
                    self.ent_pesquisar.delete(0, END)
                    self.ent_pesquisar.focus()
            else:
                try:
                    nome_informado = self.ent_pesquisar.get()
                    tecnico_nome = self.controller.pesquisar_tecnico_nome(
                        nome_informado)
                    self.tv_tecnico.delete(*self.tv_tecnico.get_children())
                    for (cpf, nome, telefone, turno, equipe) in tecnico_nome:
                        self.tv_tecnico.insert('', 'end', values=(cpf, nome, telefone,
                                                                  turno, equipe))
                except (Exception):
                    messagebox.showinfo(title='Tecnico não encontrado',
                                        message='Nome não encontadro!!!')
                finally:
                    self.ent_pesquisar.delete(0, END)
                    self.ent_pesquisar.focus()

        def limpar_entry_pesquisar():
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

        rb_cpf = Radiobutton(fr_pesquisar, text='CPF', variable=grupo_rb,
                             value=1, bg=BRANCO,
                             command=limpar_entry_pesquisar)
        rb_cpf.place(x=70, y=2)

        rb_nome = Radiobutton(fr_pesquisar, text='Nome', variable=grupo_rb,
                              value=2, bg=BRANCO,
                              command=limpar_entry_pesquisar)
        rb_nome.place(x=125, y=2)

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

        self.tv_tecnico = ttk.Treeview(fr_treeview, columns=('CPF', 'NOME', 'TELEFONE',
                                                             'TURNO', 'EQUIPE'),
                                       show='headings')

        self.tv_tecnico.column('CPF', minwidth=0, width=100)
        self.tv_tecnico.column('NOME', minwidth=0, width=220)
        self.tv_tecnico.column('TELEFONE', minwidth=0, width=95)
        self.tv_tecnico.column('TURNO', minwidth=0, width=60)
        self.tv_tecnico.column('EQUIPE', minwidth=0, width=50)

        self.tv_tecnico.heading('CPF', text='CPF')
        self.tv_tecnico.heading('NOME', text='NOME')
        self.tv_tecnico.heading('TELEFONE', text='TELEFONE')
        self.tv_tecnico.heading('TURNO', text='TURNO')
        self.tv_tecnico.heading('EQUIPE', text='EQUIPE')

        self.tv_tecnico.place(relx=0.01, rely=0.01,
                              relwidth=0.96, relheight=0.96)
        self.tv_tecnico.bind('<<TreeviewSelect>>',
                             apresentar_dados_selecionados)

        sbv = Scrollbar(fr_treeview, orient='vertical',
                        command=self.tv_tecnico.yview)
        self.tv_tecnico.configure(yscrollcommand=sbv.set)

        sbv.place(relx=0.97, rely=0.01, relwidth=0.03, relheight=0.96)

        self.controller.preencher_treeview(self.tv_tecnico)
