import random
import math

names = ["Einar", "Hilde", "Robin", "Sunniva"]

with open("image-as-seed/ToT.png", "rb") as logo:
  f = logo.read()
  b = bytearray(f)

random.seed(b)
lucky_winner = names[math.floor(random.random() * len(names))]
print(lucky_winner)
