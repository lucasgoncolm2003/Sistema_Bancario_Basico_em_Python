def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo, extrato, num_saq, usuarios, contas, limite = (0.00, "", 0, [], [], 500.00)
    while True:
        opcao = menu()
        if opcao == "1":
            valor = float(input("=> Informe o valor do Depósito: "))
            saldo, extrato = depositos(saldo, valor, extrato)
        elif opcao == "2":
            valor = float(input("=> Informe o valor do Saque: "))
            saldo, extrato = saque(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                num_saq = num_saq,
                lim_saq = LIMITE_SAQUES
            )
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "5":
            lista_conta(contas)
        elif opcao == "6":
            criar_usuario(usuarios)
        elif opcao == "7":
            break
        else:
            print("=> Operação inválida, selecione uma válida!")
def menu():
    menu = """
    MENU DE OPÇÕES
    [1] - Operação de Depósito
    [2] - Operação de Saque
    [3] - Operação de Extrato
    [4] - Criação de Novas Contas
    [5] - Listagem de Contas
    [6] - Novo Acesso de Usuário
    [7] - Operação de Saida
    =====> """
    return input(menu)
def depositos(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"\n==> Depósito de R$ {valor:.2f} efetuado com sucesso!")
    else:
        print("==> Operação Inválida! Valor Inválido")
    return saldo, extrato
def saque(*, saldo, valor, extrato, limite, num_saq, lim_saq):
    excedente_saldo = (valor > saldo)
    excedente_limite = (valor > limite)
    excedente_saque = (num_saq >= lim_saq)
    if excedente_saldo:
        print("\n==> Operação Inválida! Saldo Insuficiente!")
    elif excedente_limite:
        print("\n==> Operação Inválida! Saque excede Limite!")
    elif excedente_saque:
        print("\n==> Operação Inválida! Número de Saques excedido!")
    elif (valor > 0):
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        num_saq += 1
        print(f"\n==> Saque de R$ {valor:.2f} efetuado com sucesso!")
    else:
        print("\n==> Operação Inválida! Valor Inválido")
    return saldo, extrato
def filtro(cpf, usuarios):
    usuario_filtro = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtro[0] if usuario_filtro else None
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (sem separadores): ")
    usuario = filtro(cpf, usuarios)
    if usuario:
        print(f"\n==> Já existe usuário com esse CPF!")
        return
    nome = input("Informe o nome completo: ")
    data_nasc = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (log, número, bairro, cidade e estado): ")
    usuarios.append({"nome": nome, "data_nasc": data_nasc, "cpf": cpf, "endereco": endereco})
    print("==> Usuário criado com sucesso!")
def criar_conta(agencia, num_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtro(cpf, usuarios)
    if usuario:
        print("\n==> Conta criada com sucesso!")
        return {"agencia": agencia, "num_conta": num_conta, "usuario": usuario}
    print("\n==> Usuário não encontrado, fluxo encerrado!")
def lista_conta(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['num_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("==============================================")
        print(linha)
        print("==============================================")
main()
