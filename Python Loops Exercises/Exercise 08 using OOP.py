#Given a list of numbers, use a loop to count how many times a specific number (e.g., 10) appears.

list1 = [10, 20, 10, 30, 10, 40, 50]
target = 10

class counter:
  def __init__(self, target):
    self.target = target

  def count_target(self):
    count = 0
    for i in list1:
      if i == self.target:
        count += 1
    print(f'{self.target} appears {count} times.')

counter1 = counter(target)
counter1.count_target()