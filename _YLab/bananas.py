import re

seq = {'b-anana--': 'b.anana..',
       'b-anan--a': 'b.anan..a',
       'b-ana--na': 'b.ana..na',
       'b-an--ana': 'b.an..ana',
       'b-a--nana': 'b.a..nana',
       'b---anana': 'b...anana',
       '-banana--': '.banana..',
       '-banan--a': '.banan..a',
       '-bana--na': '.bana..na',
       '-ban--ana': '.ban..ana',
       '-ba--nana': '.ba..nana',
       '-b--anana': '.b..anana'
       }


def bananas(s) -> set:
    result = set()
    if s == 'banana':
        result.add(s)
        return result
    else:
        for key in seq:
            if re.search(seq[key], s):
                result.add(key)
#        print(result)
    return result

'''
assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}

print(seq)
'''

print(bananas("banann"))
print(bananas("banana"))
print(bananas("bbananana"))
print(bananas("bananaaa"))
print(bananas("bananana"))