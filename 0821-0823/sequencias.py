# Sequências - Lista,Tupla, dicionário e set.

# list - mutável - [4.0, "string", True, 2]
# tuple - imutável - (4.0, "string", True, 2)
# range - sequência de números - range(0,10)
print(list(range(3))) # [0,1,2]

# set - Conjunto não ordenado, nõa contém elementos duplicados - {4.0, "string", True, 2}
# string - sequência de caracteres - "Gilberto"
# bytes - sequência binaria - b"string" (??)
# dict - Conjunto associativo de pares chave-valor - {"nome": "Gilberto", "idade": 25}

# listas e dicionarios fazem parte da vida de quem usa Python.

# Lista
# As listas são usadas para armazenar varios itens em uma única variável

lista = ["maçã", "banana", "laranja"] 
print(lista)
print (type(lista))

variaveis = (1, 2, 3, 4, 5)
print(type(variaveis))

lista_numeros = list(variaveis) # Convertendo uma tupla em lista.
print(lista_numeros)
print(type(lista_numeros))