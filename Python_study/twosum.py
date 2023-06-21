class solution():
    def twosum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target==(nums[i]+nums[j]):
                    print([i,j])
                    return [i,j]
                    



a=solution()
a.twosum([3,5,2],5)