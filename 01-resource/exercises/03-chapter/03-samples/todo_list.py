print("Bem vindo(a) ao Gerenciador de Tarefas!")

tarefas = []

while True:
    print("\nEscolha uma opção: ")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Ordenar tarefas (A-Z)")
    print("5 - Mostrar quantidade de tarefas")
    print("0 - Sair")
    
    escolha = input("Digite o número da opção..: ")
    
    if escolha == "1":
        tarefa = input("Digite o nome da tarefa: ").strip()
        if tarefa:
            tarefas.append(tarefa)
            print(f"Tarefa '{tarefa}' adicionada com sucesso!")
        else:
            print("Tarefa não pode ser vazia!")
    elif escolha == "2":
        if tarefas:
            print("\nTarefas pendentes:")
            for index, tarefa in enumerate(tarefas):
                print(f"{index + 1}. {tarefa}")
        else:
            print("Nenhuma tarefa pendente.")
    elif escolha == "3":
        if tarefas:
            for index, tarefa in enumerate(tarefas):
                print(f"{index + 1}. {tarefa}")
            try:
                numero = int(input("Digite o número da tarefa a ser removida: "))
                if 1 <= numero <= len(tarefas):
                    tarefa_removida = tarefas.pop(numero - 1)
                    print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
                else:
                    print("Número inválido!")
            except ValueError:
                print("Por favor, digite um número válido.")
        else:
            print("Nenhuma tarefa para remover.")
    elif escolha == "4":
        tarefas.sort()
        print("Tarefas ordenadas em ordem alfabética com sucesso!")
    elif escolha == "5":
        print(f"Quantidade de tarefas pendentes: {len(tarefas)}")
    elif escolha == "0":
        print("Saindo do Gerenciador de Tarefas. Até logo!")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")
    input("Pressione Enter para continuar...")