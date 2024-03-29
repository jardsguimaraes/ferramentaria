from model.tecnico import Tecnico
from model.ferramenta import Ferramenta
from model.reserva import Reserva
from database.database import Database
from tkinter import messagebox
from datetime import datetime


class ControllerFerramentaria:
    """Calsse que faz a interação entre as telas e as regras de
       negocio doprograma

    Returns:
        _type_: Retorna as informações solicitadas pelo usuário
    """

    db = Database()

    def tratar_data(self, data, nome_janela):
        if nome_janela == 'ferramenta':
            data_formatada = str(data).split('-')
            data_formatada = f'{data_formatada[2]}/{data_formatada[1]}/{data_formatada[0]}'
            return str(data_formatada)
        elif nome_janela == 'reserva':
            data_formatada = datetime.strftime(data, "%d/%m/%Y")
            hora_formatada = datetime.strftime(data, "%H:%M")
            return data_formatada, hora_formatada
    
    def preencher_treeview(self, treeview, nome_tela):
        """Preenche o Treeview

        Args:
            treeview (Treeview): Treview a ser preenchido
        """

        if nome_tela == 'tecnico':
            tecnicos_cadastrados = self.db.pesquisar_tecnicos()
            treeview.delete(*treeview.get_children())
            for (cpf, nome, telefone, turno, equipe) in tecnicos_cadastrados:
                treeview.insert('', 'end', values=(cpf, nome, telefone, turno,
                                                   equipe))
        elif nome_tela == 'ferramenta':
            ferramentas_cadastradas = self.db.pesquisar_ferramenta()
            treeview.delete(*treeview.get_children())
            for (id, descricao, fabricante, voltagem, serial, tamanho,
                 manutencao, medida, tipo, material) in ferramentas_cadastradas:
                manutencao = self.tratar_data(manutencao, 'ferramenta')
                treeview.insert('', 'end', values=(id, descricao, fabricante,
                                                   voltagem, serial, tamanho,
                                                   manutencao, medida, tipo,
                                                   material))
        elif nome_tela == 'reserva':
            reservas_cadastradas = self.db.pesquisar_reservas()
            treeview.delete(*treeview.get_children())
            for (id, tecnico, ferramenta, devolucao) in reservas_cadastradas:
                data_devolucao, hora_devolucao = self.tratar_data(
                    devolucao, 'reserva')
                treeview.insert('', 'end', values=(id, tecnico, ferramenta,
                                                   data_devolucao, hora_devolucao))

    def pesquisar_tecnico_cpf(self, cpf, treeview):
        """Chama o metodo do banco de dados que retorna o tecnico
           com o CPF informado

        Args:
            cpf (str): CPF a ser consultado
        """
        tecnico_cpf = self.db.pesquisar_tecnico_cpf(cpf)
        treeview.delete(*treeview.get_children())

        for (cpf, nome, telefone, turno, equipe) in tecnico_cpf:
            treeview.insert('', 'end', values=(cpf, nome, telefone, turno,
                                               equipe))

    def pesquisar_tecnico_nome(self, nome, treeview):
        """Chama o metodo do banco de dados que retorna o tecnico
           como nome informado

        Args:
            nome (str): Nome a ser consultado
        """
        tecnico_nome = self.db.pesquisar_tecnico_nome(nome)
        treeview.delete(*treeview.get_children())

        for (cpf, nome, telefone, turno, equipe) in tecnico_nome:
            treeview.insert('', 'end', values=(cpf, nome, telefone,
                                               turno, equipe))

    def inserir_tecnico(self, *args):
        """Chama o metodo que Insere um Tecnico no banco de dados
        """
        tecnico = Tecnico(*args)
        tecnico.inserir(tecnico)

    def atualizar_tecnico(self, *args):
        """Verifica se o Tecnico existe no banco de dados, caso verdadeiro,
           chama o metodo que Atualiza um Tecnico no banco de dados
        """
        if self.db.pesquisar_tecnico_cpf(args[0]):
            tecnico = Tecnico(*args)
            tecnico.atualizar(tecnico)
        else:
            messagebox.showerror(
                title='Error', message='Tecnico não encontrado')

    def deletar_tecnico(self, *args):
        """Verifica se o Tecnico existe no banco de dados, caso verdadeiro,
           chama o metodo que Deleta um Tecnico no banco de dados
        """
        if self.db.pesquisar_tecnico_cpf(args[0]):
            tecnico = Tecnico(*args)
            tecnico.deletar(tecnico)
        else:
            messagebox.showerror(
                title='Error', message='Tecnico não encontrado')

    def pesquisar_ferramenta_id(self, id, treeview):
        """Chama o metodo do banco de dados que retorna a ferramenta
           com o ID informado

        Args:
            id (int): ID a ser pesquisado
            treeview (tkinter): Treeview a ser preenchido 
        """
        ferramenta_id = self.db.pesquisar_ferramenta_id(id)
        treeview.delete(*treeview.get_children())

        for (id, descricao, fabricante, voltagem, serial, tamanho,
             manutencao, medida, tipo, material) in ferramenta_id:
            manutencao = self.tratar_data(manutencao, 'ferramenta')
            treeview.insert('', 'end', values=(id, descricao, fabricante,
                                               voltagem, serial, tamanho,
                                               manutencao, medida, tipo,
                                               material))

    def pespesquisar_ferramenta_descricao(self, descricao, treeview):
        """Chama o metodo do banco de dados que retorna a ferramenta
           com a Descrição informada

        Args:
            descricao (str): Descição a ser pesquisada
            treeview (tkinter): Treeview a ser preenchido 
        """
        ferrmenta_descricao = self.db.pesquisar_ferramenta_descricao(descricao)
        treeview.delete(*treeview.get_children())

        for (id, descricao, fabricante, voltagem, serial, tamanho,
             manutencao, medida, tipo, material) in ferrmenta_descricao:
            manutencao = self.tratar_data(manutencao, 'ferramenta')
            treeview.insert('', 'end', values=(id, descricao, fabricante,
                                               voltagem, serial, tamanho,
                                               manutencao, medida, tipo,
                                               material))

    def pespesquisar_ferramenta_fabricante(self, fabricante, treeview):
        """Chama o metodo do banco de dados que retorna a ferramenta
           com o Fabricante informado

        Args:
            descricao (str): Fabricante a ser pesquisado
            treeview (tkinter): Treeview a ser preenchido 
        """
        ferrmenta_fabricante = self.db.pesquisar_ferramenta_fabricante(
            fabricante)
        treeview.delete(*treeview.get_children())

        for (id, descricao, fabricante, voltagem, serial, tamanho,
             manutencao, medida, tipo, material) in ferrmenta_fabricante:
            manutencao = self.tratar_data(manutencao, 'ferramenta')
            treeview.insert('', 'end', values=(id, descricao, fabricante,
                                               voltagem, serial, tamanho,
                                               manutencao, medida, tipo,
                                               material))

    def inserir_ferramenta(self, *args):
        ferramenta = Ferramenta(*args)
        ferramenta.inserir(ferramenta)

    def atualizar_ferramenta(self, *args):
        if self.db.pesquisar_ferramenta_id(args[0]):
            ferramenta = Ferramenta(*args)
            ferramenta.atualizar(ferramenta)
        else:
            messagebox.showerror(
                title='Error', message='Ferramenta não Encontrada')

    def deletar_ferramenta(self, *args):
        """"Verifica se a Ferrmenta existe no banco de dados, caso verdadeiro,
           chama o metodo que Deleta uma Ferramenta no banco de dados
        """
        if self.db.pesquisar_ferramenta_id(args[0]):
            ferramenta = Ferramenta(*args)
            ferramenta.deletar(ferramenta)
        else:
            messagebox.showerror(
                title='Error', message='Ferramenta não Encontrada')

    def pesquisar_reserva(self, id_reserva):
        reserva = self.db.pesquisar_reserva(id_reserva)
        for (tecnico_cpf, ferramenta_id) in reserva:
            return tecnico_cpf, ferramenta_id
    
    def pesquisar_reserva_tecnico(self, nome, treeview):
        nome_tecnico = self.db.pesquisar_reserva_tecnico(nome)
        treeview.delete(*treeview.get_children())

        for (id, tecnico, ferramenta, devolucao) in nome_tecnico:
            data_devolucao, hora_devolucao = self.tratar_data(
                devolucao, 'reserva')
            treeview.insert('', 'end', values=(id, tecnico, ferramenta,
                                               data_devolucao, hora_devolucao))

    def pesquisar_reserva_ferramenta(self, descricao, treeview):
        """Chama o metodo do banco de dados que retorna a Reserva
           com a ferramenta informada

        Args:
            descricao_ferramenta (str): Ferramenta a ser pesquisada
            treeview (tkinter): Treeview a ser preenchido 
        """
        ferrmenta_descricao = self.db.pesquisar_reserva_ferramneta(descricao)
        treeview.delete(*treeview.get_children())

        for (id, tecnico, ferramenta, devolucao) in ferrmenta_descricao:
            data_devolucao, hora_devolucao = self.tratar_data(
                devolucao, 'reserva')
            treeview.insert('', 'end', values=(id, tecnico, ferramenta,
                                               data_devolucao, hora_devolucao))

    def inserir_reserva(self, *args):
        reserva = Reserva(*args)
        reserva.inserir(reserva)
    
    def atualizar_reserva(self, *args):
        if self.db.pesquisar_reserva(args[0]):
            reserva = Reserva(*args)
            reserva.atualizar(reserva)
        else:
            messagebox.showerror(
                title='Error', message='Reserva não Encontrada')
    
    def deletar_reserva(self, *args):
        if self.db.pesquisar_reserva(args[0]):
            reserva = Reserva(*args)
            reserva.deletar(reserva)
        else:
            messagebox.showerror(
                title='Error', message='Reserva não Encontrada')