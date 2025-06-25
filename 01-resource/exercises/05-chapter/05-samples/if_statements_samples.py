# # Exemplo de uso de if, elif e else em Python

1
print("Exemplo de uso de if, elif e else em Python")
cars = ['ford', 'chevrolet', 'fiat']

for car in cars: 
    if car == 'ford':
        print(car.upper())
    else:
        print(car.title())
        
print()
        
# Testes Condicionais
print("\nTestes Condicionais")
car = 'bmw'
print(car == 'bmw')  # True
print(car == 'audi')  # False

print()

age = 19
print(age >= 18)

print()

requested_toppings = ['cogumelos', 'cebola']
print('cogumelos' in requested_toppings)
print('pepperoni' not in requested_toppings)

print()

# Método .lower()
print("\nMétodo .lower()")

car = 'Ford'
print(car.lower() == 'ford')  # True
print(car == 'audi')  # False

print()

# Testes com múltiplas condições (and, or)
print("\nTestes com múltiplas condições (and, or)")
age_0 = 22
age_1 = 18

print(age_0 >= 21 and age_1 >= 21)  # False
print(age_0 >= 21 or age_1 >= 21)   # True

print()

# Trabalhando com listas (in, not in)
print("\nTrabalhando com listas (in, not in)")

frutas = ['maçã', 'banana', 'laranja']
if 'banana' in frutas:
    print("Banana está na lista de frutas.")
if 'uva' not in frutas:
    print("Uva não está na lista de frutas.")

print()

# Expressões booleanas
print("\nExpressões booleanas")
game_active = True
can_edit = False

print()

# Estrutura condicionais completas
print("\nEstrutura condicionais completas")
age = 19
if age >= 18:
    print("Você pode votar!")
    
print()

# if-else
print("\nExemplo: if-else")

age = 17
if age >= 18:
    print("Você pode votar!")
else:
    print("Você não pode votar ainda.")

print()

# if-elif-else
print("\nExemplo: if-elif-else")

age = 12
if age < 4:
    price = 0
    print("Entrada gratuita!")
elif age < 18:
    price = 25
    print("Entrada com desconto!")
else:
    price = 40
    print("Entrada normal!")

print(f"O valor do ingresso é R$ {price}.")

# Verificando múltiplas condições
print("\nExemplo: Verificando múltiplas condições")

requested_toppings = ['cogumelos', 'pepperoni', 'extra queijo']
if 'cogumelos' in requested_toppings:
    print("Adicionando cogumelos.")
if 'pepperoni' in requested_toppings:
    print("Adicionando pepperoni.")
if 'extra queijo' in requested_toppings:
    print("Adicionando extra queijo.")
    
print("Pizza preparada com os ingredientes solicitados!")

# Verificando se a lista está vazia
print("\nExemplo: Verificando se a lista está vazia")

requested_toppings = []
if requested_toppings:
    for topping in requested_toppings:
        print(f"Adicionando {topping}.")
    print("Pizza preparada com os ingredientes solicitados!")
else:
    print("Você não pediu nenhum ingrediente. Pizza simples preparada!")

# Combinando listas e condições
print("\nExemplo: Combinando listas e condições")

available_toppings = ['pepperoni', 'mushrooms', 'green peppers', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for topping in requested_toppings:
    if topping in available_toppings:
        print(f"Adicionando {topping}.")
    else:
        print(f"Desculpe, não podemos adicionar {topping}.")
print("Pizza preparada com os ingredientes solicitados!")