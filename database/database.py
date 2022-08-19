from psycopg2 import DatabaseError
from database.querys import PESQUISAR_TECNICOS, PESQUISAR_TECNICO_ARGUMENTO_CPF
from database.querys import PESQUISAR_TECNICO_ARGUMENTO_NOME, INSERIR_TECNICO
from database.querys import ATUALIZAR_TECNICO, DELETAR_TECNICO

import psycopg2


class Database:

    def __init__(self):
        self.conn = None
        self.cursor = None

    def abrir_conexao(self):
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
        try:
            self.conn.close()
        except (Exception, DatabaseError) as ex:
            print('Erro ao fechar a conexão', ex)

    def pesquisar_tecnicos(self):
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
        try:
            conexao = self.abrir_conexao()
            self.cursor = conexao.cursor()
            self.cursor.execute(ATUALIZAR_TECNICO, args)
            conexao.commit()
        except (Exception, DatabaseError) as ex:
            print('Erro no Update Tecnico', ex)
        finally:
            self.fechar_conexao()





































