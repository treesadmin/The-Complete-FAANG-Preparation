
# Contributed by Paraj Shah
# https://github.com/parajshah

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(head, data):
    if head is None:
        return SinglyLinkedListNode(data)
    newNode = SinglyLinkedListNode(data)
    newNode.next = head
    head = newNode
    return head
    

if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist_head = insertNodeAtHead(llist.head, llist_item)
            llist.head = llist_head

        print_singly_linked_list(llist.head, '\n', fptr)
        fptr.write('\n')
