import random
import timeit

listRange = 15

def my_function(random_number):
    return [random.uniform(0,10000) for x in range(random_number)]

 
my_random_number = my_function(listRange)

print("Neserazeny seznam:")
print(my_random_number)
def bubbleSort(myList):
    idx = 0

    notSort = True

    #for idx2 in range(50):
    while notSort == True:
        iteration = 0
        for idx in range(listRange-1):
                         
            if myList[idx+1] < myList[idx]:
                smaller = myList[idx]
                bigger = myList[idx+1]
                myList[idx] = bigger
                myList[idx+1] = smaller
                
                
        for i in range(listRange-1):
            if myList[i+1] < myList[i]:
                
                iteration += 1
                #print(iteration)
        if iteration == 0:
            notSort = False 
        
           
        
            #my_random_number[idx+1] = my_random_number[idx]
start_time = timeit.default_timer()
bubbleSort(my_random_number)
stop_time = timeit.default_timer() - start_time
print("Serazeny seznam:")        
print(my_random_number)
print("Cas vykonani: ")
print(stop_time)
