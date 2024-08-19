import random

print("Welcome to the game of Gussing correctly")
count = 0
#guessing the number range top_of_range
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
  guess = input("Guess a number between " + str(top_of_range) + " and " + str(end_of_range) + ": ")
  print("So the number you guessed is", guess)
  count+=1

  if r == int(guess):
      print("the guessed number by computer was also", r)
      print("Yay you won")
      print("Number of guesses you took to win the game: ", count)
      break  # Indented to align with the if block

  elif r > int(guess):
      print("Your guess is too low")
      # No need for continue, the loop will naturally go to the next iteration

  elif r < int(guess):
      print("Your guess is too high")
      # No need for continue, the loop will naturally go to the next iteration
