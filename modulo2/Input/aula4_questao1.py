# Entrada de dados
comprimento = int(input("Digite o comprimento: "))
largura     = int(input("Digite a largura: " ))
preco_m2    = float(input("Digite o valor do m2: "))

# Processamento de dados
area = comprimento * largura
preco_total = area * preco_m2

# Saída de dados
print(f"O terreno possui {area}m2 e 3custa R${preco_total:,.2f}")