def power(degree):
    def square(x):
        return x**degree
    return square


result = power(4)(2)
print(result)