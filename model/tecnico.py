from database.database import Database


class Tecnico:
    """Classe responsável pelas regras de negocio do Tecnico

    Returns:
        Tecnico: Retorna os atributos do Tecnico
    """

    db = Database()

    def __init__(self, cpf, nome, telefone, turno, equipe):
        self._cpf = self.tratar_cpf(cpf)
        self._nome = nome
        self._telefone = telefone
        self._turno = turno
        self._equipe = equipe

    @property
    def cpf(self):
        return self._cpf

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
        """Converte o CPF para apenas número

        Args:
            cpf (str): CPF a ser convertido

        Returns:
            int: Retona o CPF convertido em número
        """
        crt = '.-'
        cpf_tratado = cpf.translate(str.maketrans('', '', crt))
        return int(cpf_tratado)

    def inserir(self, tecnico):
        """Trata as regras de negócio antes de chamar o metodo que 
           insere o Tecnico no Bando de Dados

        Args:
            tecnico (Tecnico): Tecnico que será inserido
        """
        parametros = (tecnico.cpf, tecnico.nome, tecnico.telefone,
                      tecnico.turno, tecnico.equipe)
        self.db.inserir_tecnico(*parametros)

    def atualizar(self, tecnico):
        """Trata as regras de negócio antes de chamar o metodo que 
           Atualiza o Tecnico no Bando de Dados

        Args:
            tecnico (Tecnico): Tecnico que será Atualizado
        """
        parametros = (tecnico.nome, tecnico.telefone, tecnico.turno,
                      tecnico.equipe, tecnico.cpf)
        self.db.atualizar_tecnico(*parametros)

    def deletar(self, tecnico):
        """Chama o metodo que Deleta o Tecnico no Bando de Dados

        Args:
            tecnico (Tecnico): Tecnico que será Deletado
        """
        self.db.deletar_tecnico(tecnico.cpf)
