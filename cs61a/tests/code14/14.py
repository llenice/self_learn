# demo_1: Account class

class Account:
	""" An account has a balance and a holder

	>>> a = Account('John')
	>>> a.deposit(100)
	100
	>>> a.withdraw(90)
	10
	>>> a.withdraw(90)
	'Insufficient funds'
	>>> a.balance
	10
	"""

	#(3) deposit = 666

	def __init__(self, account_holder):
		self.balance = 0
		self.holder = account_holder
		#(2) self.deposit = 9999

	def deposit(self, amount):
		""" Add amount to balance """
		self.balance = self.balance + amount
		return self.balance

	def withdraw(self, amount):
		"""Subtract amount from balance if funds are available """
		if amount > self.balance:
			return 'Insufficient funds'
		self.balance = self.balance - amount
		return self.balance

# python3 -m doctest demo.oy
# python3 -i demo.py
# Account
# lls = Account('lls')
# lls
# type(Account)
# type(lls)
# lls.balance
# lls.holder
# lls.deposit(10) explain this is a call expression with ()
# lls.withdraw(9)
# lls.withdraw(100)

# demo_2

#(1) lls.deposit
#    bound method deposit 
#(2) add self.deposit = 999 in __init__
#    lls.deposit
#    999
#(3) remove (2) and add deposit = 666 as class attribute
#    lls.deposit
#    bound method deposit



# Animation, Comic, Game, Novel
# ACGN = type('ACGN',(),{})
# ACGN()
# ACGN
# type(ACGN)
