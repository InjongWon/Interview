import sys

class Bank:
    def __init__(self):
        self.bank = {}
        
    def add_entry(self, card_num, pin, account, amount):
        self.bank[card_num] = {"pin":pin, "account":{account:amount}}

    def add_account(self, card_num, account, amount):
        if card_num in self.bank:
            self.bank[card_num]["account"][account] = amount

    def check_pin(self, card_num, entered_pin):
        if card_num in self.bank and self.bank[card_num]["pin"] == entered_pin:
            return self.bank[card_num]["account"]
        else:
            return None

    def update_account(self, card_num, account, amount):
        if self.bank[card_num]["account"][account] in self.bank[card_num]["account"]:
            self.bank[card_num]["account"][account] = amount
            return True
        else:
            return False


class Controller:
    def __init__(self, bank, cash):
        self.Bank = bank
        self.accounts = None
        self.cash_bin = cash

    def swipe(self, card_num, pin):
        self.accounts = self.Bank.check_pin(card_num, pin)
        if self.accounts is None:
            return 0, "Invalid Card or Incorrect Pin!"
        else:
            return 1, "Welcome "

    def account_actions(self, card_num, acc, action, amount=0):
        if action == "See Balance":
            return self.accounts[acc], 1
        elif action == "Withdraw":
            if self.accounts[acc] >= amount and self.cash_bin >= amount:
                new_balance = self.accounts[acc] - 
                
                
                
                self.accounts[acc] = new_balance
                self.Bank.update_account(card_num, acc, new_balance)
                return self.accounts[acc], 1
            else:
                return self.accounts[acc], 0
        elif action == "Deposit":
            new_balance = self.accounts[acc] + amount
            self.cash_bin += amount
            self.accounts[acc] = new_balance
            self.Bank.update_account(card_num, acc, new_balance)
            return self.accounts[acc], 1
        else:
            return self.accounts[acc], 2

 


