def custom_sort(ord_dict, by_values=False):
    if not by_values:
        for key in sorted(ord_dict):
            ord_dict.move_to_end(key)
    else:
        temp = sorted(ord_dict.values())
        for value in temp:
            for key in ord_dict.keys():
                if ord_dict[key] == value:
                    ord_dict.move_to_end(key)
                    break

