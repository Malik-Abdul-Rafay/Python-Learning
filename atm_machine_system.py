atm_data = {
    "1": {
        "name": "Rafay Khan",
        "password": "rafay2005",
        "pin": "1234",
        "balance": 5000,
        "account_type": "savings",
        "transactions": [],
        "locked": False,
        "pin_attempts": 0,
    },
    "2": {
        "name": "Ahmed Ali",
        "password": "ahmed2005",
        "pin": "5678",
        "balance": 10000,
        "account_type": "current",
        "transactions": [],
        "locked": False,
        "pin_attempts": 0,
    },
    "000453891": {
        "name": "Basit Raza",
        "password": "basit2005",
        "pin": "4321",
        "balance": 7500,
        "account_type": "savings",
        "transactions": [],
        "locked": False,
        "c": 0,
    },
}



try:
    user_card_num_input = input('Enter Your Card Number: ')
except RuntimeError as e:
    print(e)

for key , data in atm_data.items():
    if key == user_card_num_input:
        user_password = input("Enter ATM password: ")
        if data["password"] == user_password:
            print("Correct Password")
            print("""Please Choose Option:
            a. Balance Check Karen
            b. Deposit Karen
            c. Withdraw Karen
            d. exit
            """)

            while True: 
                user_option_input = input("Option Choose Karen: ")
                if user_option_input == "a":
                    print(f"Your Balance is {data["balance"]}")
                elif user_option_input == "b":
                    try: 
                        user_doposit_value = int(input('Enter Deposit Amount: '))
                    except RuntimeError as e:
                        print(e)
                    if(user_doposit_value):
                        data["balance"] += user_doposit_value
                        print('Deposit Successfully!')
                    else:
                        print("Please Correct Fill Amount Value")

                elif user_option_input == "c":
                    try: 
                        user_withdraw_value = int(input('Enter Withdraw Amount: '))
                    except RuntimeError as e:
                        print(e)
                    if(user_withdraw_value):
                        data["balance"] -= user_withdraw_value
                        print('Deposit Successfully!')
                    else:
                        print("Please Correct Fill Amount Value")
                
                elif user_option_input == "d":
                    break

        break
            


