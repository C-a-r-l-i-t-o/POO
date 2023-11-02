from datetime import date

class Cliente:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, agencia, numero, saldo, cliente):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo
        self.cliente = cliente

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        else:
            return False

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False

    def transferir(self, valor, cdest):
        if self.sacar(valor):
            cdest.depositar(valor)
            return True
        else:
            return False

    def __repr__(self):
        return f"Agência: {self.agencia}\nNúmero: {self.numero}\nSaldo: R${self.saldo:.2f}\nCliente: {self.cliente.nome}"

# Função para obter os detalhes do cliente a partir do input do usuário
def obter_detalhes_cliente():
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    data_nascimento = input("Digite a data de nascimento do cliente (formato YYYY-MM-DD): ")
    data_nascimento = date.fromisoformat(data_nascimento)
    return Cliente(nome, cpf, data_nascimento)

# Exemplo de uso
cliente1 = obter_detalhes_cliente()
conta1 = Conta("001", "12345-6", 1000.0, cliente1)
print(conta1)  # Exibir detalhes da conta

valor_deposito = float(input("Digite o valor a depositar: "))
if conta1.depositar(valor_deposito):
    print(f"Depósito realizado. Novo saldo: R${conta1.saldo:.2f}")
else:
    print("Depósito inválido. O valor deve ser maior que zero.")

cliente2 = obter_detalhes_cliente()
conta2 = Conta("002", "98765-4", 1500.0, cliente2)

valor_transferencia = float(input("Digite o valor a transferir: "))
if conta1.transferir(valor_transferencia, conta2):
    print(f"Transferência realizada. Novo saldo da conta1: R${conta1.saldo:.2f}")
    print(f"Novo saldo da conta2: R${conta2.saldo:.2f}")
else:
    print("Transferência não realizada. Saldo insuficiente.")

