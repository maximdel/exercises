# Write your code here
def penultimate(xs):
    if len(xs) < 2:
        return xs[-1]
    return xs[-2]