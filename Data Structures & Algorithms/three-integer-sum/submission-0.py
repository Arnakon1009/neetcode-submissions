class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        nums.sort()
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            result = nums[i]
            if result > 0 :return res
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if result + nums[l] + nums[r] > 0:
                    r -= 1
                elif result + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([result, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return res