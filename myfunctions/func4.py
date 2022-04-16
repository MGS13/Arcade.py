from random import randrange

def word_guess():
  g_list= ["dog", "cat", "tree", "pen", "mouse","house"]
  guess=int(randrange(0, len(g_list)))

  for word in g_list:
    print(word, end="\n")
  print("\n")

  inpt=input("Guess the word!").lower()
  print("The word was " + g_list[guess])

  return inpt==g_list[guess]
  