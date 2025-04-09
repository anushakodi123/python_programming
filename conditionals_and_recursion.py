def is_triangle():
    """
    This function checks if three sides can form a triangle.
    """
    a = int(input("Enter the length of side a: "))
    b = int(input("Enter the length of side b: "))
    c = int(input("Enter the length of side c: "))

    if a + b > c and a + c > b and b + c > a:
        print("The sides can form a triangle.")
    else:
        print("The sides cannot form a triangle.")

