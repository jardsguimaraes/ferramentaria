from database.database import Database

class Tecnico:

    db = Database()

    def __init__(self, cpf, nome, telefone, turno, equipe):
        self._cpf = cpf
        self._nome = nome
        self._telefone = telefone
        self._turno = turno
        self._equipe = equipe

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone

    @property
    def tunro(self):
        return self._turno

    @tunro.setter
    def turno(self, turno):
        self._turno = turno

    @property
    def equipe(self):
        return self._equipe

    @equipe.setter
    def equipe(self, equipe):
        self._equipe = equipe

    def tratar_cpf(self, cpf):
        crt ='.-'
        cpf_tratado = cpf.translate(str.maketrans('', '', crt))
        return int(cpf_tratado)

    def inserir(self):
        pass
    
    def atualizar(self):
        pass

    def deletar(self):
        pass

    



























































