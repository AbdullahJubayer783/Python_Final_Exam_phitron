class Bank:
    def __init__(self) -> None:
        self.name = "admin"
        self.Bank_Balance = 0
        self.total_loan_from_users = 0

        self.Accounts = []
        
        self.is_bankrupt = False
        self.Loan_feature = False

    def creat_an_account(self,account):
        flag = True
        for acc in self.Accounts:
            if acc.accuout_number == account.accuout_number:
                flag = False
        if flag:
            self.Accounts.append(account)
        else:
            print("\nThis account is alredy exist\n")

    def delete_user_account(self,account_number):
        flag = True
        for account in self.Accounts:
            if account.accuout_number == account_number:
                self.Accounts.remove(account)
                flag = False
                break
        if flag:
            print(f"\nInvalide account number {account_number}\n")   

    def see_all_user_accounts(self):
        for acc in self.Accounts:
            print(f"\nAccount Holder Name: {acc.name} Account Number: {acc.accuout_number} Account Type: {acc.account_type}\n")

    def check_total_balance(self):
        print(f"\nDear Admin Your Bank Total Balance amount is {self.Bank_Balance}\n")

    def check_total_Loan(self):
        print(f"\nDear Admin Your Bank Total Loan amount is {self.Bank_Balance}\n")

    def loan_feature(self,booll):
        self.Loan_feature = booll

    # @staticmethod
    def loan_request(self,amount):
        if self.is_bankrupt:
            return (False,"\nThe bank is bankrupt\n")
        elif self.Loan_feature:
            return (False,'\nLoan featuer off\n')
        else:
            self.Bank_Balance -= amount
            self.total_loan_from_users+=amount
            return (True , f"\nyou succesfully get loan {amount}\n")




class Account:
    def __init__(self , name , email , address , type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = type
        
        self.Balance = 0
        self.accuout_number = f'{self.name}-{self.email}-{self.address}'

        self.transaction_history = []

        self.loan_limit = 2

    # Methods.....

    def diposit(self,bank,amount):
        if bank.is_bankrupt:
            print("\nThe Bank is Bankrupt\n")
            return
        if amount > 0:
            self.Balance+=amount
            self.transaction_history.append(f'Diposit amount {amount} on account number {self.accuout_number} and current amount {self.Balance}')
            print(f'\nDiposit amount {amount} on account number {self.accuout_number} and current amount {self.Balance}\n')
        else :
            print("\nInvalid Amount...!\n")

    def withdraw(self,bank,amount):
        if bank.is_bankrupt:
            print("\nThe Bank is Bankrupt\n")
            return
        if amount <= self.Balance:
            self.Balance-=amount
            self.transaction_history.append(f'Withdraw amount {amount} on account number {self.accuout_number} and current amount {self.Balance}')
            print(f'\nWithdraw amount {amount} on account number {self.accuout_number} and current amount {self.Balance}\n')
        else :
            print("\nWithdrawal amount exceeded\n")
    
    def Transaction_history(self):
        print('\n')
        flag = True
        for tran in self.transaction_history:
            flag = False
            print(tran)
        if flag :
            print("There have no Transaction History..!")
        print('\n')
    
    def Check_available_balance(self):
        print('\nYour current Balance is \n',self.Balance)
    
    def take_loan_from_bank(self,bank,amount):
        if self.loan_limit == 0:
            print("\nSorry we can't accept your request. You alredy cross your loan limit..!\n")
        else:
            lst = bank.loan_request(amount)
            if lst[0]:
                self.Balance+=amount
                self.loan_limit-=1
                self.transaction_history.append(f"Taking loan from bank {amount} new balence is {self.Balance}")
                print(lst[1])
            else :
                print(lst[1])

    def transfer_amount(self,bank,accNum,amount):
        if amount >= self.Balance:
            print("\nNot enough Balence on your account\n")
            return
        flg = True
        for i in range(0,len(bank.Accounts)):
            if bank.Accounts[i].accuout_number == accNum:
                flg = False
                bank.Accounts[i].Balance += amount
                self.Balance-=amount
                self.transaction_history.append(f'Transfer {accNum} this account {amount} new balence is {self.Balance}')
                print(f'\nTransfer {accNum} this account {amount} new balence is {self.Balance}\n')
        if flg :
            print(f"\nThere are no account this number {accNum}\n")


bank = Bank()
acc1 = Account("1","1","1",'1')
acc2 = Account("2","2","2",'2')
bank.creat_an_account(acc1)
bank.creat_an_account(acc2)
all_acc_lst = [acc1,acc2]


curracc = None
crac = None
while True:
    if curracc == None and crac == None:
        Log = input("Admin login or User login(ad/us)? ")
        if Log == 'ad':
            paswrd = ''
            while paswrd != 'admin123':
                paswrd = input("\n\nEnter Admin login Password (password is admin123): ")
            curracc = bank
        elif Log == 'us':
            if crac == None:
                name = input("Enter your name ")
                for nm in all_acc_lst:
                    if name == nm.name:
                        crac = nm
                        break
                if crac == None:
                    print("Could Not Find Any Account")

    elif curracc != None and curracc.name == "admin":

        print("\n\npress 1 for creat an account")
        print("press 2 for delete an account")
        print("press 3 check all users of bank")
        print("press 4 check the total Balance of the bank")
        print("press 5 check total loan amount")
        print("press 6 on or off Loan feature") 
        print("press 7 for logout!")

        ch = int(input("\n\nEnter your choice: "))

        if ch == 1:

            name = input("\n\nEnter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            actype = input("Enter your actype: ")
            acc = Account(name , email , address , actype)
            curracc.creat_an_account(acc)
            all_acc_lst.append(acc)

        elif ch == 2:
            accNum = input("\n\nEnter Deleted account Number: ")
            curracc.delete_user_account(accNum)
        elif ch == 3:
            curracc.see_all_user_accounts()
        elif ch == 4:
            curracc.check_total_balance()
        elif ch == 5:
            curracc.check_total_Loan()
        elif ch == 6:
            op = bool(input("On Or Off (True/False)"))
            if op:
                curracc.loan_feature(False)
            else:
                curracc.loan_feature(True)
        elif ch == 7:
            curracc = None
        else:
            ch = int(input("Wrong choice. Enter correct choice: "))
    else:
        print("Press 1 for Diposit in account")
        print("Press 2 for Withdraw in account")
        print("press 3 for check available balance")
        print("Press 4 for check Transaction History")
        print("Press 5 for Loan from the bank")
        print("Press 6 for Transfer ammount")
        print("Press 7 for Exist")

        ch = int(input("\nEnter your choice: "))

        if ch == 1:
            amount = int(input("Enter your amount: "))
            crac.diposit(bank,amount)
        elif ch == 2:
            amount = int(input("Enter your amount: "))
            crac.withdraw(bank,amount)
        elif ch == 3:
            crac.Check_available_balance()
        elif ch == 4: 
            crac.Transaction_history()
        elif ch == 5:
            amount = int(input("Enter your amount: "))
            crac.take_loan_from_bank(bank,amount)
        elif ch == 6:
            accNum = input("Enter your account number: ")
            amount = int(input("Enter your amount you want transfer: "))
            crac.transfer_amount(bank,accNum,amount)
        elif ch == 7:
            crac = None
            break
        else:
            ch = int(input("Wrong choice. Enter correct choice: "))
                

        



