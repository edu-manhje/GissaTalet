namn=input("Vad heter du min vän?")
print(f"Hej {namn} och välkommen till mitt spel")
import random as rand
tal=rand.randint(1,10)
for i in range(3):
    while i <3:
        gissning=int(input("Gissa ett tal mellan 1-10--->  "))
        if gissning==tal:
            print("Rätt bror")
            break
        elif gissning != tal:
            print("Fel min vän, du får testa igen om du vill..")
        break
    if i==2:
        print("Nah sluta")
        
    
    