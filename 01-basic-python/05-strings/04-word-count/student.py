# Write your code here
def word_count(string):
    count = 0
    if string == "":
        return count
    for i in string:
        if i == " ":
            count += 1
    return count+ 1