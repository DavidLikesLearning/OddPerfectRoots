import numpy as np
game = True
ctr=0
ws = 0

def commas(num):
  strNum = str(num)
  nums = len(strNum)
  front = nums%3
  if front ==0:
    front = 3
  out = strNum[:front]
  remain = strNum[front:]
  left = nums-front
  while(left>0):
    next = ','+remain[:3]
    out= out+next
    left = left-3
    remain = remain[3:]
  return out

learn = False
punct = False
opts = str(input("Options:\ncommas? C\nlearn? L\n")).lower()
if (opts == 'c' or opts == 'l'):
  punct = True
if (opts == 'l'):
  learn = True
while(game):
  k = int(input("(0 to quit)\n odd root?  "))
  if(k ==0):
    game=False
    break
  truth = np.random.randint(100)
  out = np.power(truth,k)
  if learn:
    for i in range(1,10):
      print(i*10, 'to the', k, 'is ', commas((i*10)**k))
  if (punct):
    guess = int(input("What's "+commas(out)+" to the 1/"+str(k)+"? "))
  else:
    guess = int(input("What's "+str(out)+" to the 1/"+str(k)+"? "))

  ctr+=1
  if guess ==truth:
    ws+=1
    print("perhaps.\n\n",ws," out of ",ctr)
  else:
    print("No. It's "+str(truth)+ ". GUARDS!\n\n",ws," out of ",ctr)