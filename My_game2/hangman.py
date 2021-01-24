#!/usr/bin/env python3

import logging
import random
import requests as req
import urllib.request

#logging configuration
logging.info("logging configuration: start")
logging.basicConfig(filename='hangman_log.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
logging.info("logging configuration: end")

def replay():
  cont_game = str(input("Would you like to play again? Type 'y' for yes or 'n' for no\n").lower())
  if cont_game == "y":
    main()
  else:
    print("See you soon!")

def main():
  logging.info("creating main function for packaging")
  print("Game begins")

  logging.info("creating list with ascii art for hangman: start")

  hangman_art = ['''
    +---+
    |   |
        |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']
  logging.info("creating list with ascii art for hangman: end")


  hangman_art.reverse()
#logging configuration


# accessing the list from the internet

  logging.info("checking if site we get words from is working properly")
  if urllib.request.urlopen("http://www.mit.edu/~ecprice/wordlist.10000").getcode() != 200:
      f = open("words.txt", "r")
      new_list = f.read()
      word_list = new_list.split(",")
      logging.info("site failed to response, using backup text file to play")
  else:
      logging.info("accessing the list from the internet: start")
      resp = req.get("http://www.mit.edu/~ecprice/wordlist.10000")
      logging.info("accessing the list from the internet: end")

      list_of_words = resp.content #reponse en bytes

      reply = list_of_words.decode('utf-8') #transformer le type byte de content en string
      word_list = reply.split("\n") #transforming in list
      logging.info("list ready to play")
      # print(word_list)


  logging.info("choosing a random word from the list")
  chosen_word = random.choice(word_list)
  print(chosen_word)
  guessed_letters = []

  # printing _ for each letter in chosen_word
  guess_list = []
  for letter in range(len(chosen_word)):
      guess_list.append("_")
  print(guess_list)

  # condition for end of game
  end_of_game = False
  life = 6



  while not end_of_game: # while we have lives left
      print(f"Letters you already tried: {guessed_letters}\n")
      guess = input("\nPlease guess a letter\n").lower()
      guessed_letters.append(guess)
      logging.info("going throw our random word and checking if the letter is there, if it is we replace _ with the guess letter: start")
      
      hangman_art[life]
      logging.info("printing hangman art to show amount of lives left")
      
      if guess in guess_list:
        print(f"You have already guessed letter {guess}, please try another one.")
        
      logging.info("going throw the list and checking for the guessed letter")
      ki = 0 #compteur i                      # we walk throw our word and check if we guessed the letter
      for i in chosen_word:                   # and we change the _ with guessed letter
          if guess == i:                      
              guess_list[ki] = guess                                             
          ki += 1
      print(guess_list)
      print(hangman_art[life])

      if not "_" in guess_list:
        print("You guessed the word! You won!")
        replay()
        break

      if guess not in chosen_word:
        life -= 1
        print(f"You guessed wrong! You have {life} lives left")
        print(hangman_art[life])
        

        if life == 0:
          print("You lost")
          end_of_game = True #we quit the boucle
          replay()

