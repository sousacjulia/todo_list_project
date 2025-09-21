# Imports no topo do arquivo
import json

# =========================================================
# FUNÇÕES DE APOIO
# =========================================================

def salvar_tarefas(lista):
    """Salva a lista de tarefas no arquivo JSON."""
    with open("tarefas.json", "w") as arquivo:
        json.dump(lista, arquivo)

def carregar_tarefas():
    """Tenta carregar as tarefas do arquivo JSON e retorna a lista."""
    try:
        with open("tarefas.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

# =========================================================
# FUNÇÕES DE FUNCIONALIDADES
# =========================================================

def adicionar_tarefa(lista, descricao):
    """Adiciona uma nova tarefa à lista e a salva."""
    lista.append({'descricao': descricao, 'concluida': False})
    salvar_tarefas(lista)

def ver_tarefas(lista):
    """Exibe todas as tarefas da lista."""
    if len(lista) == 0:
        print("Sua lista de tarefas está vazia.")
    else:
        print("Sua lista de tarefas:")
        for indice, tarefa in enumerate(lista):
            status = "Concluída" if tarefa['concluida'] else "Pendente"
            print(f"[{status}] {indice + 1}. {tarefa['descricao']}")

# No arquivo todo_functionsList.py

def remover_tarefa(lista, indice):
    """Remove uma tarefa da lista pelo índice e salva a alteração."""
    if 0 <= indice < len(lista):
        tarefa_removida = lista.pop(indice)
        # O print e o input não são mais necessários, pois a interface já lida com isso.
        salvar_tarefas(lista)
        # Você pode retornar a tarefa removida, se quiser
        return tarefa_removida
    else:
        # Se o índice for inválido, não faz nada
        return None
        
def marcar_concluida(lista, indice):
    """Marca uma tarefa como concluída pelo índice e salva a lista."""
    # A verificação de índice é importante
    if 0 <= indice < len(lista):
        lista[indice]["concluida"] = True
        salvar_tarefas(lista)
        
        
# =========================================================
# LOOP PRINCIPAL
# =========================================================

lista_de_tarefas = carregar_tarefas()

print("\n--- Gerenciador de Tarefas ---")
print("1. Adicionar Tarefa")
print("2. Ver Tarefas")
print("3. Remover Tarefa")
print("4. Marcar como Concluída")
print("5. Sair")

while True:
    comando = input("\nDigite o número do comando: ")

    if comando == '1':
        # Pede a descrição da tarefa antes de chamar a função
        tarefa_nova = input("Digite a nova tarefa: ")
        adicionar_tarefa(lista_de_tarefas, tarefa_nova)
    elif comando == '2':
        ver_tarefas(lista_de_tarefas)
    elif comando == '3':
        remover_tarefa(lista_de_tarefas)
    elif comando == '4':
        # Pede o índice da tarefa antes de chamar a função
        try:
            numero_para_marcar = int(input("Digite o número da tarefa que deseja marcar como concluída: "))
            indice_para_marcar = numero_para_marcar - 1
            marcar_concluida(lista_de_tarefas, indice_para_marcar)
            print(f"Tarefa '{lista_de_tarefas[indice_para_marcar]['descricao']}' marcada como concluída!")
        except (ValueError, IndexError):
            print("Entrada inválida. Por favor, digite um número válido.")
    elif comando == '5':
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Comando não reconhecido. Tente novamente.")
        