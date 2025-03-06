import time

startTime = time.time()


def bubble(user_list):
    indexing_length = len(user_list) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if user_list[i] > user_list[i + 1]:
                sorted = False
                user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]
    return user_list


#print(bubble([3, 2, 1, 9, 6]))

user_list = input('enter your numbers:')
print("\n")
user_list = user_list.split()

print(f'Numbers entered by the user : {user_list} ')
print(f'Sorted numbers : {bubble(user_list)}')

executionTime = (time.time() - startTime)
print(f'Execution time in seconds:{str(executionTime)}')
