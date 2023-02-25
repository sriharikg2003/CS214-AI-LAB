import numpy as np
import time
import sys



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


file_name=sys.argv[1]
start =time.time()
coordinate_array,distance_matrix=data_process(file_name)
end=time.time()
print(end-start)


//

#ACO
for i in range(num_of_iterations):
     
    paths_of_ants=[]
    cost_array=[]
    
    for j in range(num_of_ants):
        
        current_city =  np.random.randint(num_of_cities)
        
        path=[current_city]
        
        cost=0
        
        while(len(path)<num_of_cities):
            
            max_pro=0
            
            denum=0
            
            for k in range(num_of_cities):
                
                if k not in path:
                    
                    denum +=(pheromone_matrix[current_city][k]**alpha)*(visibility_matrix[current_city][k]**beta)
                
            
            for k in range(num_of_cities):
                
                if k not in path:
                    
                    pro=(pheromone_matrix[current_city][k]**(alpha))*(visibility_matrix[current_city][k]**beta)/denum
                    
                    if pro > max_pro:
                        
                        max_pro = pro
                        index = k
            
            path.append(index)
            cost += distance_matrix[current_city][index]
            
            current_city=index
            
           
        paths_of_ants.append(path)
        cost_array.append(cost)
    
     
    for i in range(num_of_cities):
        
        for j in range(num_of_cities):
            
            pheromone_matrix[i][j] = pheromone_matrix[i][j]*(1-rho)
            
            
            
            
            