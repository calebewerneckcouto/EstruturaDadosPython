'''DESAFIO. Escreva um programa que declara uma lista com elementos de
diferentes tipos e imprime na tela essa lista invertida. Não é permitido utilizar
métodos como reverse ou sort .
def inverte_lista(lista):
...
lista = ["a", 5, {1}]
lista_invertida = inverte_lista(lista)
print(lista_invertida)
# [{1}, 5, "a"]'''


# Função para inverter a lista
def inverte_lista(lista):
    lista_invertida = []  
    for i in range(len(lista) - 1, -1, -1):  
        lista_invertida.append(lista[i]) 
    return lista_invertida


lista = ["a", 5, {1}]
lista_invertida = inverte_lista(lista)

# Imprime a lista invertida
print(lista_invertida)
