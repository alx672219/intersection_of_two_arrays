from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): 
            return self.intersect(nums2, nums1)
        
        cnt = Counter(nums1)
        ans = []
        for x in nums2:
            if cnt[x] > 0:
                ans.append(x)
                cnt[x] -= 1
        return ans

# >>> Counter("mississippi")
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# Using HashMap to store occurrences of elements in the nums1 array.
# Iterate x in nums2 array, check if cnt[x] > 0 then append x to our answer and decrease cnt[x] by one.
# To optimize the space, we ensure len(nums1) <= len(nums2) by swapping nums1 with nums2 if len(nums1) > len(nums2).