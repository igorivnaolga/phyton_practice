balance = 8000

def bank_account(starting_value: int):
    def deposit (amount: int):
      nonlocal starting_value
      starting_value += amount
      print(starting_value)

    def withdraw (amount: int):
      nonlocal starting_value
      if  amount > starting_value:
        raise ValueError("Amount can not be greater than balance")
      starting_value -= amount

    return deposit

my_deposit = bank_account(5000)
my_deposit(500)
my_deposit(300)


# deposit(7000)
# withdraw(5000)

# print(balance)