import random
character = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ#+!$%&/,.-_"
character_list = list(character)
password = input("Enter your password: ")
guess = ""
while (guess != password):
    guess = random.choices(character_list,k=len(password))
    print(guess)
    guess = "".join(guess)
    print(guess)
print("your password is " + guess)
