def indices_of(xs, condition):
    values = []
    for x in range(len(xs)):
        if condition(xs[x]):
            values.append(x)
    return values

