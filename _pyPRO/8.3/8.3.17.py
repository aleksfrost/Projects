def alg(num):
    if num > 0:
        print(num)
        alg(num-5)
        print(num)
    else:
        print(num)


alg(int(input()))
