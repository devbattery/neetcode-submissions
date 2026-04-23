class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        answer_dict = defaultdict(int)

        for num in nums:
            answer_dict[num] += 1
        
        return max(answer_dict, key=answer_dict.get)
