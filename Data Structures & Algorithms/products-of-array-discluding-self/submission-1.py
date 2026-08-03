class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [nums[0]]
        post = [nums[-1]] * len(nums)
        for i in range(1, len(nums)):
            pre.append(pre[i-1] * nums[i])
    
        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i+1] * nums[i]
        
        sol = []
        for i in range(len(nums)):
            pre_val = pre[i-1] if i-1 >= 0 else 1
            post_val = post[i+1] if i+1 < len(nums) else 1
            sol.append(pre_val * post_val)
        return sol
        
        