from random import shuffle

# Names are duplicated since O(6!) is no match for my microwave, let alone my M1 Mac. O(11!) is more fun.
names = ["Hilde_1", "Ivar_1", "Karl Yngve_1", "Robin_1", "Sunniva_1", "Hilde_2", "Ivar_2", "Karl Yngve_2", "Robin_2", "Sunniva_2"]
sorted_names = sorted(names)

iterations = 0 # in reality this is O(N) less than the actual complexity, since it doesn't take shuffling into account

while (names != sorted_names):
  candidate = names[0]
  shuffle(names)
  iterations += 1

print("The lucky winner after only", iterations, "iterations is:", candidate[0:-2])