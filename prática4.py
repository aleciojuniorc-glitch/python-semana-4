
texto = input("Digite palavras separadas por espaço: ")

palavras = texto.split()
unicos = set(palavras)

print("Quantidade digitada:", len(palavras))
print("Quantidade única:", len(unicos))
print("Palavras sem repetição:", sorted(unicos))
