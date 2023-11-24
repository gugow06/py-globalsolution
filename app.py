import os
import random

# Obtém o diretório atual do script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Paths completos dos bancos de dados
users_path = os.path.join(current_directory, "users.txt")
hospitals_path = os.path.join(current_directory, "hospitals.txt")

# Função para carregar o banco de dados de usuários
def load_users():
    try:
        with open(users_path, "r") as file:
            lines = file.readlines()
            users = {}
            for line in lines:
                # Adiciona uma verificação para garantir que há pelo menos três valores na linha
                values = line.strip().split(",")
                if len(values) == 3:
                    username, email, password = values
                    users[username] = {"email": email, "password": password}
            return users
    except FileNotFoundError:
        return {}


# Função para salvar o banco de dados de usuários
def save_users(users):
    with open(users_path, "w") as file:
        for username, data in users.items():
            file.write(f"{username},{data['email']},{data['password']}\n")

# Função para carregar o banco de dados de hospitais
def load_hospitals():
    try:
        with open(hospitals_path, "r") as file:
            lines = file.readlines()
            hospitals = []
            for line in lines:
                name, address, waiting_time = line.strip().split(",")
                hospitals.append({"name": name, "address": address, "waiting_time": int(waiting_time)})
            return hospitals
    except FileNotFoundError:
        return []

# Função para salvar o banco de dados de hospitais
def save_hospitals(hospitals):
    with open(hospitals_path, "w") as file:
        for hospital in hospitals:
            file.write(f"{hospital['name']},{hospital['address']},{hospital['waiting_time']}\n")

# Função de login
def login(users):
    email = input("Digite seu nome de usuário: ")
    password = input("Digite sua senha: ")

    if email in users and users[email]["password"] == password:
        return True, email
    else:
        print("Login inválido. Tente novamente.")
        return False, None

# Função de registro
def register(users):
    username = input("Digite seu nome de usuário: ")
    email = input("Digite seu email: ")
    password = input("Digite sua senha: ")

    if username not in users:
        users[username] = {"email": email, "password": password}
        save_users(users)
        print("Registro bem-sucedido!")
    else:
        print("Nome de usuário já existe. Tente novamente.")

# Função para carregar o banco de dados de hospitais
def load_hospitals():
    try:
        with open(hospitals_path, "r") as file:
            lines = file.readlines()
            hospitals = []
            for line in lines:
                values = line.strip().split(",")
                if len(values) >= 2:
                    name, address = values[:2]
                    hospitals.append({"name": name, "address": address})
            return hospitals
    except FileNotFoundError:
        return []


# Função para encontrar o hospital mais próximo
def find_nearest_hospital(hospitals):
    if not hospitals:
        return None

    min_waiting_time = float("inf")
    nearest_hospital = None

    for hospital in hospitals:
        waiting_time = hospital["waiting_time"]

        if waiting_time < min_waiting_time:
            min_waiting_time = waiting_time
            nearest_hospital = hospital

    return nearest_hospital

# Função principal
def main():
    users = load_users()
    hospitals = load_hospitals()

    while True:
        print("\n1 - Logar\n2 - Registrar-se\n3 - Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            success, username = login(users)
            if success:
                print(f"Seja bem-vindo, {username}!")
                break
        elif choice == "2":
            register(users)
        elif choice == "3":
            print("Até logo!")
            exit()
        else:
            print("Opção inválida. Tente novamente.")

    while True:
        print("\n1 - Cardiologista\n2 - Neurologista\n3 - Oftalmologista\n4 - Ortopedista\n5- Pediatra\n6 - Urologista\n7 - Alergista\n8 - Pneumologista\n9 - Traumatologista\n10 - Nefrologista\n11 - Sair")
        choice = input("Escolha uma opção: ")

        if choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9","10"]:
            confirmation = input("Você consegue chegar até o local? (Sim/Não): ")

            if confirmation.lower() == "sim":
                # Gerar tempos de espera aleatórios para cada hospital
                for hospital in hospitals:
                    hospital["waiting_time"] = random.randint(1, 16)
                
                nearest_hospital = find_nearest_hospital(hospitals)
                if nearest_hospital:
                    print(f"Hospital: {nearest_hospital['address']}")
                    print(f"Tempo de espera estimado: {nearest_hospital['waiting_time']} minutos")
                else:
                    print("Não há hospitais disponíveis.")
                break
            elif confirmation.lower() == "não":
                print("Em alguns minutos, uma ambulância chegará ao seu local.")
                break
            else:
                print("Resposta inválida. Tente novamente.")
        elif choice == "4":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()