from solution import BankAccount

def test_deposit_increase_balance():
    account = BankAccount(100)
    assert account.deposit(50) == 150
    assert account.deposit(25) == 175          

def test_withdraw_decreases_balance():
    account = BankAccount(200)
    assert account.withdraw(50) == 150
    assert account.withdraw(100) == 50