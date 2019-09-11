"""This programs take input of inches and converts to feet"""
def convert_inches_to_feet(inches):
    INCHES_IN_FEET = 12
    if inches > 0:
        feet = inches / INCHES_IN_FEET
    else:
        feet = 0
    return int(feet)
    # fix test_twenty_four_inches


def addition():
    x = input("Enter a number")
    print('x = ' + str(x)) # print debug statement
    y = input("Enter another number")
    return x + y

if __name__ == '__main__':
    print("Hello!")
    print("-12 inches is " + str(convert_inches_to_feet(-12)) + " feet")
