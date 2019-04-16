lista = [1550,30,56,99,475,27]
#lista = sorted(lista)
#print(lista)

#selection sort

for i in range(len(lista)):

	menor = i

	for j in range(i+1,len(lista)):

		if lista[j] < lista[menor]:
			menor = j

	if lista[i] != lista[menor]:
		aux = lista[i]
		lista[i] = lista[menor]
		lista[menor] = aux 

print (lista)	
