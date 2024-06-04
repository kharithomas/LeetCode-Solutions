from typing import List, Optional


class ListNode:
    """A single node of a LinkedList"""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, nums: Optional[List[int]] = None):
        self.head = None
        if nums:
            dummy = ListNode()
            curr = dummy
            for n in nums:
                curr.next = ListNode(n)
                curr = curr.next
            self.head = dummy.next


def print_list(head: Optional[ListNode]):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
