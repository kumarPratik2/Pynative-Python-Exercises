#Given a list and an integer k, rotate the list to the left by k positions. For example, if k=2, the first two elements move to the end of the list.

nums = [1, 2, 3, 4, 5]
k = 2
new = []

for _ in range(k):
  x = nums.pop(0)
  nums.append(x)
  print(nums)