import tkinter as tk

# Cria a janela principal
janela = tk.Tk()
janela.title("Lista de Tarefas")
janela.geometry("400x300")

# Cria a lista onde as tarefas serão exibidas
lista_tarefas = tk.Listbox(janela)
lista_tarefas.pack(fill=tk.BOTH, expand=True)

# Função para atualizar a lista de tarefas
def atualizar_tarefas():
    lista_tarefas.delete(0, tk.END)
    for tarefa in tarefas:
        lista_tarefas.insert(tk.END, tarefa)

# Cria o botão "Remover Tarefa"
def remover_tarefa():
    indice_selecionado = lista_tarefas.curselection()
    if len(indice_selecionado) > 0:
        indice = indice_selecionado[0]
        del tarefas[indice]
        atualizar_tarefas()

botao_remover = tk.Button(janela, text="Remover Tarefa", command=remover_tarefa)
botao_remover.pack()

# Cria o botão "Atualizar Tarefa"
def atualizar_tarefa():
    indice_selecionado = lista_tarefas.curselection()
    if len(indice_selecionado) > 0:
        indice = indice_selecionado[0]
        tarefa_atual = tarefas[indice]
        janela_atualizar = tk.Toplevel(janela)
        janela_atualizar.title("Atualizar Tarefa")
        entrada_tarefa_atual = tk.Entry(janela_atualizar)
        entrada_tarefa_atual.insert(0, tarefa_atual)
        entrada_tarefa_atual.pack()
        botao_atualizar = tk.Button(janela_atualizar, text="Atualizar", command=lambda: atualizar_tarefa_confirmada(indice, entrada_tarefa_atual.get(), janela_atualizar))
        botao_atualizar.pack()

def atualizar_tarefa_confirmada(indice, nova_tarefa, janela_atualizar):
    tarefas[indice] = nova_tarefa
    atualizar_tarefas()
    janela_atualizar.destroy()

botao_atualizar = tk.Button(janela, text="Atualizar Tarefa", command=atualizar_tarefa)
botao_atualizar.pack(pady=10)

# Cria o botão "Adicionar Tarefa"
def adicionar_tarefa():
    tarefa = entrada_tarefa.get().strip()
    if len(tarefa) > 0:
        tarefas.append(tarefa)
        entrada_tarefa.delete(0, tk.END)
        atualizar_tarefas()

botao_adicionar = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa)
botao_adicionar.pack(pady=10)

# Cria a caixa de entrada para digitar as tarefas
entrada_tarefa = tk.Entry(janela)
entrada_tarefa.pack(pady=10)

# Cria o Footer para a aplicação

rodape = tk.Label(janela, text="Todos os Direitos Reservados", bd=1, relief=tk.SUNKEN, anchor=tk.W)
rodape.pack(side=tk.BOTTOM, fill=tk.X)
rodape.config(font=("Arial", 10), bg="#ddd", fg="#555")

# Inicializa a lista de tarefas
tarefas = []
atualizar_tarefas()

# Inicia a interface
janela.mainloop()