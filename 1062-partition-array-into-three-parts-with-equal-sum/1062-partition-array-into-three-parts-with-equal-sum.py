class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if sum(arr)%3 != 0:
            return False
        
        target = sum(arr)/3
        running_sum, parts_found = 0, 0
        for i in range(len(arr)):
            running_sum+=arr[i]
            if running_sum == target and parts_found == 0:
                running_sum = 0
                parts_found +=1
            elif running_sum == target and parts_found == 1 and i < len(arr)-1:
                return True
        return False