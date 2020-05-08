import sys
sys.path.append("../")
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

# Building a dictionary works better.
def intersection(arrays):

    hashtable = {}

    for a in arrays:
        for i in a:
            if hashtable.get(i, None) is None:
                hashtable[i] = 0
            hashtable[i] += 1

    result = [i for i, n in hashtable.items() if n == len(arrays)]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])
    
    print(intersection(arrays))
