#Given a list of numbers, create a new list where each element is the sum of all elements from the original list up to that position.

numbers = [1, 2, 3, 4]
Sum = 0
sum_of_numbers = []

n = len(numbers)

for i in range(n):
  Sum += numbers[i] 
  sum_of_numbers.append(Sum)
print(sum_of_numbers)