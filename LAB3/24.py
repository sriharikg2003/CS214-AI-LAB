#AUTHOR : SRIHARI AND TEJAS
import numpy as np
import time
import sys
from numpy import inf
def data_process(filename):
    
    with open(file_name, "r") as file:
        print("Processing FILE")
        lines = file.read().strip().splitlines()
        type=lines[0]
        no_of_cities=int(lines[1])
        coordinate_array=[[0 for _ in range(2)] for _ in range(no_of_cities)]
        i=2
        for var in range(no_of_cities):
            i+=1
        _=0
        distance_matrix = [[0 for _ in range(no_of_cities)] for _ in range(no_of_cities)]

        temp=no_of_cities+2
        for i in range(no_of_cities):
            for j in range(no_of_cities):
                distance_matrix[i][j]=float(lines[temp].split()[j])
            temp+=1
    print(f"FILE PROCESS OVER")
    return coordinate_array,distance_matrix


def output(path):
    for i in path:
        print(i,end=" ")
    return 

file_name=sys.argv[1]
# file_name="noneuc_100"

coordinate_array,distance_matrix=data_process(file_name)


d_array=np.array(distance_matrix)


best_length = float('inf')
best_solution = None

num_of_cities=len(coordinate_array)
num_of_iterations=25

Q=num_of_cities**3


num_of_ants=5
alpha = 0.3
beta = 20
rho = 0.5


pheromone_matrix=np.ones((num_of_cities, num_of_cities))*4/10


visibility_matrix=1/d_array
visibility_matrix[visibility_matrix==inf]=0

best_so_far=inf

no_of_iterations=0

new_time=time.time()
print(f"ITERATION ABOUT TO START\n\n\n")
while(time.time()-new_time < 290):
 
    
    paths_of_ants=[]
    cost_array=[]
    
    for a in range(num_of_ants):
        
        current_city =  np.random.randint(num_of_cities)

        path=[current_city]
        
        cost=0
                
        
        
        while(len(path)<num_of_cities):
            
            max_pro=0
            
            denum=0
            
            for b in range(num_of_cities):
                
                if b not in path:
                    
                    denum +=(pheromone_matrix[current_city][b]**alpha)*(visibility_matrix[current_city][b]**beta)

            if denum==0:
                    break        
            
            for c in range(num_of_cities):
                
                if c not in path:
                    
                    pro=(pheromone_matrix[current_city][c]**(alpha))*(visibility_matrix[current_city][c]**beta)/denum
                    
                    if pro > max_pro:
                        
                        max_pro = pro
                        index = c
            
            path.append(index)
            if (distance_matrix[current_city][index])==0:
                break
            
            pheromone_matrix[current_city][index]+=(Q/(distance_matrix[current_city][index]))
            cost+=distance_matrix[current_city][index]

            if(len(path)==(num_of_cities)):
                cost+=distance_matrix[path[0]][path[-1]] 
            if (best_solution):
                if(len(best_solution)==num_of_cities):
                    if(num_of_cities<250):
                        for w in range(num_of_cities):
                            pheromone_matrix[best_solution[w]][best_solution[(w+1)%num_of_cities]]+=(Q**2/(distance_matrix[best_solution[w]][best_solution[(w+1)%num_of_cities]]))           
             
            current_city=index
           
        paths_of_ants.append(path)
        
        cost_array.append(cost)
        
        if cost < best_so_far :
            if(len(path)==num_of_cities):
                best_so_far = cost
                best_solution = path
                print(f"\n***************************************")
                print(f"\n\nBEST COST: {best_so_far}\n")
                print(f"\n\nBEST PATH : \n")
                output(best_solution)
                print("\n")


    pheromone_matrix=(1*rho)*pheromone_matrix
    no_of_iterations+=1
if(len(path)==num_of_cities):    
    print(f"\n\n\n\n***************************************")
    print(f"\n*****************CONCLUSION*************")
    print(f"BEST COST: {best_so_far}")
    print(f"\n\nBEST PATH : \n")
    output(best_solution)


# # To verify best so path  

def cost(array,distance_matrix):
    cost=0
    for i in range(len(array)-1):
        cost+= distance_matrix[array[i]][array[i+1]]
   
    cost+=distance_matrix[array[-1]][array[0]]
    return cost
if(len(path)==num_of_cities):    
    print("\n COST  + ",cost(best_solution,distance_matrix))



