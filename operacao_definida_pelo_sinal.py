num1 = int(input("Digite um número para a realização da operação que você escolherá:"))
num2 = int(input("\n Digite outro número para a realização da operação que você escolherá:"))
sinal = str(input("\n Digite o sinal da operação que deseja realizar: +|-|*|/|**:"))

if sinal == "+":
	print("\n A soma é: ", num1 + num2)
elif sinal == "-":
	print("\n A subtração é: ", num1 - num2)
elif sinal == "*":
	print("\n A multiplicação é: ", num1 * num2)
elif sinal == "/":
	print("\n A dvisão é: ", num1 / num2)
elif sinal == "**":
	print("\n A exponenciação é: ", num1 ** num2)
else:
	print("\n Você não digitou um sinal válido!")				