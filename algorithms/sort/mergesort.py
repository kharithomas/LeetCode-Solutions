from typing import List


class MergeSort:
    def merge(self, a: List[int], b: List[int]) -> List[int]:
        c = []
        i, j = 0, 0

        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1

        # Add remaining elements from a
        while i < len(a):
            c.append(a[i])
            i += 1

        # Add remaining elements from b
        while j < len(b):
            c.append(b[j])
            j += 1

        return c

    def sort(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # base case
        if n <= 1:
            return nums

        # split arr into halves
        mid = n // 2
        left, right = nums[:mid], nums[mid:]

        return self.merge(self.sort(left), self.sort(right))


ms = MergeSort()

print(ms.sort([5, 4, 3, 2, 1]))
print(ms.sort([54, 26, 93, 17, 77, 20]))
