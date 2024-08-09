from typing import Optional
from helpers.linked_list import ListNode, print_list

# TC: O(max(m,n))
# SC: O(1), extra-space


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode()
        carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            carry = total // 10
            remainder = total % 10
            curr.next = ListNode(remainder)
            curr = curr.next

        return dummy.next


s = Solution()

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

print_list(s.addTwoNumbers(l1, l2))

l1 = ListNode(0)
l2 = ListNode(0)

print_list(s.addTwoNumbers(l1, l2))

l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)

print_list(s.addTwoNumbers(l1, l2))
