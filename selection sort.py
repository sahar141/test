# selection sort
import time

startTime = time.time()


def selection_sort(user_list):
    indexing_length = range(0, len(user_list) - 1)
    for i in indexing_length:
        min_value = i
        for j in range(i + 1, len(user_list)):
            if user_list[j] < user_list[min_value]:
                min_value = j

            if min_value != i:
                user_list[min_value], user_list[i] = user_list[i], user_list[min_value]
    return user_list


# print(selection_sort([8, 5, 2, 1]))

user_list = input('enter your numbers:')
print("\n")
user_list = user_list.split()

print(f'Numbers entered by the user : {user_list} ')
print(f'Sorted numbers : {selection_sort(user_list)}')

executionTime = (time.time() - startTime)
print(f'Execution time in seconds:{str(executionTime)}')
