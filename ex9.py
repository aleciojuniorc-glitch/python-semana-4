
notas = (7.5, 9.0, 6.0, 8.5, 10.0)

estatisticas = (
    min(notas),
    max(notas),
    sum(notas) / len(notas)
)

print("Menor nota:", estatisticas[0])
print("Maior nota:", estatisticas[1])
print(f"Média: {estatisticas[2]:.2f}")
