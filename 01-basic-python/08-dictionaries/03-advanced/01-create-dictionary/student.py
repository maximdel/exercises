# Write your code here
def create_dictionary(keys, values):
    dict = {}
    for i, j in zip(keys, values):
        dict[i] = j
    return dict