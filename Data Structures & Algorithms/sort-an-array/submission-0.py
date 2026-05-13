class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(l: int, mid: int, r: int):
            lt = nums[l : mid+1]
            rt = nums[mid+1 : r+1]

            lp = 0
            rp = 0
            p = l

            while lp < len(lt) and rp < len(rt):
                if lt[lp] <= rt[rp]:
                    nums[p] = lt[lp]
                    lp += 1
                else:
                    nums[p] = rt[rp]
                    rp += 1
                
                p += 1
            
            # add all to lt
            while lp < len(lt):
                nums[p] = lt[lp]
                lp += 1
                p += 1

            # add all to rt
            while rp < len(rt):
                nums[p] = rt[rp]
                rp += 1
                p += 1

        
        def divideSort(lp: int, rp: int):
            if lp >= rp:
                return
            
            mid = (lp + rp) // 2

            divideSort(lp, mid)  # left half sort
            divideSort(mid + 1, rp)  # right half sort

            mergeSort(lp, mid, rp)
        
        divideSort(0, len(nums) - 1)
        
        return nums
