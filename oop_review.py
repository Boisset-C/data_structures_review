# OBJECT ORIENTED PROGRAMMING (OOP)

# FOUR KEY PRINCIPLES:

# 1. Encapsulation: bundling of the attributes and methods of an object into a single unit, the CLASS.
# using encapsulation you can hide the internal state of the object using public methods and attribute that act as an interface (setters and getters). Behind those doors are private attributes and methods that control how data changes and how it is exposed.

# SUMMARY
# Python uses encapsulation to organize internal data behind clear public interfaces whithout enforcing access restrictions in an absolute manner. It centralizes data modification within public methods, you establish a reliable way to validate input and protect classes from accidental tampering. 

# USING A SINGLE UNDERSCORE: convention says attribute is meant for internal use. Should not be accessible from the outside
class Wallet:
   def __init__(self, balance):
       self._balance = balance # For internal use by convention

   def deposit(self, amount):
       if amount > 0:
           self._balance += amount # Add to the balance safely

   def withdraw(self, amount):
       if 0 < amount <= self._balance:
           self._balance -= amount # Remove from the balance safely

# USING A DOUBLE UNDERSCORE: triggers a mechanism called name mangling where Python automatically renames the attribute behind the scenes.
# EXAMPLE: __balance becomes _Wallet__balance
# This is used as a safeguard to prevent accidental collisions, making it harder to happen on accident but not foolproof.

class Wallet1:
   def __init__(self, balance):
       self.__balance = balance # Private attribute

   def deposit(self, amount):
       if amount > 0:
           self.__balance += amount # Add to the balance safely

   def withdraw(self, amount):
       if 0 < amount <= self.__balance:
           self.__balance -= amount # Remove from the balance safely

account = Wallet1(500)
print(account.__balance) # AttributeError: 'Wallet' object has no attribute '__balance'

# To get the current value of __balance, you can define a get_balance method
# Example below:

class Wallet1_Correct:
   def __init__(self, balance):
       self.__balance = balance

   def deposit(self, amount):
       if amount > 0:
           self.__balance += amount

   def withdraw(self, amount):
       if 0 < amount <= self.__balance:
           self.__balance -= amount
  
   def get_balance(self):
       return self.__balance


acct_one = Wallet1_Correct(100)
acct_one.deposit(50)
print(acct_one.get_balance()) # 150

acct_two = Wallet1_Correct(450)
acct_two.withdraw(28)
print(acct_two.get_balance()) # 422

acct_two.deposit(150)
print(acct_two.get_balance()) # 572

# DEFINING PRIVATE METHODS: using __validate to check if every deposit or withdrawal is a positive number

class Wallet_With_Private_Method:
   def __init__(self):
       self.__balance = 0

   def __validate(self, amount):
       if amount <= 0:
           raise ValueError('Amount must be positive')

   def deposit(self, amount):
       self.__validate(amount)
       self.__balance += amount

   def withdraw(self, amount):
       self.__validate(amount)
       if amount > self.__balance:
           raise ValueError('Insufficient funds')
       self.__balance -= amount

   def get_balance(self):
       return self.__balance

acct_one = Wallet_With_Private_Method()
acct_one.deposit(3)
print(acct_one.get_balance()) # 3

acct_one.deposit(50)
print(acct_one.get_balance()) # 53

acct_one.deposit(-4)  # ValueError: Amount must be positive
acct_one.withdraw(-8) # ValueError: Amount must be positive
acct_one.withdraw(58) # ValueError: Insufficient funds

# PROPERTIES
# attributes that act like methods under the hood. You define like a method but use it as an attribute. Properties can be accessed using dot. They run logic behind the scene when you get, set, or delete values. 

# GETTER EXAMPLE: 
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self): # A getter to get the radius
        return self._radius
  
    @property
    def area(self):  # A getter to calculate area
        return 3.14 * (self._radius ** 2)

my_circle = Circle(3)

print(my_circle.radius) # 3
print(my_circle.area) # 28.26

# SETTER EXAMPLE: 
class Circle:
    def __init__(self, radius):
        self.radius = radius # Calling the setter

    @property
    def radius(self):  # A getter to get the radius
        return self._radius

    @radius.setter
    def radius(self, value):  # A setter to set the radius
        if value <= 0:
            raise ValueError('Radius must be positive')
        self._radius = value

my_circle = Circle(3)
print('Initial radius:', my_circle.radius) # Initial radius: 3

my_circle.radius = 8
print('After modifying the radius:', my_circle.radius) # After modifying the radius: 8

# Summary

# The takeaway from this is that:

  # - Getters let you retrieve a value or even compute a value on the fly.
  # - Setters let you modify the values safely by running checks before assignment.
  # - Properties are what tie these getters and setters together so you can write logic # while still using dot notation.
  # - Deleters let you define what happens when an attribute is deleted.



# 2. Inheritance:

# 3. Polymorphism:

# 4. Abstraction:
