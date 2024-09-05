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

for i in lista_numeros: # Iterando sobre uma lista.
    print(i, end=', ')

print("\n----------------\n")
lista_aninhada = [1, 2, 3, ["maçã", "banana", "laranja"]] # Lista aninhada.

for i in lista_aninhada: # Iterando sobre uma lista aninhada.
    if type(i) == list:
        for j in i:
            print(j, end=' ')
    else:
        print(i, end=' ')

# Itens da lista são indexados. É o endereço do item na lista.
print(lista[1]) # 'banana'
print(list(enumerate(lista))) # O que esse enumerate faz?

print(lista_numeros[len(lista_numeros) - 1]) # 5
print(lista_numeros[-1]) # 5 - Acesso ao último item da lista de forma mais simples.
print(lista_aninhada[3][2]) # 'laranja'

#Slicing - Explicar melhor
# sintaxe: lista[inicio:fim:passo]

listaB = [1, 2, 3, 4, 5]
print(listaB[1:3]) # [2, 3] - Retorna os itens da posição 1 até a posição 3 (mas sem incluir a posição 3).
listaB[1:3] = [11, 9, 7] # Substitui os itens da posição 1 e posição 2 pelos itens da lista [11, 9, 7].
print(listaB) # [1, 11, 9, 7, 4, 5]

print(listaB[2:-1]) # [9, 7, 4] - Retorna os itens da posição 2 até a penúltima posição.

print(listaB[2:5:2]) # [9, 4] - Retorna os itens da posição 2 até a posição 5 (mas sem incluir a posição 5), incrementando de 2 em 2.

print("\n----------------\n")
#List comprehension
thislist = ["apple", "banana", "cherry"]
for i in thislist:
    print(i) # modo detalhado

print("\n---\n")
[print(x) for x in thislist] # modo mais compacto de fazer um loop for. / Me lembra ternário

print("\n---\n")
# " List comprehension serve para criar novas listas a partir de uma iteração de forma abreviada, onde cada resultado da iteração é um novo item na nova lista. Ela também permite transformar ou filtrar os elementos durante o processo."

listinha = [2,3,4,5,6]
listinha_par = [valor for valor in listinha if valor % 2 == 0] # "Itere sobre cada valor da listinha e se o valor for par, adicione-o a listinha_par"

# "Retorne o valor se ele for par a cada valor  em listinha"
# # List comprehension com condicional.
#Achei util, é tipo um .map() e filter() do JS
print(listinha_par) # [2, 4, 6]


# Declaração break - Interrompe o loop e sai do bloco de código.
roupas = ["camisa", "calça", "meia", "cueca", "bermuda", "sapato"]

for roupa in roupas:
    if roupa == "cueca": # Se a roupa for cueca, interrompa o loop.
        break
    print(roupa)

print("\n---\n")

# Declaração continue - Interrompe a iteração atual e executa a próxima iteração do loop.
for roupa in roupas:
    if roupa == "cueca": # Se a roupa for cueca, pule para a próxima iteração do loop.
        continue
    print(roupa)

print("\n---\n")
# Else do for - O bloco de código dentro do else será executado quando o loop terminar.
for x in range():
    print(x)
else:
    print("Loop terminado!")

# OBS: Se houver um break no loop e ele for acionado, o bloco de código dentro do else nunca será executado.

# pass - Quando uma declaração é requerida sintaticamente, mas você não quer executar nenhum código, use a declaração pass.

for x in range(6):
    pass # Não faz nada, mas também não gera erro.