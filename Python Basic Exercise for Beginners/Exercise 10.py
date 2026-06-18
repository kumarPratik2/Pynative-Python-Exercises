#Given a list of integers, find and print both the largest and the smallest numbers.

nums = [45, 2, 89, 12, 7]
largest = nums[0]
smallest = nums[0]
for x in nums:
    if x > largest:
        largest = x
print(f'largest = {largest}')
for x in nums:
    if x < smallest:
        smallest = x
print(f'smallest = {smallest}')