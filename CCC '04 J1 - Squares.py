def Solution1():

    Area = int(input())

    import math

    sqrtarea = math.sqrt(Area)
    print(sqrtarea)
    if sqrtarea.is_integer() == True:
        print("The largest square has side length " + str(int(sqrtarea)) + ".")
    else:
        for i in range(1, Area):
            Otherarea = Area - i - 0.0
        if Otherarea.is_integer() == True:
            print("The largest square has side length " + str(math.sqrt(Otherarea)) + ".")
            
def Solution2():
    numberoftiles = int(input())
    sidelength = int(numberoftiles ** 0.5)
    print("The largest square has side length " + str(sidelength) + ".")


