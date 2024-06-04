from helpers.linked_list import ListNode, LinkedList, print_list


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


l = LinkedList([1, 2, 3, 4, 5])
print_list(l.head)

s = Solution()
reversed_list = s.reverseListIteratively(l.head)
# reversed_list = s.reverseListRecursively(l.head)

print_list(reversed_list)
