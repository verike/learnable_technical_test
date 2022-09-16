from collections import Counter
from inspect import signature
from ast import List


int_list = [1,2,3,4,5,6,7,92,3,2,35,9,2,43,4,9,9,9]

def nth_most_rare_signature(list:List, n:int):
    list_arr = Counter(list).items()
    
    # This loop below extracts the item and number of times the item occurred 
    for (item,occurrance) in list_arr:
        if n == occurrance:
            nth_rarest = f' {item} is the number {n} rarest in the listed items'
            return print(nth_rarest)
        



# The signature function is assigned to a variable and
#  returns the arguments passed into the functions parameter
sign_of_Func = signature(nth_most_rare_signature)
para_1_sign = sign_of_Func.parameters['list'].annotation
para_2_sign = sign_of_Func.parameters['n'].annotation

# calling the function
nth_most_rare_signature(int_list,2)


# reveals the properties of the function wrapped inside the signature function 
print(f'Signature of function: {sign_of_Func}')
print(f'Signature of parameter "list" passed into the function: {para_1_sign}')
print(f'Signature of parameter "list" passed into the function: {para_2_sign}')