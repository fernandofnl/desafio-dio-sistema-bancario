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
        
        while True:

            print("\n======= Depositar =======\n")
            deposito = float(input("Digite o valor do depósito: "))

            if deposito <= 0:
                print("Não é possível depositar esse valor!")

            else:
                break
        
        print(".")
        sleep(1)
        print("..")
        sleep(1)
        print("...")
        sleep(1)
        saldo += deposito
        print("Depósico confirmado")
        sleep(1)
        extrato += f'\nDepósito no valor de R$ {deposito}'

    elif escolha_usuario == 2:

        while True:
            
            print("\n======= Saque =======\n")
            saque = float(input("Digite o valor do saque: "))

            if saque <= 0:
                print("Valor inválido!")

            else:
                break
            
        print(".")
        sleep(1)
        print("..")
        sleep(1)
        print("...")
        sleep(1)

        if saldo - saque < 0:
            print("Não será possível sacar o dinheiro por falta de saldo.")

        elif numero_saques < LIMITE_SAQUE and saque <= limite_por_saque:
            saldo -= saque
            print("Saque confirmado")
            numero_saques += 1
            extrato += f'\nSaque no valor de R$ {saque}'

        else:
            if numero_saques >= LIMITE_SAQUE:
                print("Saque não realizado! Ultrapassou o limite de saques diários.")
            elif saque > limite_por_saque:
                print("Tentativa de sacar valor maior que o seu limite diário de R$ 500.00!")
                print("Se necessário entre em contato com a agência.")
         
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
