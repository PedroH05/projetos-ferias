from tarefas import adicionar_tarefas, listar_tarefas, excluir_tarefas, marcar_tarefas

print("O que você vai fazer hoje?")

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Excluir tarefa")
    print("4 - Marcar tarefa como concluída")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        print("Você escolheu adicionar uma tarefa.")
        adicionar_tarefas()

    elif opcao == "2":
        print("Você escolheu listar suas tarefas.")
        listar_tarefas()

    elif opcao == "3":
        print("Você escolheu excluir uma tarefa.")
        excluir_tarefas()

    elif opcao == "4":
        print("Você escolheu marcar uma tarefa como concluída.")
        marcar_tarefas()

    elif opcao == "5":
        print("Saindo...")
        break

    else:
        print("Opção inválida! Tente novamente.")
