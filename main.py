valid_password = False #this is a flag

#until we get a valid password
while not valid_password:

    password = input("please set a new password :")
    
    special_character_check = "!" in password
    length_valid = False

    password_length_check = len(password) < 16

    if len(password) < 16 and len(password) > 5:
        print("password is the right length")
        length_valid = True
    elif len(password) < 5:
        print("the password is too short")
    else:
        print("passwprd must be between 5 and 16 characters")

    special_characther_valid = False
    if special_character_check:
        print("special character found")
        special_characther_valid = True
    else:
        print("This password needs an ! characther somewhere")
    
    if length_valid and special_characther_valid:
        print("Your password has been set")
        valid_password = True

print ("thank you for the valid password")