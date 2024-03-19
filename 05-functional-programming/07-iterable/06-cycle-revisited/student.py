def cycle(xs):
    values = list(xs)
    while True:
        for item in values:
            yield item
