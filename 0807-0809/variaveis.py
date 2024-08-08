nome_da_variavel = "256"
print(type(nome_da_variavel)) # Retorna o tipo da informação

nome_da_variavel = float(nome_da_variavel) # Muda a variavel para tipo float
print(nome_da_variavel,"-",type(nome_da_variavel))

idade = input("Insira a sua idade: ") # input retorna sempre uma string
print(type(idade)) # <class 'str'>

num = float(input("Insira um número: ")) # Se o usuario escrever uma string a função float() não consegue convertê-lo.
print(num)

