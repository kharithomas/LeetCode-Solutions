from typing import List, Optional

from helpers.linked_list import ListNode, LinkedList, print_list

# TC : O(N*logK), where N is the total number of nodes and K is the number of lists
# SC : O(1)


class Solution:
    def merge2Lists(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        head = curr = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l1
                l1 = curr.next.next

            curr = curr.next

        curr.next = l1 or l2

        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        amount = len(lists)
        interval = 1

        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0] if amount > 0 else None


s = Solution()

lists = [
    LinkedList([1, 4, 5]).head,
    LinkedList([1, 3, 4]).head,
    LinkedList([2, 6]).head,
]

print_list(s.mergeKLists(lists))
