

from copy import deepcopy
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


class State:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.stack3 = Stack()    


def heuristic_1(noob,goal):
    ans = 0
    for x in noob.stack1.list : 
        if x in goal.stack1.list : 
            ans +=1 
            if noob.stack1.list.index(x) == goal.stack1.list.index(x) :
                ans += 1
            else : 
                ans -= 0 
        else : 
            ans -= 2

    for x in noob.stack2.list : 
        if x in goal.stack2.list : 
            ans +=1 
            if noob.stack2.list.index(x) == goal.stack2.list.index(x) :
                ans += 1
            else : 
                ans -= 0
        else : 
            ans -= 2

    for x in noob.stack3.list : 
        if x in goal.stack3.list : 
            ans +=1 
            if noob.stack3.list.index(x) == goal.stack3.list.index(x) :
                ans += 1
            else : 
                ans -= 0 
        else : 
            ans -= 2

    return ans 


# start_stiring = "CBA,DE,"
"""
    initial state : 
    C 
    B D
    A E
"""
# goal_string = "BA,E,CD"
"""
    B   C
    A E D
"""
with open("input1.txt", "r") as file:
    lines = file.read().strip().splitlines()
    start_stiring = lines[0].strip()    
    goal_string = lines[1].strip()

s1 = Stack()
s2 = Stack()
s3 = Stack()


start_split = start_stiring.split(",")
# print("start state is : ")
# print(start_split)
s1.list = list((start_split[0])[::-1])
s2.list = list((start_split[1])[::-1])
s3.list = list((start_split[2])[::-1])


g1 = Stack()
g2 = Stack()
g3 = Stack()

goal_split = goal_string.split(",")
g1.list = list((goal_split[0])[::-1])
g2.list = list((goal_split[1])[::-1])
g3.list = list((goal_split[2])[::-1])
# print("goal state is : ")
# print(goal_split)


initial = State() 
initial.stack1 = s1
initial.stack2 = s2
initial.stack3 = s3

final = State() 
final.stack1 = g1
final.stack2 = g2
final.stack3 = g3

def moveGen(current_state):
    nbr = []
    nbr_current = deepcopy(current_state)
    if(nbr_current.stack1.list):
        move = nbr_current.stack1.pop()
        nbr_current.stack2.push(move)
        nbr.append(deepcopy(nbr_current))
    
    nbr_current = deepcopy(current_state)
    if(nbr_current.stack1.list):
        move = nbr_current.stack1.pop()
        nbr_current.stack3.push(move)
        nbr.append(deepcopy(nbr_current))
    
    nbr_current = deepcopy(current_state)
    if(nbr_current.stack2.list):
        move = nbr_current.stack2.pop()
        nbr_current.stack1.push(move)
        nbr.append(deepcopy(nbr_current))
    
    nbr_current = deepcopy(current_state)
    if(nbr_current.stack2.list):
        move = nbr_current.stack2.pop()
        nbr_current.stack3.push(move)
        nbr.append(deepcopy(nbr_current))

    nbr_current = deepcopy(current_state)
    if(nbr_current.stack3.list):
        move = nbr_current.stack3.pop()
        nbr_current.stack1.push(move)
        nbr.append(deepcopy(nbr_current))
    
    nbr_current = deepcopy(current_state)
    if(nbr_current.stack3.list):
        move = nbr_current.stack3.pop()
        nbr_current.stack2.push(move)
        nbr.append(deepcopy(nbr_current))
    
    return nbr
print("START STATE HEURISTIC IS :" , heuristic_1(initial , final),"\n")
print("INITIAL CONFIGURATION :" , start_split,"\n")
print("FINAL CONFIGURATION : " , goal_split,"\n")
print("***********HILL CLIMBING STARTS*************","\n")
start_time = time.time()
it = 0
best=heuristic_1(initial, final)
while(True):

    neighbours = moveGen(initial)
    neighbours_heuristic = [heuristic_1(i, final) for i in neighbours]
    if(best >=max(neighbours_heuristic)):
        print("Goal state not achieved !","\n")
        break
    else : 
        best = max(neighbours_heuristic)

    num = neighbours_heuristic.index(max(neighbours_heuristic))
    initial = neighbours[num]
    
    print("BEST CONFIGURATION SO FAR :" , end = " : ")
    
    print("[" , end = "")
    for x in initial.stack1.list : 
        print(x , end = " ")
    print("]" , end = "")

    print("[" , end = "")
    for x in initial.stack2.list : 
        print(x , end = " ")
    print("]" , end = "")

    print("[" , end = "")
    for x in initial.stack3.list : 
        print(x , end = " ")
    print("]" , end = "")

    print("\n")
    it+=1
    if(heuristic_1(initial , final) == heuristic_1(final,final)):
        print("\nGoal state achieved in" , it , "iterations ")
        end_time = time.time()
        print("\nTOTAL TIME TAKEN: ", end_time - start_time , "seconds")
        break
    