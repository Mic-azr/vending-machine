#A Class representing a wallet holding an amount of cash, represented by an int
#Utilizes dataclass
#Version 1.0 2.17.2022
#Author: Michael Cummings

from dataclasses import dataclass, field
from typing import final

@dataclass
class Wallet:
    wallet_funds: int = field(default=2500) #Currency will be represented in pennies (integers) then divided by 100
    max_capacity = 10000 #Wallet should only hold up to $100.00, or 10,000 pennies


    def print_wallet_funds(self):
        print(f"Your wallet has ${(self.wallet_funds/100.00):.2f} in cash.")

    def add_wallet_funds(self):
        try:
            funds_to_add = int(input("Enter a whole dollar amount to add to your wallet: "))#Save adding change for another day...

            if ((funds_to_add * 100) + self.wallet_funds) <= self.max_capacity:
                funds_to_add *= 100 #converting to pennies
                self.wallet_funds += funds_to_add
            else:
                print("Your wallet would contain greater than $100.00 if you added that much! Please enter a lower amount, or remove some money from your wallet.")
                self.add_wallet_funds()

        except ValueError:
            print("Please type a whole dollar amount with no change, without the $ symbol (Ex. '25', '2')")
            self.add_wallet_funds()

    def remove_wallet_funds(self):
        try:
            funds_to_remove = int(input("Enter a whole dollar amount to remove from your wallet: "))

            if funds_to_remove * 100 <= self.wallet_funds: #Checking if the wallet has enough money to remove
                funds_to_remove *= 100 #converting to pennies
                self.wallet_funds -= funds_to_remove
            else:
                print("You can't remove more money from your wallet than what's already inside!")
                self.remove_wallet_funds()

        except ValueError:
            print("Please type a whole dollar amount with no change, without the $ symbol (Ex. '25' '2')")
            self.remove_wallet_funds()

    def convert_to_bills(self): #Method to represent the funds in the wallet as a stack of bills of different denominations
        remaining_funds = self.wallet_funds
        one_dollar_bills = 0
        five_dollar_bills = 0
        ten_dollar_bills = 0
        twenty_dollar_bills = 0
        fifty_dollar_bills = 0
        onehundred_dollar_bills = 0

        if(remaining_funds == 10000): #Special case, wallet is full
            remaining_funds -= 10000
            onehundred_dollar_bills += 1
        while(remaining_funds >= 5000):
            remaining_funds -= 5000
            fifty_dollar_bills += 1
        while(remaining_funds >= 2000):
            remaining_funds -= 2000
            twenty_dollar_bills += 1
        while(remaining_funds >= 1000):
            remaining_funds -= 1000
            ten_dollar_bills += 1
        while(remaining_funds >= 500):
            remaining_funds -= 500
            five_dollar_bills += 1
        while(remaining_funds >= 100):
            remaining_funds -= 100
            one_dollar_bills += 1

        print("The money in your wallet can be converted to: \n")
        if(onehundred_dollar_bills > 0):
            print(f"{onehundred_dollar_bills} x $100\n")
        if(fifty_dollar_bills > 0):
            print(f"{fifty_dollar_bills} x $50\n")
        if(twenty_dollar_bills > 0):
            print(f"{twenty_dollar_bills} x $20\n")
        if(five_dollar_bills > 0):
            print(f"{five_dollar_bills} x $5\n")
        if(one_dollar_bills > 0):
            print(f"{one_dollar_bills} x $1\n")
