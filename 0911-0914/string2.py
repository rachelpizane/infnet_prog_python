# Relembrando o que aprendemos e trabalhando com outros métodos.
frase = "  Python é incrível!   "
print(frase.strip()) # Remove espaços em branco do início e do fim da string
print(frase.upper())
print(frase.lower())
print(frase.capitalize())

txt = "rw........laranja ..... rw.."
print(txt.strip("r.w ")) # Remove os caracteres especificados

# replace()
frase2 = "A boa prática é a mãe do bom código."
print(frase2.replace("boa", "ótima"))
print(frase2.replace("bom", "ótimo")) # Se a palavra não existir, não será feita a substituição e a string original será retornada.

#split()
frase3 = "Hello, World!"
print(frase3.split("o")) # Divide a string em substrings se encontrar instâncias do separador especificado
data_aula = "11/12/2024"
print(data_aula.split("/")) # Retorna uma lista com os elementos separados pelo separ
dia, mes, ano = data_aula.split("/") # Isso aqui é util!!!!
print(dia, mes, ano)
print(int(dia))

#join() - Junta apenas iteráveis de strings
myTuple = ("John", "Peter", "Vicky")
myTuple_string = " - ".join(myTuple) # Junta todos os itens de um iterável em uma string
print(myTuple_string)

# find()
frase4 = "Era uma vez um reino muito distante."
print(frase4.find("reino")) # Retorna a posição da primeira ocorrência da palavra
print(frase4.find("reinado")) # Se a palavra não existir, retorna -1

# center() # bacana!
frase5 = " Python "
print(" Javascript ".center(20, "-")) # Centraliza a string, utilizando um especificador de preenchimento
print(frase5.center(20)) # Se não for especificado o preenchimento, será preenchido com espaços

#ljust() e rjust()
print(frase5.ljust(20, "-")) # Alinha a string à esquerda