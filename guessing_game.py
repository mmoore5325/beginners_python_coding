import random

secret_num =random.randint(1, 30)

def welcome(number):
  print("Welcome to the guessing game.  You have {} guesses.  If you win, you live!.".format(number))
  main(0)

def main(number):
    try:
      guess = int(input("Guess a number between 1 and 30: "))
    except ValueError:
      print("You fool...you wasted a guess...not good for you...")
      guess_counting(number)
    else:
      if int(guess) == int(secret_num):
        number += 1
        print("""You got it!  The number was {}!
        Bad news though...the real prize was you get shot as many guesses as it took.
        Only 6 rounds in the gun, which is why you only got 6 guesses, so you might make it...
        How many bullets do you think you can take to the head?...*click*""".format(secret_num))
        print("""
        ...................
        ...................
        ...................
        """)
        print("BOOM! " * number)
        print("Looks like you're still alive...somehow....would you like to play again?")
        play_again()
      elif int(guess) > int(secret_num):
        print("Nope.  Your guess was too high.  Guess again.")
        guess_counting(number)
      elif int(guess) < int(secret_num):
        print("Nope.  Your guess was too low.  Guess again.")
        guess_counting(number)
      
def guess_counting(number_of_guesses):
  number_of_guesses +=1
  if number_of_guesses == 6:
    print("You wasted all your guesses.  Time to die.")
  else:
    print("You have used {} of 6 guesses.  Choose wisely".format(number_of_guesses))
    main(number_of_guesses)

def play_again():
  again = input("Speak plainly...yes or no? ")
  if again.lower() == "yes":
    print("GREAT!  Let me get a bandaid for your nasty head wound real quick before we play again.")
    welcome(6)
  elif again.lower() == "no":
    print("I'm so disappointed...")
    russian_roulette = random.randint(3,6)
    print("*click*")
    print("BOOM! " * russian_roulette)
  else:
    print(again)
    print("I won't put up with ignorance.")
    russian_roulette = random.randint(3,6)
    print("*click*")
    print("BOOM! " * russian_roulette)
    
welcome(5)