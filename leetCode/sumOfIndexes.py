def sumOfIndexes(self, nums: list[int], target: int) -> list[int]:
        output, i, j = [], 0, 1
        while True:
            if i != j:
                if nums[i] + nums[j] == target:
                    output.extend([i,j])
                    return output
            j = j + 1
            if j == len(nums): 
                i = i + 1
                j = i + 1
            if j >= len(nums): return output
            
            
# when test case too big
def twoSum(self, nums: list[int], target: int) -> list[int]:
        output, i, j = [], 0, 1
        while True:
            if i != j:
                if nums[i] + nums[j] == target:
                    output.extend([i,j])
                    return output
                if len(nums) > 40:
                    if nums[len(nums) - (i + 1)] + nums[len(nums)-(j + 1)] == target:
                        output.extend([len(nums) - (i+1),len(nums) - (j+1)])
                        return output
            j = j + 1
            if j == len(nums): 
                i = i + 1
                j = i + 1
            if j >= len(nums): return output
