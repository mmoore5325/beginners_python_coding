import random
guessed_letters = []
hangman_words = ["wonderfulee"]

def main(num):
  the_word = hangman_word()
  rep = representation(the_word)
  num -= 1
  the_rules(num)
  print(rep)
  the_noose(num, the_word, rep)

  
def game(num, the_word, rep):
    
    thisround = False
    try:
      guess = str(input("Guess as if your life depends on it: "))
      if guess in guessed_letters:
        print("Are you stoopid or sumthin?")
        num -=1
        the_noose(num, the_word, rep)
        
      guessed_letters.append(guess)
      
      i = 0
      while i < len(the_word):
         if the_word[i] == guess:
            rep[i] = guess
            print(rep)
            thisround = True
         i+=1
      if rep == the_word:
        game_won()
      elif thisround == True:
        game(num, the_word, rep)
      else:
        num -=1
        the_noose(num, the_word, rep)
    except:
      print("You must want to hang")
      num -=1
      the_noose(num, the_word, rep)

    
def the_rules(num):
  print("""
  You have {} chances before you are hung.
  There are no numbers.
  Guessing numbers will be counted against you, and you will be hung.
  Here is your lifeline:""".format(num))

def representation(the_word):   
    rep = []
    word_length = len(the_word)
    while word_length > 0:
      rep.append("X")
      word_length -= 1
      
    return rep
    
def game_won():
  print("""
  You escaped the noose today....
  ....but I know where you live.""")
  
def hangman_word():
  hangman_word = random.sample(hangman_words, 1)
  hangman_word = hangman_word[0]
  the_word = list(hangman_word)
  return the_word

def the_noose(num, the_word, rep):
  if int(num) == 0:
    game_over()
  elif int(num)== 1:
    miss_five(num, the_word, rep)
  elif int(num)== 2:
    miss_four(num, the_word, rep)
  elif int(num)== 3:
    miss_three(num, the_word, rep)
  elif int(num)== 4:
    miss_two(num, the_word, rep)
  elif int(num)== 5:
    miss_one(num, the_word, rep)
  elif int(num)== 6:
    miss_zero(num, the_word, rep)
  
    
def game_over():
  print("""
      _____
      |    |
      O    |
     /|\   |
     / \ __|___
     
 DIE DIE DIE DIE DIE""")
  exit()
  
def miss_zero(num, the_word, rep):
  print("""
      _____
      |    |
           |
           |
         __|___
     """)
  game(num, the_word, rep)
  
def miss_one(num, the_word, rep):
  print("""
      _____
      |    |
           |
           |
       \ __|___
     """)
  game(num, the_word, rep)
  
def miss_two(num, the_word, rep):
  print("""
      _____
      |    |
           |
           |
     / \ __|___
     """)
  game(num, the_word, rep)
  
def miss_three(num, the_word, rep):
  print("""
      _____
      |    |
           |
      |    |
     / \ __|___
     """)
  game(num, the_word, rep)
  
def miss_four(num, the_word, rep):
  print("""
      _____
      |    |
           |
     /|    |
     / \ __|___
     """)
  game(num, the_word, rep)
  
def miss_five(num, the_word, rep):
  print("""
      _____
      |    |
           |
     /|\   |
     / \ __|___
     """)
  game(num, the_word, rep)
  
main(7)