import random
import timeit

def make_list(size):
    test_list = []
    for _ in range(size):
        number = random.randint(-10000, 10000)
        test_list.append(number)
    return test_list

list_1 = make_list(100)
list_2 = make_list(200)
list_3 = make_list(300)
list_4 = make_list(400)
list_5 = make_list(500)
list_6 = make_list(600)
list_7 = make_list(700)
list_8 = make_list(800)
list_9 = make_list(900)
list_10 = make_list(1000)
list_11 = make_list(1100)
list_12 = make_list(1200)
list_13 = make_list(1300)
list_14 = make_list(1400)

def stoogesort(arr, low = None, high = None):
    if high == None:
        high = len(arr) - 1 
        low = 0

    if low >= high:
        return

    # swap if lower value is greater than higher value
    if arr[low] > arr[high]:
        temp = arr[low]
        arr[low] = arr[high]
        arr[high] = temp

    if (high-low + 1) > 2:

        # one third of array
        third = (high-low + 1)//3

        # first two third
        stoogesort(arr, low, high-third)
        # second two third
        stoogesort(arr, low+third, high)

        # first two third again
        stoogesort(arr, low, high-third)

print(f"Array Size: 100   | Sort Time: {timeit.timeit(lambda: stoogesort(list_1), number=1)}")
print(f"Array Size: 200   | Sort Time: {timeit.timeit(lambda: stoogesort(list_2), number=1)}")
print(f"Array Size: 300   | Sort Time: {timeit.timeit(lambda: stoogesort(list_3), number=1)}")
print(f"Array Size: 400   | Sort Time: {timeit.timeit(lambda: stoogesort(list_4), number=1)}")
print(f"Array Size: 500   | Sort Time: {timeit.timeit(lambda: stoogesort(list_5), number=1)}")
print(f"Array Size: 600   | Sort Time: {timeit.timeit(lambda: stoogesort(list_6), number=1)}")
print(f"Array Size: 700   | Sort Time: {timeit.timeit(lambda: stoogesort(list_7), number=1)}")
print(f"Array Size: 800   | Sort Time: {timeit.timeit(lambda: stoogesort(list_8), number=1)}")
print(f"Array Size: 900   | Sort Time: {timeit.timeit(lambda: stoogesort(list_9), number=1)}")
print(f"Array Size: 1000  | Sort Time: {timeit.timeit(lambda: stoogesort(list_10), number=1)}")
print(f"Array Size: 1100  | Sort Time: {timeit.timeit(lambda: stoogesort(list_11), number=1)}")
print(f"Array Size: 1200  | Sort Time: {timeit.timeit(lambda: stoogesort(list_12), number=1)}")
print(f"Array Size: 1300  | Sort Time: {timeit.timeit(lambda: stoogesort(list_13), number=1)}")
print(f"Array Size: 1400  | Sort Time: {timeit.timeit(lambda: stoogesort(list_14), number=1)}")


