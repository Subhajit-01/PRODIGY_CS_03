import string

password = input("Enter the password: ")

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

characters = [upper_case, lower_case, special, digits]

length = len(password)

score =  0

with open('hackable_passwords.txt', encoding='utf-8') as f:
    common = f.read()

if password in common:
    print("Password is found in a Hackable_Password list. Scrore 0")
    exit()

if length < 4:
    score += 1
elif length < 8:
    score += 2
elif length < 10:
    score += 3
elif length >= 10:
    score += 4


print(f"Password length is {length}, adding {str(score)} points!")

if sum(characters) == 1:
    score += 1
elif sum(characters) == 2:
    score += 2
elif sum(characters) == 3:
    score += 3
elif sum(characters) >= 4:
    score += 4

print(f"Passwords has {str(sum(characters))} different character types! adding {str(sum(characters) - 1)}")

if score <= 3 :
    print("Password is Weak! :( )")
elif score < 6:
    print("Password is good but may be more strong..!")
elif score >= 6:
    print("Password is Strong. :) ")