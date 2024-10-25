pessoa = {"nome": "Alice", "idade": 30, "email": "alice@example.com"}

# Método get retorna o valor da chave, caso não exista retorna o valor padrão
print(pessoa.get("curso", "Não encontrado")) #Como não existe a chave "curso" ele retorna o valor padrão "Não encontrado"

# Método update adiciona ou atualiza o valor da chave
pessoa.update({"curso": "Python"}) #Adiciona a chave "curso" com o valor "Python"
pessoa.update({"idade": 31}) #Atualiza o valor da chave "idade" para 31

print(pessoa)
print(pessoa.keys()) #Retorna as chaves do dicionário
print(pessoa.values()) #Retorna os valores do dicionário