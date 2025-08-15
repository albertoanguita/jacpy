

def print_formatted_list(l: list, sep = ', ', init = '[', end = ']', printer = None) -> str:
    printer = _init_printer(printer)
    res = init

    for e in l[:-1]:
        res += printer(e)
        res += sep

    if l:
        e = l[-1]
        res += printer(e)

    res += end
    return res


def print_formatted_dict(d: dict, sep = ', ', div = ' => ', init = '{', end = '}', key_printer = None, value_printer = None) -> str:
    key_printer = _init_printer(key_printer)
    value_printer = _init_printer(value_printer)
    res = init

    items = list(d.items())
    for k, v in items[:-1]:
        res += key_printer(k)
        res += div
        res += value_printer(v)
        res += sep

    if items:
        k, v = items[-1]
        res += key_printer(k)
        res += div
        res += value_printer(v)

    res += end
    return res

def _init_printer(printer):
    if printer is None:
        return str
    return printer