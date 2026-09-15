print("==============================")
print("       CLÍNICA VIDA+")
print("==============================")

pacientes = []


def cadastrar_paciente():
    print("\n--- CADASTRO DE PACIENTE ---")

    nome = input("Nome do paciente: ").strip()
    

    while nome == "":
        print("Erro: o nome não pode ficar vazio.")
        nome = input("Nome do paciente: ").strip()

    while True:
        try:
            idade = int(input("Idade: "))

            if idade < 0 or idade > 120:
                print("Erro: informe uma idade válida entre 0 e 120.")
            else:
                break

        except ValueError:
            print("Erro: digite a idade usando apenas números.")

    telefone = input("Telefone: ").strip()

    while telefone == "":
        print("Erro: o telefone não pode ficar vazio.")
        telefone = input("Telefone: ").strip()

    paciente = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    }

    pacientes.append(paciente)

    print("\nPaciente cadastrado com sucesso!")


def mostrar_estatisticas():
    print("\n--- ESTATÍSTICAS DOS PACIENTES ---")

    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.")
        return

    total = len(pacientes)

    soma_idades = sum(paciente["idade"] for paciente in pacientes)
    media = soma_idades / total

    mais_novo = min(pacientes, key=lambda paciente: paciente["idade"])
    mais_velho = max(pacientes, key=lambda paciente: paciente["idade"])

    print(f"Total de pacientes: {total}")
    print(f"Idade média: {media:.1f} anos")
    print(
        f"Paciente mais novo: {mais_novo['nome']} "
        f"({mais_novo['idade']} anos)"
    )
    print(
        f"Paciente mais velho: {mais_velho['nome']} "
        f"({mais_velho['idade']} anos)"
    )


def buscar_paciente():
    print("\n--- BUSCAR PACIENTE ---")

    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.")
        return

    nome_busca = input("Digite o nome do paciente: ").strip().lower()

    encontrados = []

    for paciente in pacientes:
        if nome_busca in paciente["nome"].lower():
            encontrados.append(paciente)

    if len(encontrados) == 0:
        print("Paciente não encontrado.")
        return

    print("\nPaciente(s) encontrado(s):")

    for paciente in encontrados:
        print("------------------------------")
        print(f"Nome: {paciente['nome']}")
        print(f"Idade: {paciente['idade']} anos")
        print(f"Telefone: {paciente['telefone']}")


def listar_pacientes():
    print("\n--- TODOS OS PACIENTES ---")

    if len(pacientes) == 0:
        print("Nenhum paciente cadastrado.")
        return

    for numero, paciente in enumerate(pacientes, start=1):
        print(f"\nPaciente {numero}")
        print(f"Nome: {paciente['nome']}")
        print(f"Idade: {paciente['idade']} anos")
        print(f"Telefone: {paciente['telefone']}")
        print("------------------------------")


while True:
    print("\n================================")
    print("     SISTEMA CLÍNICA VIDA+")
    print("================================")
    print("1. Cadastrar paciente")
    print("2. Ver estatísticas")
    print("3. Buscar paciente")
    print("4. Listar todos os pacientes")
    print("5. Sair")
    print("================================")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_paciente()

    elif opcao == "2":
        mostrar_estatisticas()

    elif opcao == "3":
        buscar_paciente()

    elif opcao == "4":
        listar_pacientes()

    elif opcao == "5":
        print("\nSistema encerrado. Até logo!")
        break

    else:
        print("\nErro: opção inválida. Escolha uma opção de 1 a 5.")