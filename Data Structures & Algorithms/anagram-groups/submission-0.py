class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)

        for s in strs:
            answer["".join(sorted(s))].append(s)
        
        print(answer)
        return list(answer.values())
