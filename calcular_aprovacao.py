nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

soma = nota4 + nota3 + nota2 + nota1
media = soma/4

if media >= 6:
	print("Você foi aprovado com a media: ",media)
else:
	print("Você foi reprovado com a media: ",media)	