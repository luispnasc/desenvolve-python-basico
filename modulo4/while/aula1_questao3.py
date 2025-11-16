n1 = float(input("Digite sua nota: "))
n2 = float(input("Digite sua nota: "))
n3 = float(input("Digite sua nota: "))
m = (n1 + n2 + n3) / 3
print(f"Sua média é: {m: .0f}")

if m>=60:
    print("Aprovado")
elif m>=40:
    print("Recuperação")
else:
    print("Reprovado")

print("Fim")