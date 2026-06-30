import os
import json
import random as r
import string as s

print('Welcome to the Python-Pass-Manager!')

# Check Password Strength  
def strengthChecker():
    password = input("Enter your Password: ")
    
    if len(password) < 6:
        print('Password is weak !')
        return
    if len(password) < 10:
        print('Password is Moderate !')
        return
    if len(password) > 12:
        print('Password is Strong !')
        return

# Generate Password
def generate():
    password = ""
    length = int(input('Enter Length of your Password: '))
    isNum = input('Do you want to add Numbers to your Password, [Y, N]')

    if isNum.lower() == 'n':
       for i in range(length):
           password += s.ascii_lowercase[r.randrange(0, len(s.ascii_lowercase))]
       print(f"Your password is: {password}")
       return
       
    elif isNum.lower() == 'y':
        merge = s.ascii_lowercase + s.digits
        for i in range(length):
           password += merge[r.randrange(0, len(merge))]
        print(f"Your password is: {password}")
        return

# Get all account
def get():
    # Master Password to access vault
    with open(".env", "r") as f:
        admin_pass = f.readline().strip().lower()[6:]
        
    admin = input("Enter Admin Password: ").strip().lower()
    if admin == admin_pass:
        with open("accounts.json", "r") as file:
            data = json.load(file)
            for d in data:
                print(d)
                
    else: 
        print("INVALID CREDENTIALS !")
        return
        
# Add new account
def add():
    website = input('Enter Website name: ')
    username = input('Enter Username: ')
    password = input('Enter your Password: ')
    description = input('Enter Description: ')

    account = {
        "Website": website,
        "Username": username,
        "Password": password,
        "Description": description
    }

    if os.path.exists("accounts.json"):
        with open("accounts.json", "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []  # if file is empty or invalid
    else:
        data = []
        
    data.append(account)

    with open("accounts.json", "w") as file:
        result = json.dump(data, file, indent=4)
        if result: 
            print(f"Successfully added Account => {result}")
            return


def main():
   print("'A' to Add Passwords\n'G' to Get all Passwords\n'F' to Generate Password\n 'D' to Check your Password's Strength")
   
   user_choice = input('Enter your choice: ')
   
   if user_choice.lower() == 'a': 
       add()
   elif user_choice.lower() == 'g':
       get()
   elif user_choice.lower() == 'f':
       generate()
   elif user_choice.lower() == 'd':
       generate()

main()