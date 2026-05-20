class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        lt, mid, rt = 0, 0, len(nums) - 1

        while mid <= rt:
            if nums[mid] == 0:
                nums[lt], nums[mid] = nums[mid], nums[lt]
                lt += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2:
                nums[mid], nums[rt] = nums[rt], nums[mid]
                rt -= 1
        
        