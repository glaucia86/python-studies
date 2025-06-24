# Pense em pelo menos três tipos de pizza que você gosta. 
# Armazene esses nomes em uma lista chamada pizzas. Depois, use um laço for para imprimir o nome de cada pizza.
# Em seguida, modifique o laço para imprimir uma frase usando o nome de cada pizza, como por exemplo: “Eu gosto de pizza de pepperoni.”
# Por fim, adicione uma linha fora do laço, dizendo o quanto você gosta de pizza.

# calabresa, quatro queijos, camarão

pizzas = ['calabresa', 'quatro queijos', 'camarão']
for pizza in pizzas:
    print(pizza.title())
for pizza in pizzas:
    print(f"Eu gosto muito de pizza de {pizza.title()}!")
print("Eu gosto de pizza de um modo geral, mas essas são as minhas favoritas!")