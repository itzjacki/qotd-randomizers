from random import shuffle

names = ["Hilde", "Ingvild", "Vegard", "Kjartan",
         "Sondre", "Sunniva", "Karl Yngve", "Ivar", "Robin"]
sorted_names = sorted(names)

# in reality this is O(N) less than the actual complexity, since it doesn't take shuffling into account
iterations = 0

while (names != sorted_names):
    candidate = names[0]
    shuffle(names)
    iterations += 1

print("The lucky winner after only", iterations,
      "iterations is:", candidate)
