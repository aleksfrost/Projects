
def linear(my_list: list) -> list:
    another_list = []
    for num in my_list:
        if isinstance(num, list):
            another_list.extend(linear(num))
        else:
            another_list.append(num)
    return another_list


my_list = [3, [4], [5, [6, [7, 8]]]]
print(linear(my_list))


my_list = [10, 20, 30, 40, 50]

print(linear(my_list))