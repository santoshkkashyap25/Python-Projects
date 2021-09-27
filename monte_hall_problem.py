import random
doors=[0]*3
goat_door=[0]*2
swap=0#swap wins
dont_swap=0#dont swap wins
j=0
while(j<10):
    x=random.randint(0,2)
    doors[x]="BMW"
    for i in range(0,3):
        if(i==x):
            continue
        else:
            doors[i]="goat"
            goat_door.append(i)
    choice=int(input("enter your choice"))
    #open a door comprising of goat
    door_open=random.choice(goat_door)
    while(door_open==choice):
        door_open=random.choice(goat_door)
    ch=input("Do you want swap? y/n")
    if(ch=='y'):
        if(doors[choice]=='goat'):
            print("player wins")
            swap=swap+1
        else:
            print("player loss")
    else:
        if(doors[choice]=='goat'):
            print("player loss")
        else:
            print("player wins")
            dont_swap=dont_swap+1
    j=j+1
print(swap)
print(dont_swap)


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        