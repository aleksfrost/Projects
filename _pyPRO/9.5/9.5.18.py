def sourcetemplate(url):
    def query(**kwargs):
        if kwargs:
            s = []
            sort_s = sorted(kwargs.items())
            for tup in sort_s:
                s.append(f'{tup[0]}={tup[1]}')
            return url + '?' + '&'.join(s)
        else:
            return url
    return query



url = 'https://beegeek.ru'
load = sourcetemplate(url)
print(load(name='timur'))

url = 'https://stepik.org/lesson/651459/step/14'
load = sourcetemplate(url)
print(load(thread='solutions', unit=648165))

url = 'https://beegeek.ru'
load = sourcetemplate(url)
print(load())

url = 'https://all_for_comfort_life.com'
load = sourcetemplate(url)
print(load(smartphone='iPhone', notebook='huawei', sale=True))