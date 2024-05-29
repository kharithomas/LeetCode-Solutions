class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        res = []

        curr = self
        while curr is not None:
            res.append(str(curr.val))
            curr = curr.next

        print(', '.join(res))

# Note: Above code is not part of solution

# TC : O(N)
# SC : O(1)


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev


n5 = ListNode(5)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

s = Solution()
n1.printList()
s.reverseList(n1)
n5.printList()
