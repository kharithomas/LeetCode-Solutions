# reverse singly linked list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        curr = self
        while curr is not None:
            print(curr.val)
            curr = curr.next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None

        while head is not None:
            next = head.next
            head.next = prev
            prev = head
            head = next

        return prev

# Linked List
n5 = ListNode(5)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

s = Solution()
n1.printList()
s.reverseList(n1)
n5.printList()