# Write your code here
def drop_nth(xs, n):
    list = xs[:n] + xs[n+1:]
    return list