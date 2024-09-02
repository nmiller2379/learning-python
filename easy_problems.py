# You are given two vectors starting from the origin (x=0, y=0) with coordinates (x1,y1) and (x2,y2). Your task is to find out if these vectors are collinear. Collinear vectors are vectors that lie on the same straight line. They can be directed in the same or opposite directions. One vector can be obtained from another by multiplying it by a certain number. In terms of coordinates, vectors (x1, y1) and (x2, y2) are collinear if (x1, y1) = (k*x2, k*y2) , where k is any number acting as a coefficient.

# For the vectors to be collinear, the following equations must be true:
# 𝑥1 = 𝑘*𝑥2
# y1 = k*y2

# restate this
# k1 = x1/x2
# k2 = y1/y2

# Output: Boolean indicating whether vectors are collinear.
# Input: Four numbers, each represening x1, y1 and x2, y2)

# Examples:
# (1,1,1,1) ➞ true
# (1,2,2,4) ➞ true
# (1,1,6,1) ➞ false
# (1,2,-1,-2) ➞ true
# (1,2,1,-2) ➞ false
# (4,0,11,0) ➞ true
# (0,1,6,0) ➞ false
# (4,4,0,4) ➞ false
# (0,0,0,0) ➞ true
# (0,0,1,0) ➞ true
# (5,7,0,0) ➞ true

# Withi this example,(1,1,1,1) ➞ true, the equation would be
# x1 = 1, y1 = 1
# x2 = 1, y2 = 1
# Equations
# 1 = k * 1
# 1 = k * 1

# To solve for k in each equation, we would divide both sides of the equation by both sides of each equation by 1 (because that is what k is multiplied by. In this case both x2 and y2 are 1). That would give us 1/1 = k. This evaulates to k = 1. Since the value of k is true in both equations, we would return true.

# With this example, (5,7,0,0) ➞ true, the equations would be
# x1 = 5, y1 = 7
# x2 = 0, y2 = 0

# Equations
# 5 = k * 0
# 0 = k * 0 

# We don't really need the equtions here. Since one vector, in this case x2, y2 is 0,0, any line is colinear with it. If one vector is 0,0, we can return true out of the function.

# Algorithm
# If all four inputs equal each other, return true
# If inputs include 0
    # If args[0] and args[2] equal 0, or args[1] and args[3] return true
    # else return false
# If neither of those early returns happen, calculate k for both equations 
# Return the result of comparing the two values of k

def collinearity(x1, y1, x2, y2):
    if (x1 == y1 and x2 == y2):
        return True
    args = [x1, y1, x2, y2]
    count_zeros = 0
    for num in args:
        if (num == 0):
            count_zeros += 1
    if (count_zeros == 1):
        return False
    if (count_zeros == 2):
        if ((x1 and x2 == 0) or (y1 and y2 ==0)):
            return True
        else:
            return False
    if (count_zeros > 2):
        return True
    k1 = x1/x2
    k2 = y1/y2
    return k1 == k2
    

print(collinearity(0,0,1,0)) # True
print(collinearity(1,2,2,4)) # True
print(collinearity(1,1,6,1)) # False
print(collinearity(1,2,-1,-2)) # True
print(collinearity(0,1,6,0)) # False -- Need to fix this one. Not sure why it's not working.

    