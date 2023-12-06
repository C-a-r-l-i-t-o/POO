from tempo import Tempo

tempo1 = Tempo(23, 30, 45)
tempo2 = Tempo(1, 45, 15)

tempo_soma = tempo1 + tempo2
tempo_subtracao = tempo1 - tempo2

print(f"Tempo 1: {tempo1}")
print(f"Tempo 2: {tempo2}")
print(f"Soma: {tempo_soma}")
print(f"Subtração: {tempo_subtracao}")
print(f"Tempo 1 > Tempo 2: {tempo1 > tempo2}")
