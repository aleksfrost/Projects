

def reverse():
    temp = int(input())
    if temp != 0:
        reverse()
    print(temp)


reverse()
