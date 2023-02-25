import numpy as np
import time

class Stack:
    "A container with a last-in-first-out (LIFO) queuing policy."
    def __init__(self):
        self.list = []
        self.size=0

    def push(self,item):
        "Push 'item' onto the stack"
        self.list.append(item)
        self.size += 1

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop() 
        self.size -= 1

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0
        
    def __del__(self):
        return 

num = 3 

def Heuristic_2(current,goal):
    """
    Heuristic_2
    Heuristic used : Height * (1 or -1) depending on present on right place or not
    Examples :

    start="ABC,,ED"
    WORKS
    goal_str="BC,,AED" 
    goal_str="BC,EA,D" 
    goal_str="C,BA,ED"
    goal_str="DBC,EA," 
    NOT WORKS
    goal_str= "DBC,A,E" 

    start="ABCD,EF,"
    NOT WORKS
    goal_str="D,EF,CBA" #NOT WORKS

    start="ABC,DE,"
    goal_str="ADBC,E," #WORKS

    """
    heur_value=0
    for i in range(num):
       
        for j in range(len(current[i].list)):
           
            if current[i].list[j] in goal[i].list:   
                if goal[i].list.index(current[i].list[j])==j:
                    heur_value+=(j+1)
                else:
                    heur_value-=(j+1)
                           
            else:
                heur_value-=(j+1)
      
    return heur_value      



def ret_stacks(stri):
    stri=stri.split(",")
    state=[Stack() for _ in range(num)]
    for j in range(num):
        for i in stri[j][::-1]:
            state[j].push(i)
    return state


with open("input2.txt", "r") as file:
    lines = file.read().strip().splitlines()
    start = lines[0].strip()
    goal_str = lines[1].strip()

goal=ret_stacks(goal_str)
start_state_stacks=ret_stacks(start)

goal_heur=0

for i in goal:
    for j in range(i.size):
        goal_heur+=(j+1)

best_heur=Heuristic_2(start_state_stacks, goal)

print(f"START STATE HEURISTIC  : {best_heur} \n")
print(f"GOAL STATE HEURISTIC : {goal_heur} \n")

print("INITIAL CONFIGURATION ",start_state_stacks[0].list , start_state_stacks[1].list , start_state_stacks[2].list,"\n")
print("FINAL CONFIGURATION ",goal[0].list , goal[1].list , goal[2].list,"\n")
print("******** HILL CLIMBING STARTS ******","\n")

iter =0

current = start_state_stacks

best=ret_stacks(start)

for i in range(num):
    best[i].list=(np.array(current[i].list)).tolist()
start_time = time.time()
explored=0
while True:
    print("BEST CONFIGURATION OBTAINED SO FAR ",best[0].list , best[1].list , best[2].list,"\n")

    best_old=best_heur


    for i in range(num):
      

        if len(current[i].list)>=1:
            # print(f"{i} {current[i].list}")            
            current[(i+1)%num].push(current[i].pop())
            if (Heuristic_2(current, goal) > best_heur):
                best_heur=Heuristic_2(current, goal)
                del best
                best=[Stack() for _ in range(num)]
                for j in range(num):
                    best[j].list=(np.array(current[j].list)).tolist()    
                if goal_heur==best_heur:
                    del current
                    current=best
                    break
           
            current[i].push(current[(i+1)%num].pop())
            # print(f"{i} {current[i].list}")
            current[(i+2)%num].push(current[i].pop())
            if (Heuristic_2(current, goal) > best_heur):
                best_heur=Heuristic_2(current, goal)
                del best
                best=[Stack() for _ in range(num)]
                for j in range(num):
                    best[j].list=(np.array(current[j].list)).tolist()
                if goal_heur==best_heur:
                    del current
                    current=best
                    break
           
            current[i].push(current[(i+2)%num].pop())
            # print(f"{i} {current[i].list}\n")  
            explored+=2
        
    del current
    current=best

    if best_heur<=best_old:
            break
    iter+=1
    
end_time = time.time()

print("********** ITERATION ENDS******","\n")
print(f"BEST COST SO FAR IS : {best_heur}","\n")

print(f"GOAL STATE HEURISTIC VALUE : {goal_heur}","\n")
print("LAST CONFIGURATION OBTAINED ",current[0].list , current[1].list , current[2].list,"\n")
if goal_heur==best_heur:
    print("GOAL STATE ACHEIVED",f" after {iter} iterations \n" )
else:
    print("GOAL STATE NOT REACHED",f" after {iter} iterations \n" )

print(f"TOTAL STATE EXPLORED {explored}\n")    

print("TOTAL TIME TAKEN: ", end_time - start_time , "seconds")
