# Created by developer @Atom1clhu on Github
# Atom Development

# importing modules
import os, time
from time import sleep

# main ui
pw = input("Please type the password correctly! : ")
if pw == "your password":
    print("Wow! You did it right!")
    name = input("Can i ask for your name? : ")
    print(f'Oh great, Your name is {name}!')
    sleep(20)
else:
    print("Wrong password, try again maybe..?")
    sleep(20)

# You can implement this with your own app/program/code!
# Leave a credit if you were using this!