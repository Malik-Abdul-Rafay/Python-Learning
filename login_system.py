users = {
    "Rafay": {"password": "rafay2005"},
    "Ahmed": {"password": "ahmed2005"},
    "basit": {"password": "basit2005"},
}

user_name = input("Enter User Name: ")
password_correct = False
user_correct = False
for user in users:
    print(user.lower())
    if(user.lower() == user_name.lower()):
        print("User is Found")
        user_correct = True
        user_password = input("Enter User Password: ")
        if(user_password.lower() == users[user]["password"]):
            print('True Password')
            password_correct = True
        break

if not user_correct:
    print('User Not Found!')
elif not password_correct:
    print("password is not correct")


