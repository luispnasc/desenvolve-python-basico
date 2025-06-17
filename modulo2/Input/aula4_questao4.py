valor = int(input("Digite o valor: ")) #576

notas_100 = valor // 100 #5  (quantia notas)
valor     = valor % 100  #76 (valor restante)

notas_50 = valor // 50 #1
valor    = valor % 50  #26

notas_20 = valor // 20 #1
valor    = valor % 20  #6

notas_10 = valor // 10 #0
valor    = valor % 10  #6

notas_5 = valor // 5  #1
valor    = valor % 5  #1

notas_2 = valor // 2  #0
valor    = valor % 2  #1

notas_1 = valor 

print(f"{notas_100} notas de 100")
print(f"{notas_50} notas de 50")
print(f"{notas_20} notas de 20")
print(f"{notas_10} notas de 10")
print(f"{notas_5} notas de 5")
print(f"{notas_2} notas de 2")
print(f"{notas_1} notas de 1")