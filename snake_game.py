import random
def game_win(compt,you):
    if compt== you:
        return None 
    elif compt== "s":
        if you== "w":
            return True
        elif you=="g":
                return True
        elif compt=="w":
             if you=="g":
                  return False
             elif you=="s":
                  return True
             elif compt=="s":
                  if you=="w":
                       return False
                  elif you=="g":
                       return True
print("compt chose w for water, g for gun and s for snake:??")
rannumber= random.randint(1,3)
if rannumber==1:
     compt="s"
elif rannumber==2:
     compt="w"
elif rannumber==3:
     compt="g"
you=input("Enter your choice: s,w,g?\n")
a= game_win(compt,you)
print(f"computer chose: {compt}")
print(f"you chose: {you}")
if a==None:
     print("game tie")
elif True:
     print("You Win")
else: 
     print("You lose")
                  
           

