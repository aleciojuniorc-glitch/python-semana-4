
texto = input("Digite as notas separadas por espaço: ")

notas = [float(x) for x in texto.split()]

estatisticas = (
    min(notas),
    max(notas),
    sum(notas) / len(notas)
)

print(f"Menor nota: {estatisticas[0]:.2f}")
print(f"Maior nota: {estatisticas[1]:.2f}")
print(f"Média: {estatisticas[2]:.2f}")
