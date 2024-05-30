from typing import Optional

from helpers.linked_list import LinkedList, ListNode, print_list


# TC : O(N+M)
# SC : O(1)


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy

        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next

            temp = temp.next

        # if any list has nodes left over
        temp.next = list1 or list2

        return dummy.next


s = Solution()

l1, l2 = LinkedList([1, 2, 4]), LinkedList([1, 3, 4])
m1 = s.mergeTwoLists(l1.head, l2.head)
print_list(m1)

l3, l4 = LinkedList([]), LinkedList([])
m2 = s.mergeTwoLists(l3.head, l4.head)
print_list(m2)

l5, l6 = LinkedList([]), LinkedList([0])
m3 = s.mergeTwoLists(l5.head, l6.head)
print_list(m3)
