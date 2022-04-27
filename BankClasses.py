class User:
    def __init__(self,name,pin,password):
        self.name = name
        self.pin = pin
        self.password = password
    
    def change_name(self,name):
        self.name = name

    def change_pin(self,pin):
        self.pin = pin

    def change_password(self,password):
        self.password = password

""" Driver Code for Task 1 """
# u = User("Bob","1234","password")
# print(u.name,u.password,u.pin)
""" Driver Code for Task 2 """
# u.change_name("Bobby")
# u.change_pin("4321")
# u.change_password("newpassword")
# print(u.name,u.password,u.pin)

class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
    
    def show_balance(self):
        return print("{:} has an account balance of: ${:.2f}".format(self.name,self.balance))

    def withdraw(self,withdrawn_amt):
        self.balance = self.balance - withdrawn_amt
    
    def deposit(self,deposit_amt):
        self.balance = self.balance + deposit_amt

    def transfer_money(self,user,transfer_amt):
        while True:
            print(f"You are transferring ${transfer_amt} to {user.name}")

            if transfer_amt > self.balance:     # Checks balance in each account
                print("Insufficient Funds.")
                break

            print("Authentication Required.")
            pin = input ("Enter your PIN: ")
            if pin == self.pin:
                print("Transfer Authorized")
                print(f"Transferring {transfer_amt} to {user.name}")
                self.balance = self.balance - transfer_amt
                user.balance = user.balance + transfer_amt
                return True
            else:
                print("Invalide PIN. Transaction Failed.")
            return False
    
    def request_money(self,user,req_amt):

        while True:
            print(f"You are requesting ${req_amt} from {user.name}")
            
            if req_amt > user.balance:      # Checks balance in each account
                print(f"{user.name} does not have enough funds.")
                break

            print("User Authentication Requrired...")
            pin = input (f"Enter {user.name}'s PIN: ")
            password = input(f"Enter your password: ")

            # Matches the pin and password
            if pin == user.pin and password == self.password:
                print("Request Authorized")
                print(f"{user.name} sent {req_amt}")
                self.balance = self.balance + req_amt
                user.balance = user.balance - req_amt
                return True
            else:
                print("Authorization Failed.")
                return False
                

""" Driver Code for Task 3 """
# user1 = BankUser("Bob","1234","password")
# print(user1.name,user1.password,user1.pin,user1.balance)

""" Driver Code for Task 4 """
# user1.show_balance()
# user1.deposit(1000)
# user1.show_balance()
# user1.withdraw(500)
# user1.show_balance()

""" Driver Code for Task 5 """
# user1 = BankUser("Bob","1234","password")
# user2 = BankUser("Alice","4321","alicepassword")

# user2.deposit(5000)
# user2.show_balance()
# user1.show_balance()
# print("\n")
# user2.transfer_money(user1,500)
# user2.show_balance()
# user1.show_balance()
# print("\n")
# user2.request_money(user1,250)
# user2.show_balance()
# user1.show_balance()

