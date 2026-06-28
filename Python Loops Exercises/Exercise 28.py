#Given a dictionary of student scores, create a new dictionary that only includes students who scored above a certain threshold (e.g., 75).

scores = {"Alice": 85, "Bob": 70, "Charlie": 95, "David": 60}

new = {}
for i in scores:
  if scores[i] >= 75:
    new.update({i:scores[i]})
print(new)