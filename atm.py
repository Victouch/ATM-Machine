infos = [
    {
        "Name" : "Clement Airiohuodion",
        "Account number" : 2014586998,
        "Account balance" : 70000,
        "User name" : "Clemobrain".casefold(),
        "password" : "Clemo234@",
        "Date" : "23/04/2012"
    },
    {
        "Name" : "Abraham Airiohuodion",
        "Account number" : 2083658945,
        "Account balance" : 65000,
        "User name" : "Abdion".casefold(),
        "password" : "Construction7&",
        "Date" : "30/04/2012"
    }
]

class AtmMachine:

    def __init__(self, username, password) -> None:

        self.username = username
        self.password = password

    def personal_data(self):

        for info in infos:
            if self.username != info["User name"] or self.password != info["password"]:
                continue
            else:
                print(info)
                break
                

        return "Successful"

    def create_account(self):

        new_account = {}
        name = input("Enter your full name: \n")
        # rechoose_password = input("Confirm password: \n")
        amount_deposited = int(input("Amount to be deposited: \n"))
        date = input("Enter todays date: \n")
        new_account["Name"] = name
        new_account["User name"] = self.username
        new_account["Password"] = self.password
        new_account["Account balance"] = amount_deposited
        new_account["Date"] = date
        infos.append(new_account)
        print(infos[-1])

    def withdrawal(self):
        for infom in infos:
            if username != infom["User name"] or password != infom["password"]:    
                continue
            
            else:
                current_amount = infom["Account balance"] - amount_withdrawn
                print(current_amount)


# print("Welcome to ATM machine app.")
# username = input("Enter your user name: \n")
# password = input("Enter your password: \n")
while True:
    print("\nWelcome to ATM Simulation App\n".upper())
    try:
        choose = int(input("Enter'1' to Sign in, and '2' to Sign up---> "))
    except:
        print("Invalid input")
        continue
    if choose == 1:
        username = input("Enter your user name: \n")
        password = input("Enter your password: \n")
        try:
            select = int(input("\nEnter'3' for details, and '4' for withdrawal---> "))
        except:
            print("Invalid input")
        for info in infos:
            if username != info["User name"] or password != info["password"]:    
                continue
            
            else:
                if select == 3:
                    atm0 = AtmMachine(username, password).personal_data()
                    again = int(input("\nEnter'5' to close app, and any other digit to continue---> "))
                    if again == 5:
                        break
                    else:
                        continue
                elif select == 4:
                    amount_withdrawn = int(input("Enter amount: "))
                    atm2 = AtmMachine(username, password).withdrawal()
                    break
            print("Incorrect username or password")
            
            
    elif choose == 2:
        username = input("Enter a user name: \n")
        password = input("Enter a password: \n")
        atm1 = AtmMachine(username, password).create_account()
        break
    else:
        print("Not part of the option! ")
print("\nThank you for using this app!")

