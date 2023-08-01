import textwrap


def menu():
    menu = """

    Caro usuário, seja bem-vindo ao Banco Tudo faz!

    Digite a operação desejada:

    [0] Depósito
    [1] Saque
    [2] Extrato
    [3] Nova Conta
    [4] Listar contas
    [5] Novo usuário
    [6] Sair

    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Não é possível realizar essa operação. Você não tem saldo suficiente.")
        
    elif excedeu_limite:
        print("Não é possível realizar essa operação. Você excedeu o valor da operação.")
        
    elif excedeu_saques:
        print("Não é possível realizar essa operação. Você excedeu o número máximo de transações para o da de hoje.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("Operação realizada com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def exibir_extrato(salfo, /, *, extrato):
    print("\n########## EXTRATO ##########")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("########################################################")


def criar_usuario(usuarios):

def filtrar_usuario(pf, usuario):

def criar_conta(agencia, numero_conta, usuarios):

def listar_contas(contas):

def main():
    # Variáveis
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

while True:

    opcao = menu()

## Depósito ##
# Permitir apenas valores positivos
# Todos os valores devem ser armazenados numa variável
# Perguntar qual vaor deseja depositar?

    if opcao =="0":
        valor = float(input("Informe o valor do depósito: "))

        saldo, extato = depositar(saldo, valor, extrato)

## Saque ##
# Permitir 3 saques diários máximo R$500,00
# Se não tiver limite exibir: "Não será possível sacar o dinheiro por falta de sado"
# Todos os valores devem ser armazenados numa variável

    elif opcao == "1":
        valor = float(input("Qual valor deseja sacar? "))
        
        saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )

## Extrato ##
# Listar todas as operações de depósito e saque
# No final dos valores deve exibir resultado da conta no formato R$ xxx.xx
# Todos os valores devem ser armazenados numa variável

    elif opcao == "2":
        exibir_extrato(saldo, extrato=extrato)
        
### Nova Conta[3] ###


### Listar contas [4] ###


### Novo usuário [5] ###

    elif opcao == "6":
        break

    else:
        print("Opção incorreta, por favor selecione novamente uma opção do menu.")

main()