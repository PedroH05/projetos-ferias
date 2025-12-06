tarefas = []

def adicionar_tarefas():
    texto = input("Digite sua tarefa: ")
    tarefa = {"texto": texto, "concluida": False}
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso.")


def listar_tarefas():
    if len(tarefas) == 0:
        print("Você ainda não adicionou tarefas.")
        return
    
    for numero, tarefa in enumerate(tarefas, start=1):
        status = "✔️" if tarefa["concluida"] else "❌"
        print(f"{numero} - {status} {tarefa['texto']}")


def excluir_tarefas():
    if len(tarefas) == 0:
        print("Você ainda não adicionou tarefas.")
        return

    listar_tarefas()
    numero = int(input("Digite o número da tarefa que você quer excluir: "))

    if 1 <= numero <= len(tarefas):
        tarefas.pop(numero - 1)
        print("Tarefa excluída com sucesso.")
    else:
        print("Número inválido. Tente novamente.")


def marcar_tarefas():
    if len(tarefas) == 0:
        print("Você ainda não adicionou tarefas.")
        return

    listar_tarefas()
    numero = int(input("Digite o número da tarefa que você quer marcar como concluída: "))

    if 1 <= numero <= len(tarefas):
        tarefas[numero - 1]["concluida"] = True
        print("Tarefa marcada como concluída!")
    else:
        print("Número inválido. Tente novamente.")
