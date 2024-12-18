'''DESAFIO. Uma string ( str ) também pode ser percorrida utilizando o for .
for x in "abc":
print(x)
# Vai imprimir:
# a
# b
# c
Escreva um programa que solicite uma string para o usuário e imprima quantas
vezes cada letra aparece na palavra. Por exemplo:
"banana"
# O resultado deve ser
{
'a': 3,
'b': 1,
'n': 2
}
'''


palavra = input("Digite uma palavra: ")


contagem = {}


for letra in palavra:
    if letra in contagem:  
        contagem[letra] += 1
    else:  
        contagem[letra] = 1


print(contagem)
