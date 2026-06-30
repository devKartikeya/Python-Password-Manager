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
    
# Edit Password
def edit():
    password = input('Enter Password to be edit: ')
    new_password = input("Enter New Password: ")
    with open("accounts.json", "r") as f:
        data = json.load(f)
        for d in data:
            if password == d["Password"]:
                d["Password"] = new_password
                data.remove(d)
                data.append(d)
                with open("accounts.json", "w") as file: 
                    json.dump(data, file, indent=4)
                    print('Password changed: ', d)
                    return
                                      
def delete():
    account = input('Enter Account to be deleted: ').strip().lower()
    admin = input('Enter Admin Password: ').strip().lower() 
    with open(".env", "r") as f:
        admin_pass = f.readline().strip().lower()[6:]
    if admin == admin_pass:
        with open("accounts.json", "r") as f:
            data = json.load(f)
            for d in data:
                if account == d["Website"]:
                    confirmation = input('Are you sure you want to delete your account? [Y/N] ').strip().lower()
                    if confirmation == 'y':
                        data.remove(d)
                        with open("accounts.json", "w") as file: 
                            json.dump(data, file, indent=4)
                            print('Password deleted: ', d)
                            return
                    else:
                        print('Password did not deleted !')
                        return
                else: 
                    print('Account not found !')
                    return
    else: 
        print('INVALID CREDENTIALS !')
        return
            
# Add new account
def add():
    website = input('Enter Website name: ')
    username = input('Enter Username: ')
    password = input('Enter your Password: ')
    description = input('Enter Description: ')

    account = {
        "Website": website.lower().strip(),
        "Username": username.strip(),
        "Password": password.strip(),
        "Description": description.strip()
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

# Search Account
def search():
     # Master Password to access vault
    with open(".env", "r") as f:
        admin_pass = f.readline().strip().lower()[6:]
        
    account = input("Enter Account to be searched !").strip().lower()
        
    admin = input("Enter Admin Password: ").strip().lower()
    if admin == admin_pass:
        with open("accounts.json", "r") as file:
            data = json.load(file)
            for d in data:
                website = d["Website"]
                if (website == account):
                    print(d)
                else: 
                    print("Not found !")
                
    else: 
        print("INVALID CREDENTIALS !")
        return
   
# Exit App 
def Exit():
    print("Thanks for your arrival !\nSee you soon !")
    exit()
    
def main():
   print("'A' to Add Passwords\n'G' to Get all Passwords\n'E' to Edit Password\n'D' to Delete Password\n'F' to Generate Password\n'I' to Check your Password's Strength\n'S' to Search an Account\n'Z' to Exit")
   
   user_choice = input('Enter your choice: ').strip()
   
   if user_choice.lower() == 'a': 
       add()
   elif user_choice.lower() == 'g':
       get()
   elif user_choice.lower() == 'e':
       edit()
   elif user_choice.lower() == 'd':
       delete()
   elif user_choice.lower() == 'f':
       generate()
   elif user_choice.lower() == 'i':
       strengthChecker()
   elif user_choice.lower() == 's':
       search()
   elif user_choice.lower() == 'z':
       Exit()
   else:
       print("Please enter a valid choice !")
       exit()
   
main()