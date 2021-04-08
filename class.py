class Budget:

  def __init__(self, name):
    self.name = name
    self.balance = 0


  def deposit(self, amount):
    self.balance = amount

    return f"Your new balance is {self.balance} in {self.name} budget"

  def withdraw(self, amount):
    if self.balance < amount:
      return "Insufficient funds"
    else:
      self.balance = self.balance - amount

      feedback = "Transaction was successful \n"
      feedback += f"Your new balance is {self.balance} in {self.name} budget"

      return feedback

  def get_balance(self):
    feedback = f"The balance for {self.name} is {self.balance}"

    return feedback

  def transfer_balance(self, amount, category_object):
    if self.name == category_object.name:
      feedback = "Error \n"
      feedback += "You cannot transfer within the same category"

      return feedback


    if self.balance < amount:
      return "Insufficient funds"
    else:
      self.balance -= amount
      category_object.balance += amount

      feedback = "Transfer Successful \n"
      feedback += f"The balance for {self.name} is {self.balance} \n"
      feedback += f"The balance for {category_object.name} is {category_object.balance}"

      return feedback

  

food = Budget("food")
clothing = Budget("clothing")
entertainment = Budget("entertainment")

food.deposit(10000)
clothing.deposit(50000)
entertainment.deposit(250000)

print(food.withdraw(12000))
print(clothing.withdraw(5000))
print(entertainment.withdraw(25000))

print(food.get_balance())
print(clothing.get_balance())
print(entertainment.get_balance())

print(food.transfer_balance (1200, entertainment))
print(food.transfer_balance(200, clothing))
print(clothing.transfer_balance(12000, entertainment))
print(clothing.transfer_balance(2000, food))
print(entertainment.transfer_balance(12000, food))
print(entertainment.transfer_balance(2300, clothing))


   
