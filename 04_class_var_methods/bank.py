# 4. Class Variables and Class Methods
#Assignment:
#Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Global Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder}, Bank: {Bank.bank_name}")                                                            


# create instances
account1 = Bank("Ali")
account2 = Bank("Ibrahim")

# display initial bank name
account1.display()
account2.display()

# change bank name
Bank.change_bank_name("Universal Bank")

# display updated bank name
account1.display()
account2.display()
        
