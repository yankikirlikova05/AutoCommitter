from os import system
from time import sleep
from random import choice

#burayı kendinize göre deiştirin
direc = "dekstop/codes/FRC2021"


#messages may be changed personally
messages = ["saygılar burak abi","a couple things added","maraba","git desktop kullanan da ne bilm"]

#bu fonksiyonlardan birini kullanın, while döngüsüne yazabilirsiniz
#bunu kullanırsanız sizden input isticek commitlemek için
def inputlu():
    s = input("Enter: ")
    if s == "c":
        mess = choice(messages)
        system(f"cd {direc}; git commit -m '{mess}' ")
    elif s == "p":
        system(f"cd {direc};git push")

    system(f"cd {direc}; git add .")
    print("added")

#bunda 10 saniyede bir otomatik commit atiyo
def timing():
    system(f"cd {direc}; git add .")
    mess = choice(messages)
    system(f"cd {direc}; git commit -m '{mess}' ")
    system(f"cd {direc}; git push")
    sleep(10)
    print("saved.")

while True:
    timing()
    

