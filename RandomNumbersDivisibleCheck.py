import random
import numpy as np

def is_count_int(count):
  while True:
    count = input("Въведете брой числа, които да се генерират:\n")
    try:
      int(count) #проверяваме дали е цяло число
      return count
      break
    except:
      print("Въведете цяло число!\n")

def is_divisor_int(divisor):
  while True:
    divisor = input("Въведете делител:\n")
    try:
      int(divisor) #проверяваме дали е цяло число
      return int(divisor)
      break
    except:
      print("Въведете цяло число!\n")

def generate_nums(number, count, nums_list):
  for number in range(int(count)): #обхождаме броя числа
    number = random.randint(1, 100)
    nums_list.append(number)

def check_if_divisible(number, nums_list, divisor):
  if number % int(divisor) == 0: #ако числото се дели на делителя го добавяме към списъка с делящите се числа
      nums_list_2.append(number)

def print_initial_nums(nums_arr):
  print("Изтеглени числа:")
  print(np.array2string(nums_arr, separator=", ")) #принтираме изтеглените числа

def check_array_empty(nums_arr_2, divisor):
  if len(nums_arr_2) != 0: #ако масивът не е празен
    print("Числа, делящи се на {}:".format(divisor))
    print(np.array2string(nums_arr_2, separator=", ")) #принтираме делящите се числа
  else: #ако масивът е празен
    print("Няма числа, делящи се на {}".format(divisor))

nums_arr = np.array([])
nums_arr_2 = np.array([])
nums_list = []
nums_list_2 = []
count = 0
divisor = 1
number = 0

count = is_count_int(count)

divisor = is_divisor_int(divisor)

generate_nums(number, count, nums_list)
check_if_divisible(number, nums_list, divisor)

#пълним масивите с данните от списъците:
nums_arr = np.array(nums_list)
nums_arr_2 = np.array(nums_list_2)

print_initial_nums(nums_arr)

check_array_empty(nums_arr_2, divisor)
