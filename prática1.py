
numeros = []

qtd = int(input("Quantos números deseja digitar? "))

for i in range(qtd):
    n = int(input("Digite um número: "))
    numeros.append(n)

print("Lista:", numeros)
print("Tamanho:", len(numeros))
