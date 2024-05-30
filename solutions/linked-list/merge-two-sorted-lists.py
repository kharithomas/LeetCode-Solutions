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

m1 = s.mergeTwoLists(LinkedList([1, 2, 4]).head, LinkedList([1, 3, 4]).head)
print_list(m1)

m2 = s.mergeTwoLists(LinkedList([]).head, LinkedList([]).head)
print_list(m2)

m3 = s.mergeTwoLists(LinkedList([]).head, LinkedList([0]).head)
print_list(m3)
