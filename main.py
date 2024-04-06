import math

numbers = [4, 9, 16, 25]
sqrt_map = map(math.sqrt, numbers)

print(list(sqrt_map))


names = []

while True:
    name = input("ingrese nombre (o 'q' para salir): ")
    if name == "q":
        break
    names.append(name)

vowels = ['a', 'e', 'i', 'o', 'u']
vowel_names = list(map(lambda name: ''.join([char for char in name if char.lower() in vowels]), names))

print(vowel_names)
lengths = list(map(len, vowel_names))
print(lengths)
