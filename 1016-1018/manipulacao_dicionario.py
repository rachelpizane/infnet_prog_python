estoque = {"mouse": 69.90, "cadeira": 54.00, "sabonete": 2.80}

print(estoque.items())

# Para iterar um objeto, normalmente utilizamos .items() para acessar sua chave e seu valor ao mesmo tempo.
c = 1
for chave, valor in estoque.items(): # [()]
    print(f"nº {c} \nProduto: {chave} \nPreço: {valor}", sep="\n", end="\n\n")
    c += 1
    
estoque_aumento_10porc = {}
for chave, valor in estoque.items():
    estoque_aumento_10porc.update({chave: round(valor * 1.1, 2)})
    
print(estoque_aumento_10porc) # {'mouse': 76.89, 'cadeira': 59.4, 'sabonete': 3.08}

# Dict comprehensions
# Uma forma de escrever o codigo acima de maneira mais concisa.
# Sintaxe: {chave: valor for item in iterável if condição}
estoque_aumento_10porc_2v = {chave: round(valor * 1.1, 2) for chave, valor in estoque.items()}

print(estoque_aumento_10porc_2v) # {'mouse': 76.89, 'cadeira': 59.4, 'sabonete': 3.08}


print('--------------------------------------------------')
print("DESAFIOS")
# Desafio 
# 1. Crie uma lista aleatória e usando list comprehensions remova todos multiplos de 5 desta lista e exiba ela.

numeros_aleatorios = [12, 47, 85, 19, 36, 57, 4, 98, 23, 61, 77, 2, 45, 31, 68, 73, 9, 88, 15, 54]

numeros_multiplos_5 = [num for num in numeros_aleatorios if num % 5 == 0 ]

print(numeros_multiplos_5)

# 1. Dado um dicionario contendo nomes de alunos e suas respectivas notas, crie uma funcao que retorna um novo dicionario apenas com os alunos aprovados (nota >= 7).

notas_alunos = {
    "Alice": 8.5,
    "Bruno": 7.2,
    "Carlos": 9.1,
    "Daniela": 6.8,
    "Eduardo": 5.5,
    "Fernanda": 8.0,
    "Gabriel": 7.9,
    "Helena": 9.6,
    "Igor": 6.3,
    "Juliana": 7.0,
    "Kleber": 4.9,
    "Laura": 9.3,
    "Marcos": 5.8,
    "Natália": 8.4,
    "Otávio": 6.0,
    "Patrícia": 10.0,
    "Rafael": 3.7,
    "Sabrina": 7.6,
    "Tiago": 5.2,
    "Vanessa": 8.9
}

notas_alunos_aprovados = {chave: valor for chave, valor in notas_alunos.items() if valor >= 7}

print(notas_alunos_aprovados)