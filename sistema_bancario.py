from time import sleep

def depositar(saldo, valor, extrato, /):
    saldo += valor
    print("Depósico confirmado")
    sleep(1)
    extrato += f'\nDepósito no valor de R$ {valor:.2f}'

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite_por_saque, numero_saques, limite_saque):
    if saldo - valor < 0:
            print("Não será possível sacar o dinheiro por falta de saldo.")

    elif numero_saques < limite_saque and valor <= limite_por_saque:
        saldo -= valor
        print("Saque confirmado")
        numero_saques += 1
        extrato += f'\nSaque no valor de R$ {valor:.2f}'

    else:
        if numero_saques >= limite_saque:
            print("Saque não realizado! Ultrapassou o limite de saques diários.")
        elif valor > limite_por_saque:
            print("Tentativa de sacar valor maior que o seu limite diário de R$ 500.00!")
            print("Se necessário entre em contato com a agência.")

    return saldo, extrato

def menu():
    menu = """
======= BEM-VINDO AO Diobank =======

[1] Depósito
[2] Saque
[3] Extrato
[0] Sair

"""
    return int(input(f"{menu}Escolha uma opção: "))


saldo = 0
extrato = ""
LIMITE_SAQUE = 3
numero_saques = 0
limite_por_saque = 500

while True:

    escolha_usuario = menu()

    if escolha_usuario == 1:
        
        while True:

            print("\n======= Depositar =======\n")
            valor = float(input("Digite o valor do depósito: "))

            if valor <= 0:
                print("Não é possível depositar esse valor!")

            else:
                break
        
        print(".")
        sleep(1)
        print("..")
        sleep(1)
        print("...")
        sleep(1)

        saldo, extrato = depositar(saldo, valor, extrato)
        sleep(1)

    elif escolha_usuario == 2:

        while True:
            
            print("\n======= Saque =======\n")
            valor = float(input("Digite o valor do saque: "))

            if valor <= 0:
                print("Valor inválido!")

            else:
                break
            
        print(".")
        sleep(1)
        print("..")
        sleep(1)
        print("...")
        sleep(1)

        saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite_por_saque=limite_por_saque,
            numero_saques=numero_saques,
            limite_saque=LIMITE_SAQUE)
        
        sleep(1)

    elif escolha_usuario == 3:

        relatorio_extrato = f"""\n======= Extrato ======= {extrato}
        \nSaldo: {saldo}
        """
        print(relatorio_extrato)

    elif escolha_usuario == 0:
        break

    else:
        print("\nOpção errada. Escolha uma das opções")

print("\n======= Obrigado por ser nosso cliente, tenha um bom dia! =======\n")
