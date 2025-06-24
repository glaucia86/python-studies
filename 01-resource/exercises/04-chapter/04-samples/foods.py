# Pegue qualquer versão do programa das comidas favoritas (foods.py) e escreva 
# dois laços for para imprimir cada item das duas listas (a original e a cópia).

pizzas = ['calabresa', 'quatro queijos', 'camarão']
friend_pizzas = pizzas[:]

pizzas.append('pepperoni')
friend_pizzas.append('mussarela')

print("Minhas pizzas favoritas são:")
for pizza in pizzas:
    print(pizza.title())

print("\nAs pizzas favoritas do meu amigo são:")
for pizza in friend_pizzas:
    print(pizza.title())
