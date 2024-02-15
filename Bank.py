class Bank:
    def __init__(self, num = 0):
        self.balance = num
    def logtr(self, op, num):
        if op == 'D':
            with open ('log.txt', 'a') as file:
                file.writelines(f"Deposit {num}$. Current balance = {self.balance}\n")
        if op == 'W':
            with open ('log.txt', 'a') as file:
                file.writelines(f"Withdraw {num}$. Current balance = {self.balance}\n")
    def Withdraw(self):
        num = input('Enter amount of money for withdraw\t')
        try:
            num = float(num)
        except Exception:
            print("Something goes wrong, please try next time")
            return True
        if self.balance < num:
            print("Your balance is lover than you want to withdraw")
            return False
        else:
            print(f"You balance before withdraw:\t {self.balance}")
            self.balance -= num
            self.logtr('W', num)
            print(f"You balance after withdraw:\t {self.balance}")
            return True
    def Deposit(self):
        num = input('Enter amount of money for deposit\t')
        try:
            num = float(num)
        except Exception:
            print("Something goes wrong, please try next time")
            return True
        print(f"You balance before deposit:\t {self.balance}")
        self.balance += num
        self.logtr('D', num)
        print(f"You balance after deposit:\t {self.balance}")
        return True
AN_bank = Bank()
while True:
    print(f"Your balance currently is:\t {AN_bank.balance}")
    command = input("Enter D for deposit or W for withdraw or STOP to stop operation\t")
    if command == "W":
        AN_bank.Withdraw()
    elif command == "D":
        AN_bank.Deposit()
    elif command == "STOP":
        break
    else:
        print("You've entered wrong command!")
print(f"Your balance currently is:\t {AN_bank.balance}")
print("Have a good one!")
    
    
            
    