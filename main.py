#import random
import sys
sys.path.append('/myfunctions/func1.py')
sys.path.append('/myfunctions/func2.py')
sys.path.append('/myfunctions/func3.py')
sys.path.append('/myfunctions/func4.py')
from myfunctions.func1 import coin_flipper
from myfunctions.func2 import guess_num
from myfunctions.func3 import m_tester
from myfunctions.func4 import word_guess
import os, time
clear=lambda: os.system('clear')
score=0
while True:
  
  print("Welcome to Game Master 4")
  print("=============================")
  print("=============================")
  print("Games:\n1. Coin Flipper\n2. Guess the Number between 1-10\n3.Multiplication Tester\n4.Guess the word")
  answer=int(input("Which game do you want to play? (1/2/3/4): "))
  if answer==1:
    print("Let's play Coin Flipper!")
  
    guess = int(input("please put 0 or 1 " ))
    if coin_flipper(guess):
      score+=1
    
    else:
      score-=1
    print(score)
  elif answer==2:
    print("Let's play Guess the Number!")
    guessn = int(input("guess the number! "))  
    if guess_num(guessn):
      score+=1
    else:
      score-=1
  elif answer==3:
    print("Let's play Multiplication Tester!")
    mguess1=int(input("What is 10 * 10? "))
    mguess2=int(input("What is 5 * 5? "))
    mguess3=int(input("What is 7*7? "))
    if m_tester(mguess1, mguess2, mguess3):
      score+=1
      time.sleep(2)
    else:
      score-=1
  elif answer==4:
    print("Let's play Guess the word!")
    if word_guess():
      print("Correct!")
      score+=1
    else:
      score-=1
      print("Incorrect!\n")
  print("Your score is: ", score)
  time.sleep(5)
  clear()
  
