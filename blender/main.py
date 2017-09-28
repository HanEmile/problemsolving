import numpy as np

# arr_size has to be a positive even integer
arr_size = 8

# initialize array
arr = np.zeros((arr_size + 1, arr_size + 1))

# initialize corner values
arr[0, 0] =                 3
arr[0, arr_size] =          3
arr[arr_size, 0] =          3
arr[arr_size, arr_size] =   3

# executes the diamond step
def diamond_step( a, b ):
    print("a: " + str(a))
    print("b: " + str(b))

    # define corner coortinates
    pa = arr[a[0], a[1]]
    pb = arr[b[0], b[1]]
    pc = arr[a[0], b[1]]
    pd = arr[b[0], a[1]]

    print("pa: " + str(a[0]) + " " + str(a[1]) )
    print("pb: " + str(b[0]) + " " + str(b[1]) )
    print("pc: " + str(a[0]) + " " + str(b[1]) )
    print("pd: " + str(b[0]) + " " + str(a[1]) )

    print("")

    # find the middle of the selected field
    mag = int( ( b[1] - a[1] ) / 2 )

    # assign the average value to the midpoint
    arr[a[0] + mag , a[1] + mag] = (pa + pb + pc + pd) / 4

# depth 1
arr_s = int(arr_size)
diamond_step( [0, 0], [arr_s, arr_s] )

# depth 2
arr_s2 = int(arr_size / 2)
diamond_step( [0, 0], [arr_s2, arr_s2] )
diamond_step( [0, arr_s2], [arr_s2, arr_size] )
diamond_step( [arr_s2, 0], [arr_size, arr_s2] )
diamond_step( [arr_s2, arr_s2], [arr_size, arr_size] )

arr_s4 = int(arr_size / 4)

# print the array
print("\n" + str(arr))


# diamond_step(a, b)

# a O O O O
# O O O O O
# O O O O O
# O O O O O
# O O O O b

# 1. Find the Midpoint X

# a O O O O
# O O O O O
# O O X O O
# O O O O O
# O O O O b

# 2. Find the other two points of the rectangle

# a O O O c
# O O O O O
# O O X O O
# O O O O O
# d O O O b

# 3. Assign X the Value of the average of a, b, c and d

# 4. Define new Values e, f, g and h

# a O f O c
# O O O O O
# e O X O g
# O O O O O
# d O h O b

# 4. Repeat for aX, fg, Xb and eh
