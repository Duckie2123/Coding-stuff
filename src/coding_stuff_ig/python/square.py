def check_square():
    values = list(map(int, input("Give four numbers: ").split(",")))

    if len(values) != 4:
        print("You did not give four numbers. Try again.")
        return

    if values[0] == values[1] == values[2] == values[3]:
        area = values[0] * values[1]
        perimeter = 4 * values[0]
        print("These numbers can create a square.")
        print("The area of the square is", area, "and the perimeter is", perimeter)
    else:
        print("These numbers cannot create a square.")

check_square()