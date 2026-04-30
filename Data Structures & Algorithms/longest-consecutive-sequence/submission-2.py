class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lst = list(set(nums))
        if not lst: return 0
        lst.sort()
        print(lst)
        max_con = 0
        con = 1
        for i in range(1, len(lst)):
            if lst[i] - 1 == lst[i-1]:
                con += 1
            else:
                max_con = max(max_con, con)
                con = 1
        max_con = max(max_con, con)
        return max_con