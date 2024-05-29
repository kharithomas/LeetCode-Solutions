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
# SC : O(1) or O(N) for recursive solution


class Solution:
    def reverseListIteratively(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

    def reverseListRecursively(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        new_head = self.reverseListRecursively(head.next)
        head.next.next = head  # head is actually the curr node
        head.next = None

        return new_head


n5 = ListNode(5)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

s = Solution()
n1.printList()
s.reverseListIteratively(n1)
# s.reverseListRecursively(n1)
n5.printList()
