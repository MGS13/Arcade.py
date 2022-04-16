import random

def guess_num(guessn):
  correct=random.randint(1,11)
  
  if guessn == correct:
    print("You are correct!", str(guessn))  
    return True
  else:
    print("You are wrong!", str(correct), "was the correct number!")
    return False


