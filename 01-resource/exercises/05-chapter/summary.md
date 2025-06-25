# Chapter 05 - If Statements

Claro! Segue o **resumo descritivo do Capítulo 5 – if Statements**, com exemplos em Python, explicações didáticas e, ao final, um comparativo com JavaScript/TypeScript para quem vem desse universo.

---

## Capítulo 5 – if Statements

A tomada de decisões é um dos pilares da programação. O capítulo 5 apresenta as **estruturas condicionais** do Python, permitindo que você controle o fluxo de execução do seu programa a partir de testes lógicos. O `if` é o principal mecanismo para avaliar condições e decidir que caminhos o código irá seguir.

### Condições e if simples

Em Python, usamos o `if` para verificar se uma expressão é verdadeira. Se for, o bloco indentado abaixo do `if` é executado. Por exemplo, imagine que você tenha uma lista de carros e queira destacar 'bmw' em maiúsculas e os demais apenas com a primeira letra maiúscula:

```python
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```

Nesse caso, o teste `car == 'bmw'` retorna `True` apenas para o valor 'bmw'. Para os demais, o `else` é executado. Esse padrão é muito comum em decisões binárias.

### Testes condicionais

Um **teste condicional** é uma expressão que retorna `True` ou `False`. Ele pode ser de igualdade (`==`), diferença (`!=`), maior/menor que (`>`, `<`), maior/menor ou igual (`>=`, `<=`), ou mesmo testar se um item está em uma lista (`in`, `not in`).

```python
car = 'bmw'
print(car == 'bmw')      # True
print(car == 'audi')     # False

age = 19
print(age < 21)          # True

requested_toppings = ['mushrooms', 'onions']
print('mushrooms' in requested_toppings)  # True
print('pepperoni' not in requested_toppings)  # True
```

#### Sensibilidade a maiúsculas/minúsculas

Em Python, comparações de strings são sensíveis a maiúsculas/minúsculas. Portanto, `'Audi' == 'audi'` retorna `False`. Para comparar ignorando o caso, use o método `.lower()`:

```python
car = 'Audi'
print(car.lower() == 'audi')  # True
```

### Testes com múltiplas condições (and, or)

É possível combinar condições usando `and` (E) e `or` (OU):

```python
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)  # False
print(age_0 >= 21 or age_1 >= 21)   # True
```

### Trabalhando com listas

Para saber se um valor está (ou não está) em uma lista, use `in` ou `not in`:

```python
fruits = ['apple', 'banana', 'orange']
if 'banana' in fruits:
    print("Tem banana na lista!")

if 'grape' not in fruits:
    print("Não tem uva na lista.")
```

### Expressões booleanas

Uma expressão booleana sempre resulta em `True` ou `False`. É possível criar variáveis booleanas explícitas:

```python
game_active = True
can_edit = False
```

### Estruturas condicionais completas

#### if simples

```python
age = 19
if age >= 18:
    print("Você pode votar!")
```

#### if-else

```python
age = 17
if age >= 18:
    print("Você pode votar!")
else:
    print("Você ainda não pode votar.")
```

#### if-elif-else

Quando há mais de duas possibilidades, usa-se `if`, `elif` e `else`. Por exemplo, para calcular o preço do ingresso baseado na idade:

```python
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"O valor do ingresso é R${price}.")
```

É possível usar vários `elif` e até omitir o `else` se quiser tratar todos os casos explicitamente:

```python
age = 70
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
```

### Checando múltiplas condições separadamente

Se precisar executar várias ações que podem ser verdadeiras ao mesmo tempo (exemplo: adicionar mais de um ingrediente), use `if` independentes e não `if-elif-else`, pois este último para no primeiro teste verdadeiro.

```python
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adicionando cogumelos.")
if 'pepperoni' in requested_toppings:
    print("Adicionando pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adicionando queijo extra.")

print("Pizza finalizada!")
```

### Condições em listas e checando listas vazias

Você pode usar o nome de uma lista diretamente numa condição. Uma lista vazia retorna `False`:

```python
requested_toppings = []
if requested_toppings:
    for topping in requested_toppings:
        print(f"Adicionando {topping}.")
    print("Pizza pronta!")
else:
    print("Você quer mesmo uma pizza sem nada?")
```

### Combinando listas e condições

É possível cruzar listas para garantir que só ingredientes disponíveis sejam adicionados:

```python
available_toppings = ['mushrooms', 'olives', 'pepperoni']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for topping in requested_toppings:
    if topping in available_toppings:
        print(f"Adicionando {topping}.")
    else:
        print(f"Desculpe, não temos {topping}.")
print("Pizza finalizada!")
```

---

## **Comparativo: Python x JavaScript/TypeScript em if Statements**

* **Sintaxe**: Ambos usam `if`, `else if` (em JS/TS) e `else`. No Python, não existe `else if`, mas sim `elif`.

  * Python:

    ```python
    if condicao:
        # ação
    elif outra_condicao:
        # outra ação
    else:
        # ação padrão
    ```
  * JavaScript:

    ```js
    if (condicao) {
      // ação
    } else if (outraCondicao) {
      // outra ação
    } else {
      // ação padrão
    }
    ```

* **Indentação**: Python depende da indentação para definir blocos de código. JS/TS usa `{}` (chaves) para isso.

* **Comparação de valores**:

  * Python usa `==` (igualdade) e `!=` (diferença). Para identidade de objetos, usa `is`.
  * JavaScript usa `==`, `===`, `!=`, `!==`. O triplo igual (`===`) compara valor e tipo.

* **Verificação de lista/vetor**:

  * Python: `'item' in lista`
  * JS/TS: `array.includes('item')`

* **Valores verdadeiros/falsos**:

  * Python: listas, strings e números vazios são avaliados como `False` em condições.
  * JS/TS: valores falsy incluem `null`, `undefined`, `''`, `0`, `NaN`, `false`.

* **Case sensitivity**:

  * Ambas as linguagens são case sensitive em strings.

* **Parênteses em condições**:

  * Python não exige parênteses na condição do `if`; em JS/TS são obrigatórios.

---

## **Resumo Final**

O capítulo mostrou como usar `if`, `elif` e `else` para controlar o fluxo do programa, realizar testes lógicos, combinar condições, comparar valores e trabalhar com listas em Python. Para quem vem do mundo JavaScript/TypeScript, a principal diferença está na sintaxe mais enxuta do Python (sem chaves, sem parênteses obrigatórios), no uso da indentação e na presença do `elif`. O funcionamento lógico, porém, é bastante parecido, facilitando a migração de conhecimento entre as duas linguagens.

