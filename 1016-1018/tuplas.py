tupla = ()

print(tupla)

bichos = 'Cachorro', # Para ser uma tupla, é necessário colocar a vírgula no final. Caso contrário, será uma string
print(bichos)

# Desempacotando uma tupla = Tipo o destruncturing do JS

frutas = ('Banana', 'Maca')
fruta1, fruta2 = frutas
print(fruta1, fruta2)

# Criar uma tupla a partir do tuple()
lista = [1, 2, 3]
tupla_lista = tuple(lista)
print(tupla_lista)

a = (7, 2)
b = (7, 2)
print(a == b) # True

# Tupla também é iterável e pode ser usada em loops
for i in a:
    print(i)

# Tupla não pode ser alterada, mas pode ser concatenada
# Sempre tem uma gambiarra...
tupla2 = (1, 2, 3)
list_tupla2 = list(tupla2)
list_tupla2.append(4)
tupla2 = tuple(list_tupla2)
print(tupla2)

# Método count() retorna a quantidade de vezes que um elemento aparece na tupla
tupla3 = (1, 2, 3, 1, 1)
print(tupla3.count(1))

# Método index() retorna o índice do elemento passado como argumento
print(tupla3.index(3))