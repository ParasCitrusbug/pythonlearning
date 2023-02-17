class atm:
    def __init__(self, account_holder_name: str, acccount_number: int, balance=0):
        self.account_holder_name = account_holder_name
        self.acccount_number = acccount_number
        self.balance = balance
        self.pin = int

    def view_account_info(self) -> str:
        return f" account holder name = {self.account_holder_name}\n accountnumber = {self.acccount_number} \n account balance = {self.balance}"

    def create_pin(self) -> int:
        input_pin = int(input("Enter new pin: "))
        self.pin = input_pin
        return f"your pin is {self.pin}"

    def add_amount(self) -> str:
        input_pin = int(input("enter your pin: "))
        if input_pin == self.pin:
            input_balance = int(input("Enter the amount: "))
            self.balance = self.balance + input_balance
            return f"Now your balence is {self.balance}"
        else:
            return f"Invalid pin please enter valid pin"

    def withdrawal_amount(self) -> str:
        input_pin = int(input("enter your pin: "))
        if input_pin == self.pin:
            input_balance = int(input("Enter the amount: "))
            if input_balance < self.balance:
                self.balance = self.balance - input_balance
                return f"Now your balence is {self.balance} and withdrawal is sucess"
            else:
                return "insufisant balance"
        else:
            return f"Invalid pin please enter valid pin"

    def check_balance(self) -> str:
        input_pin = int(input("enter your pin: "))
        if input_pin == self.pin:
            return f"Your balance is {self.balance}"
        else:
            return f"Invalid pin please enter valid pin"
