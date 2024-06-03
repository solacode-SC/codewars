
# def accum(s):
#     return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


def accum(st):
    returnedSt = ""
    i = 0
    while i < len(st):
        j = 0
        num = i + 1
        while (j < num):
            if (j == 0):
                returnedSt += st[i].upper()
            else:
                returnedSt += st[i].lower()
            j+=1
        if (i != len(st) -1):
            returnedSt += "-"
        i+=1
    return returnedSt

print(accum("ZpglnRxqenU"))