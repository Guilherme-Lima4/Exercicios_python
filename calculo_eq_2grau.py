from math import sqrt

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

delta = (b**2) - 4 * a * c
raiz_delta = sqrt(delta)

x1 = (-b + raiz_delta) / 2 * a
x2 = (-b - raiz_delta) / 2 * a

if delta > 0:
	print("Raiz 1 = ", x1)
	print("Raiz 2 = ", x2)
else:
	print("O valor de delta é negativo")	