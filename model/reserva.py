from database.database import Database


class Reserva:

    db = Database()

    def __init__(self, id, tecnico, ferramenta,
                 devolucao):
        self._id = id
        self._tecnico = tecnico
        self._ferramenta = ferramenta
        self._devolucao = devolucao

    @property
    def id(self):
        return self._id

    @property
    def tecnico(self):
        return self._tecnico

    @tecnico.setter
    def tecnico(self, id_tecnico):
        self._tecnico = id_tecnico

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, id_ferramenta):
        self._ferramenta = id_ferramenta
    
    @property
    def devolucao(self):
        return self._devolucao

    @devolucao.setter
    def data_devolucao(self, devolucao):
        self._devolucao = devolucao

    def tratar_devolucao(data, hora):
        devolucao_formatada = str(data) + ' ' + str(hora)
        print(type(devolucao_formatada))
        print(devolucao_formatada)
        
        return devolucao_formatada

    def inserir(self, reserva):
        """Chama o metodo que Insere a Reserva no Bando de Dados

        Args:
            reserva (Reserva): Reserva que será Inserida
        """
        parametros = (reserva.tecnico,
                      reserva.ferramenta,
                      reserva.devolucao)
        self.db.inserir_reserva(*parametros)

    def atualizar(self, reserva):
        """Chama o metodo que Atualiza a Reserva no Bando de Dados

        Args:
            reserva (Reserva): Reserva que será Atualizada
        """
        # devolucao = self.tratar_devolucao(reserva.data_devolucao,
        #                                   reserva.hora_devolucao)
        parametros = (reserva.tecnico,
                      reserva.ferramenta,
                      reserva.devolucao,
                      reserva.id)
        self.db.atualizar_reserva(*parametros)

    def deletar(self, reserva):
        """Chama o metodo que Deleta a Reserva no Bando de Dados

        Args:
            reserva (Reserva): Reserva que será Deletada
        """
        self.db.deletar_reserva(reserva.id)
