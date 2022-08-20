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

    def preencher_treeview(self, treeview):
        """Preenche o Treeview

        Args:
            treeview (Treeview): Treview a ser preenchido 
        """
        tecnicos_cadastrados = self.db.pesquisar_tecnicos()

        for (cpf, nome, telefone, turno, equipe) in tecnicos_cadastrados:
            treeview.insert('', 'end', values=(cpf, nome, telefone, turno,
                                               equipe))

    def pesquisar_tecnico_cpf(self, cpf):
        """Chama o metodo do banco de dados que retorna o tecnico
           como CPF informado

        Args:
            cpf (str): CPF a ser consultado

        Returns:
            Tecnico: Retorna o Tecnico com o campo CPF com apenas números
        """
        return self.db.pesquisar_tecnico_cpf(cpf)

    def pesquisar_tecnico_nome(self, nome):
        """Chama o metodo do banco de dados que retorna o tecnico
           como nome informado

        Args:
            nome (str): Nome a ser consultado

        Returns:
            Tecnico: Retorna o Tecnico com o Informado
        """
        return self.db.pesquisar_tecnico_nome(nome)

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
            messagebox.showerror(title='Error', message='Tecnico não encontrado')

    def deletar_tecnico(self, *args):
        """Verifica se o Tecnico existe no banco de dados, caso verdadeiro,
           chama o metodo que Deleta um Tecnico no banco de dados 
        """
        if self.db.pesquisar_tecnico_cpf(args[0]):            
            tecnico = Tecnico(*args)
            tecnico.deletar(tecnico)
        else:
            messagebox.showerror(title='Error', message='Tecnico não encontrado')


        

    

