# Repetição e iteração for e while.
# for x in y - Iterando através de sequência.
# Usado para iterar sobre uma sequencia (lista, tupla, dicionário, conjunto, string).

for i in range(1, 6): # Iterando sobre uma sequência de números.
    print(i) # Imprime os números de 1 a 5.

for x in "banana": # Iterando sobre uma string.
    print(x)
print(x) # A variável x mantém o último valor da iteração. A varia´vel x não fica presa ao loop. Contudo, não é recomendado usar a variável x fora do loop.

for y in [0, 2, 5]: # Iterando sobre uma lista.
    print(y)

# Função range() - Gera uma sequência de números. 
# Sintaxe: range(inicio, parada, interação)
# - inicio: O número inicial da sequência.
# - parada: Até onde a sequência deve ir, mas sem incluir esse número.
# - interação: De quanto em quanto a sequência deve ser incrementada.
range_ex = range(6) # range(parada)

# Muito comum utilizar o range() em um loop for.
# Quando não utilizado em um loop for, o range retorna um objeto range, que pode ser convertido em uma lista.
# - range(0,6) != [0,1,2,3,4,5]
print(range_ex) 
print(type(range_ex)) # <class 'range'>

print(list(range_ex)) # [0,1,2,3,4,5]
print(type(list(range_ex))) # <class 'list'>

print(list(range(2,6))) # retorna [2,3,4,5]

# Voltando para o for
for i in range(2, 32, 3): # itera de 2 a 32 (mas sem incluir o 32), incrementando de 3 em 3.
    print(i)

