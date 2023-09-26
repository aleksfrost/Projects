def parse_ranges(ranges: str) -> None:
    rangs = (x for x in ranges.split(","))
    res = (x.split("-") for x in rangs)
    result = (list((k for k in range(int(x[0]), int(x[1])+1))) for x in res)
    resultt = (ark for arg in result for ark in arg)
    return resultt

""" return (j
            for i in ranges.split(',')
            for a, b in [i.split('-')]
            for j in range(int(a), int(b) + 1))"""



print(*parse_ranges('1-2,4-4,8-10'))


print(*parse_ranges('1-10,2-10'))