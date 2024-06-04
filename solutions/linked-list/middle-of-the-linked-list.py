

from typing import Optional

from data_structures.linked_list import LinkedList, ListNode

# TC : O(N), where N is the number of nodes in the list
# SC : O(1)


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


l = LinkedList([1, 2, 3, 4, 5])

s = Solution()
print(s.middleNode(l.head).val)
