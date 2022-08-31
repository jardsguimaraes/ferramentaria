from constantes.constantes import BRANCO, VERDE_CLARO
from controller.controller_ferramentaria import ControllerFerramentaria
from tkinter import Button, Entry, Frame, LabelFrame, Scrollbar, Tk
from tkinter import messagebox, ttk
from tkinter.constants import END


class JanelaReservaPesqFerramenta:

    def __init__(self, ent_id_ferramenta, nome_ferramenta):
        self.ent_id_ferramenta = ent_id_ferramenta
        self.nome_ferramenta = nome_ferramenta
        self.controller = ControllerFerramentaria()
        self.janela = Tk()
        self.janela.title('Reserva - Pesquisa Tecnico')
        largura_janela = 500
        altuta_janela = 300
        largura_screen = self.janela.winfo_screenwidth()
        altura_screen = self.janela.winfo_screenheight()
        posx = largura_screen/2 - largura_janela/2
        posy = altura_screen/2 - altuta_janela/2
        self.janela.geometry('%dx%d+%d+%d' %
                             (largura_janela, altuta_janela, posx, posy))
        self.janela.resizable(False, False)
        self.janela.configure(bg=BRANCO)
        self.carrega_frame_pesquisa()

    def carrega_frame_pesquisa(self):

        def botao_pesquisar():
            try:
                descricao_informada = self.ent_pesquisar.get()
                self.controller.pespesquisar_ferramenta_descricao(
                    descricao_informada, self.tv_ferramenta)
            except (Exception):
                messagebox.showinfo(title='Ferramenta não encontrada',
                                    message='Ferramenta não encontrada. '
                                    'Valide o nome da Ferramenta!!!')

        def ferramenta_selecionada(event):
            ferramneta = self.tv_ferramenta.selection()
            valores = self.tv_ferramenta.item(ferramneta, 'values')

            self.ent_id_ferramenta.delete(0, END)
            self.nome_ferramenta.set(None)

            self.ent_id_ferramenta.insert(0, valores[0])
            self.nome_ferramenta.set(valores[1])

            self.janela.destroy()

        # Frame Pesquisar
        fr_pesquisar = LabelFrame(self.janela, text='Pesquisar pelo Nome da Ferramenta',
                                  width=497, height=62, relief='solid',
                                  bg=BRANCO, border=1)
        fr_pesquisar.grid(column=0, row=0)

        self.ent_pesquisar = Entry(fr_pesquisar, width=65, justify='left',
                                   relief='solid')
        self.ent_pesquisar.place(x=5, y=10)

        # Botão pesquisar
        btn_pesquisar = Button(fr_pesquisar, text='Pesquisar', width=7,
                               font='Ivy 8 bold', bg=VERDE_CLARO, fg=BRANCO,
                               relief='raised', overrelief='ridge',
                               command=botao_pesquisar)
        btn_pesquisar.place(x=405, y=5)

        # Frame Treeview
        fr_treeview = Frame(self.janela, width=497, height=230,
                            relief='solid', bg=BRANCO, border=1)
        fr_treeview.grid(column=0, row=1)

        self.tv_ferramenta = ttk.Treeview(fr_treeview, columns=('CPF', 'NOME', 'TELEFONE',
                                                                'TURNO', 'EQUIPE'),
                                          show='headings')

        self.tv_ferramenta.column('CPF', minwidth=0, width=100)
        self.tv_ferramenta.column('NOME', minwidth=0, width=220)
        self.tv_ferramenta.column('TELEFONE', minwidth=0, width=95)
        self.tv_ferramenta.column('TURNO', minwidth=0, width=60)
        self.tv_ferramenta.column('EQUIPE', minwidth=0, width=100)

        self.tv_ferramenta.heading('CPF', text='CPF')
        self.tv_ferramenta.heading('NOME', text='NOME')
        self.tv_ferramenta.heading('TELEFONE', text='TELEFONE')
        self.tv_ferramenta.heading('TURNO', text='TURNO')
        self.tv_ferramenta.heading('EQUIPE', text='EQUIPE')

        self.tv_ferramenta.place(relx=0.01, rely=0.01,
                                 relwidth=0.96, relheight=0.96)
        self.tv_ferramenta.bind('<Double-1>', ferramenta_selecionada)

        sbv = Scrollbar(fr_treeview, orient='vertical',
                        command=self.tv_ferramenta.yview)
        sbh = Scrollbar(fr_treeview, orient='horizontal',
                        command=self.tv_ferramenta.xview)
        self.tv_ferramenta.configure(yscrollcommand=sbv.set,
                                     xscrollcommand=sbh.set)

        sbv.place(relx=0.97, rely=0.01, relwidth=0.03, relheight=0.96)
        sbh.place(relx=0.01, rely=0.97, relwidth=0.96, relheight=0.03)

        self.controller.preencher_treeview(self.tv_ferramenta, 'ferramenta')
