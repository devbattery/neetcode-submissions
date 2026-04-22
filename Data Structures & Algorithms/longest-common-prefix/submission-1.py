class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ''

        for i in range(len(strs[0])):
            judg = strs[0][i]

            for s in strs:
                if i == len(s) or judg != s[i]:
                    return answer
            
            answer += judg
        
        return answer
