import random # Randomly generate a Password
import string # String will be used to generate string (lower case, upper case, numbers)

option=0 # It will hold the option seleted by the User Input
len=4 # It will store the length of the password, default length will be 4

# Creating function according to the respective purposes, as the name of function suggests
def lower_case_pass(len):
    alphabets=string.ascii_lowercase # Getting all the 26 alphabets in small letter
    password=''.join(random.choice(alphabets) for i in range(len)) # Using join to add two string 
    # for loop will help adding random string length times
    print("Your Random Password: ",password)
    main_menu()

def upper_case_pass(len):
    alphabets=string.ascii_uppercase # Getting all the 26 alphabets in capital letter
    password=''.join(random.choice(alphabets) for i in range(len)) # Using join to add two string 
    # for loop will help adding random string length times
    print("Your Random Password: ",password)
    main_menu()

def number_pass(len):
    alphabets=string.digits # Getting all the ten number from 0 to 9
    password=''.join(random.choice(alphabets) for i in range(len)) # Using join to add two string 
    # for loop will help adding random string length times
    print("Your Random Password: ",password)
    main_menu()

def lower_and_upper_case_pass(len):
    alphabets=string.ascii_lowercase + string.ascii_uppercase # Getting all the 26 alphabets in small letter and 26 alphabets of capital letter
    password=''.join(random.choice(alphabets) for i in range(len)) # Using join to add two string 
    # for loop will help adding random string length times
    print("Your Random Password: ",password)
    main_menu()

def lower_and_number_pass(len):
    alphabets=string.ascii_lowercase + string.digits 
    password=''.join(random.choice(alphabets) for i in range(len)) # Using join to add two string 
    # for loop will help adding random string length times
    print("Your Random Password: ",password)
    main_menu()

def upper_and_number_pass(len):
    alphabets=string.ascii_uppercase + string.digits 
    password=''.join(random.choice(alphabets) for i in range(len)) # Using join to add two string 
    # for loop will help adding random string length times
    print("Your Random Password: ",password)
    main_menu()

def hard_pass(len):
    alphabets=string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password=''.join(random.choice(alphabets) for i in range(len)) # Using join to add two string 
    # for loop will help adding random string length times
    print("Your Random Password: ",password)
    main_menu()


# Creating the Main Menu function, which will contain the main driver code
def main_menu():
    print("\n*****Welcome to the Random Password Generator*****")
    print('''
    1: Easy Password ( Only Lower Case )
    2: Easy Password ( Only Upper Case )
    3: Easy Password ( Number Only )
    4: Intermidiate Password ( Lower Case + Upper Case )
    5: Intermidiate Password ( Lower Case + Number )
    6: Intermidiate Password ( Upper Case + Number )
    7: Hard Password ( Lower Case + Upper Case + Number )
    8: Exit
    ''')

    # Using Error Handling for Option, so that user's wrong entered option becomes invalid
    try:
        option=int(input("Select an Option: "))
    except:
        print("Please select a valid Option")
        main_menu() # Again moving to main menu to select valid option

    # Checking that the Selected Option is available or not
    if option>8 or option<1:
        print("Please select a valid Option")
        main_menu() # Again moving to main menu to select valid option

    # Checking here that the User wants to Quit the Program or not
    if option==8:
        print("Thanks for using Password Generator\nCreated and Designed by Vinay Pratap Singh")
        exit(0) # Quitting the Program using exit()

    try:
        len=int(input("Enter the Length of the Password ( Minimum = 4 ): "))
    except:
        print("Please enter a valid length of the Password")
        main_menu() # Again moving to main menu to select valid option

    # Checking that the length is greater than or equal to 4 or not
    if len<4:
        print("Please select a Valid Length of Password\nMinimum Length of Password is 4\n")
        main_menu()


    # Using nesting or if else ladder to operate the program 
    if option==1:
        lower_case_pass(len)
    elif option==2:
        upper_case_pass(len)
    elif option==3:
        number_pass(len)
    elif option==4:
        lower_and_upper_case_pass(len)
    elif option==5:
        lower_and_number_pass(len)
    elif option==6:
        upper_and_number_pass(len)
    elif option==7:
        hard_pass(len)
    else: # If we will not use it, then there will not be any problem at all
        # Just used it to complete the if elif and else ladder
        print("Please select a valid Option")
        main_menu()

__name__=='__main__' # As we use main function in C / C++ / Java, I am using this to execute my program from here
main_menu()