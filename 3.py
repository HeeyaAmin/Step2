def subsetXORSum(nums):
    def backtrack(index, subset_xor):
        nonlocal total_xor
        total_xor += subset_xor

        for i in range(index, len(nums)):
            backtrack(i + 1, subset_xor ^ nums[i])

    total_xor = 0
    backtrack(0, 0)
    return total_xor

# Test the function
nums_length = int(input("Enetr the number of elements in nums array: "))
nums = []
for _ in range(nums_length):
    element = int(input("Enter a number: "))
    nums.append(element)

xor_sum = subsetXORSum(nums)
print("Sum of XOR totals for every subset:", xor_sum)
