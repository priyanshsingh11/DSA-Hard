class Solution(object):
    def combinationSum2(self, candidates, target):
        result=[]
        candidates.sort()

        def backtrack(index,path,target):
            if target==0: 
                result.append(path[:])
                return


            if target<0: return 

            for i in range(index,len(candidates)):
                if i>index and candidates[i]==candidates[i-1]: continue #i>index checks whether the index is same or different

                path.append(candidates[i])
                backtrack(i+1,path,target-candidates[i]) #this is because we can not take the same valur again this make up to use the element same times
                path.pop()

        backtrack(0,[],target)
        return result
