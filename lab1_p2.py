import math

def testP2():
    assert distanta(1, 5, 4, 1) == 5
    assert distanta(1, 1, 1, 1) == 0
    assert distanta(1, 2, 13, 7) == 13

def distanta(ax, ay, bx, by):
    sx = bx - ax
    sy = by - ay 
    return math.sqrt(sx * sx + sy * sy)

def main():
    ax = int(input("aX = "))
    ay = int(input("aY = "))
    bx = int(input("bX = "))
    by = int(input("bY = "))
    print("Distanta: " + str(distanta(ax, ay, bx, by)))


testP2()
main()
