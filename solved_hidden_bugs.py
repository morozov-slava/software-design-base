import unittest


class BankAccount:
	def __init__(self, initial_balance: float):
		self.balance = initial_balance

	def deposit(self, value: float) -> None:
		if value < 0:
			raise AssertionError("Value can't be negative")
		self.balance += value

	def withdraw(self, value: float) -> None:
		if value < 0:
			raise AssertionError("Value can't be negative")
		if self.balance - value < 0:
			raise AssertionError("Insufficient funds on balance")
		self.balance -= value

	def getBalance(self) -> float:
		return self.balance


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(1000.0)

    def test_initial_balance(self):
        self.assertEqual(self.account.getBalance(), 1000.0)

    def test_deposit(self):
        self.account.deposit(500.0)
        self.assertEqual(self.account.getBalance(), 1500.0)
        
    def test_deposit_negative_value(self):
        with self.assertRaises(AssertionError):
              self.account.deposit(-200.0)
			
    def test_withdraw(self):
        self.account.withdraw(200.0)
        self.assertEqual(self.account.getBalance(), 800.0)

    def test_withdraw_insufficient_funds_on_balance(self):
        with self.assertRaises(AssertionError):
              self.account.withdraw(1200.0)

    def test_withdraw_negative_value(self):
        with self.assertRaises(AssertionError):
              self.account.withdraw(-500.0)

    def test_multiple_operations(self):
        self.account.deposit(300.0)
        self.account.withdraw(100.0)
        self.account.deposit(200.0)
        self.assertEqual(self.account.getBalance(), 1400.0)


if __name__ == "__main__":
    unittest.main()


