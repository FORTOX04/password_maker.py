import random, time, math
from math import sqrt
pwlenght=int(input("how long do you want the password?\n[}>>>"))
v = 1
c = pwlenght - 1
u = c + 1
q = random.randint(0,1)
q2 = q
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","z"]
pwordone = ""
pwordzero = ""
randomzero = ""
pword = ""
def passwordmaker():
  if q == 1:
    randomone = (random.randint(0,9))
    pword = pword + randomone
  elif q == 0:
    randomzero = 1
    randomzero = randomzero + abc[random.randint(0,25)]
    pword = pword + ramdomzero
    print(randomzero)
    time.sleep(4)
while u >= pwlenght:
  passwordmaker()
  q = random.randint(0,1)
  q2 = q
  u = u - 1
print(pword)
print("this is your password")
