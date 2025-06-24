# Pense em pelo menos três animais diferentes que têm uma característica em comum 
# (por exemplo, animais de estimação ou animais que voam). Armazene os nomes desses animais em uma lista.
# Use um laço for para exibir o nome de cada animal.
# Depois, modifique o programa para imprimir uma afirmação sobre cada animal, 
# como: “Um cachorro seria um ótimo animal de estimação.”
# Finalize com uma frase fora do laço, dizendo o que esses animais têm em comum.
# Esses animais são todos ótimos animais de estimação!

# cachorro, gato, coelho

animais = ['cachorro', 'gato', 'coelho']
for animal in animais:
    print(animal.title())
for animal in animais:
    print(f"Um {animal} seria um ótimo animal de estimação.")
print("Esses animais são todos ótimos animais de estimação!")