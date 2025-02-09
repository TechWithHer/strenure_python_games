import random
from colorama import Fore, Style
import sys
import time
from rich.console import Console
console = Console()
import pyfiglet
import pygame


def animated_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

pygame.init()
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Glitch Text Effect")

font = pygame.font.Font(None, 50)
text = "GLITCH EFFECT!"

running = True
while running:
    screen.fill((0, 0, 0))
    text_surface = font.render(text, True, (random.randint(100, 255), 0, random.randint(100, 255)))
    screen.blit(text_surface, (random.randint(90, 110), random.randint(90, 110)))
    pygame.display.flip()
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()



print(pyfiglet.figlet_format("GUESS NUMBER GAME!", font="slant"))
animated_text(Fore.RED + Style.BRIGHT + "Hello, Player! Get ready for an adventure! 🚀 Welcome to the game of Gussing correctly \N{grinning face} \n" + Style.RESET_ALL)
animated_text(Fore.BLUE + "Read the RULES carefully: " + Style.RESET_ALL)
animated_text(" 1) You have to guess the number between the range you provide")
animated_text(" 2) If you guess the number correctly, you win the game")
animated_text(" 3) If you guess the number incorrectly, you will be prompted to guess again")
animated_text(" 4) The game will continue until you guess the number correctly")
animated_text(" 5) The number of guesses you took to win the game will be displayed at the end of the game")
animated_text(" 6) If you want to exit or stop the game, press" + Fore.GREEN + "'Q' or 'q'" + Style.RESET_ALL)
console.print("[bold red]Game Over![/bold red] 😱")
console.print("[bold green] So the WAIT IS OVER ! LETS START! 🎉[/bold green]", style="bold underline")



guess_count = 0

top_of_range = input("Input the top range number, greater than zero: ")
if top_of_range.isdigit():
   top_of_range = int(top_of_range)
   if top_of_range <= 0:
    print("Please input a number greater than zero next time.")
else: 
  print ("Please enter a valid number")
  quit()

#guessing the number range end_of_range
end_of_range = input("Input the end range number: ")
if end_of_range.isdigit() and (int(end_of_range) > int(top_of_range)):
  end_of_range = int(end_of_range)
else:
  print ("Please enter a valid end range")
  quit()

r = random.randrange(top_of_range,end_of_range)

while True:
  guess = input("Guess a number between " + int(top_of_range) + " and " + int(end_of_range) + ": ")
  guess_count+=1

  if r == int(guess):
      print("the guessed number by computer was also", r)
      print("Yay you won")
      print("Number of guesses you took to win the game: ", guess_count)
      break  # Indented to align with the if block

  elif r > int(guess):
      print("Your guess is too low")
      # No need for continue, the loop will naturally go to the next iteration

  elif r < int(guess):
      print("Your guess is too high")
      # No need for continue, the loop will naturally go to the next iteration
