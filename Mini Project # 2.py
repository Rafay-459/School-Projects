# Get the user's input for the total distance traveled

# ! Don't worry this block is only used for taking inputs from the user.

while True:
    try:
        total_distance = float(input("Enter the total distance you traveled (in km): "))
        total_time = float(input("Enter the total time taken (in hours): "))
        if total_distance <= 0:
            print("Invalid input. Please enter a positive value.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number.")

distance_charge = total_distance * 5  # Calculate the distance charge

time_charge = total_time * 100  # Calculate the time charge

input = input(("Are you already a customer? (y/n): ")).lower()

if input == "y":

    total_cost = max(distance_charge, time_charge)

    print(f"\nYou are a customer, so you get a discount.\n")
    print(
        f"The total cost for traveling {total_distance} km within {total_time} hour(s) is: {total_cost} rs"
    )

else:

    total_cost = distance_charge + time_charge

    print("You are not a customer, so you don't get a discount.")
    # Print the result
    print(
        f"The total cost for traveling {total_distance} km within {total_time} hour(s) is: e {total_cost} rs"
    )
