# Implement the algorithm here
import random
import math
import time

def main(N,M,N_best,byer):
    pop_list = []
    lst = list(range(0,byer))
    
    for i in range(N):
        random.shuffle(lst)
        pop_list.append(lst[:])
    
    best = 0
    
    for i in range(M):
        pop_list = generic(N,pop_list)
        best = findDistance(pop_list[0])
        N_best[i] += best
    return N_best,pop_list[0],pop_list[-1],best

def generic(N,pop_list):
    for i in range(0,N,2):
        child1, child2 = pmx(pop_list[i],pop_list[i+1])
        if child1 not in pop_list:
            pop_list.append(child1)
        if child2 not in pop_list:
            pop_list.append(child2)
    new_pop = sorted(pop_list,key = findDistance)
    return new_pop[:N]
 
def pmx(parent1, parent2):
    length = len(parent1)
    p1, p2 = sorted([random.randint(0, length-1) for _ in range(2)])

    offspring1 = parent1.copy()
    offspring2 = parent2.copy()

    for i in range(p1, p2):
        gene = parent2[i]
        idx = parent1.index(gene)
        offspring1[i], offspring1[idx] = offspring1[idx], offspring1[i]

        gene = parent1[i]
        idx = parent2.index(gene)
        offspring2[i], offspring2[idx] = offspring2[idx], offspring2[i]
    return offspring1, offspring2

def findDistance(lists):
    temp_distance = 0
    first = lists[0]
    last = lists[-1]
    temp_distance = temp_distance + float(data[first+1][last])
        
    for i in range(0,len(lists)-1):
        temp_distance = temp_distance + float(data[lists[i]+1][lists[i+1]])
    return temp_distance

t1 = time.time()
#Plotter for 10 byer først med 10 i populasjon
M = 100
N_best = [0] * M

for i in range(20):  
    city_ending_list = []
    best_list, best_path, worst_path, best_distance = main(10,M,N_best,10)

average1 = np.array(best_list)/20

for i in best_path:
    city_ending_list.append(data[0][i])
    
mean = np.mean(best_list)
std = np.std(best_list)
    
print("Population of 10: \n")
print("The best path we found: ")
plot_plan(city_ending_list)
print("With the distance: " , best_distance)
    
print("The worst we found was: " , best_list[-1])
print("The mean was: ", mean)
print("The standard deviation was: ", std)

#For 10 byer med 50 i populasjon
N_best = [0] * M
for i in range(20):  
    city_ending_list = []
    best_list, best_path, worst_path, best_distance = main(50,M,N_best,10)

average2 = np.array(best_list)/20
    
for i in best_path:
    city_ending_list.append(data[0][i])
    
mean = np.mean(best_list)
std = np.std(best_list)
    
print("Population of 50 \n")
print("The best path we found: ")
plot_plan(city_ending_list)
print("With the distance: " , best_distance)
    
print("The worst we found was: " , best_list[-1])
print("The mean was: ", mean)
print("The standard deviation was: ", std)

#For 10 byer med 100 i populasjon
N_best = [0] * M
for i in range(20):  
    city_ending_list = []
    best_list, best_path, worst_path, best_distance = main(100,M,N_best,10)


average3 = np.array(best_list)/20

for i in best_path:
    city_ending_list.append(data[0][i])
    
mean = np.mean(best_list)
std = np.std(best_list)

    
print("Population of 100 \n")
print("The best path we found: ")
plot_plan(city_ending_list)
print("With the distance: " , best_distance)
    
print("The worst we found was: " , best_list[-1])
print("The mean was: ", mean)
print("The standard deviation was: ", std)

plt.plot(range(0,M),average1,label='Population 10')
plt.plot(range(0,M),average2,label='Population 50')
plt.plot(range(0,M),average3,label='Population 100')
plt.xlabel("Generations")
plt.ylabel("Distance")
plt.legend()
plt.show()

#Plotter for 24 byer først med 10 i populasjon
for i in range(20):  
    city_ending_list = []
    best_list, best_path, worst_path, best_distance = main(10,M,N_best,24)

average4 = np.array(best_list)/20

for i in best_path:
    city_ending_list.append(data[0][i])
    
mean = np.mean(best_list)
std = np.std(best_list)
    
print("For 20 runs: \n")
print("The best path we found: ")
plot_plan(city_ending_list)
print("With the distance: " , best_distance)
    
print("The worst we found was: " , best_list[-1])
print("The mean was: ", mean)
print("The standard deviation was: ", std)

#For 24 byer med 50 i populasjon
N_best = [0] * M

for i in range(20):  
    city_ending_list = []
    best_list, best_path, worst_path, best_distance = main(50,M,N_best,24)

average5 = np.array(best_list)/20

for i in best_path:
    city_ending_list.append(data[0][i])
    
mean = np.mean(best_list)
std = np.std(best_list)
    
print("For 20 runs: \n")
print("The best path we found: ")
plot_plan(city_ending_list)
print("With the distance: " , best_distance)
    
print("The worst we found was: " , best_list[-1])
print("The mean was: ", mean)
print("The standard deviation was: ", std)

#For 24 byer med 100 i populasjon
N_best = [0] * M

for i in range(20):
    city_ending_list = []
    best_list, best_path, worst_path, best_distance = main(100,M,N_best,24)

average6 = np.array(best_list)/20

for i in best_path:
    city_ending_list.append(data[0][i])
    
mean = np.mean(best_list)
std = np.std(best_list)
    
print("For 20 runs: \n")
print("The best path we found: ")
plot_plan(city_ending_list)
print("With the distance: " , best_distance)
    
print("The worst we found was: " , best_list[-1])
print("The mean was: ", mean)
print("The standard deviation was: ", std)

plt.plot(range(0,M),average4,label='Population 10')
plt.plot(range(0,M),average5,label='Population 50')
plt.plot(range(0,M),average6,label='Population 100')
plt.xlabel("Generations")
plt.ylabel("Distance")
plt.legend()
plt.show()

t2 = time.time()
sec = t2-t1
print("Time total: ", sec)
