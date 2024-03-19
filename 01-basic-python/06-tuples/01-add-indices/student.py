# Write your code here
def add_indices(xs):
    ind = [i for i in range(len(xs))]
    return list(zip(ind, xs))