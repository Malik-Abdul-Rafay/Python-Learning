try:
    user_marks = int(input("Enter Your Marks: "))
except RuntimeError as e:
    print(e)


if user_marks > 89:
    result = "A+"
elif user_marks > 79:
    result = "A"
elif user_marks > 69:
    result = "B"
elif user_marks > 59:
    result = "C"
elif user_marks > 49:
    result = "D"
else:
    result = "F"


print(f"Your Grade is {result}")
