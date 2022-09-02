from faker import Faker
from database.database import Database

fake = Faker('pt_BR')
db = Database()

def cpf_tratado():
    cpf = str(fake.cpf())
    crt = '.-'
    cp = cpf.translate(str.maketrans('', '', crt))
    return cp


def povoar_tecnico():  # (id, cpf, nome, telefone, turno, equipe)
    for i in range(0, 50):
        cpf = cpf_tratado()
        tec = [cpf, fake.name(), fake.phone_number(), 'NOITE', 'NOVELA']
        db.inserir_tecnico(*tec)


povoar_tecnico()