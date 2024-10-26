file = open('1016-1018/arquivo.txt', 'r') # caminho do arquivo e modo de abertura
# Ele retorna o objeto file, que possui o método read()
print(file.read())
file.close()
# Todo arquivo precisa ser fechado. 
# Para manipular precisa abri-lo.
# processador, vai no arquivo e escrever no final. Conversa ta bem baixo nivel.
# Fechar o arquivo é importante se nao vai dar ruim

# Comando With é um controle de contexto. Ele garante que o arquivo será fechado, mesmo que ocorra uma exceção.

# O trecho acima seria dessa forma abaixo.
with open('1016-1018/arquivo.txt', 'r') as file:
    print(file.read())
    
# with open('1016-1018/arquivo.txt', 'w') as file:
    # file.write('Escrevendo no arquivo2v')
    
with open('1016-1018/arquivo.txt', 'r') as file:
    info = file.read() # Armazena o conteúdo do arquivo na variável info

print(info) # Imprime o conteúdo do arquivo após fecha-lo.

with open('1016-1018/arquivo.txt', 'r') as file:
    line = file.readline() # Lê a primeira linha do arquivo cada linha uqe é chamada, ele lê a próxima linha
    while line:
        print(line, end='')
        line = file.readline()

with open('1016-1018/arquivo.txt', 'r') as file:
    lines = file.readlines()
    
print(lines)

# wrtie
#writelines

# mode = a