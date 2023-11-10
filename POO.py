class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Conta:
    def __init__(self, numero, saldo=0):
        self.numero = numero
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

class Cliente(Pessoa, Conta):
    def __init__(self, nome, idade, numero, saldo):
        Pessoa.__init__(self, nome, idade)
        Conta.__init__(self, numero, saldo)

    def __str__(self):
        return f"{self.nome}, {self.idade}, CC{self.numero}, Saldo: R${self.saldo:.2f}"

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        Pessoa.__init__(self, nome, idade)
        self.salario = salario

    def aumentarSalario(self, valor):
        self.salario += valor

    def __str__(self):
        return f"{self.nome}, {self.idade}, R$ {self.salario}"

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Conta:
    def __init__(self, numero, saldo=0):
        self.numero = numero
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

class Cliente(Pessoa, Conta):
    def __init__(self, nome, idade, numero, saldo):
        Pessoa.__init__(self, nome, idade)
        Conta.__init__(self, numero, saldo)

    def __str__(self):
        return f"{self.nome}, {self.idade}, CC{self.numero}, Saldo: R${self.saldo:.2f}"

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        Pessoa.__init__(self, nome, idade)
        self.salario = salario

    def aumentarSalario(self, valor):
        self.salario += valor

    def __str__(self):
        return f"{self.nome}, {self.idade}, R$ {self.salario}"

class Privilegio:
    def __init__(self, diretor=None, gerente=None, cliente=None):
        self.login = None
        if diretor:
            self.login = diretor
        elif gerente:
            self.login = gerente
        elif cliente:
            self.login = cliente

    def __str__(self):
        return f"Login: {self.login}"

class FuncCC(Funcionario, Conta):
    def __init__(self, nome, idade, salario, numero, saldo):
        Funcionario.__init__(self, nome, idade, salario)
        Conta.__init__(self, numero, saldo)

class Diretor(FuncCC):
    def __init__(self, nome, idade, salario, bonifica, numero, saldo):
        FuncCC.__init__(self, nome, idade, salario, numero, saldo)
        self.bonifica = self.salario * 1.20
        self.nivel = "Diretor"

    def login(self):
        pass

class Gerente(FuncCC):
    def __init__(self, nome, idade, salario, bonifica, numero, saldo):
        FuncCC.__init__(self, nome, idade, salario, numero, saldo)
        self.bonifica = self.salario * 1.10
        self.nivel = "Gerente"

    def login(self):
        pass

class ContaCC(Conta):
    def __init__(self, numero, saldo, digito):
        self.digito = digito
        Conta.__init__(self, numero, saldo)

class ContaPP(Conta):
    def __init__(self, numero, saldo):
        Conta.__init__(self, numero, saldo)

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# Exemplo de uso da classe Cliente:
nome_cliente = input("Digite o nome do cliente: ")
idade_cliente = int(input("Digite a idade do cliente: "))
numero_conta_cliente = input("Digite o número da conta do cliente: ")
saldo_conta_cliente = float(input("Digite o saldo inicial da conta do cliente: "))

cliente1 = Cliente(nome_cliente, idade_cliente, numero_conta_cliente, saldo_conta_cliente)
print("Informações do Cliente:")
print(cliente1)

# Exemplo de uso da classe Diretor:
nome_diretor = input("Digite o nome do diretor: ")
idade_diretor = int(input("Digite a idade do diretor: "))
salario_diretor = float(input("Digite o salário do diretor: "))
numero_conta_diretor = input("Digite o número da conta do diretor: ")
saldo_conta_diretor = float(input("Digite o saldo inicial da conta do diretor: "))
username_diretor = input("Digite o nome de usuário do diretor: ")
password_diretor = input("Digite a senha do diretor: ")

diretor1 = Diretor(nome_diretor, idade_diretor, salario_diretor, numero_conta_diretor, saldo_conta_diretor, username_diretor, password_diretor)
print(diretor1.login())

