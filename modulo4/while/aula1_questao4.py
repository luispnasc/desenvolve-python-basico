n = float(input())
maior = 0

while n>0:
   x = float(input())
if x > maior:
   maior = x
   n -= 1
else:
   print(maior)