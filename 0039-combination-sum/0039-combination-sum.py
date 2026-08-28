class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []

        def backtrack(start, currArray, currSum):
            if currSum == target:
                output.append(currArray[:])
                return
            if currSum > target:
                return
            
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                currSum += candidate
                currArray.append(candidate)
                backtrack(i,currArray,currSum )
                currArray.pop()
                currSum-=candidate
        backtrack(0,[],0)
        return output