from cgi import test
from psycopg2 import DatabaseError
from database.querys import PESQUISAR_TECNICOS, PESQUISAR_TECNICO_ARGUMENTO_CPF
from database.querys import PESQUISAR_TECNICO_ARGUMENTO_NOME, INSERIR_TECNICO
from database.querys import ATUALIZAR_TECNICO, DELETAR_TECNICO

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






































