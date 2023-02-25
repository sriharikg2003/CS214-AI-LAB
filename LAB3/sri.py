
import numpy as np
import time
import sys
from numpy import inf

def data_process(filename):
    
    with open(file_name, "r") as file:
        lines = file.read().strip().splitlines()
        type=lines[0]
        no_of_cities=int(lines[1])
        coordinate_array=[[0 for _ in range(2)] for _ in range(no_of_cities)]
        i=2
        for var in range(no_of_cities):
            coordinate_array[var][0]=float(lines[i].split()[0])
            coordinate_array[var][1]=float(lines[i].split()[1])
            i+=1
        _=0
        distance_matrix = [[0 for _ in range(no_of_cities)] for _ in range(no_of_cities)]

        temp=no_of_cities+2
        for i in range(no_of_cities):
            for j in range(no_of_cities):
                distance_matrix[i][j]=float(lines[temp].split()[j])
            temp+=1
    return coordinate_array,distance_matrix

i=0
j=0
k=0
a=0
b=0
q=0
z=0


# file_name=sys.argv[1]
file_name="euc_100"
start =time.time()
coordinate_array,distance_matrix=data_process(file_name)
end=time.time()
print(end-start)

d_array=np.array(distance_matrix)


best_length = float('inf')
best_solution = None

num_of_cities=len(coordinate_array)
num_of_iterations=100
num_of_ants=5
alpha = 0.5
beta = 2
rho = 0.9
Q=1000

random_cities= np.random.choice(np.arange(0,num_of_cities), num_of_ants, replace=False)


# pheromone_matrix=np.random.rand(num_of_cities,num_of_cities)

pheromone_matrix=np.ones((num_of_cities, num_of_cities))


visibility_matrix=1/d_array
visibility_matrix[visibility_matrix==inf]=0

best_so_far=inf

no_of_iterations=2

new_time=time.time()

# while(time.time()-new_time < 280):
for num_of_iterations in range(100):
    print(f"RUNNING ITERATIONS {no_of_iterations}")
    
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
                
            
            for c in range(num_of_cities):
                
                if c not in path:
                    
                    pro=(pheromone_matrix[current_city][c]**(alpha))*(visibility_matrix[current_city][c]**beta)/denum
                    
                    if pro > max_pro:
                        
                        max_pro = pro
                        index = c
            
            path.append(index)
            # cost += distance_matrix[current_city][index]
            print(f" {pheromone_matrix[current_city][index]-Q/distance_matrix[current_city][index]}")

            pheromone_matrix[current_city][index]+=(Q/distance_matrix[current_city][index])
            
            if len(path) == num_of_cities:
                pheromone_matrix[index][current_city]+=pheromone_matrix[index][current_city]
            current_city=index

        for theta in range(len(path)):

            cost+=distance_matrix[path[theta]][path[(theta+1)%len(path)]]
            
           
        paths_of_ants.append(path)
        
        cost_array.append(cost)
        
        if cost < best_so_far :
            
            best_so_far = cost
            best_solution = path
    print(f"COST NOW IS {cost}")        
    print(f"BEST : {best_so_far} in iteration {no_of_iterations}")
    print(f"\n\nTIME RUNNING : {time.time()-new_time}")
    # for z in range(num_of_cities):

    #             for q in range(num_of_cities):

    #                 pheromone_matrix[z][q] = pheromone_matrix[z][q]*(1-rho)
    pheromone_matrix*=(1-rho)

    # for road in paths_of_ants:

        # for o in range(len(road)):

        #     pheromone_matrix[road[o]][road[(o+1)%len(road)]]+=(Q/cost)
    no_of_iterations+=1
     
print(f"\n\nTIME RUNNING : {time.time()-new_time}")

print("BEST LENGTH ",best_so_far) 

