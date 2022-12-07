#A Class representing a wallet holding an amount of cash, represented by an int
#Utilizes dataclass
#Version 1.0.1 12.7.2022
#Author: Michael Cummings

from dataclasses import dataclass, field
from typing import final

@dataclass
class Wallet:
    wallet_funds: int = field(default=2500) #Currency will be represented in pennies (integers), then divided by 100 when presented to the user
    max_wallet_capacity = 50000 #Wallet should only hold up to $500.00, or 50,000 pennies


    def print_wallet_funds(self):
        print(f"Your wallet has ${(self.wallet_funds/100.00):.2f} in cash.")

    def add_wallet_funds(self):
        user_input = input("Enter a dollar amount to add to your wallet:")
        try:
            funds_to_add_to_wallet = int(user_input)
            funds_to_add_to_wallet_as_pennies = funds_to_add_to_wallet * 100
            
            if (funds_to_add_to_wallet_as_pennies + self.wallet_funds) <= self.max_wallet_capacity:
                self.wallet_funds += funds_to_add_to_wallet_as_pennies
            else:
                print(f"Your wallet would contain greater than ${(self.max_wallet_capacity / 100.0):.2f} if you added that much! Please enter a lower amount, or remove some money from your wallet.")
                self.add_wallet_funds()

        except ValueError:
            try:
                funds_to_add_to_wallet = float(user_input)
                funds_to_add_to_wallet_as_pennies = int(funds_to_add_to_wallet * 100)

                if (funds_to_add_to_wallet_as_pennies + self.wallet_funds) <= self.max_wallet_capacity:
                    self.wallet_funds += funds_to_add_to_wallet_as_pennies
                else:
                    print(f"Your wallet would contain greater than ${(self.max_wallet_capacity / 100.0):.2f} if you added that much! Please enter a lower amount, or remove some money from your wallet.")
                    self.add_wallet_funds()

            except ValueError:
                print("Please type a dollar amount without the $ symbol (Ex. '25' '2', '5.25')")
                self.add_wallet_funds()

    def remove_wallet_funds(self):
        user_input = input("Enter a dollar amount to add to your wallet:")
        try:
            funds_to_remove_from_wallet = int(user_input)
            funds_to_remove_from_wallet_as_pennies = funds_to_remove_from_wallet * 100

            if funds_to_remove_from_wallet_as_pennies <= self.wallet_funds:
                self.wallet_funds -= funds_to_remove_from_wallet_as_pennies
            else:
                print("You can't remove more money from your wallet than what's already inside!")
                self.remove_wallet_funds()
                
        except ValueError:
            try:
                funds_to_remove_from_wallet = float(user_input)
                funds_to_remove_from_wallet_as_pennies = int(funds_to_remove_from_wallet * 100)
                
                if funds_to_remove_from_wallet_as_pennies <= self.wallet_funds:
                    self.wallet_funds -= funds_to_remove_from_wallet_as_pennies
                else:
                    print("You can't remove more money from your wallet than what's already inside!")
                    self.remove_wallet_funds()

            except ValueError:
                print("Please type a dollar amount without the $ symbol (Ex. '25' '2', '5.25')")
                self.remove_wallet_funds()

    def convert_to_bills(self): #Method to represent the funds in the wallet as a stack of bills of different denominations
        remaining_funds_in_wallet = self.wallet_funds
        one_dollar_bills = 0
        five_dollar_bills = 0
        ten_dollar_bills = 0
        twenty_dollar_bills = 0
        fifty_dollar_bills = 0
        onehundred_dollar_bills = 0

        if(remaining_funds_in_wallet >= 10000):
            remaining_funds_in_wallet -= 10000
            onehundred_dollar_bills += 1
        while(remaining_funds_in_wallet >= 5000):
            remaining_funds_in_wallet -= 5000
            fifty_dollar_bills += 1
        while(remaining_funds_in_wallet >= 2000):
            remaining_funds_in_wallet -= 2000
            twenty_dollar_bills += 1
        while(remaining_funds_in_wallet >= 1000):
            remaining_funds_in_wallet -= 1000
            ten_dollar_bills += 1
        while(remaining_funds_in_wallet >= 500):
            remaining_funds_in_wallet -= 500
            five_dollar_bills += 1
        while(remaining_funds_in_wallet >= 100):
            remaining_funds_in_wallet -= 100
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
