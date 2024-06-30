# Importing
import random
import os
from colorama import Fore
import re
import time
import sys
from replit import db

# Function: Clear Screen
def Clear_Screen():
  print("\033c", end="", flush=True)


# Function: Main
def main():
  # Assigning Variabes
  start = 'Y'
  topic = ''
  answer = ''
  number = 0
  dash = '-' * 48
  go_on = 'N'
  game_over_ascii = '''---------------------------------------------
|   ______      ___      _        _ ______  |
|  / _____|    / _ \\    |  \\    /  |  ____| |
| | /  ___    / / \\ \\   | |\\\\  //| | |__    |
| | | |__ \\  / /___\\ \\  | | \\\\// | | |__|   |
| | \\____| |/ /     \\ \\ | |  \\/  | | |____  |
|  \\______//_/       \\_\\|_|      |_|______| |
|       _____        __ _____________       |
|      / _ \\  \\     / / |  ____||  _ \\      |
|     | | | |\\ \\   / /  | |__   | |_| |     |
|     | | | | \\ \\ / /   | |__|  |    /      |
|     | |_| |  \\ V /    | |____ | |\\ \\      |
|      \\___/    \\_/     |______||_| \\_\\     |
---------------------------------------------'''
  welcome_ascii = '''------------------------------------------------------
| __          _______ _     ____ ___  __  __ _____   |
| \\ \\        / / ____| |   / ___/ _ \\|  \\/  | ____|  |
|  \\ \\  /\\  / /|  _| | |  | |  | | | | |\\/| |  _|    |
|   \\ \\/  \\/ / | |___| |__| |__| |_| | |  | | |___   |
|    \\__/\\__/  |_____|_____\\____\\___/|_|  |_|_____|  |
------------------------------------------------------'''
  math_ascii = '''--------------------------------------
|  __    __    ____  _______ _    _  |
| |   \\/   |  / __ \\|___ ___| |__| | |
| |  |\\/|  | / /__\\ \\  | |  |  __  | |
| |  |  |  |/ /    \\ \\ | |  | |  | | |
| |__|  |__|_/      \\_\\|_|  |_|  |_| |
--------------------------------------'''
  wrong_ascii = '''--------------------------------------------------------
| __            ______    ___  ___     _  _______   _  |
| \\ \\          / /  _ \\  / _ \\|   \\   | |/  _____| | | |
|  \\ \\   /\\   / /| |_| || | | | |\\ \\  | |  /  ___  | | |
|   \\ \\ /  \\ / / |    / | | | | | \\ \\ | |  | |__ \\ |_| |
|    \\ V /\\ V /  | |\\ \\ | |_| | |  \\ \\| |\\ \\____| | _  |
|     \\_/  \\_/   |_| \\_\\ \\___/|_|   \\___| \\______/ |_| |
--------------------------------------------------------'''
  correct_ascii = '''------------------------------------------------------------
|   _____   ___  ____   ____   ______   _____ _________ _  |
|  /  ___| / _ \\/  _ \\ /  _ \\ |  ____| /  ___|____ ____| | |
| |  /    | | | | |_| || |_| || |__   |  /       | |   | | |
| | |     | | | |    / |    / |  __|  | |        | |   |_| |
| |  \\___ | |_| | |\\ \\ | |\\ \\ | |____ |  \\___    | |    _  |
|  \\_____| \\___/|_| \\_\\|_| \\_\\|______| \\_____|   |_|   |_| |
------------------------------------------------------------'''
  hundred_points = '''--------------------------------------------
|              __  ___   ___               |
|             /_ |/ _ \\ / _ \\              |
|              | | | | | | | |             |
|              | | | | | | | |             |
|              | | |_| | |_| |             |
|              |_|\\___/ \\___/              |
|  _____   ____ _____ _   _ _______ _____  |
| |  __ \\ / __ \\_   _| \\ | |__   __/ ____| |
| | |__) | |  | || | |  \\| |  | | | (___   |
| |  ___/| |  | || | | . ` |  | |  \\___ \\  |
| | |    | |__| || |_| |\\  |  | |  ____) | |
| |_|     \\____/_____|_| \\_|  |_| |_____/  |
  --------------------------------------------'''
  english_ascii = '''------------------------------------------------------------
|  ______  ___     _  ______   _       _  _____  _      _  |
| | _____||   \\   | |/ _____| | |     | |/ ____|| |    | | |
| | |__   | |\\ \\  | | /  ___  | |     | | (___  | |____| | |
| | |__|  | | \\ \\ | | | |__ \\ | |     | |\\___ \\ |  ____  | |
| | |____ | |  \\ \\| | \\____| || |_____| |____) || |    | | |
| |______||_|   \\___|\\______/ |_______|_|_____/ |_|    |_| |
------------------------------------------------------------'''
  current_points = 0
  required_points = 70
  math_question = {
      1:
      "State the formula for Pythagora's Theogram",
      2:
      "State the formula for the area of a circle",
      3:
      "State the formula for the area of a triangle",
      4:
      "State the formula for the area of a rectangle",
      5:
      "What is 18000 divided by 201? (Give answer to 3 S.F.)",
      6:
      "AB = 9cm, BC = 13cm, AC = ?cm. Find the value of AC, if AC is the hypotenuse"
      "(Give answer with units, Give answer to 3 S.F.)",
      7:
      "Is the following a right triangle? (Yes/No) AB = 12cm, BC = 5cm, AC = 13cm",
      8:
      "Is 73824847 divisible by 3? (With no remainder) (Yes/No)",
      9:
      "What is the square root of 6969? (Give answer to 3 S.F.)",
      10:
      "What is 65 times 82?",
      11:
      "What is the square root of 750? (Give answer to 3 S.F.)",
      12:
      "What is the cube root of 625? (Give answer to 3 S.F.)",
      13:
      "What is the perimeter of a circle if its radius is 6? (Give answer to 3 S.F.)",
      14:
      "What is the area of a circle if its circumference is 54? \
(Give answer to 2 D.P.)",
      15:
      "What is 334 divided by 5?",
      16:
    """A farmer has chickens and cows. He knows that he has a total of 20 
animals on his farm. 
He also knows that there are twice as many chickens as cows. How many chickens does the farmer have?""",
      17:
      "A rectangular garden is 12 meters long and 8 meters wide. \
What is the area of the garden? (Give answer with units)",
      18:
      "A store sells apples for $1.50 each and oranges for $0.75 each. \
If you buy 3 apples and 5 oranges, how much will you spend in total? \
(Give answer with units)",
      19:
      "A bakery sells cupcakes for $2.50 each. If you buy 6 \
cupcakes, how much change will you receive from a $20 bill? \
(Give answer with units)",
      20: "What is the square root of 1296? (Give answer in 3 S.F.)"
  }
  math_answer = {
      1: "a^2 + b^2 = c^2",
      2: "pi * r^2",
      3: "1\\2 * base * height",
      4: "length * breadth",
      5: "89.6",
      6: "15.8cm",
      7: "No",
      8: "No",
      9: "83.5",
      10: "5330",
      11: "27.4",
      12: "8.55",
      13: "37.7",
      14: "232.05",
      15: "66.5",
      16: "12",
      17: "96 meters",
      18: "$9.75",
      19: "$5.00",
      20: "36.0"
  }
  english_question = {
      1: "What is the past tense of 'go'?",
      2: "What is the plural form of 'child'?",
      3: "What is the opposite of 'happy'?",
      4: "Complete the sentence: 'The quick brown ___ jumps over the lazy dog.'",
      5: "Which word is a synonym for 'big': large, small or tiny?",
      6: "Which word is a noun: 'run', 'cat', or 'quickly'?",
      7: "What is the correct spelling of the word 'color' in British English?",
      8: "What is the opposite of 'hot'?",
      9: "What is the plural form of 'mouse'?",
      10: "What is an antonym for 'large': large, small or massive?",
      11: "What is the past tense of 'eat'?",
      12: "Which of these sentences is grammatically correct: 'I am going to the store'\
    or 'I going to the store'? (Type out the correct sentence)",
      13: "What is the correct way to write the possessive form of 'cat'?",
      14: "What is the correct way to write the plural form of 'dog'?",
      15: "Which pronoun correctly completes this sentence: 'The dog chased ___ ball.'",
      16: "What is the correct past participle of 'swim'?",
      17: "What is the correct plural form of 'ox'?",
      18: "Identify the adjective in the following sentence: " + 
    "'The tall tree swayed in the wind.'",
      19: """Complete the sentence with the correct form of the verb 'to be': \
    'The cat ____ sleeping.'""",
      20: "What does the idiom 'once in a blue moon' mean?",
      21: "What does the expression 'spill the beans' mean?",
      22: "Identify the subject in the sentence: 'The bird sang sweetly.'",
      23: "Identify the verb in the sentence: 'The birds sang sweetly.'",
      24: "Rewrite the sentence 'The dog barked at the mailman' in the passive voice."
  }
  english_answer = {
      1: "went",
      2: "children",
      3: "sad",
      4: "fox",
      5: "large",
      6: "cat",
      7: "colour",
      8: "cold",
      9: "mice",
      10: "small",
      11: "ate",
      12: "I am going to the store",
      13: "cat's",
      14: "dogs",
      15: "its",
      16: "swum",
      17: "Oxen",
      18: "Tall",
      19: "is",
      20: "very rarely",
      21: "reveal a secret",
      22: "Birds",
      23: "Sang",
      24: "The mailman was barked at by the dog"
  }

  # Function: Clearing Screen
  def Clear_Screen():
    print("\033c", end="", flush=True)

  # Function: Bold
  def bold(type):
    sys.stdout.write("\033[1m" + type + "\033[0m")

  # Function: Underline
  def underline(type):
    sys.stdout.write("\033[4m" + type + "\033[0m")

  # Function: go_back
  def go_back(test):
    while True:
      print(' ')
      print(dash)
      print('Would you like to go back to the main menu?')
      go_on = str(input('Answer (Y/N): ')).upper()
      if go_on == 'Y':
        Clear_Screen()
        time.sleep(0.5)
        print('Opening Main Menu...')
        time.sleep(1)
        Clear_Screen()
        main()
        return
      elif go_on == 'N':
        Clear_Screen()
        bold(test)
        exit()
      else:
        print('Invalid input. Please enter Y or N.')

  # Function: Conversion
  def conversion():
    underline("Math Converstion to Computer Text:")
    print(' ')
    print(dash)
    print('''1) Addition
2) Subtraction
3) Multiplication
4) Division
5) Square Root
6) Cube Root
7) Squaring
8) Cubing
9) Factions
10) Variables
11) Percentage
12) Greater Than
13) Lesser Than
14) Equal To
15) Not Equal To
16) Greater Than or Equal To
17) Lesser Than or Equal To''')
    print(dash)
    option = str(input('Which option would you like to see?: ')).upper()

    if option == '1' or option == 'ONE':
      Clear_Screen()
      bold("Addition in Computer Text: +")
      go_back("Addition in Computer Text: +")

    elif option == '2' or option == 'TWO':
      Clear_Screen()
      bold('Subtraction in Computer Text: -')
      go_back('Subtraction in Computer Text: -')

    elif option == '3' or option == 'THREE':
      Clear_Screen()
      bold('Multiplication in Computer Text: *')
      go_back('Multiplication in Computer Text: *')

    elif option == '4' or option == 'FOUR':
      Clear_Screen()
      bold('Division in Computer Text: /')
      go_back('Division in Computer Text: /')

    elif option == '5' or option == 'FIVE':
      Clear_Screen()
      bold('Square Root in Computer Text: $2')
      go_back('Square Root in Computer Text: $2')

    elif option == '6' or option == 'SIX':
      Clear_Screen()
      bold('Cube Root in Computer Text: $3')
      go_back('Cube Root in Computer Text: $3')

    elif option == '7' or option == 'SEVEN':
      Clear_Screen()
      bold('Squaring in Computer Text: ^2')
      go_back('Squaring in Computer Text: ^2')

    elif option == '8' or option == 'EIGHT':
      Clear_Screen()
      bold('Cubing in Computer Text: ^3')
      go_back('Cubing in Computer Text: ^3')

    elif option == '9' or option == 'NINE':
      Clear_Screen()
      bold('Fractions in Computer Text: \\')
      go_back('Fractions in Computer Text: \\')

    elif option == '10' or option == 'TEN':
      Clear_Screen()
      bold('''Variables in Computer Text:
1) length(l)
2) breadth(b)
3) height(h)
4) radius(r)
5) base(b)
6) area(a)
7) perimeter(p)
8) volume(v)''')
      go_back('''Variables in Computer Text:
1) length(l)
2) breadth(b)
3) height(h)
4) radius(r)
5) base(b)
6) area(a)
7) perimeter(p)
8) volume(v)''')

    elif option == '11' or option == 'ELEVEN':
      Clear_Screen()
      bold('Percentage in Computer Text: %')
      go_back('Percentage in Computer Text: %')

    elif option == '12' or option == 'TWELVE':
      Clear_Screen()
      bold('Greater Than in Computer Text: >')
      go_back('Greater Than in Computer Text: >')

    elif option == '13' or option == 'THIRTEEN':
      Clear_Screen()
      bold('Lesser Than in Computer Text: <')
      go_back('Lesser Than in Computer Text: <')

    elif option == '14' or option == 'FOURTEEN':
      Clear_Screen()
      bold('Equal To in Computer Text: =')
      go_back('Equal To in Computer Text: =')

    elif option == '15' or option == 'FIFTEEN':
      Clear_Screen()
      bold('Not Equal To in Computer Text: !=')
      go_back('Not Equal To in Computer Text: !=')

    elif option == '16' or option == 'SIXTEEN':
      Clear_Screen()
      bold('Greater Than or Equal To in Computer Text: >=')
      go_back('Greater Than or Equal To in Computer Text: >=')

    elif option == '17' or option == 'SEVENTEEN':
      Clear_Screen()
      bold('Lesser Than or Equal To in Computer Text: <=')
      go_back('Lesser Than or Equal To in Computer Text: <=')

    else:
      time.sleep(0.01)
      Clear_Screen()
      time.sleep(0.01)
      conversion()

  # Function: Topic Menu
  def Topic_Menu():
    bold(f'{Fore.BLUE}{welcome_ascii}{Fore.WHITE}')
    print(' ')
    underline("Topics Avalible:")
    print('''
1) Math
2) English''')
    underline("Extra Options:")
    print('''
A) Exit the program
B) Restart the program
C) Math Conversion to Computer Text''')
    print(dash)
    while True:
      topic = str(input('What would you like to choose?: ')).upper()
      if topic in ['1', 'ONE', '2', 'TWO', 'A', 'B', 'C']:
        return topic
      else:
        Clear_Screen()
        print('ERROR: INVALID TOPIC INPUT. Please enter a valid option.')

  # Function: Game Over
  def game_over():
    bold(f'{Fore.RED}{game_over_ascii}{Fore.WHITE}')
    print(' ')
    bold(f'{Fore.BLUE}YOU GOT TOO LITTLE POINTS.{Fore.WHITE}')
    print(' ')
    bold(f'{Fore.WHITE}PLEASE RESTART THIS PROGRAM TO CONTINUE{Fore.WHITE}')
    print(' ')
    print(dash)
    exit()

  # Function: Math
  def math():
    nonlocal current_points, required_points
    number = random.randint(1, 20)
    if int(current_points) != -20:
      bold(f'{Fore.BLUE}{math_ascii}{Fore.WHITE}')
      print(' ')
    print(f'{Fore.MAGENTA}Current Points: {current_points}{Fore.WHITE}')
    print(f'{Fore.YELLOW}Required Points: {required_points}{Fore.WHITE}')
    print(dash)
    print(math_question[number])
    answer = str(input(f'{Fore.BLUE}Answer: {Fore.WHITE}'))

    if answer.upper() == math_answer[number].upper():
      bold(f'{Fore.GREEN}{correct_ascii}{Fore.WHITE}')
      print(' ')
      current_points += 5
      print(f'{Fore.MAGENTA}Current Points: {current_points}{Fore.WHITE}')
      print(f'{Fore.YELLOW}Required Points: {required_points}{Fore.WHITE}')
      print(dash)
      if int(current_points) == 100:
        bold(f'{Fore.LIGHTGREEN_EX}{hundred_points}{Fore.WHITE}')
        print(' ')
        print(dash)
      go_on = str(input('Would you like to continue? (Y/N): ')).upper()
      if go_on == 'Y':
        Clear_Screen()
        math()

      else:
        Clear_Screen()
        main()

    else:
      bold(f'{Fore.RED}{wrong_ascii}{Fore.WHITE}')
      print(' ')
      print(f'{Fore.LIGHTBLUE_EX}The Correct Answer Was: '
            f'{math_answer[number]}{Fore.WHITE}')
      print(dash)
      current_points -= 5
      print(f'{Fore.MAGENTA}Current Points: {current_points}{Fore.WHITE}')
      print(f'{Fore.YELLOW}Required Points: {required_points}{Fore.WHITE}')
      print(dash)
      if current_points == -20:
        game_over()
      go_on = str(input('Would you like to continue? (Y/N): ')).upper()
      if go_on == 'Y':
        Clear_Screen()
        math()

      else:
        Clear_Screen()
        main()

    current_points = current_points
    return current_points, required_points

  # Function: English
  def english():
    nonlocal current_points, required_points
    number = random.randint(1,24)
    if int(current_points) != -20:
      bold(f'{Fore.BLUE}{english_ascii}{Fore.WHITE}')
      print(' ')
    print(f'{Fore.MAGENTA}Current Points: {current_points}{Fore.WHITE}')
    print(f'{Fore.YELLOW}Required Points: {required_points}{Fore.WHITE}')
    print(dash)
    print(english_question[number])
    answer = str(input(f'{Fore.BLUE}Answer: {Fore.WHITE}'))

    if answer.upper() == english_answer[number].upper():
      bold(f'{Fore.GREEN}{correct_ascii}{Fore.WHITE}')
      print(' ')
      current_points += 5
      print(f'{Fore.MAGENTA}Current Points: {current_points}{Fore.WHITE}')
      print(f'{Fore.YELLOW}Required Points: {required_points}{Fore.WHITE}')
      print(dash)
      if int(current_points) == 100:
        bold(f'{Fore.LIGHTGREEN_EX}{hundred_points}{Fore.WHITE}')
        print(' ')
        print(dash)
      go_on = str(input('Would you like to continue? (Y/N): ')).upper()
      if go_on == 'Y':
        Clear_Screen()
        english()
      else:
        Clear_Screen()
        main()

    else:
      bold(f'{Fore.RED}{wrong_ascii}{Fore.WHITE}')
      print(' ')
      print(f'{Fore.LIGHTBLUE_EX}The Correct Answer Was: '
           f'{english_answer[number]}{Fore.WHITE}')
      print(dash)
      current_points -= 5
      print(f'{Fore.MAGENTA}Current Points: {current_points}{Fore.WHITE}')
      print(f'{Fore.YELLOW}Required Points: {required_points}{Fore.WHITE}')
      print(dash)
      if current_points == -20:
        game_over()
      go_on = str(input('Would you like to continue? (Y/N): ')).upper()
      if go_on == 'Y':
        Clear_Screen()
        english()
      else:
        Clear_Screen()
        main()

    current_points = current_points
    return current_points, required_points

  # Main Loop
  if start == 'Y':
    while True:
      topic = Topic_Menu()
      if topic == '1' or topic == 'ONE':
        Clear_Screen()
        current_points, required_points = math()

      elif topic == '2' or topic == 'TWO':
        Clear_Screen()
        current_points, required_points = english()

      elif topic == 'A':
        Clear_Screen()
        print('Exiting the program...')
        time.sleep(2)
        Clear_Screen()
        time.sleep(0.25)
        print('Program Exited')
        exit()

      elif topic == 'B':
        restart()

      elif topic == 'C':
        Clear_Screen()
        conversion()

      else:
        Clear_Screen()
        print('ERROR: INVALID TOPIC INPUT')
        exit()


# Function: Restart
def restart():
  time.sleep(0.1)
  Clear_Screen()
  time.sleep(0.1)
  main()


# Main Loop
main()
