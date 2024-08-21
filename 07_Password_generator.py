import random
import string

#define a function

def generate_password(length, special_char=True, numbers=True):
  print("Let me suggest a password for you")

#character set for password  
  letters = string.ascii_letters
  digits = string.digits
  special = string.punctuation
 
  character = letters
  password = ""
  
  if special_char:
   character += special
  if numbers:
   character += digits
  else:
   quit()
    
  while len(password) < length:
    password += random.choice(character)
  
  print(password)

generate_password(8)
