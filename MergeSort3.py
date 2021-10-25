import random
import timeit

listRange = 1000

def my_function(random_number):
    return [random.uniform(0,10000) for x in range(random_number)]

 
my_random_number = my_function(listRange)
new_list = list()

print("Neserazeny seznam:")
print(my_random_number)


def mergeSort(myList):
    if len(myList) > 1:
        halfLength = len(myList) // 2
        
        leftList = myList[:halfLength]
        rightList = myList[halfLength:]

        mergeSort(leftList)
        mergeSort(rightList)

        i = 0
        j = 0
        k = 0

        while i < len(leftList) and j < len(rightList):
            if leftList[i] <=  rightList[j]:
                myList[k] = leftList[i]
                i += 1
            else:
                myList[k] = rightList[j]
                j += 1
            k += 1

        while i < len(leftList):
            myList[k] = leftList[i]
            i += 1
            k += 1

        while j < len(rightList):
            myList[k] = rightList[j]
            j += 1
            k += 1
start_time = timeit.default_timer()
mergeSort(my_random_number)
stop_time = timeit.default_timer() - start_time
print("Serazeny seznam: ")
print(my_random_number)
print("Cas vykonani: ")
print(stop_time)
