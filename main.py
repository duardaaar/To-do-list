
import json

# Funçao para carregar tarefas de um arquivo json

def carregar_tarefas(nome_arq):
    try:
        with open(nome_arq, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

# Funçao para salvar tarefas em um arquivo json

def salvar_tarefas(nome_arq, tarefas):
    with open(nome_arq, 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)

# Funçao para adicionar uma nova tarefa

def adicionar_tarefas(tarefas):
    titulo = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    tarefa = {
        "titulo": titulo,
        "descrição": descricao,
        "status": "Pendente"
    }

    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

# Funçao para listar todas as tarefas

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa foi adicionada")
    else:
        for idx, tarefa in enumerate(tarefas):
            print(f"{idx + 1}. {tarefa['titulo']} - {tarefa['status']}")
            print(f" Descrição: {tarefa['descrição']}")
            print("-" * 40)

# Funçao para atualizar uma tarefa existente

def atualizar_tarefas(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return
    
    numero = int(input("Digite o número da tarefa que deseja atualizar: ")) - 1

    if 0 <= numero < len(tarefas):
        tarefa = tarefas[numero]
        print(f"1. Título: {tarefa['titulo']}")
        print(f"2. Descrição: {tarefa['descrição']}")
        print(f"3. Status: {tarefa['status']}")
        opcao = input("O que você deseja atualizar? (1- Título, 2- Descrição, 3- Status): ")

        if opcao == '1':
            tarefa['titulo'] = input("Novo título: ")
        elif opcao == '2':
            tarefa['descrição'] = input("Nova descrição: ")
        elif opcao == '3':
            novo_status = input("Novo status (Pendente/Concluída): ")
            if novo_status in ["Pendente", "Concluída"]:
                tarefa['status'] = novo_status
            else:
                print("Status inválido")
            print("Tarefa atualizada com sucesso!")
        else:
            print("Número de tarefa inválido")

# Funçao para remover uma tarefa

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    if not tarefas:
        return
    
    numero = int(input("Digite o número da tarefa que deseja remover: ")) - 1

    if 0 <= numero < len(tarefas):
        tarefas.pop(numero)
        print("Tarefa removida com sucesso!")
    else:
        print("Número de tarefa inválido")

# Funçao principal para exibir o menu e lidar com as opçoes do usuário

def menu():
    nome_arq = 'tarefas.json'
    tarefas = carregar_tarefas(nome_arq)

    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Atualizar Tarefa")
        print("4. Remover Tarefa")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_tarefas(tarefas)
        elif opcao == '2':
            listar_tarefas(tarefas)
        elif opcao == '3':
            atualizar_tarefas(tarefas)
        elif opcao == '4':
            remover_tarefa(tarefas)
        elif opcao =='5':
            salvar_tarefas(nome_arq, tarefas)
            print("Tarefas salvas com sucesso!. Saindo...")
            break
        else:
            print("Opçao inválida. Tente novamente")

# Executa o menu principal

if __name__ == "__main__":
    menu()

