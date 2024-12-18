'''Suponha o seguinte programa:
# Alunos e suas respectivas notas
alunos = [
("Alice", 8),
("Bob", 7),
("Carlos", 9),
]
Escreva uma programa que calcula a média das notas de todos os alunos'''

alunos = [
    ("Alice", 8),
    ("Bob", 7),
    ("Carlos", 9),
]

soma_notas = 0  


for x, y in alunos:
    soma_notas += y 


media = soma_notas // len(alunos)  

print("Média das notas:", media )

