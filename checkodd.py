def get_odd_number():
    try:
        num = int(input("Enter an odd number: "))
        if num % 2 == 0:
            print("This number is not odd\n")
            return get_odd_number()  # Call the function again if input is not odd
        else:
            print("This number is odd")
            return num  # Return the valid odd number
    except ValueError:
        print("This is not a number")
        return get_odd_number()  # Call the function again if input is not a number


odd_number = get_odd_number()
