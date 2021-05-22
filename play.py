import numpy as np
game = True
ctr=0
ws = 0
while(game):
  k = int(input("root? (0 to quit) "))
  if(k ==0):
    game=False
    break
  truth = np.random.randint(100)
  out = np.power(truth,k)
  guess = int(input("What's "+str(out)+" to the 1/"+str(k)+"? "))
  ctr+=1
  if guess ==truth:
    ws+=1
    print("perhaps.\n\n",ws," out of ",ctr)
  else:
    print("No. It's "+str(truth)+ ". GUARDS!\n\n",ws," out of ",ctr)