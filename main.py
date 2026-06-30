import json
import os

print('Welcome to the Python-Pass-Manager!')

def get():
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
        json.dump(data, file, indent=4)

def main():
    # add()
    get()

main()