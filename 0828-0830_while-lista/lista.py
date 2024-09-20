# Sequencias são estruturas de dados
# listas e dicionarios fazem parte da vida de quem usa Python.
# len() - Retorna o tamanho da sequencia.
lista = ["pera", "uva", "maçã", "banana", "laranja"]
print(len(lista)) 
print(type(lista))

# metodos de listas. Classe lista tem conjunto de funções. Normalmente um método alterar o elemento que está sendo aplicado.

#.reverser() - Inverte a ordem dos elementos da lista.
lista.reverse()
print(lista) # ['laranja', 'banana', 'maçã', 'uva', 'pera']
print("\n---\n")

# Slicing - fatiamento
# Retorna parte da lista
# Sintaxe: lista[inicio:fim] / O fim não é incluido.
print(lista[1:4]) # fatiamento
lista[1:3] = ["manga"] # Vai substituir banana e maçã por manga.
print(lista)
print("\n---\n")

# extend() - Adiciona elementos iteravela outra lista.
lista2 = ["abacaxi", "melancia"]
lista.extend(lista2)
print(lista)

print("\n---\n")
# append() - Adiciona um item ao final da lista.
animais = ["cachorro", "gato", "papagaio"]
animais.append("coelho")
print(animais)

animais.append(["cavalo", "vaca"]) # Adiciona um item composto por uma lista
print(animais)

print("\n---\n")
# insert(index, item) - Adiciona um item em uma posição específica.
animais.insert(1, "passarinho")
print(animais)

print("\n---\n")
# remove(valor) - Remove um item da lista.
animais.remove("gato") # remove a primeira vez que aparecer gato. Ele começar a scanear da esquerda para direita.
print(animais)

# pop() - Remove o último item da lista, se não for passado um índice. Se passar um índice, remove o item da posição.
animais.pop() # remove ["cavalo", "vaca"]
animais.pop(3)
print(animais)

print("\n---\n")
# Utilizando del - Me perdi aqui.
temperatura = [22, 25, 27, 30]
print(temperatura)
del temperatura[2:]

print(temperatura)
# clear() - Remove todos os elementos da lista.
temperatura.clear()
print(temperatura)

print("\n---\n")
# list comprehension - Criar uma nova lista a partir de uma iteração de uma outra lista
comida = ["arroz", "feijão", "macarrão"]
comida_upper = [c.upper() for c in comida]
print(comida_upper)

comida.pop() # Mostrando que mesmo que você remova uma elemento da lista original, a lista criada com list comprehension não é alterada.

print(comida)
print(comida_upper) 

# sort() - Ordena a lista em ordem crescente de acordo com a tabela ASCII.
# Me perdi aqui
# reverse() - Inverte a ordem dos elementos da lista.

print("\n---\n")
# Concaternar lista 
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2 
print(lista3)

# Veremos tupla e set mais para frente.