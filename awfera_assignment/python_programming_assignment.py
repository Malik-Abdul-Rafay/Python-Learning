user_input = input("Enter Input: ")

reversed_text = user_input[::-1]



vowels_num = "aeiou"
vowels_count = 0

for user_input_num in user_input:
    if user_input_num.lower() in vowels_num:
        vowels_count += 1
print(f"Reversed Input is: {reversed_text}")
print(f"Total Numbers of Vowels is {vowels_count}")