Filtros de Pares em Lista 

numeros = []
for i in range(10):
    n = int(input9f"Digite o {i+1}° número: "))
    numeros,append(n)

# Usando List Comprehenion para filtrar
pares = [n for n in numeros if n % 2 == 0]
print(f"Números pares: {pares}")
    
