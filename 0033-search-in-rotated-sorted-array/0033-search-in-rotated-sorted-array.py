class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def iforgotsearchname(arr):
            '''
            So we split into two, we have right, left and middle.
            '''
            left, right = 0, len(arr)-1
            while left <= right:
                mid = (left+right)//2
                if arr[mid] == target:
                    return mid
                if arr[mid] >= arr[right]: #left side sorted, right side not
                    if arr[left] <= target <= arr[mid]:
                        right = mid -1
                    else:
                        left = mid + 1
                else: #right side sorted
                    if arr[mid] <= target <= arr[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
            
            return -1
        
        return iforgotsearchname(nums)
                    
        