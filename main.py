from collections import Counter
from inspect import signature


int_list = [1,2,3,4,5,6,7,92,3,2,35,9,2,43,4,9,9,9]

def nth_most_rare(list_arr, n):
    list_arr = Counter(list_arr).items()
    
    # This loop below extracts the key as the item and the value as
    #  the number of times the item occurred 
    for (item,occurrance) in list_arr:
        if n == occurrance:
            nth_rarest = f' {item} is the number {n} rarest in the listed items'
            return print(nth_rarest)
        

    # complist = sorted([(k, v) for k,v in list_arr],reverse=True)[n-1][1]
    # return complist

# The signature function returns the arguments passed into the functions parameter
sign = signature(nth_most_rare)

nth_most_rare(int_list,3)
print(sign)