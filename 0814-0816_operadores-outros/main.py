# Tipagem
x = 8
y = "InfNet"
Y = 'Rachel Maia'
w = 3.14
z = [5, 14.3, "Python"]
variavel = (True, 3-5j)

print(x, "-", type(x)) # int
print(y, "-", type(y)) #str
print(Y, "-", type(Y)) #str
print(w, "-", type(w)) #float
print(z, "-", type(z)) #list
print(z[0], "-", type(z[0])) #int
print(variavel, "-", type(variavel)) #tuple
print(variavel[0], "-", type(variavel[0])) #bool
print(variavel[1], "-", type(variavel[1])) #complex

w = 3
print(w, "-", type(w)) #int - sobrepondo o valor de w

print("---\n")
# Casting  - Conversão de tipos 
a = str(3)
b = int(-3)
c = float(3)
d = int (3.14)

print(a, "-", type(a)) #str
print(b, "-", type(b)) #int
print(c, "-", type(c)) #float
print(d, "-", type(d)) #int - retira o valor decimal e retorna apenas o valor inteiro

print("---\n")
# Declaração Multipla
x,y,z = "Orange", "Banana", "Cherry"
print(x, "-", y, "-", z) # # Bem prático

print("---\n")
# Desempacotando uma lista - Tipo o destructuring do JS
fruits = ["apple", "banana", "cherry"]
w, y, z = fruits 
print(w, "-", y, "-", z)

print("---\n")
# Concatenando
x = "Python é"
y = "incrível"
print(x, y) # Com virgula - espaço entre as palavras
print(x + y) # Com sinal de + - sem espaço entre as palavras
