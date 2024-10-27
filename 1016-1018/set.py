# SET
# Set é um tipo de dado que guarda uma coleção de valores onde a repetição desses valores não são válidos.
# Ele é não ordenado, imutável* e iteravel
# É imutavel, mas podemos adicionar e remover itens.
# Ordem não importa e não pode ter duplicadas ? Use sets!
# Utilizado para operacoes matematicas tipo união, interseção, diferença e diferença simetrica.
set1 = {12, 14, 15, 31, 3}
print(set1)

set2 = {1, 1, 3, 2, 3, 1, 3, 3, 3}
print(set2) # {1, 2, 3}
print(len(set2)) # 3 / Não conta os valores repetidos

for i in set2:
    print(i)
    
# Podemos fazer um set de strings, mas pelo o que eu entendi o mais comum é de numeros.
set3 = {"oi", "banana", "caio", "oi", "Oi"}
print(set3)

# Métodos 
# .add() - Adicionar um valor ao set / Lembrando que ele pode aparecer em qualquer lugar do set.
numeros = {45, 89, 72, 8, 11, 6, 72, 8, 45}

print(numeros)

numeros.add(4)
print(numeros)

numeros.add(11) # Não muda em nada, pos já tem o valor 11 no set, e não pode valor repetido.
print(numeros)

# .remove() / Remove um valor do set. Se o valor não existir o código dará erro.
numeros.remove(89)
print(numeros)

print("------------------------")
# Operações de conjuntos:
conj_a = {1, 2, 5, 6}
conj_b = {1, 5, 7, 9, 10}

print("União: ", conj_a | conj_b) # {1, 2, 5, 6, 7, 9, 10}
print("Intersecao: ", conj_a & conj_b) # {1, 5}
print("Diferença: ", conj_a - conj_b) # {2, 6}
print("Diferença Smétrica: ", conj_a ^ conj_b) # {2, 6, 7, 9, 10}

# Fazendo as operações pelos métodos
print(conj_a.union(conj_b)) 
print(conj_a.intersection(conj_b)) 
print(conj_b.difference(conj_a)) # {9, 10, 7} / Retorna os valores que só tem no conj_b, e não no conj_a.
print(conj_b.symmetric_difference(conj_a)) # {2,6,7,9,10} Retorna todos os valores dos dois sets, menos aqueles que estão presentes em ambos.

# Subconjuntos e superconjuntos

conj_c = {4, 5, 6}
conj_d = {4, 5}

print("D é subconjunto de C?", conj_d.issubset(conj_c)) # True

print("C é superconjunto de D?", conj_c.issuperset(conj_d)) # True

## Desafio:
# 1. Criar um programa que simule a operação de dois grupos de amigos decidindo para quais filmes irão juntos ao cinema. 
#   1. Cada grupo tem sua própria lista de filmes preferidos (com possíveis duplicatas). 
#   2. O programa deve determinar quais filmes são comuns a ambos os grupos (interseção) e sugerir essas opções.

set_filmes_1 = {
    "Inception", "Avatar", "The Matrix", "Interstellar", "Forrest Gump",
    "The Godfather", "The Dark Knight", "Pulp Fiction", "Fight Club", "Gladiator"
}

set_filmes_2 = {
    "Inception", "Avatar", "Titanic", "Gladiator", "The Shawshank Redemption",
    "The Matrix", "Jurassic Park", "Toy Story", "The Lion King", "Forrest Gump"
}

set_filmes_intersection = set_filmes_1.intersection(set_filmes_2)

print("Sugestões de filmes")
for contador, filme in enumerate(set_filmes_intersection):
    print(f"  {contador + 1}. {filme}")