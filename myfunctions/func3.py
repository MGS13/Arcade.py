
def m_tester(input1,input2,input3):
  test1=10*10
  test2=5*5
  test3=7*7

  if input1==test1:
    print("Your first answer is correct, checking 2...")
    if input2==test2:
      print("Your second answer is correct, checking 3...")
      if input3==test3:
        print("You got all of them correct!")
    return True
  else:
    print("You are wrong")





