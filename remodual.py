# find the pattern for password
import getpass
import re
class re_modual:
    def password_chck(self,pettarn_password) ->bool:
        check_re = re.compile("^[A-Z][a-z]+[a-z0-9@#$%^!*&?><]{8,}$")
        
        if re.fullmatch(check_re,pettarn_password):
            return True
        else:
            print("Enter valid Password")
            return False

    def email_chack(self,pettarn_email)->bool:
        email_valid = re.compile("^[a-z]+[.]*[a-z0-9]+[@][a-z]+[.][a-z]{2,}$")

        if re.fullmatch(email_valid,pettarn_email):
            
            return True
        else:
            print("unvalid email")
            return False
        
obj = re_modual()

password_input = getpass.getpass("enter password")
email_input = input("enter email")

print(obj.password_chck(password_input))
print(obj.email_chack(email_input))
