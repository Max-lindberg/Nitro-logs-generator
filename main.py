from time import sleep
import random
import string

print("Welcome to Xflick community project")

print("____  ___  _____ .__   .__          __                                                        .__   __            
\   \/  /_/ ____\|  |  |__|  ____  |  | __      ____   ____    _____    _____   __ __   ____  |__|_/  |_  ___.__. 
 \     / \   __\ |  |  |  |_/ ___\ |  |/ /    _/ ___\ /  _ \  /     \  /     \ |  |  \ /    \ |  |\   __\<   |  | 
 /     \  |  |   |  |__|  |\  \___ |    <     \  \___(  <_> )|  Y Y  \|  Y Y  \|  |  /|   |  \|  | |  |   \___  | 
/___/\  \ |__|   |____/|__| \___  >|__|_ \     \___  >\____/ |__|_|  /|__|_|  /|____/ |___|  /|__| |__|   / ____| 
      \_/                       \/      \/         \/              \/       \/             \/             \/      ")

sleep(1)

logs = input("How many Discord logs do you want? ")

print("Ok")
print("1% generated")
sleep(1)
print("24% generated")
sleep(2)
print("45% generated")
sleep(0.7)
print("79% generated")
sleep(0.9)
print("100% generated")


def generat_code():
  return randomword(27)



import random, string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

if logs is int:
    print("Ok")
    print("1% generated")
    sleep(1)
    print("24% generated")
    sleep(2)
    print("45% generated")
    sleep(0.7)
    print("79% generated")
    sleep(0.9)
    print("100% generated")

file1 = open("MyFile.txt", "w")
i = 0
while i < int(logs):
  file1.write("https://discord.com/billing/promotions/" + generat_code() + "\n")
  print("https://discord.com/billing/promotions/" + generat_code())
  i += 1

file1.close()
