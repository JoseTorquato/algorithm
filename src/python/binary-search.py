import random
import time

MAX_NUMBER = 1234567

number_list = list(range(0, MAX_NUMBER))
random_number = random.choice(number_list)

print(f"Random number: {random_number}/{len(number_list)}")

def simple_search(number_list, target):
    result = -1
    i = 0
    for number in number_list:
        if number == target:
            result = number
            break
        i += 1
    return result


def binary_search(number_list, target):
    min = 0
    max = len(number_list) - 1
    j = 0
    while min <= max:
        average = min + (max - min) // 2

        if number_list[average] == target: 
            return number_list[average]
        if number_list[average] < target:
            min = average + 1
        if number_list[average] > target: 
            max = average - 1
        
        j += 1
    
    return -1

start = time.perf_counter()
result = simple_search(number_list, random_number)
end = time.perf_counter()
elapsed = end - start
print(f'Time Simple Search: {elapsed:.6f} seconds')

start = time.perf_counter()
result = binary_search(number_list, random_number)
end = time.perf_counter()
elapsed = end - start
print(f'Time Binary Search: {elapsed:.6f} seconds')