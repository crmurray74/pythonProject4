# fixed program.
cont = True
while cont:
    number = int(input("Please enter a number to get the square root or enter 0 to exit: "))
    if number == 0:
        cont = False
        break
    print("Square of {} is {}".format(number, number * number))
print("Good Bye!")
