from model.tecnico import Tecnico
from database.database import Database


class ControllerFerramentaria:

    db = Database()

    def preencher_treeview(self, treeview):
        tecnicos_cadastrados = self.db.pesquisar_tecnicos()

        for (cpf, nome, telefone, turno, equipe) in tecnicos_cadastrados:
            treeview.insert('', 'end', values=(cpf, nome, telefone, turno,
                                               equipe))
