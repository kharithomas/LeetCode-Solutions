# TC: O(n)
# SC: O(n)

class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        n = len(hamsters)
        buckets = set()

        for i in range(n):
            # Skip food locations
            if hamsters[i] == '.':
                continue

            # If the hamster has already been fed from left
            if i > 0 and (i - 1) in buckets:
                continue

            # Try to place a bucket on the right side
            if i < (n - 1) and hamsters[i + 1] == '.':
                buckets.add(i + 1)

            # If not possible, try to place it on the left side
            elif i > 0 and hamsters[i - 1] == '.':
                buckets.add(i - 1)

            # If no place to put a bucket, return -1
            else:
                return -1

        return len(buckets)


s = Solution()

print(s.minimumBuckets("H..H"))
print(s.minimumBuckets(".H.H."))
print(s.minimumBuckets(".HHH."))
print(s.minimumBuckets("H"))
