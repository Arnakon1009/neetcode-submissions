class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        f = Counter(nums)
        for i in f.values():
            if i > 1:
                return True
        return False