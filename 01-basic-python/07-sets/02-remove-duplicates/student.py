# Write your code here
def remove_duplicates(xs):
    dupes = set()
    result = []
    
    for i in xs:
        if i not in dupes:
            result.append(i)
            dupes.add(i)

    return result