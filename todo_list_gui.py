#import interface gráfica, vamos usar o Tkinter
import tkinter as tk

#importar as funções do arquivo todo_functionsList
from todo_functionsList import adicionar_tarefa, remover_tarefa, ver_tarefas, salvar_tarefas, carregar_tarefas, marcar_concluida

#chamar a função
lista_de_tarefas = carregar_tarefas()

# ============================
# FUNÇÕES DA INTERFACE
# ============================

def atualizar_listbox():
    #limpa o listbox, para evitar duplicatas
    listbox_tarefas.delete(0, tk.END)
    #insere as tarefas 
    for tarefa in lista_de_tarefas:
      status = "Concluida" if tarefa['concluida'] else "Pendente"
      listbox_tarefas.insert(tk.END, f"[{status}] {tarefa['descricao']}")

# ============================
# CÓDIGO DA INTERFACE
# ============================

#criação e medida da janela principal
janela = tk.Tk()
janela.title("To Do List")
janela.geometry("400x400")

#criação e posição do listbox
listbox_tarefas = tk.Listbox(janela, height=15, width=50)
listbox_tarefas.pack(pady=20) #pady = para espaço vertical


#FUNÇÕES DE BOTÃO 
def adicionar_tarefa_gui():
    nova_tarefa = entrada_tarefa.get()
    if nova_tarefa:
      adicionar_tarefa(lista_de_tarefas, nova_tarefa)
      atualizar_listbox()
      entrada_tarefa.delete(0, tk.END)

def remover_tarefa_gui():
  try: #pega o indice da tarefa selecionada
    indice_selecionado = listbox_tarefas.curselection()[0]
    remover_tarefa(lista_de_tarefas, indice_selecionado) #remove a tarefa da lista
    atualizar_listbox()
  except IndexError:
    pass #ignora se nada for selecionado
  
def marcar_concluida_gui():
  try:
    indice_selecionado = listbox_tarefas.curselection()[0]                                                        ]
    marcar_concluida(lista_de_tarefas, indice_selecionado)
    atualizar_listbox()
  except IndexError:
    pass


#cria um botão e os posiciona
entrada_tarefa = tk.Entry(janela, width=40)
entrada_tarefa.pack(pady=5)

botao_adicionar = tk.Button(janela, text='Adicionar', command=adicionar_tarefa_gui) # <-- CORREÇÃO: Chame a função da GUI
botao_adicionar.pack() #posiciona o botão na janela principal

botao_remover = tk.Button(janela, text="Remover Tarefa", command=remover_tarefa_gui)
botao_remover.pack(pady=5)

botao_marcar_concluida = tk.Button(janela, text="Marcar como concluída", command=remover_tarefa_gui)
botao_remover.pack(pady=5)

#função para a exibir as tarefas carregas
atualizar_listbox()

#loop da janela principal
janela.mainloop()
