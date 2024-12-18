'''Escreva um programa que lê números inteiros positivos do usuário, um após o
outro, e monta uma lista a partir desses números e depois imprime a lista montada.
O programa deve continuar solicitando por números até que o elemento digitado
seja um número negativo (que não deve ser inserido na lista).'''


lista = []

n = int(input("Informe um numero:"))

while n > 0:
    lista.append(n)
    n = int(input("Informe um numero:"))
    
print(lista)    