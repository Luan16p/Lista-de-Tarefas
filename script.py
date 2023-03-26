import os

tarefas = []
lista_comandos = ["/adicionaritem", "/removeritem", "/veritem", "/atualizaritem"]

def verLista():    
    enter = input("Pressione Enter para iniciar ou digite '.exit' para sair >")

    if enter == ".exit":
        print("Algoritmo Finalizado...")
        return False
    else:
        mostrar_comandos()

def adicionar_item():
    os.system('cls')
    item = input("Digite o Item a ser adicionado >")
    tarefas.append(item)

    verLista()

def remover_item():
    os.system('cls')

    indice = input("Digite o ID do item que quer remover >")
    try:
        indice = int(indice)
        tarefas.pop(indice)
        print("Item Removido Com sucesso")
    except (ValueError, IndexError):
        print("ID inválido, tente novamente")
    verLista()
    
def ver_item():
    os.system('cls')
    indice = input("Digite o ID do item que quer ver separadamente >")
    try:
        indice = int(indice)
        print(f"{tarefas[indice]}")
    except (ValueError, IndexError):
        print("ID inválido, tente novamente")

def atualizar_item():
    os.system('cls')
    indice = input("Digite o ID do item que quer atualizar >")
    novo_valor = input("Digite o Novo valor que deseja >")
    try:
        indice = int(indice)
        tarefas[indice] = novo_valor
        print(f"Atualizado Com Sucesso!\nNovo valor do item {indice}: {tarefas[indice]}")
    except (ValueError, IndexError):
        print("ID inválido, tente novamente")
    verLista()

def mostrar_comandos():
    os.system('cls')
    print("_"*5 + " CRUD: Lista de Tarefas " + "_"*5)

    for i in range(len(tarefas)):
        print(str(i) + ":" + tarefas[i])
    for i in range(len(lista_comandos)):
        print(lista_comandos[i])
    print("_"*10)
    print("\nDIGITE...")
    comando_usuario = input("> ")
    if comando_usuario == "/adicionaritem":
        adicionar_item()
    elif comando_usuario == "/removeritem":
        remover_item()
    elif comando_usuario == "/veritem":
        ver_item()
    elif comando_usuario == "/atualizaritem":
        atualizar_item()
    else:
        print("Comando Inválido, tente novamente!")

continuar = True
while continuar:
    continuar = verLista()
    if continuar:
        mostrar_comandos()
