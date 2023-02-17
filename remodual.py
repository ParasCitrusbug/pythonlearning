# find the pattern for password

import re

check_re = re.compile("^[A-Z][a-z]+[a-z0-9@#$%^!*&?><]{8,}$")


pettarn_password = "Ajhjfjj2@#@dffg"
if re.fullmatch(check_re,pettarn_password):
    print("good password")
else:
    print("bad password")


#para.citrusbug@gmail.com

email_valid = re.compile("^[a-z]+[.]*[a-z0-9]+[@][a-z]+[.][a-z]{2,}$")

pettarn_email = "paras.citrusbug@yahoo.in"
if re.fullmatch(email_valid,pettarn_email):
    print("valid email")
else:
    print("unvalid email")