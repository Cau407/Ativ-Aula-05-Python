from functools import reduce

# Função quadrados

numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x : x ** 2, numeros))
print("Quadrados: ", quadrados)

# Função pares

pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Pares: ", pares)

# Função soma

soma = reduce(lambda x, y: x + y, numeros)
print("Soma: ", soma)