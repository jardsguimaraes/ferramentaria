from database.database import Database


class Ferramenta:

    db = Database()

    def __init__(self, id, descricao, fabricante,
                 voltagem, serial, tamanho, manutencao,
                 medida, tipo, material):
        self._id = id
        self._descricao = descricao
        self._fabricante = fabricante
        self._voltagem = voltagem
        self._serial = serial
        self._tamanho = tamanho
        self._manutencao = manutencao
        self._medida = medida
        self._tipo = tipo
        self._material = material

    @property
    def id(self):
        return self._id

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante

    @property
    def voltagem(self):
        return self._voltagem

    @voltagem.setter
    def voltagem(self, voltagem):
        self._voltagem = voltagem

    @property
    def serial(self):
        return self._serial

    @serial.setter
    def serial(self, serial):
        self._serial = serial

    @property
    def tamanho(self):
        return self._tamanho

    @tamanho.setter
    def tamanho(self, tamanho):
        self._tamanho = tamanho

    @property
    def manutencao(self):
        return self._manutencao

    @manutencao.setter
    def manutencao(self, manutencao):
        self._manutencao = manutencao

    @property
    def medida(self):
        return self._medida

    @medida.setter
    def medida(self, medida):
        self._medida = medida

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, material):
        self._material = material

    def tratar_data(self, data):
        print(data)
        data_formatada = str(data).split('-')
        data_formatada = f'{data_formatada[2]}/{data_formatada[1]}/{data_formatada[0]}'
        return str(data_formatada)

    def inserir(self, ferramenta):
        parametros = (ferramenta.descricao, ferramenta.fabricante, ferramenta.voltagem,
                      ferramenta.serial, ferramenta.tamanho,
                      ferramenta.manutencao, ferramenta.medida,
                      ferramenta.tipo, ferramenta.material)
        self.db.inserir_ferramenta(*parametros)

    def atualizar(self, ferramenta):
        pass

    def deletar(self, ferramenta):
        """Chama o metodo que Deleta a Ferramenta no Bando de Dados

        Args:
            ferramenta (Ferramenta): Ferramenta que será Deletada
        """
        self.db.deletar_ferramenta(ferramenta.id)

        """self, id, descricao, fabricante,
                 voltagem, serial, tamanho, manutencao,
                 medida, tipo, material)
        """
