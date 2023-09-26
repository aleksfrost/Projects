def reverse(sequence):
    for member in sequence[::-1]:
        yield member


print(*reverse([1, 2, 3, 4, 5]))

generator = reverse('beegeek')

print(type(generator))
print(*generator)