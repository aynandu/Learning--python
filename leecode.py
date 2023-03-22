class Solution:
   def twoSum(self, nums, target):
    for i in range(len(nums)):
       for j in range(i+1,len(nums)):
        sum_total = nums[i]+nums[j]
        if sum_total == target:
           return [i,j]


nums=[2,7,11,15]
target=9
count = Solution()
count.twoSum(nums,target)
print(count())