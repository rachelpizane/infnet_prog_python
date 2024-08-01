print("Olá Mundo!")

# Demostrando tipagem dinâmica
idade = 43
print(idade)
print(type(idade)) # tipo inteiro

idade = float(idade); # Transformei o dado para float
print(idade,"-",type(idade))

idade = str(idade); # Transformei o dado para string
print(idade + "24") # 43.024

num1 = 5; # retorna inteiro
num2 = 2; # retorna inteiro
resultado = num1 / num2 # retorna float

print(num1, "-", type(num1), "\n",num2, "-", type(num2), "\n",resultado, "-", type(resultado))

# Exercicio - Conversão de minutos
min = 186
hrs = min / 60
seg = min * 60
dia = (min / 60) / 24

print("\n----")
print(min, "minutos equivalem a: ")
print(round(dia,2), "dias")
print(hrs, "horas")
print(seg, "segundos.")

