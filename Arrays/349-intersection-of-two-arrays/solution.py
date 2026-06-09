class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
    
# # Example usage:
# solution = Solution()
# print(solution.intersection([1, 2, 2, 1], [2, 2]))  # Output: [2]
# print(solution.intersection([4,9,5], [9,4,9,8,4]))  # Output: [9, 4]