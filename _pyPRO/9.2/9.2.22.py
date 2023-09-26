funk = input()
a, b = [int(i) for i in input().split(" ")]

res = [eval(funk) for x in range(a, b + 1)]
print(f"Минимальное значение функции {funk} на отрезке [{a}; {b}] равно {min(res)}")
print(f"Максимальное значение функции {funk} на отрезке [{a}; {b}] равно {max(res)}")
