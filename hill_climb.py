# Implement the algorithm here
import random
import math
import time
import numpy as np

def hillClimb(data):
    N = 24
    city_ending_list = []
    start_list = list(range(0,N))
    random.shuffle(start_list)
    distance = math.inf 
    teller = 0
    
    while(teller < N*N):
        for p in range(len(start_list)-1):
            for a in range(len(start_list)-1):

                swap(start_list[p], start_list[a], start_list)
                temp = findDistance(start_list)

                if temp < distance: 
                    distance = temp
                    teller = 0

                else:
                    swap(start_list[a],start_list[p], start_list)
                    teller += 1
        
    for i in start_list:
        city_ending_list.append(data[0][i])
    
    return distance,city_ending_list

def swap(index1, index2, start_list):
    ind1 = start_list.index(index1)
    ind2 = start_list.index(index2)
    start_list[ind1] , start_list[ind2] = start_list[ind2] , start_list[ind1]
    return start_list
    

def findDistance(lists):
    temp_distance = 0
    first = lists[0]
    last = lists[-1]
    temp_distance = temp_distance + float(data[first+1][last])
        
    for i in range(0,len(lists)-1):
        temp_distance = temp_distance + float(data[lists[i]+1][lists[i+1]])
    return temp_distance

t1 = time.time()
global_distance = math.inf
worst_distance = - math.inf
distance_list = []
best_list = []
worst_list = []

for i in range(20):
    distance,city_ending_list = hillClimb(data)
    distance_list.append(distance)
    
    if distance < global_distance: 
        global_distance = distance
        best_list = city_ending_list
    
    if distance > worst_distance: 
        worst_distance = distance
        worst_list = city_ending_list
        
print("The worst path we found: ")
plot_plan(worst_list)
print("With the distance: " , worst_distance)
print("The best path we found: ")
plot_plan(best_list)
print("With the distance: " , global_distance)

mean = np.mean(distance_list)
std = np.std(distance_list)

print("The mean is: ", mean)
print("The standard deviation is: ", std)
t2 = time.time()
sec = (t2-t1)
print("Time used: " , sec)
    
