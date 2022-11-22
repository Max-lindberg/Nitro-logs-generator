from time import sleep
import random
import string

print("Welcome to Xflick community project")

sleep(1)

logs = input("How many Discord logs do you want?")

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
 
# initializing size of string
#N = 7
 
# using random.choices()
# generating random strings
#res = ''.join(random.choices(string.ascii_uppercase +
#                             string.digits, k=N))
 
# print result
#print("The generated random string : " + str(res))



