"""This programs take input of inches and converts to feet"""
def convert_inches_to_feet(inches):
    INCHES_IN_FEET = 12
    feet = inches / INCHES_IN_FEET
    return int(feet)
    # fix test_twenty_four_inches


if __name__ == '__main__':
    print("Hello!")
    print("28 inches is " + str(convert_inches_to_feet(28)) + " feet")
