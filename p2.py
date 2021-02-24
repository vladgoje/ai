import math

ax = int(input("aX = "))
ay = int(input("aY = "))
bx = int(input("bX = "))
by = int(input("bY = "))

sx = bx - ax
sy = by - ay 
dist = math.sqrt(sx * sx + sy * sy)

print("Distanta: " + str(dist))
