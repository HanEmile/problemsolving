# problemsolving
Repo for the various solutions of problemsolving websites and personal problems
that are to be solved.


### Project Euler:
- [Project Euler](https://projecteuler.net)


### Blender
- Terrain Generation using the Diamond-square algorithm
```
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
```
