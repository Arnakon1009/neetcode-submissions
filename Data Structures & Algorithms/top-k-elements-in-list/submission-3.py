class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        f = Counter(nums)
        s = []
        # Sort the items by frequency in descending order
        sorted_items = sorted(f.items(), key=lambda x: x[1], reverse=True)
        for i,v in sorted_items:
            s.append(i)
            if len(s) == k:
                return s