def my_function():
    print("Hello from a function")

my_function()

def saudacao_nome(nome): # parâmetro
    print(f"Hello {nome}")
    
saudacao_nome("Jorge") # argumento posicional

# parametro opcional
def saudacao_nome2(nome = "Amanda"): # parametro opcional
    print(f"Hello {nome}")

saudacao_nome2()
# argumento palavra-chave me perdi aqui
saudacao_nome2(nome="Jorge")

print("\n---\n")
coisa1, *coisa2, coisa3 = "Hello", "World", "Python", "Programming", "Language"

print(coisa1)
print(coisa2)
print(coisa3)

print
# Função que retorna com n valores # me perdi aqui
def valores(*valores):
    print(valores)

valores(1, 2, 3, 4, 5)

# forçar args posicionais
def forcar_posicionais(a, b, /):
    print(a, b)

forcar_posicionais(1, 2)

# forçar args palavra-chave
def forcar_palavra_chave(*, a, b):
    '''Testando docstring'''
    print(a, b)

forcar_palavra_chave(a=1, b=2)
print(forcar_palavra_chave.__doc__)
# global 

# Docstring 
# Faz parte da documentação da função.