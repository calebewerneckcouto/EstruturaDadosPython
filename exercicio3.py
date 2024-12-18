'''Data uma lista de números inteiros, escreva um programa que calcula a média dos
números na lista. O resultado não deve incluir números decimais. Exemplo: 12.3
deve imprimir apenas 12 .
Se preferir, pode utilizar a lista abaixo como exemplo:
lista = [1, 10, 20, 35, 22, 12]
# Resultado deve ser 16
P.S.: Pode utilizar o operador // (divisão inteira)'''


lista = [1, 10, 20, 35, 22, 12]

soma = 0
for i in lista:
    soma += i  

media = soma // len(lista)  
print("Média dos números na lista:", media)

    