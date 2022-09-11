from collections import Counter


int_list = [1,2,3,4,5,6,7,92,3,2,35,9,2,43,4,9,9,9]

def nth_most_rare(list_arr, n):
    list_arr = Counter(list_arr).items()
    

    for (k,v) in list_arr:
        if n == v:
            print(f'This number : {k} is the number {v} rarest in the item list')
        print(k,v)

    # complist = sorted([(k, v) for k,v in list_arr],reverse=True)[n-1][1]
    # return complist

nth_most_rare(int_list,2)