# Um número elevado ao cubo é chamado de cubo (por exemplo, o cubo de 2 é 2**3).
# Crie uma lista com os primeiros 10 cubos (de 1³ a 10³) e use um laço for para exibir cada valor.

cubos = []
for valor in range(1, 11):
    cubos.append(valor ** 3)

for cubo in cubos:
    print(cubo)