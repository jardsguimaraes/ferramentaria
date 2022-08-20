from model.tecnico import Tecnico
from database.database import Database


class ControllerFerramentaria:

    db = Database()

    def preencher_treeview(self, treeview):
        tecnicos_cadastrados = self.db.pesquisar_tecnicos()

        for (cpf, nome, telefone, turno, equipe) in tecnicos_cadastrados:
            treeview.insert('', 'end', values=(cpf, nome, telefone, turno,
                                               equipe))

    def pesquisar_tecnico_cpf(self, cpf):
        return self.db.pesquisar_tecnico_cpf(cpf)

    def pesquisar_tecnico_nome(self, nome):
        return self.db.pesquisar_tecnico_nome(nome)

    def inserir_tecnico(self, *args):
        tecnico = Tecnico(*args)
        tecnico.inserir(tecnico)

    def atualizar_tecnico(self, *args):
        if self.db.pesquisar_tecnico_cpf(args[0]):
            tecnico = Tecnico(*args)
            tecnico.atualizar(tecnico)
        else:
            print('tecnico_vazio')

        

    

