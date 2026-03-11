tarefas = []


def salvar_tarefas():
    with open("tarefas.txt", "w", encoding="utf-8") as arquivo:
        for tarefa in tarefas:
            linha = f"{tarefa['nome']}|{tarefa['concluida']}\n"
            arquivo.write(linha)


def carregar_tarefas():
    try:
        with open("tarefas.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                if linha != "":
                    partes = linha.split("|")
                    nome = partes[0]
                    concluida = partes[1] == "True"

                    tarefas.append({
                        "nome": nome,
                        "concluida": concluida
                    })

    except FileNotFoundError:
        pass


def mostrar_menu():
    print("\n=== LISTA DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Remover tarefa")
    print("4 - Editar tarefa")
    print("5 - Sair")
    print("6 - Concluir tarefa")


def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ").strip()

    if tarefa == "":
        print("Tarefa vazia não pode ser adicionada.")
        return

    for item in tarefas:
        if item["nome"].lower() == tarefa.lower():
            print("Essa tarefa já existe.")
            return

    tarefas.append({
        "nome": tarefa,
        "concluida": False
    })

    salvar_tarefas()
    print("Tarefa adicionada com sucesso!")


def ver_tarefas():
    if len(tarefas) > 0:
        print("\n--- SUAS TAREFAS ---")

        for i, tarefa in enumerate(tarefas):
            status = "✔" if tarefa["concluida"] else "✖"
            print(i, "-", tarefa["nome"], status)

    else:
        print("Nenhuma tarefa cadastrada.")


def remover_tarefa():
    if len(tarefas) > 0:
        print("\n--- REMOVER TAREFA ---")

        for i, tarefa in enumerate(tarefas):
            status = "✔" if tarefa["concluida"] else "✖"
            print(i, "-", tarefa["nome"], status)

        indice = int(input("Digite o número da tarefa para remover: "))

        if indice < len(tarefas):
            tarefas.pop(indice)
            salvar_tarefas()
            print("Tarefa removida!")
        else:
            print("Número inválido.")

    else:
        print("Não há tarefas para remover.")


def editar_tarefa():
    if len(tarefas) > 0:
        print("\n--- EDITAR TAREFA ---")

        for i, tarefa in enumerate(tarefas):
            status = "✔" if tarefa["concluida"] else "✖"
            print(i, "-", tarefa["nome"], status)

        indice = int(input("Digite o número da tarefa que deseja editar: "))

        if indice < len(tarefas):
            nova_tarefa = input("Digite a nova tarefa: ").strip()

            if nova_tarefa == "":
                print("A tarefa não pode ficar vazia.")
                return

            tarefas[indice]["nome"] = nova_tarefa
            salvar_tarefas()
            print("Tarefa atualizada!")

        else:
            print("Número inválido.")

    else:
        print("Não há tarefas para editar.")


def concluir_tarefa():
    if len(tarefas) > 0:
        print("\n--- CONCLUIR TAREFA ---")

        for i, tarefa in enumerate(tarefas):
            status = "✔" if tarefa["concluida"] else "✖"
            print(i, "-", tarefa["nome"], status)

        indice = int(input("Qual tarefa deseja concluir? "))

        if indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            salvar_tarefas()
            print("Tarefa marcada como concluída!")
        else:
            print("Número inválido.")

    else:
        print("Não há tarefas.")


carregar_tarefas()

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()

    elif opcao == "2":
        ver_tarefas()

    elif opcao == "3":
        remover_tarefa()

    elif opcao == "4":
        editar_tarefa()

    elif opcao == "5":
        print("Encerrando programa...")
        break

    elif opcao == "6":
        concluir_tarefa()

    else:
        print("Opção inválida!")