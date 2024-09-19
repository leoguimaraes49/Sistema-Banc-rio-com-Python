menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite_saque = 500
extrato_bancario = ""
total_saques = 0
LIMITE_MAXIMO_SAQUES = 3


def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def sacar(valor, saldo, extrato, total_saques, limite_saque):
    if valor > saldo:
        print("Operação falhou! Saldo insuficiente.")
    elif valor > limite_saque:
        print(f"Operação falhou! Limite máximo de saque é de R$ {limite_saque:.2f}.")
    elif total_saques >= LIMITE_MAXIMO_SAQUES:
        print(f"Operação falhou! Você já realizou {LIMITE_MAXIMO_SAQUES} saques hoje.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        total_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, total_saques


def exibir_extrato(saldo, extrato):
    print("\n============= EXTRATO =============")
    print("Nenhuma movimentação realizada." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("===================================")


while True:
    opcao = input(menu).lower()

    if opcao == "d":
        valor_deposito = float(input("Informe o valor do depósito: "))
        saldo, extrato_bancario = depositar(valor_deposito, saldo, extrato_bancario)

    elif opcao == "s":
        valor_saque = float(input("Informe o valor do saque: "))
        saldo, extrato_bancario, total_saques = sacar(
            valor_saque, saldo, extrato_bancario, total_saques, limite_saque
        )

    elif opcao == "e":
        exibir_extrato(saldo, extrato_bancario)

    elif opcao == "q":
        print("Saindo do sistema. Obrigado!")
        break

    else:
        print("Opção inválida! Tente novamente.")
