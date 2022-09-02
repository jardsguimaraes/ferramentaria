# QUERYS TABELA TECNICO
#   SELECT
PESQUISAR_TECNICOS = "SELECT * FROM tecnico ORDER BY cpf"
PESQUISAR_TECNICO_ARGUMENTO_CPF = "SELECT * FROM tecnico WHERE cpf = %s"
PESQUISAR_TECNICO_ARGUMENTO_NOME = """SELECT * FROM tecnico
                                      WHERE nome like '%%' || %s || '%%'"""

#   INSERT
INSERIR_TECNICO = "INSERT INTO tecnico VALUES (%s, %s, %s, %s, %s)"

#   UPDATE
ATUALIZAR_TECNICO = """UPDATE tecnico SET nome = %s, contato = %s, turno = %s,
                       equipe = %s WHERE cpf = %s"""

#   DELETE
DELETAR_TECNICO = "DELETE FROM tecnico WHERE cpf = %s"


# QUERYS TABELA FERRAMENTA
#   SELECT
PESQUISAR_FERRAMENTAS = "SELECT * FROM ferramenta ORDER BY id"
PESQUISAR_FERRAMENTA_ID = "SELECT * FROM ferramenta WHERE id = %s"
PESQUISAR_FERRAMENTA_DESCRICAO = """SELECT * FROM ferramenta
                                    WHERE descricao like '%%' || %s || '%%'"""
PESQUISAR_FERRAMENTA_FABRICANTE = """SELECT * FROM ferramenta WHERE
                                     fabricante like '%%' || %s || '%%'"""

#   INSERT
INSERIR_FERRAMENTA = """INSERT INTO ferramenta (descricao, fabricante,
                        voltagem, serial, tamanho, manutencao, medida, tipo,
                        material)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

#   DELETE
DELETAR_FERRAMENTA = "DELETE FROM ferramenta WHERE id = %s"

#   UPDATE
ATUALIZAR_FERRAMENTA = """UPDATE ferramenta SET descricao = %s, fabricante = %s,
                          voltagem = %s, serial = %s, tamanho = %s,
                          manutencao = %s, medida = %s, tipo = %s,
                          material = %s WHERE id = %s"""

# QUERYS TABELA FERRAMENTA
#   SELECT
PESQUISAR_RESERVA = """SELECT tecnico.cpf, ferramenta.id
                         FROM ferramenta, tecnico, reserva
                        WHERE reserva.tecnico_cpf = tecnico.cpf AND
                              reserva.ferramenta_id = ferramenta.id AND
                              reserva.id = %s
                        ORDER BY
                              reserva.id"""
PESQUISAR_RESERVAS = """SELECT reserva.id, tecnico.nome,
                               ferramenta.descricao, reserva.devolucao
                         FROM ferramenta, tecnico, reserva
                         WHERE reserva.tecnico_cpf = tecnico.cpf AND
                               reserva.ferramenta_id = ferramenta.id
                         ORDER BY reserva.id"""
PESQUISAR_RESERVA_TECNICO = """SELECT reserva.id, tecnico.nome,
                                      ferramenta.descricao, reserva.devolucao
                               FROM ferramenta, tecnico, reserva
                               WHERE reserva.tecnico_cpf = tecnico.cpf AND
                                     reserva.ferramenta_id = ferramenta.id AND
                                     tecnico.nome like '%%' || %s || '%%'
                               ORDER BY reserva.id"""
PESQUISAR_RESERVA_FERRAMENTA = """SELECT reserva.id, tecnico.nome,
                                         ferramenta.descricao, reserva.devolucao
                                  FROM ferramenta, tecnico, reserva
                                  WHERE reserva.tecnico_cpf = tecnico.cpf AND
                                        reserva.ferramenta_id = ferramenta.id AND
                                        ferramenta.descricao like '%%' || %s || '%%'
                                  ORDER BY reserva.id"""
#   INSERT
INSERIR_RESERVA = """INSERT INTO reserva (tecnico_cpf, ferramenta_id, devolucao)
                     VALUES (%s, %s, %s)"""
#   DELETE
DELETAR_RESERVA = """DELETE FROM reserva WHERE id = %s"""

#   UPDATE
ATUALIZAR_RESERVA = """UPDATE reserva SET tecnico_cpf = %s, ferramenta_id = %s,
                          devolucao = %s WHERE id = %s"""