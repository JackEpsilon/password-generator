import random #module used to generate random numbers, characters, or shuffle items.
import string #module that contains useful constants like ascii_letters, digits, and punctuation.
def generate_password(length=12):
    """Generate a random password with the give length."""
    if length < 8:
        print("Password length should be least 8 characters.")
        return none
    letters = string.ascii_letters #a string containing all uppercase A-Z and lowercase a-z.
    digits = string.digits
    special_chars = string.punctuation
    all_chars = letters + digits + special_chars #all_chars combines letters, digits, and special characters into one pool.
    password = [
        random.choice(letters),
        random.choice(digits),               #random.choice() selects one random character from each pool.
        random.choice(special_chars)
        #these are the building blocks for generating a diverse password.
        #this ensures the password has at least one letter, one digit, and one special character.
        ]
    password += random.choices(all_chars, k=length - 3)
    #random.choices():Picks length - 3 random characters from all_chars to complete the password.
    #this ensures the password is of the user-specified length while maintaining randomness.
    random.shuffle(password)
    #why shuffle? if we always pick one character from each category first, the order will be predictable. Shuffling randomizes the final password to avoid patterns.
    return ''.join(password) #converts the list of characters into a single string. The final password is returned as a single string.
try:
    user_length = int(input("Enter the desired password length (minimun 8):")) #asks the user to input the desired password length. #converts the input to an integer (int()). 
    generated_password = generate_password(user_length)
    if generated_password:
        print(f"Generated password: {generated_password}")
except ValueError:
    print("Please enter a valid number.") #if the user inputs invalid data (e.g, letters instead of numbers), a ValueError is caught, and an appropriate message is displayed.

    