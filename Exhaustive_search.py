# Implement the algorithm here
from itertools import permutations
import math
import time

def TSP(data):
    t1 = time.time()
    N = 10
    city_dict = {}
    j = 0;
    for city in data[0]:
        j += 1
        city_dict[city] = data[j][:]

    cities = list(range(0,N))
    
    perm_cities = permutations(cities)
    
    distance = math.inf
    
    temp_distance = 0
    best_list = []
    city_ending_list = []
    
    for lists in perm_cities:
        
        first = lists[0]
        last = lists[-1]
        temp_distance = temp_distance + float(data[first+1][last])
        
        for i in range(0,len(lists)-1):
        
            if temp_distance > distance:
                break
                
            temp_distance = temp_distance + float(data[lists[i]+1][lists[i+1]])
        
        if temp_distance < distance: 
                distance = temp_distance
                best_list = lists
                
        temp_distance = 0
    
    for i in best_list:
        city_ending_list.append(data[0][i])
    
    t2 = time.time()
    sec = (t2-t1)
    print(distance)
    print("Time: " , sec)
    plot_plan(city_ending_list)
    
        
TSP(data)  