class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt_dict = collections.Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]  # 0 to len(nums)

        for num, freq in cnt_dict.items():
            buckets[freq].append(num)
        
        answer = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                answer.append(num)

                if k == len(answer):
                    return answer
