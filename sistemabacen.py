import datetime
import pytz

# 1. Variáveis Essenciais
saldo = 1000.0
extrato = ""
LIMITE_SAQUE_POR_OPERACAO = 500.00 # Renomeado para clareza
LIMITE_SAQUES_DIARIOS = 3 # Novo: Limite de 3 saques por dia

saques_hoje = 0 # Contador de saques para o dia atual
# Armazena a data do último saque para resetar o contador diariamente
# Inicializa com uma data "passada" para garantir que o primeiro saque do dia seja contabilizado
ultima_data_saque = None # Novo: Para rastrear a data do último saque

# Define o fuso horário de São Paulo (que cobre grande parte do Brasil)
fuso_horario_brasil = pytz.timezone('America/Sao_Paulo')

# Função auxiliar para obter a hora atual do Brasil
def obter_hora_brasil():
    return datetime.datetime.now(fuso_horario_brasil)

# 2. Funções
def depositar(valor):
    global saldo, extrato # Indica que estamos usando as variáveis globais
    if valor > 0:
        momento_deposito = obter_hora_brasil()
        saldo += valor
        extrato += f"{momento_deposito.strftime('%d/%m/%Y %H:%M:%S')} - Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

def sacar(valor):
    global saldo, extrato, saques_hoje, ultima_data_saque # Adicionando as novas variáveis globais

    # Obtém a data e hora atual do Brasil
    momento_saque = obter_hora_brasil()
    data_saque_atual = momento_saque.date() # Apenas a data (ano, mês, dia)

    # Verifica se o dia mudou para resetar o contador de saques
    if ultima_data_saque is None or data_saque_atual != ultima_data_saque:
        saques_hoje = 0 # Reseta o contador de saques
        ultima_data_saque = data_saque_atual # Atualiza a última data de saque

    excedeu_saldo = valor > saldo
    excedeu_limite_por_operacao = valor > LIMITE_SAQUE_POR_OPERACAO
    excedeu_limite_diario = saques_hoje >= LIMITE_SAQUES_DIARIOS


    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
    elif excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite_por_operacao:
        print(f"Operação falhou! O valor do saque excede o limite por operação de R$ {LIMITE_SAQUE_POR_OPERACAO:.2f}.")
    elif excedeu_limite_diario:
        print(f"Operação falhou! Você excedeu o limite de {LIMITE_SAQUES_DIARIOS} saques diários.")
    else: # Se todas as condições acima forem falsas (saque válido).
        saldo -= valor
        extrato += f"{momento_saque.strftime('%d/%m/%Y %H:%M:%S')} - Saque: R$ {valor:.2f}\n"
        saques_hoje += 1 # Incrementa o contador de saques do dia
        print("Saque realizado com sucesso!")

def exibir_extrato():
    print("\n---------- EXTRATO ----------")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("------------------------------")

# 3. Menu e Loop Principal
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

while True:
    opcao = input(menu)

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: "))
            depositar(valor)
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: "))
            sacar(valor)
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")
    elif opcao == "e":
        exibir_extrato()
    elif opcao == "q":
        print("Saindo do sistema. Obrigado por usar nosso banco!")
        break
    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")