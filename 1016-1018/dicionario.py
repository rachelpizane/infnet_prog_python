print("TESTANDO")

pessoa = {
  "nome": "Rachel",
  "idade": 27
}
print(list(pessoa)) # ['nome', 'idade'] / Quando transformamos um dicionario em uma lsita, ele retorna as chaves como os valores dessa nova lista.
print(pessoa)

pessoa["sexo"] = "feminino"
pessoa["idade"] = 21
print(pessoa)


del pessoa["sexo"]
print(pessoa)
print("-------------------")

# Principas métodos: .get(), .keys(), .values() e .items()

print(pessoa.keys()) #Retorna uma visualização das chaves do objeto iterável. 
print(pessoa.values()) # Retorna uma visualização iterável dos valores do objeto. 
print(pessoa.items()) # Retorna uma visualização iterável do pares das chave-valor do objeto em forma de tuplas. 

# Essas visualizações funcionam como uma lista, mas não são extamente uma, pois elas se adaptam a mudanças feitas no dicionário. Segue o exemplo:

chaves = pessoa.keys()
pessoa['genero'] = "F"
print(chaves) # Mesmo que as chaves tenham sido armazenadas antes da inclusão de "genero", ao ser chamada, ela retorna com a nova chave, pois a visualização reflete a ultima alteração feita no dicionario.

# Mas se quiser, podemos transforma-las em listas, atraves do list()
lista_chaves = list(chaves)
pessoa["cidade"] = "Rio de Janeiro"

print(chaves)
print(lista_chaves) # Não incluiu a chave "cidade"

# .get() / Retorna o valor da chave. Se não existir, podemos incluir um segundo argumento como um valor padrão.
print(pessoa.get("idade")) # 21
print(pessoa.get("pais")) # None
print(pessoa.get("data_nascimento", "Não encontrado")) # Não encontrado
print("-------------------")

# update(dict2)
# Atualiza o dicionario com pares chave-valor de outro dicionário

alimento = {
  "nome": "banana",
  "tipo": "fruta",
}

cor = {
  "cor": "amarelo"
}

print(alimento) # {'nome': 'banana', 'tipo': 'fruta'}

alimento.update(cor)
print(alimento) # {'nome': 'banana', 'tipo': 'fruta', 'cor': 'amarelo'}

alimento.update({"validade": "vencida"})
print(alimento) # {'nome': 'banana', 'tipo': 'fruta', 'cor': 'amarelo', 'validade': 'vencida'}

# pop(chave, valor_padrao=None) - Remove par-chave e retorna o valor do par removido.
remover_item = alimento.pop("tipo")
print(remover_item) # fruta
print(alimento) # {'nome': 'banana', 'cor': 'amarelo', 'validade': 'vencida'}

# popitem() Remove o ultimo par-chave do dicionário e retorna uma tupla com a chave e o valor removido.
remover_par = alimento.popitem()
print(remover_par) # ('validade', 'vencida')
print(alimento) # {'nome': 'banana', 'cor': 'amarelo'}

print('--------------------------------------------------')
print("DESAFIOS")

### Desafio 1
# 1. Crie um dicionário para armazenar informações sobre um livro, incluindo título, autor e ano de publicação. Adicione um campo de gênero e remova o ano de publicação.

livro = {
  "titulo": "Era uma vez um padra",
  "autor": "Caio",
  "ano_publicacao": 1988
}

livro["genero"] = "auto-ajuda"
livro.pop("ano_publicacao")

print(livro)

### Desafio 2
# 1. Crie um dicionario que represente um catalogo de produtos de uma loja. Cada chave é o nome do produto e o valor é o preco do produto. 
#2. Adicione pelo menos tres produtos ao catalogo. Em seguida, adicione uma funcionalidade para aplicar um desconto de 10% em todos os produtos.

estoque = {"mouse": 69.90, "cadeira": 54.00, "sabonete": 2.80}

estoque.update({"fone": 250.00, "mesa": 174.00, "tv": 2000.00})

estoque_desconto = {}
for chave, valor in estoque.items():
    estoque_desconto.update({chave: round(valor * 0.9,2)})   

print(estoque_desconto)

estoque_desconto2v = {chave: round(valor * 0.9,2) for chave, valor in estoque.items()}

print(estoque_desconto2v)