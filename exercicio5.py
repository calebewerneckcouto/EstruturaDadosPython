'''Suponha o seguinte programa:
Exercícios – Estruturas de dados 2
# Alunos e suas notas representados através de dicionários
alunos = [
{
"nome": "Alice",
"nota": 8,
},
{
"nome": "Bob",
"nota": 7,
},
{
"nome": "Carlos",
"nota": 9,
}
]
Escreva uma programa que calcula a média das notas de todos os alunos'''
alunos = [
{
"nome": "Alice",
"nota": 8,
},
{
"nome": "Bob",
"nota": 7,
},
{
"nome": "Carlos",
"nota": 9,
}
]

alunos = [
    {"nome": "Alice", "nota": 8},
    {"nome": "Bob", "nota": 7},
    {"nome": "Carlos", "nota": 9},
]

soma_notas = 0  


for aluno in alunos:
    soma_notas += aluno["nota"]  


media = soma_notas // len(alunos)  

print("Média das notas:", media)
