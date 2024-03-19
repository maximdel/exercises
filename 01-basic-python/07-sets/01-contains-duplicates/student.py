# Write your code here
def contains_duplicates(xs):
    ys = set(xs)
    return len(ys) != len(xs)