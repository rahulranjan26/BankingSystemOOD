class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return "My name is:{}. I am {} years old  and I am a {}.".format(
            self.name, self.age, self.gender)


class Bank(User):
    def __init__(self, name, age, gender) -> None:
        super().__init__(name, age, gender)
        self.balance = 0.0

    def account_balance(self):
        print('Your Account Balance is {}'.format(self.balance))

    def deposit_amount(self, amount):
        self.balance += amount
        self.account_balance()

    def withdraw_amount(self, amount):
        if self.balance < amount:
            print('You have insufficient Balance in your account.', self.balance)
        else:
            self.balance -= amount
            self.account_balance()

    def view_details(self):
        print(self)


julie = Bank('Julie', 19, 'Female')
# julie.account_balance()
julie.deposit_amount(500)
julie.deposit_amount(300)
julie.withdraw_amount(200)
julie.withdraw_amount(500)
julie.withdraw_amount(400)
julie.view_details()
