
import sys
sys.path.append("../")
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = {}
    route = [None] * length

    #iterate thru the tickets
    for ticket in tickets:
        #insert each ticket into the hashtable, key = source, value = destination
        hashtable[ticket.source] = ticket.destination

    current = hashtable["NONE"] #start where source = NONE
    #assign the first destination to variable
    i = 0

    #iterate until we reach the final destination of 'NONE'
    while current != "NONE":
        route[i] = current
        current = hashtable[current]
        i += 1
    route[i] = "NONE"

    #return the list of destinations
    return route
