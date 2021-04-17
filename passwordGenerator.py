import random
leng = int(input("How long do you want your password to be?"))
passw = ''
while leng > 0:
    passw += chr(random.randrange(48,57))
    leng -= 1
print(passw)
