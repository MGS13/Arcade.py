import random

def coin_flipper(guess):
  correct=random.getrandbits(1)
  if guess==correct:
    print("You are correct!", str(correct))
    return True
  else:
    print("You're wrong!", str(correct), "is the answer")
    return False

