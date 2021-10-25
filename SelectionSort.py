import random
import timeit

listRange = 15

def my_function(random_number):
    return [random.uniform(0,10000) for x in range(random_number)]

my_random_number2 = listRange* [0]  
my_random_number = my_function(listRange)
#my_random_number2 = my_random_number
print("Neserazeny seznam:")
print(my_random_number)
def selectionSort(myList):
    for idx in range(listRange):
    #print(my_random_number[idx])
        my_random_number2[idx] = min(myList)
        my_random_number.remove(min(myList))
        
       
        #smaller = my_random_number[idx+1]
       # my_random_number[idx] = smaller
        #my_random_number[idx+1] = bigger
start_time = timeit.default_timer()
selectionSort(my_random_number)
stop_time = timeit.default_timer() - start_time
print("Serazeny seznam:")        
print(my_random_number2)
print("Cas vykonani: ")
print(stop_time)
