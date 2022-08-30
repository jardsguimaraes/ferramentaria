from psycopg2 import DatabaseError
from database.querys import PESQUISAR_FERRAMENTA_DESCRICAO, PESQUISAR_TECNICOS
from database.querys import PESQUISAR_TECNICO_ARGUMENTO_NOME
from database.querys import INSERIR_TECNICO, PESQUISAR_TECNICO_ARGUMENTO_CPF
from database.querys import ATUALIZAR_TECNICO, DELETAR_TECNICO
from database.querys import PESQUISAR_FERRAMENTAS, PESQUISAR_FERRAMENTA_ID
from database.querys import PESQUISAR_FERRAMENTA_FABRICANTE
from database.querys import INSERIR_FERRAMENTA, DELETAR_FERRAMENTA
from database.querys import ATUALIZAR_FERRAMENTA, PESQUISAR_RESERVAS
from database.querys import PESQUISAR_RESERVA_TECNICO, PESQUISAR_RESERVA_FERRAMENTA

import psycopg2


class Database:
    """Classe que faz a interação com o SGBD
    """

    def __init__(self):
        self.conn = None
        self.cursor = None

    def abrir_conexao(self):
        """Abre uma conexão com o SGBD

        Returns:
            connection: Retorna uma conexão com o SGBD
        """
        try:
            self.conn = psycopg2.connect(database='postgres',
                                         user='postgres',
                                         password='@Adm10092007',
                                         host='127.0.0.1',
                                         port='5432')
            return self.conn
        except (Exception, DatabaseError) as ex:
            print('Erro a se conectar no Banco', ex)

    def fechar_conexao(self):
        """Fecha o cursor e a conexão aberta com o SGBD
        """
        try:
            self.conn.close()
        except (Exception, DatabaseError) as ex:
            print('Erro ao fechar a conexão', ex)

    def pesquisar_tecnicos(self):
        """Realiza um Select no Banco

        Returns:
            list:  Retorna todos os Tecnicos cadastrados
        """
        try:
            conexao = self.abrir_conexao()
            self.cursor = conexao.cursor()
            self.cursor.execute(PESQUISAR_TECNICOS)
            resultado = self.cursor.fetchall()
            return resultado
        except (Exception, DatabaseError) as ex:
            print('Erro no Select Tecnico ', ex)
        finally:
            self.fechar_conexao()

    def pesquisar_tecnico_cpf(self, cpf):
        """Realiza um Select no Banco

        Args:
            cpf (int): CPF a ser procurado no Bando de Dados. 
                       Deve ser informado apenas os números

        Returns:
            list:  Retorna o Tecnico com o CPF informado
        """
        try:
            conexao = self.abrir_conexao()
            self.cursor = conexao.cursor()
            self.cursor.execute(PESQUISAR_TECNICO_ARGUMENTO_CPF, (cpf, ))
            resultado = self.cursor.fetchall()
            return resultado
        except (Exception, DatabaseError) as ex:
            print('Erro no Select Tecnico CPF ', ex)
        finally:
            self.fechar_conexao()

    def pesquisar_tecnico_nome(self, nome):
        """Realiza um Select no Banco

        Args:
            nome (str): Nome a ser procurado no Bando de Dados. 

        Returns:
            list:  Retorna o Tecnico com o Nome informado
        """
        try:
            conexao = self.abrir_conexao()
            self.cursor = conexao.cursor()
            self.cursor.execute(PESQUISAR_TECNICO_ARGUMENTO_NOME, (nome, ))
            resultado = self.cursor.fetchall()
            return resultado
        except (Exception, DatabaseError) as ex:
            print('Erro no Select Tecnico Nome ', ex)
        finally:
            self.fechar_conexao()

    def inserir_tecnico(self, *args):
        """Insere um Tecnico no SGBD
        """
        try:
            conexao = self.abrir_conexao()
            self.cursor = conexao.cursor()
            self.cursor.execute(INSERIR_TECNICO, args)
            conexao.commit()
        except (Exception, DatabaseError) as ex:
            print('Erro no Insert Tecnico', ex)
        finally:
            self.fechar_conexao()

    def deletar_tecnico(self, cpf):
        """Deleta um Tecnico no SGBD

        Args:
            cpf (int): Deve ser informado o CPF do Tecnico a ser Deletado
        """
        try:
            conexao = self.abrir_conexao()
            self.cursor = conexao.cursor()
            self.cursor.execute(DELETAR_TECNICO, (cpf, ))
            conexao.commit()
        except (Exception, DatabaseError) as ex:
            print('Erro no Delete Tecnico', ex)
        finally:
            self.fechar_conexao()

    def atualizar_tecnico(self, *args):
        """Atualiza um Tecnico no SGBD

        Args:
            args (Tecnico): Deve ser passado todas os attibutos da classe Tecnico
        """
        try:
            conexao = self.abrir_conexao()
            self.cursor = conexao.cursor()
            self.cursor.execute(ATUALIZAR_TECNICO, args)
            conexao.commit()
        except (Exception, DatabaseError) as ex:
            print('Erro no Update Tecnico', ex)
        finally:
            self.fechar_conexao()

    def pesquisar_ferramenta(self):
        """Função para pesquisar todas as Ferramentas

        Returns:
            list: Retorna todas as Ferramentas cadastradas no SGBD
        """
        try:
            conexao = self.abrir_conexao()
            self.cursor = conexao.cursor()
            self.cursor.execute(PESQUISAR_FERRAMENTAS)
            resultado = self.cursor.fetchall()
            return resultado
        except (Exception, DatabaseError) as ex:
            print('Erro no Select Ferramenta ', ex)
        finally:
            self.fechar_conexao()

    def pesquisar_ferramenta_id(self, id):
        """Função para pesquisar Ferramenta pelo ID

        Args:
            id (int): ID da Ferramenta a ser pesquisada

        Returns:
            list: Retorna a Ferramenta cadastradas no SGBD com o ID
            informado
        """
        try:
            conexao = self.abrir_conexao()
            self.cursor = conexao.cursor()
            self.cursor.execute(PESQUISAR_FERRAMENTA_ID, (id, ))
            resultado = self.cursor.fetchall()
            return resultado
        except (Exception, DatabaseError) as ex:
            print('Erro no Select Ferramenta ID ', ex)
        finally:
            self.fechar_conexao()

    def pesquisar_ferramenta_descricao(self, descricao):
        """Função para pesquisar Ferramenta pela Descrição

        Args:
            descricao (str): Descrição da Ferramenta

        Returns:
            list: Retorna todas as Ferramentas cadastradas no SGBD com a
            descrição informada
        """
        try:            
            conexao = self.abrir_conexao()
            self.cursor = conexao.cursor()
            self.cursor.execute(PESQUISAR_FERRAMENTA_DESCRICAO, (descricao, ))
            resultado = self.cursor.fetchall()
            return resultado
        except (Exception, DatabaseError) as ex:
            print('Erro no Select Ferramenta Descrição ', ex)
        finally:
            self.fechar_conexao()

    def pesquisar_ferramenta_fabricante(self, fabricante):
        """Função para pesquisar Ferramenta pelo fabricante

        Args:
            fabricante (str): fabricante da Ferramenta

        Returns:
            list: Retorna todas as Ferramentas cadastradas no SGBD com o
            fabricante informado
        """
        try:            
            conexao = self.abrir_conexao()
            self.cursor = conexao.cursor()
            self.cursor.execute(PESQUISAR_FERRAMENTA_FABRICANTE, (fabricante, ))
            resultado = self.cursor.fetchall()
            return resultado
        except (Exception, DatabaseError) as ex:
            print('Erro no Select Ferramenta_fabricante', ex)
        finally:
            self.fechar_conexao()

    def inserir_ferramenta(self, *args):
        """Função para Cadastrar uma Ferramenta no SGBD
        """
        try:
            conexao = self.abrir_conexao()
            self.cursor = conexao.cursor()
            self.cursor.execute(INSERIR_FERRAMENTA, args)
            conexao.commit()
        except (Exception, DatabaseError) as ex:
            print('Erro no Insert Ferramenta', ex)
        finally:
            self.fechar_conexao()

    def deletar_ferramenta(self, id):
        """Função para Deletar uma Ferramenta no SGBD

        Args:
            id (int): ID da ferramenta
        """
        try:
            conexao = self.abrir_conexao()
            self.cursor = conexao.cursor()
            self.cursor.execute(DELETAR_FERRAMENTA, (id, ))
            conexao.commit()
        except (Exception, DatabaseError) as ex:
            print('Erro no Select Ferramenta Fabricante', ex)
        finally:
            self.fechar_conexao()

    def atualizar_ferramenta(self, *args):
        try:
            conexao = self.abrir_conexao()
            self.cursor = conexao.cursor()
            self.cursor.execute(ATUALIZAR_FERRAMENTA, args)
            conexao.commit()
        except (Exception, DatabaseError) as ex:
            print('Erro no Atualizar Ferramenta', ex)
        finally:
            self.fechar_conexao()

    def pesquisar_reserva(self):
        """Função para pesquisar todas as Reservas

        Returns:
            list: Retorna todas as Reservas cadastradas no SGBD
        """
        try:
            conexao = self.abrir_conexao()
            self.cursor = conexao.cursor()
            self.cursor.execute(PESQUISAR_RESERVAS)
            resultado = self.cursor.fetchall()
            return resultado
        except (Exception, DatabaseError) as ex:
            print('Erro no Select Reserva ', ex)
        finally:
            self.fechar_conexao()
    
    def pesquisar_reserva_tecnico(self, nome):
        """Realiza um Select no Banco

        Args:
            nome (str): Nome a ser procurado a Reserva no Bando de Dados. 

        Returns:
            list:  Retorna a Reserva com o Nome do Tecnico informado
        """
        try:
            conexao = self.abrir_conexao()
            self.cursor = conexao.cursor()
            self.cursor.execute(PESQUISAR_RESERVA_TECNICO, (nome, ))
            resultado = self.cursor.fetchall()
            return resultado
        except (Exception, DatabaseError) as ex:
            print('Erro no Select Reserva Tecnico ', ex)
        finally:
            self.fechar_conexao()

    def pesquisar_reserva_ferramneta(self, ferramenta):
        """Realiza um Select no Banco

        Args:
            ferramenta (str): Ferramenta a ser procurado a Reserva no Bando de Dados.

        Returns:
            list:  Retorna a Reserva com o Nome da Ferramenta informada
        """
        try:
            conexao = self.abrir_conexao()
            self.cursor = conexao.cursor()
            self.cursor.execute(PESQUISAR_RESERVA_FERRAMENTA, (ferramenta, ))
            resultado = self.cursor.fetchall()
            return resultado
        except (Exception, DatabaseError) as ex:
            print('Erro no Select Reserva Ferrramenta ', ex)
        finally:
            self.fechar_conexao()

    
    def inserir_reserva(self):        
        pass












