class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer_dict = {}  # {v: i} for index

        for i, v in enumerate(nums):
            diff = target - v

            if diff in answer_dict:
                return [answer_dict[diff], i]

            answer_dict[v] = i