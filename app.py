from flask import Flask
from models import db, Cidade, Rua, Cliente, Fiscal, Vaga
import getpass
import locale

# Ajuste de locale para evitar problemas de codificação
try:
    locale.setlocale(locale.LC_CTYPE, 'Portuguese_Brazil.1252')
except locale.Error:
    print("Locale setting not supported. Using default locale.")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:brenodias@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def get_input(prompt):
    return input(prompt).encode('latin1').decode('utf-8')

def insert_cidade():
    nome = get_input("Nome da Cidade: ")
    new_record = Cidade(nome=nome)
    db.session.add(new_record)
    db.session.commit()
    print(f"Cidade '{nome}' inserida com sucesso!")

def insert_rua():
    nome = get_input("Nome da Rua: ")
    idcidade = int(get_input("ID da Cidade: "))
    new_record = Rua(nome=nome, idcidade=idcidade)
    db.session.add(new_record)
    db.session.commit()
    print(f"Rua '{nome}' inserida com sucesso!")

def insert_cliente():
    placa = get_input("Placa do Carro: ")
    cpf = get_input("CPF: ")
    email = get_input("Email: ")
    senha = getpass.getpass("Senha: ")  # Usando getpass para evitar exibição de senha no terminal
    estado = get_input("Estado: ")
    cidade = get_input("Cidade: ")
    new_record = Cliente(placadocarro=placa, cpf=cpf, email=email, senha=senha, estado=estado, cidade=cidade)
    db.session.add(new_record)
    db.session.commit()
    print(f"Cliente com placa '{placa}' inserido com sucesso!")

def insert_fiscal():
    cpf = get_input("CPF: ")
    email = get_input("Email: ")
    senha = getpass.getpass("Senha: ")  # Usando getpass para evitar exibição de senha no terminal
    estado = get_input("Estado: ")
    cidade = get_input("Cidade: ")
    new_record = Fiscal(cpf=cpf, email=email, senha=senha, estado=estado, cidade=cidade)
    db.session.add(new_record)
    db.session.commit()
    print(f"Fiscal com CPF '{cpf}' inserido com sucesso!")

def insert_vaga():
    horaentrada = get_input("Hora de Entrada (YYYY-MM-DD HH:MM:SS): ")
    horasaida = get_input("Hora de Saída (YYYY-MM-DD HH:MM:SS): ")
    idrua = int(get_input("ID da Rua: "))
    placadocarro = get_input("Placa do Carro: ")
    expirada = get_input("Expirada (true/false): ").lower() == 'true'
    new_record = Vaga(horaentrada=horaentrada, horasaida=horasaida, idrua=idrua, placadocarro=placadocarro, expirada=expirada)
    db.session.add(new_record)
    db.session.commit()
    print(f"Vaga inserida com sucesso!")

def delete_record():
    table = get_input("Nome da Tabela: ")
    id_value = get_input("ID do Registro: ")

    if table == 'cidade':
        record = Cidade.query.get(id_value)
    elif table == 'rua':
        record = Rua.query.get(id_value)
    elif table == 'cliente':
        record = Cliente.query.get(id_value)
    elif table == 'fiscal':
        record = Fiscal.query.get(id_value)
    elif table == 'vaga':
        record = Vaga.query.get(id_value)
    else:
        print("Tabela não encontrada.")
        return

    db.session.delete(record)
    db.session.commit()
    print(f"Registro da tabela '{table}' com ID '{id_value}' excluído com sucesso!")

def main():
    while True:
        print("\n1. Inserir Cidade")
        print("2. Inserir Rua")
        print("3. Inserir Cliente")
        print("4. Inserir Fiscal")
        print("5. Inserir Vaga")
        print("6. Excluir Registro")
        print("7. Sair")

        choice = int(input("\nEscolha uma opção: "))

        with app.app_context():
            if choice == 1:
                insert_cidade()
            elif choice == 2:
                insert_rua()
            elif choice == 3:
                insert_cliente()
            elif choice == 4:
                insert_fiscal()
            elif choice == 5:
                insert_vaga()
            elif choice == 6:
                delete_record()
            elif choice == 7:
                break
            else:
                print("Opção inválida!")

if __name__ == "__main__":
    main()
