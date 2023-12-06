class Tempo:
    def __init__(self, horas, minutos, segundos):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    def __add__(self, other):
        segundos = self.segundos + other.segundos
        minutos = self.minutos + other.minutos + segundos // 60
        horas = self.horas + other.horas + minutos // 60
        segundos %= 60
        minutos %= 60
        return Tempo(horas, minutos, segundos)

    def __sub__(self, other):
        segundos = self.segundos - other.segundos
        if segundos < 0:
            self.minutos -= 1
            segundos += 60
        minutos = self.minutos - other.minutos
        if minutos < 0:
            self.horas -= 1
            minutos += 60
        horas = self.horas - other.horas
        return Tempo(horas, minutos, segundos)

    def __lt__(self, other):
        return (self.horas, self.minutos, self.segundos) < (other.horas, other.minutos, other.segundos)

    def __le__(self, other):
        return (self.horas, self.minutos, self.segundos) <= (other.horas, other.minutos, other.segundos)

    def __gt__(self, other):
        return (self.horas, self.minutos, self.segundos) > (other.horas, other.minutos, other.segundos)

    def __ge__(self, other):
        return (self.horas, self.minutos, self.segundos) >= (other.horas, other.minutos, other.segundos)

    def __eq__(self, other):
        return (self.horas, self.minutos, self.segundos) == (other.horas, other.minutos, other.segundos)

    def __ne__(self, other):
        return (self.horas, self.minutos, self.segundos) != (other.horas, other.minutos, other.segundos)

    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}"
