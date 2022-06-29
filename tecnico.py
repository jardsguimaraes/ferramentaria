class Tecnico:

    def __init__(self, cpf, nome, contato, turno, equipe):
        self.cpf = cpf
        self.nome = nome
        self.contato = contato
        self.turno = turno
        self.equipe = equipe

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, valor):
        if isinstance(valor, str):
            valor = valor.replace('-', '')
            valor = valor.replace('.', '')
        self._cpf = valor

    @property
    def contato(self):
        return self._contato

    @contato.setter
    def contato(self, valor):
        valor = eval(valor.replace('-', ''))
        self._contato = valor

    def incluir_tecnico(self, tecnico):
        pass

    def alterar_tecnico(self, tecnico):
        pass

    def excluir_tecnico(self, tecnico):
        pass
