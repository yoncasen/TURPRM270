import random

def gen_pass(password_length):

  chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

  password = ""

  for i in range(password_length):
    char = random.choice(chars)
    password += char

  return password

#password = gen_pass(15)
#print(password)