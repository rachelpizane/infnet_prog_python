# String
# São sequências de caracteres usadas para armazenar e manipular texto 
# Se comporta como um objeto iterável e ordenado. 
primeiro_nome = "Maria"
sobrenome = "Silva"
nome_completo = primeiro_nome + " " + sobrenome
print("Primeira letra: ", primeiro_nome[0]) # Podemos acessar os caracteres de uma string como se fosse uma lista.
print("Ultima letra", sobrenome[-1])
print("Números de caracteres: ", len(primeiro_nome)) # Conseguimos saber o número de caracteres de uma string com a função len(). // Barra de espaço também é um caracter.
print(nome_completo[2:6]) 

# Conseguimos utilizar todos os métodos de lista em strings, como append, insert, remove, pop, etc.

print("\n--\n")
# Dividir Strings usando Slicing
b = "Hello, World!"
print(b[2:]) # Retorna: llo, World!
print(b[-5:-2])
print(b[::-1]) # Inverte a string

print("\n--\n")
# Casting - Conversão de tipos str <> int
# Se a string tiver uma letra, não será possível converter para int.
x = 10
x_str = str(x)
print(x_str, type(x_str))

print("\n--\n")
#string multilinhas
a = """Lorem ipsum dolor sit amet, 
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) # Retorna a string com quebra de linha

print("\n--\n")
# Operador de Identificação
txt = "The best things in life are free!"
print("free" in txt) # free esta em txt?? True or False. Essa é boa hein.

# Como imprimir com as aspas
print("Hello \"World\"") # \" - Aspas duplas - Adiciona aspas duplas
print("Hello \\World\\") # \\ - Barra invertida - Adiciona uma barra invertida
print("Hello \tWorld") # \t - Tab - Adiciona um tab 
print("Hello \rWorld") # \r - Carriage Return - Retorna o cursor para o início da linha e substitui o texto que estava lá antes.
print("Hello\b World") # \b - Backspace - Apaga o caracter anterior.
print("\x48\x65\x76\x65\x6C\x6F") # \x - Caracteres hexadecimais

print("\n--\n")
print(ord('H')) # Retorna o valor Unicode do caracter / Bem util para criptografia
print(chr(72)) # Retorna o caracter do valor Unicode 

print("\n--\n")
#Métodos de String
frase = "Python é incrível! "
print(frase.upper())
print(frase.lower())

print(frase.strip()) # Remove espaços em branco do início e do fim da string 
print(frase.strip(" P!l")) # Remove os caracteres especificados

print(frase.replace("Python", "Java")) # Substitui uma string por outra
print(frase.replace(" ",""))

print(frase.split(" ")) # Divide a string em substrings se encontrar instâncias do separador especificado
texto = "Python, Java, C++, Ruby"
print(texto.split(",")) 

myTuple = ("John", "Peter", "Vicky")
x = ", ".join(myTuple) # Junta todos os itens de um iterável em uma string / Usado para reconstruir informações
print(x)