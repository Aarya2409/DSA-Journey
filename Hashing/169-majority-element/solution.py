class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        limit = len(nums) // 2

        for num, freq in count.items():
            if freq > limit:
                return num
            
print(Solution().majorityElement([2,2,1,1,1,2,2]))