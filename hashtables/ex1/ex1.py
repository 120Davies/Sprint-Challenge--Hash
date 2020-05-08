import sys
sys.path.append('../')
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    hashtable = HashTable(16)

    # Iterate through weights
    for i, weight in enumerate(weights):
        diff = limit - weight

        # Check to see if weight remainder (diff) is in hashashtableable...
        if hash_table_retrieve(hashtable, diff) is not None:

            # ... if it is, return the location of the difference, and tuple of current index.
            return i, hash_table_retrieve(hashtable, diff)[1]

        # ... if it's not, store a new key:value pair of weight.
        hash_table_insert(hashtable, weight, (diff, i))

    #if no solution is found, return None
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
