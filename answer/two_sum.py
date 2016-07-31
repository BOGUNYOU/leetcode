class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = []
        for i in range(nums.__len__()):
            for j in range(i+1,nums.__len__()):
                if nums[i]+nums[j] == target:
                    a.append(i)
                    a.append(j)
                    return a
                    break
