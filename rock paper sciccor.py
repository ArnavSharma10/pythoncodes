import random

Human_Choice = 2
Computer_Choice = random.randint(1, 3)



def Comp_Func_Choice(a):
    if a == 1:
        return "Rock"
    elif a == 2:
        return "Scissors"
    elif a == 3:
        return "Paper"

    
def Hum_Func_Choice(b):
    if b == 1:
        return "Rock"
    elif b == 2:
        return "Scissors"
    elif b == 3:
        return "Paper"

print("Computer Choice:", Comp_Func_Choice(Computer_Choice))
print("Your Choice:", Hum_Func_Choice(Human_Choice))



if Human_Choice == Computer_Choice:
    print("Neutral! Please Re-roll The Dice!")
    
elif Human_Choice == 1 and Computer_Choice == 2:
    print("Human Wins!")
elif Human_Choice == 1 and Computer_Choice == 3:
    print("Computer Wins!")

    
elif Human_Choice == 2 and Computer_Choice == 1:
    print("Computer Wins!")
elif Human_Choice == 2 and Computer_Choice == 3:
    print("Human Wins!")

elif Human_Choice == 3 and Computer_Choice == 2:
    print("Computer Wins!")
elif Human_Choice == 3 and Computer_Choice == 1:
    print("Human Wins!")﻿

human_choice.mainloop()    
