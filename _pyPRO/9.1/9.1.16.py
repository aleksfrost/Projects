import string

to_sort = input()
upper = [s for s in to_sort if s in string.ascii_uppercase]
lower = [s for s in to_sort if s in string.ascii_lowercase]
even = [s for s in to_sort if s in string.digits and int(s) % 2 == 0]
odd = [s for s in to_sort if s in string.digits and int(s) % 2 != 0]


print("".join(sorted(lower)) + "".join(sorted(upper)) + "".join(sorted(odd)) + "".join(sorted(even)))



"""
Sorting1234

n0tEast3rEgg

3DYrz34UXl
"""