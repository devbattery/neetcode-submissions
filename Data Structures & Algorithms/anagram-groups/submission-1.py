class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)

        for s in strs:
            cnt = [0] * 26  # a to z

            for c in s:
                cnt[ord(c) - ord('a')] += 1  # a: 0, b: 1, ...
            
            answer[tuple(cnt)].append(s)  # key of defaultdict(list) can't be list
        
        return list(answer.values())


