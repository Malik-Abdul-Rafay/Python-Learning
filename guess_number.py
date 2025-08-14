import random


try: 
    random_num = random.randint(1, 100)
except ValueError as e:
    print(e)

while True:
    user_input = input("Enter your value: ")
    
    try:
        user_value = int(user_input)
        if random_num == user_value:
            print("🎉 Great! You Win.")
            break
        elif random_num < user_value:
            print("🔻 Your typed number is greater than the guessed number.")
        else:
            print("🔺 Your typed number is smaller than the guessed number.")
    except ValueError:
        print("❌ Invalid input! Please enter a valid integer.")

