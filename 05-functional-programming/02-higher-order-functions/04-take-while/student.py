def take_while(xs, condition):
    list0 = []
    list1 = []
    for x in list(enumerate(xs)):
        if not condition(x[1]):
            list1 = xs[x[0]:]
            break
        else:
            list0.append(x[1])
    return (list0, list1)

'''
def take_while(xs, condition):
    list0 = []
    list1 = []
    for x in xs:
        if not condition(x):
            list1 = xs[xs.index(x):]
            break
        else:
            list0.append(x)
    return (list0, list1)
    '''