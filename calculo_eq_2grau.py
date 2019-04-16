a = int(input())
b = int(input())
c = int(input())

delta = (b**2) - 4 * a * c

x1 = (-b + (delta ** 0.5)) / 2 * a
x2 = (-b - (delta ** 0.5)) / 2 * a

if delta > 0:
	print("Raiz 1 : ", x1)
	print("Raiz 2 : ", x2)
else:
	print("O valor de delta é negativo")	