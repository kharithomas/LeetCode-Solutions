# TC: O(1), each transaction just a O(1) account lookup
# SC: O(1), extra space each transaction not incl. O(N) to store accounts in array

from typing import List

class Bank:

    def __init__(self, balance: List[int]):        
        self.balance = balance

    def exists(self, account: int) -> bool:
        """Checks if an account exists"""
        return len(self.balance) > 0 and 0 < account <= len(self.balance)
    
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.exists(account1) and self.exists(account2) and money <= self.balance[account1 - 1]:
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True

        return False

    def deposit(self, account: int, money: int) -> bool:
        if self.exists(account):
            self.balance[account - 1] += money
            return True
        
        return False

        

    def withdraw(self, account: int, money: int) -> bool:
        if self.exists(account) and money <= self.balance[account - 1]:
            self.balance[account - 1] -= money
            return True
            
        return False


bank = Bank([10, 100, 20, 50, 30]);
bank.withdraw(3, 10);    # return true, account 3 has a balance of $20, so it is valid to withdraw $10.
                         # Account 3 has $20 - $10 = $10.
bank.transfer(5, 1, 20); # return true, account 5 has a balance of $30, so it is valid to transfer $20.
                         # Account 5 has $30 - $20 = $10, and account 1 has $10 + $20 = $30.
bank.deposit(5, 20);     # return true, it is valid to deposit $20 to account 5.
                         # Account 5 has $10 + $20 = $30.
bank.transfer(3, 4, 15); # return false, the current balance of account 3 is $10,
                         # so it is invalid to transfer $15 from it.
bank.withdraw(10, 50);   # return false, it is invalid because account 10 does not exist.