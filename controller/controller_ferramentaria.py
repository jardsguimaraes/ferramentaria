from datetime import datetime
from optparse import Values
from model.tecnico import Tecnico
from database.database import Database
from tkinter import messagebox


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

    def preencher_treeview(self, treeview, nome_tela):
        """Preenche o Treeview

        Args:
            treeview (Treeview): Treview a ser preenchido 
        """

        if nome_tela == 'tecnico':
            tecnicos_cadastrados = self.db.pesquisar_tecnicos()

            for (cpf, nome, telefone, turno, equipe) in tecnicos_cadastrados:
                treeview.insert('', 'end', values=(cpf, nome, telefone, turno,
                                                   equipe))
        elif nome_tela == 'ferramenta':
            ferramentas_cadastradas = self.db.pesquisar_ferramenta()
            for (id, descricao, fabricante, voltagem, serial, tamanho,
                 manutencao, medida, tipo, material) in ferramentas_cadastradas:
                manutencao = self.tratar_data(manutencao, 'ferramenta')
                treeview.insert('', 'end', values=(id, descricao, fabricante,
                                                   voltagem, serial, tamanho,
                                                   manutencao, medida, tipo,
                                                   material))
        elif nome_tela == 'reserva':
            pass

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

    def pesquisar_ferramenta_id(self, id):
        """Chama o metodo do banco de dados que retorna a ferramenta
           com o ID informado

        Args:
            id (int): id a ser consultado

        Returns:
            list: Retorna a Ferramenta com o id informado
        """
        return self.db.pesquisar_ferramenta_id(id)

    def pespesquisar_ferramenta_descricao(self):
        pass

    def pespesquisar_ferramenta_fabricante(self):
        pass
