class FormaGeometrica:
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(FormaGeometrica):
    def __init__(self, comprimento, largura):
        super().__init__()
        self.comprimento = comprimento
        self.largura = largura

    def calculaArea(self):
        self.area = self.comprimento * self.largura
        return self.area

    def calculaPerimetro(self):
        self.perimetro = 2 * (self.comprimento + self.largura)
        return self.perimetro

class Triangulo(FormaGeometrica):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calculaArea(self):
        self.area = 0.5 * self.base * self.altura
        return self.area

    def calculaPerimetro(self):
        # Os triângulos não têm um único perímetro fixo,
        # portanto, não implementamos esse método aqui.
        return None

# Função para receber valores do usuário e criar objetos de forma geométrica
def criar_forma():
    forma = input("Digite 'R' para criar um retângulo ou 'T' para criar um triângulo: ")
    
    if forma.upper() == 'R':
        comprimento = float(input("Digite o comprimento do retângulo: "))
        largura = float(input("Digite a largura do retângulo: "))
        return Retangulo(comprimento, largura)
    
    elif forma.upper() == 'T':
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        return Triangulo(base, altura)
    
    else:
        print("Opção inválida. Tente novamente.")
        return criar_forma()

# Código de teste
forma = criar_forma()

print(isinstance(forma, FormaGeometrica))  # Verifica se é uma instância de FormaGeometrica

area = forma.calculaArea()

print(f"Área da forma selecionada: {area}")

