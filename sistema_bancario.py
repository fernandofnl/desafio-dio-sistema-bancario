from time import sleep

menu = """
======= BEM-VINDO AO Diobank =======

[1] Depósito
[2] Saque
[3] Extrato
[0] Sair

"""

saldo = 0
extrato = ""
LIMITE_SAQUE = 3
numero_saques = 0
limite_por_saque = 500

while True:

    escolha_usuario = int(input(f"{menu}Escolha uma opção: "))

    if escolha_usuario == 1:
        print("\n======= Depositar =======\n")
        deposito = float(input("Digite o valor do depósito: "))
        print(".")
        sleep(1)
        print("..")
        sleep(1)
        print("...")
        sleep(1)
        saldo += deposito
        print("Depósico confirmado")
        sleep(1)
        extrato += f'\nDepósito no valor de {deposito}'

    elif escolha_usuario == 2:
        print("\n======= Saque =======\n")
        saque = float(input("Digite o valor do saque: "))
        print(".")
        sleep(1)
        print("..")
        sleep(1)
        print("...")
        sleep(1)

        if numero_saques <= LIMITE_SAQUE and saque <= limite_por_saque:
            saldo -= saque
            print("Saque confirmado")
            numero_saques += 1
        
        if saldo - saque < 0:
            print("Não será possível sacar o dinheiro por falta de saldo.")
        
        sleep(1)
        extrato += f'\nSaque no valor de {saque}'

        

    elif escolha_usuario == 3:
        relatorio_extrato = f"""\n======= Extrato ======= {extrato}
        \nSaldo: {saldo}
        """
        print(relatorio_extrato)

    elif escolha_usuario == 0:
        break

    else:
        print("Opção errada. Escolha uma das opções")

print("\n======= Obrigado por ser nosso cliente, tenha um bom dia! =======\n")