nums = [1, 5, 3, 7, 4]
target = 8


def TwoSum(nums, target):
    for i in range (len(nums)):
        for j in range(i + 1, len(nums)):
            soma = nums[i] + nums[j]
            if soma == target:
                return [i, j]