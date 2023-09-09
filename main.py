import random

base = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

size = int(input("Какой размер пароля?"))

password = ""

for i in range(size):
    k = random.randint(0, len(base) - 1)
    password += base[k]

print(password)