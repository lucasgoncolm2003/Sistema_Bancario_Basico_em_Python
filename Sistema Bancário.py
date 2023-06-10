saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
while True:
    opcao = int(input("\n[1] - Depósito\n[2] - Saque\n[3] - Extrato\n[4] - Saída\nOpção => "))
    if (opcao == 1):
        valor = float(input("Informe o Depósito: "))
        if (valor > 0):
            saldo += valor
            print(f"-> Depósito efetuado de: R$ {valor:.2f}")
            print("================================================")
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação inválida e valor inválido")
            print("================================================")
    elif (opcao == 2):
        valor = float(input("Informe o Saque: "))
        excedente_de_saldo = valor > saldo
        excedente_de_limite = valor > limite
        excedente_de_saques = numero_saques >= LIMITE_SAQUES
        if excedente_de_saldo:
            print("Operação inválida! Saldo Insuficiente!")
            print("================================================")
        elif excedente_de_limite:
            print("Operação inválida! Excedente de Limite!")
            print("================================================")
        elif excedente_de_saques:
            print("Operação inválida! Número de Saques excedido!")
            print("================================================")
        elif (valor > 0):
            saldo -= valor
            print(f"Saque efetuado de: R$ {valor:.2f}")
            print("================================================")
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação inválida! Valor Informado Inválido!")
            print("================================================")
    elif (opcao == 3):
        print("\n============== Extrato Bancário ==============")
        print("Sem Movimentações até o momento :)" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("================================================")
    elif (opcao == 4):
        break
    else:
        print("Operação Inválida, selecione uma Operação Válida!")
