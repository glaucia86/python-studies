# Um restaurante oferece apenas cinco tipos de comida.
# Armazene os nomes desses pratos em uma tupla.
# Use um laço para imprimir cada comida.
# Tente alterar um dos itens da tupla e veja que o Python rejeita a mudança.
# O restaurante muda o cardápio: sobrescreva a tupla com dois pratos diferentes e 
# imprima o novo cardápio.

buffet = ('sushi', 'lasanha', 'hambúrguer', 'tacos', 'salada')

print("=== Pratos disponíveis no buffet: ===")
for comida in buffet:
    print(comida.title())

# buffet[0] = 'pizza'  # Isso causará um erro, pois tuplas são imutáveis.

buffet = ('pizza', 'risoto', 'frutos do mar', 'torta de limão', 'sopa de cebola')
print("\n=== Novo cardápio do buffet: ===")
for comida in buffet:
    print(comida.title())