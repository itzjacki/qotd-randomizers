import random
import math

names = ["Einar", "Ivar", "Robin", "Sunniva", "Karl Yngve"]

with open("image-as-seed/ToT-new.png", "rb") as logo:
  f = logo.read()
  b = bytearray(f)

random.seed(b)
lucky_winner = names[math.floor(random.random() * len(names))]
print(lucky_winner)
