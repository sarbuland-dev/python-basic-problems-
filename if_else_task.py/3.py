while True:
    try:
        x = int(input("Enter your first side: "))
        y = int(input("Enter your second side: "))
        z = int(input("Enter your third side: "))

        
        if x <= 0 or y <= 0 or z <= 0:
            print("Plz enter positive integer values")
            continue

        
        if (x + y) <= z or (x + z) <= y or (y + z) <= x:
            print("This is Invalid triangle")
        elif x == y == z:
            print("This is Equilateral triangle")
        elif x == y or y == z or z == x:
            print("This is Isosceles triangle")
        else:
            print("This is Scalene triangle")

    except ValueError:
        print("Plz enter values in integer form only")

