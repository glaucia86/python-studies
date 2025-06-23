
(print("=== Working with a list... ==="))
motorcycles = ['honda', 'yamaha', 'suzuki', 'kawasaki']
print(motorcycles)
print(motorcycles[0].title())

print()


# Accessing elements in a list
print("=== Accessing elements in a list... ===")
motorcycles[0] = 'ducati'
print(motorcycles)
print(motorcycles[0].title())

print()


# Add an element to the end of the list (append)
print("=== Adding an element to the end of the list... ===")
motorcycles.append('bmw')
print(motorcycles)

print()

# Add an element in the list (insert)
print("=== Adding an element in the list... ===")
motorcycles.insert(0, 'harley')
print(motorcycles[0].title())

print()

# Remove an element from the list (del)
print("=== Removing an element from the list... ===")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

print()

# Remove an element from the list (pop)
print("=== Removing an element from the list using pop()... ===")
motorcycles = ['honda', 'yamaha', 'ducati', 'bmw', 'suzuki']
print(motorcycles)

print()

# Pop an element from the list
print("=== Popping an element from the list... ===")
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle.title())
print(f"The last motorcycle I owned was a {popped_motorcycle.title()}.")

print()


# Show an element from the list (pop)
print("=== Popping an element from the list by index... ===")
motorcycles = ['honda', 'yamaha', 'ducati', 'bmw', 'suzuki']
first_owned = motorcycles.pop(0)
print(motorcycles)
print(f"My first motorcycle was a {first_owned.title()}.")

print()


# Remove an element from the list (remove)
print("=== Removing an element from the list using remove()... ===")
motorcycles = ['honda', 'yamaha', 'ducati', 'bmw', 'suzuki']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

print()

