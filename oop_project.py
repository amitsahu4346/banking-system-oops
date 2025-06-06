from bank_accounts import BankAccount, InterestRewardsAcct, SavingsAcct

Amit = BankAccount(1000, "Amit")
Anjali = BankAccount(2000, "Anjali")

print(Amit.getBalance())
print(Anjali.getBalance())

print(Anjali.deposit(500))

print(Amit.withdraw(10000))
print(Amit.withdraw(10))

print(Amit.transfer(10000, Anjali))
print(Amit.transfer(100, Anjali))

Dipesh = InterestRewardsAcct(1000, "Dipesh")

print(Dipesh.getBalance())

print(Dipesh.deposit(100))

print(Dipesh.transfer(100, Amit))

Ritesh = SavingsAcct(1000, "Ritesh")

print(Ritesh.getBalance())

print(Ritesh.deposit(100))

print(Ritesh.transfer(10000, Anjali))
print(Ritesh.transfer(1000, Anjali))
