import random

chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password_length = int(input("Şifrenin uzunluğunu girin: "))

password = ""

for i in range(password_length):
  char = random.choice(chars)
  password += char

print(password)

