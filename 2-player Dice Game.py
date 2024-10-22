import random

user_1 = input("Enter your name: ")
user_2 = input("Enter your name: ")
user_1_score = 0
user_2_score = 0

while True:
    user_1_score += random.randint(1, 6)
    user_2_score += random.randint(1, 6)

    print(user_1, "'s score: ", user_1_score)
    print(user_2, "'s score: ", user_2_score)
    if user_1_score > 100:
        print(user_1, "won!")
        break
    elif user_2_score > 100:
        print(user_2, "won!")
        break
