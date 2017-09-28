import numpy as np

# arr_size has to be a positive even integer
arr_size = 4

# initialize array
arr = np.zeros((arr_size + 1, arr_size + 1))

# initialize corner values
arr[0, 0] =                 1
arr[0, arr_size] =          2
arr[arr_size, 0] =          1
arr[arr_size, arr_size] =   1

# def diamond_step():
#     # find midpoint of the array
#     mid = int( ( arr_size ) / 2 )
#
#     # print the x and y coortinate of the midpoint
#     print(mid)
#
#     # get the corner values
#     a = arr[mid - mid, mid - mid]
#     b = arr[mid - mid, mid + mid]
#     c = arr[mid + mid, mid - mid]
#     d = arr[mid + mid, mid + mid]
#
#     # find the average of the corner values
#     e = (a + b + c + d) / 4
#
#     # assign the median of the corner values to the center field
#     arr[mid, mid] = e
#
# diamond_step()

def diamond_step_proto(n, arr_size):
    n = n * 2
    mid = int( arr_size / n )

    print(mid)

diamond_step_proto(1, arr_size)

# print the array
print(arr)
