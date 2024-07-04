import random 
import string

def generate_password(MIN_LENGTH,numbers=True,special_characters=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation
    
    characters=letters
    if (numbers):
        characters+=digits
    if (special_characters):
        characters+=special    
   
    pwd= ""
    meets_criteria=False
    has_number=False
    has_special_characters=False
    while not meets_criteria or len(pwd) < MIN_LENGTH:
        random_char=random.choice(characters)
        pwd+=random_char
        
        if random_char in digits:
            has_number=True
        if random_char in special:
             has_special_characters=True
            
        meets_criteria=True
            
        if not has_number:
            meets_criteria=has_number
        if not has_special_characters:
            meets_criteria=has_special_characters
        
    return pwd

minimum= int(input("What is the minimum characters a password have: " ))
numbers=input("shall the password has numbers: (Y or n) ").lower()[0]
special_characters=input("shall the password have special characters: (Y or n) ").lower()[0]
numbers1=False
special_characters1=False
if numbers=="y":
    numbers1=True
if special_characters == "y":
    special_characters1=True    
password=generate_password(minimum,numbers,special_characters)
print(password)