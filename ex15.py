
numeros = [10, 5, 20, 3, 42, 7]

maiores = [n for n in numeros if n > 10]
pares = [n for n in numeros if n % 2 == 0]

print("Maiores que 10:", maiores)
print("Números pares:", pares)
