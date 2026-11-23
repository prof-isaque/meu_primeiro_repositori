 Sistema Bancário (POO)

Python
class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado.")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def extrato(self):
        print(f"Titular: {self.titular} | Saldo atual: R$ {self.saldo:.2f}")

# Exemplo de uso:
conta = ContaBancaria("Ana")
conta.depositar(500)
conta.sacar(200)
conta.extrato()
