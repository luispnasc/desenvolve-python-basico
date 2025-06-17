nome_p1  = (input("Digite o nome do produto 1: "))
preco_p1 = float(input("Digite o preço unitário do produto 1: "))
quant_p1 = int(input("Digite a quantidade do produto 1: "))

nome_p2  = (input("Digite o nome do produto 2: ")) 
preco_p2 = float(input("Digite o preço unitário do produto 2: "))
quant_p2 = int(input("Digite a quantidade do produto 2: "))

nome_p3  = (input("Digite o nome do produto 3: "))
preco_p3 = float(input("Digite o preço unitário do produto 3: "))
quant_p3 = int(input("Digite a quantidade do produto 3: "))

preco_t1 = preco_p1 * quant_p1
preco_t2 = preco_p2 * quant_p2
preco_t3 = preco_p3 * quant_p3

preco_total = preco_t1 + preco_t2 + preco_t3
print(f"Total: R${preco_total:,.2f}") 