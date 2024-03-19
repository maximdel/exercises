# Write your code here
def odd_keys_dict(dict):
    result = {}
    for i, j in dict.items():
        if i % 2 != 0:
            result[i] = j
    return result
