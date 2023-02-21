import getpass
import re


class ReModule:
    """Check for password and email validation."""

    def password_chck(self, pattern_password: str) -> bool:
        """Check password validation."""
        password_valid = re.compile("^[A-Z][a-z]+[a-z0-9@#$%^!*&?><]{8,}$")

        if re.fullmatch(password_valid, pattern_password):
            return pattern_password
        else:
            return "Enter valid Password"

    def email_chack(self, pattern_email: str) -> str:
        """Check email validation."""
        email_valid = re.compile("^[a-z]+[.]*[a-z0-9]+[@][a-z]+[.][a-z]{2,}$")

        if re.fullmatch(email_valid, pattern_email):

            return email_input
        else:
            return "unvalid email"


obj = ReModule()

password_input = getpass.getpass("enter password")
email_input = input("enter email")

print(obj.password_chck(password_input))
print(obj.email_chack(email_input))
