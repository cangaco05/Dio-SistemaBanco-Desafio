while True:
    print("== Sistema Bancário ==")
    print("1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")

    opcao = input("Selecione uma opção: ")

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
    if opcao == "2":
        valor = float(input("Informe o valor do saque: "))
    if opcao == "3":
        valor = float(input("Informe o valor do depósito: ")) 
       
        

        
class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def deposito(self, valor):
        self.saldo += valor
        self.depositos.append(valor)
        print(f"Depósito de R$ {valor:.2f} realizado. Saldo atual: R$ {self.saldo:.2f}")

    def saque(self, valor):
        if len(self.saques) < 3 and valor <= 500 and valor <= self.saldo:
            self.saldo -= valor
            self.saques.append(valor)
            print(f"Saque de R$ {valor:.2f} realizado. Saldo atual: R$ {self.saldo:.2f}")
        elif valor > 500:
            print("Limite máximo de saque por transação é de R$ 500.00")
        elif len(self.saques) >= 3:
            print("Número máximo de saques diários atingido.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def extrato(self):
        print("Extrato:")
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
        else:
            for deposito in self.depositos:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in self.saques:
                print(f"Saque: R$ {saque:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")


# Loop principal do sistema bancário
conta = ContaBancaria()

