# While
# Repetição enquanto uma condição for verdadeira.
x = 0
while x <= 7:
    print(x)
    x += 1

print("\n---\n")
i = 0
while i < 6:
    print(i)
    i += 1
    if i == 3:
        break
print("\n---\n")   

i = 1
while i < 4:
    i += 1
    if i == 3:
        continue
    print(i)

# while True: 
#     # use com cuidado, fique atenta que o loop não seja infinito.
#     # comum utilizar na criação de menus.
#     print("Digite 'sair' para sair do loop.")
#     entrada = input()
#     if entrada == 'sair':
#         break
#     print("Você digitou: ", entrada)

# Exemplo de uso do while com variável de controle.
# entrada_usuario = ''
# while entrada_usuario != 'sair':
#     entrada_usuario = input("Digite 'sair' para sair do loop.").lower()
#     print("Você digitou: ", entrada_usuario)


