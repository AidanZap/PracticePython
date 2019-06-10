#Exercise14
    #Create a function that takes a list and returns a list with no duplicates

def remove_duplicates(OGlist):
    OGlist = set(OGlist)
    return list(OGlist)

a = [1,2,3,4,5,4,3,2,1,]
b = remove_duplicates(a)

print(a)
print(b)