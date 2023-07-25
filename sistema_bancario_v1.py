# Operações: depósito, saque e extrato

menu = """

Caro usuário, seja bem-vindo ao Banco Tudo faz!

Digite a operação desejada:

[0] Depósito
[1] Saque
[2] Extrato
[3] Sair

=> """

# Variáveis
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

## Depósito ##
# Permitir apenas valores positivos
# Todos os valores devem ser armazenados numa variável
# Perguntar qual vaor deseja depositar?

    if opcao =="0":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

## Saque ##
# Permitir 3 saques diários máximo R$500,00
# Se não tiver limite exibir: "Não será possível sacar o dinheiro por falta de sado"
# Todos os valores devem ser armazenados numa variável

    elif opcao == "1":
        valor = float(input("Qual valor deseja sacar? "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Não é possível realizar essa operação. Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Não é possível realizar essa operação. Você excedeu o valor da operação.")
        
        elif excedeu_saques:
            print("Não é possível realizar essa operação. Você excedeu o número máximo de transações para o da de hoje.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

## Extrato ##
# Listar todas as operações de depósito e saque
# No final dos valores deve exibir resultado da conta no formato R$ xxx.xx
# Todos os valores devem ser armazenados numa variável

    elif opcao == "2":
        print("\n###### EXTRATO ######")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("########################################################")

    elif opcao == "3":
        break

    else:
        print("Opção incorreta, por favor selecione novamente uma opção do menu.")