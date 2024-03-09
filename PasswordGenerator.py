import random
import string

print("Welcome to the Password generator!\n")

#length of password
lengthofpassword = int(input("How long should be the password: ")) 

#Elements that will be used in password generation
Lowercase = string.ascii_lowercase
Uppercase = string.ascii_uppercase
Number = string.digits
Symbols = string.punctuation

allelements = Lowercase + Uppercase + Number + Symbols

#Password Generated
password = "".join(random.sample(allelements,lengthofpassword))

print(f"Your password is: {password}")