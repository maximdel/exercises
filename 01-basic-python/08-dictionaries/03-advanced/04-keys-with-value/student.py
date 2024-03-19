# Write your code here
def keys_with_value(dict, val):
    return [
        k
        for k, v in dict.items()
        if v == val
    ]