## Desafios:
# 1. Crie uma funcao que recebe uma matriz (lista de listas) e retorna a transposta dessa matriz.

def criar_matriz_transposta(matriz):
    num_colunas = len(matriz)
    num_linhas = len(matriz[0])
    print(num_colunas, num_linhas)
    matriz_transposta =  []

    for i in range(num_linhas):
      linha_matriz_transposta = []
      
      for j in range(num_colunas):
        linha_matriz_transposta.append(matriz[j][i])
        
      matriz_transposta.append(linha_matriz_transposta)
      
    print(matriz_transposta)

matriz = [[2,3,4], [11,7,9]]
criar_matriz_transposta(matriz)

matriz2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
criar_matriz_transposta(matriz2)

matriz3 = [[1]]
criar_matriz_transposta(matriz3)

# 2. Crie uma matriz 3x3 que represente um tabuleiro de jogo da velha, inicialmente vazio, onde cada célula é representada por um espaço em branco " " e imprima o tabuleiro.
# 3. Em seguida, escreva um código que permite adicionar 'X' ou 'O' em posições especificadas pelo usuário.
tabuleiro = [[" " for j in range(3)] for i in range(3)]

def gerar_tabuleiro():
    for index_linha, linha in enumerate(tabuleiro):
        for index_coluna, item_coluna in enumerate(linha):
            if index_coluna == len(linha) - 1:
                print(tabuleiro[index_linha][index_coluna], end= "\n")
                break
        
            print(tabuleiro[index_linha][index_coluna], end= " | ")   
     
        if index_linha != len(tabuleiro) - 1:  
            print("---------")
            continue
          
        print("\n\n")
        
def atualizar_tabuleiro(i, j, simbolo):
    tabuleiro[i-1][j-1] = simbolo
    gerar_tabuleiro() 


gerar_tabuleiro()  
 
while True:
    print("Defina a posição que jogará atraves das linhas e colunas")
    
    lin = int(input("Escolha a linha [1-3]: "))
    col = int(input("Escolha a coluna [1-3]: "))
    simbol = input("Escolha o simbolo 'X' ou 'O' para preencher: ")
    atualizar_tabuleiro(lin, col, simbol)
    
    resposta = input("Deseja continuar?")
    
    if resposta == "Nao":
        break
  
