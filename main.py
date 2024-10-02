import random
import time

about_me = []

for i in range(3):
    fakt = input("Podaj coś o sobie: ")
    about_me.append(fakt)
    print(about_me)


print("losowanie")
time.sleep(3)
print("losowy fakt o tobie to, ",random.choice(about_me))
