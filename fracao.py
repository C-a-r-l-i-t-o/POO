class Fracao:
    def __init__(self, n, d):
        self._numerador = n
        self._denominador = d
        self.simplificar()

    def __repr__(self) -> str:
        return f"{self._numerador}/{self._denominador}"

    @property
    def numerador(self):
        return self._numerador

    @property
    def denominador(self):
        return self._denominador

    def simplificar(self):
        def simplificar(n, d):
            while d:
                n, d = d, n % d
            return n

        mdc = simplificar(self._numerador, self._denominador)
        self._numerador //= mdc
        self._denominador //= mdc

    def __mul__(self, outra: 'Fracao'):
        numerador = self.numerador * outra.numerador
        denominador = self.denominador * outra.denominador
        fracao = Fracao(numerador, denominador)
        fracao.simplificar()
        return fracao

    def __truediv__(self, outra: 'Fracao'):
        numerador = self.numerador * outra.denominador
        denominador = self.denominador * outra.numerador
        fracao = Fracao(numerador, denominador)
        fracao.simplificar()
        return fracao

    def __add__(self, outra: 'Fracao'):
        numerador = self.numerador * outra.denominador + outra.numerador * self.denominador
        denominador = self.denominador * outra.denominador
        fracao = Fracao(numerador, denominador)
        fracao.simplificar()
        return fracao

    def __sub__(self, outra: 'Fracao'):
        numerador = self.numerador * outra.denominador - outra.numerador * self.denominador
        denominador = self.denominador * outra.denominador
        fracao = Fracao(numerador, denominador)
        fracao.simplificar()
        return fracao
