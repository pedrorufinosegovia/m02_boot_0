def maxi(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for ix in range (1, len(l)):
        if l[ix] > m:
            m = l[ix]
    return m

def mini(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for ix in range (1, len(l)):
        if l[ix] < m:
            m = l[ix]
    return m

def media(*l):
    if len(l) == 0:
        return 0
    sumas = 0
    for valor in l:
        sumas += valor
    return (sumas / len(l))

print(media(4, 999, 6, 23, 4, 5))