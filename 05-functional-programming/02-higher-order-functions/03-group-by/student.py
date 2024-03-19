def group_by(xs, key_function):
    dict = {}
    for x in xs:
        key = key_function(x)
        if key not in dict:
            dict[key] = []
        dict[key].append(x)
    return dict
