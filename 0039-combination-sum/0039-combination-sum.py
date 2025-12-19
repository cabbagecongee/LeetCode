class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        solutions = []
        n = len(candidates)

        def search(idx, sol, curr_total):
            if curr_total == target: #base case
                solutions.append(sol[:])
                return
            
            if idx > n or curr_total > target:
                return
                
            for i in range(idx, n): #go through all choices
                if curr_total + candidates[i] <= target: #check if valid choice
                    #apply choice
                    sol.append(candidates[i])
                    search(i, sol, curr_total + candidates[i]) #recurse
                    #undo choice
                    sol.pop()

        search(0, [], 0)
        return solutions


                
            
        