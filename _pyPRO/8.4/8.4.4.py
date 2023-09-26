
def recursive_sum(my_list: list, res=0) -> int:
    for num in my_list:
        if isinstance(num, list):
            res += recursive_sum(num)
        else:
            res += num
    return res


my_list = [1, [4, 4], 2, [1, [2, 10]]]
print(recursive_sum(my_list))
my_list = []
print(recursive_sum(my_list))
