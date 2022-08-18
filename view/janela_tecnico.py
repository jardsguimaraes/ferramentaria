from fractions import Fraction
from itertools import tee
from msilib.schema import RadioButton
from select import select
from turtle import width
from constantes.constantes import AZUL, BRANCO, VERDE_CLARO, VERMELHO, VERDE, PRETO
from view.janela import Janela
from tkinter import Button, Frame, IntVar, Label, LabelFrame, Entry, Scrollbar
from tkinter import Radiobutton, messagebox, ttk
from tkinter.constants import NW


class JanelaTecnico(Janela):

    def __init__(self, janela_principal):
        super().__init__(janela_principal)
        self.carregar_frame_cima()
        self.carregar_frame_baixo()
        self.carregar_frame_direita()

    def valida_formulario(self):
        retorno = True

        return retorno

    def carregar_frame_cima(self):
        lb_titulo = Label(self.frame_cima, text='Tecnico', font='Ivy 13 bold',
                          fg=BRANCO, bg=VERDE, relief='flat')
        lb_titulo.place(x=10, y=10)

    def carregar_frame_baixo(self):

        def botao_inserir():
            if self.valida_formulario():
                pass
            else:
                messagebox.showerror(title='Error', message='Todos os campos '
                                                            'devem estar '
                                                            'preeenchidos!!!')

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
            pass

        def botao_pesquisar():
            pass

        def limpar_entry_pesquisar():
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

        tv_tecnico = ttk.Treeview(fr_treeview, columns=('CPF', 'NOME', 'TELEFONE',
                                                        'TURNO', 'EQUIPE'),
                                                        show='headings')
        
        tv_tecnico.column('CPF', minwidth=0, width=100)
        tv_tecnico.column('NOME', minwidth=0, width=220)
        tv_tecnico.column('TELEFONE', minwidth=0, width=95)
        tv_tecnico.column('TURNO', minwidth=0, width=60)
        tv_tecnico.column('EQUIPE', minwidth=0, width=50)
        
        tv_tecnico.heading('CPF', text='CPF')
        tv_tecnico.heading('NOME', text='NOME')
        tv_tecnico.heading('TELEFONE', text='TELEFONE')
        tv_tecnico.heading('TURNO', text='TURNO')
        tv_tecnico.heading('EQUIPE', text='EQUIPE')

        tv_tecnico.place(relx=0.01, rely=0.01, relwidth=0.96, relheight=0.96)
        tv_tecnico.bind('<<TreeviewSelect>>', apresentar_dados_selecionados)

        sbv = Scrollbar(fr_treeview, orient='vertical', command=tv_tecnico.yview)
        tv_tecnico.configure(yscrollcommand=sbv.set)

        sbv.place(relx=0.97, rely=0.01, relwidth=0.03, relheight=0.96)
