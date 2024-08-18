nome = 0

if nome:
    print("Nome é verdadeiro")

# Operadores de identidade - is / is not
# Verifica se duas variáveis ou valores são o mesmo objeto.
str1 = "Python"
str2 = "Python"
str3 = str1
num1 = 10
num2 = 10
print(str1 is str2) # False
print(str1 is str3) # True
print(num1 is num2) # True

# Operador de associação - in / not in
# Verifica se um valor está presente em uma sequência de valores.
# Exemplo:
frutas = ["banana","laranja","uva","ameixa"]

fruta_1 = "ameixa"
fruta_2 = "melancia"

print(fruta_1 in frutas)  #True
print(fruta_2 not in frutas) # True
# CONDICIONAL
a = 10
b = 30
c = 40
if a < b:
    print("A é menor que b")

if c > b > a: # python aceita Dessa forma. ( c > b and c > a)
    print("C é maior que todos!")

# IF aninhada
x = int(input("Digite um numero: "))

if x > 10:
    print("Maior que 10")
    if (x % 2) == 0:
        print(" e também é par.")
        if x > 100:
            print(" e maior que 100!")

# If + Else
p = 200
q = 30

if p < 30:
    print("Menor...")
else:
    print("Maior!")

# modo ternário:
# Sintaxe: valor_se_verdadeiro if condição else valor_se_falso
print("A") if a > b else print("B")

#ternários aninhados
numero_user = int(input("Informe um número inteiro: "))
resultado = "positivo" if numero_user > 0 else "neutro" if numero_user == 0 else "negativo"

print(resultado)
p = q
# IF + Elif + Else
if p > q:
    print("P é maior que Q")
elif p == q:
    print("P é igual a Q")
else:
    print("P é menor que Q")

# pass 
if p > q:
    pass # não faz nada. Seu uso é comum em loops ou funções que ainda não foram implementadas. Tipo um marcador de lugar.