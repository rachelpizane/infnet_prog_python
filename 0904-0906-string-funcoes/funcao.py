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
# argumento palavra-chave
saudacao_nome2(nome="Jorge")

print("\n---\n")
coisa1, *coisa2, coisa3 = "Hello", "World", "Python", "Programming", "Language"

print(coisa1)
print(coisa2)
print(coisa3)

print
# Função que retorna com n valores
def valores(*valores): # formato de tupla
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

print("\n-Escopo das variáveis--\n")
# Escopo das variáveis
def teste():
    print(x)

def teste2():
    x = 1
    print(x)

def teste3():
    print(y)
x = 2
teste() # Retorna: 2 // Utiliza a variavel global
teste2() # Retorna: 1 // Função da preferência a variavel com mesmo nome criada dentro dela mesma
print(x) # Retorna: 2 // OBS: A variável global continua com mesmo valor

def main():
    def teste4():
        print(y)

    y = 3
    # teste3() # Retorna: erro. A função só consegueria usar a variavel y se ela tivesse sido criada dentro da função main(). Como não é o caso, precisaria colocar o Y como argumento para funcionar.
    teste4() # Aqui ja deu certo.

main()

# Docstring 
# Faz parte da documentação da função.
