# function simpal
def myfunc():
    print("working function")
myfunc()

# with arrgument
def myfunc(name):
    print("my name is " + name)

myfunc("paras")


# with arbitrary arrgument
def myfunc(*name):
    print("my full name is" , *name)

myfunc("paras","rajubhai", "pethani")

# keyword arrgument
def myfunc(fname, mname, lname):
    print("my full name is" , fname, lname)

myfunc(fname="paras",mname="rajubhai", lname="pethani")

# ricursion function
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

tri_recursion(5)
def sum(a,b):
    return a+b

sum()
# lambda funcsion
lamda_val = lambda a,b: a //b
print(lamda_val(50,12))


def myfunc(name):
    lambda a : a * name

lamda_var= myfunc("paras")
print(lamda_var)

#class python
class person:
    def __init__(self,fname,lname):
        self.fristname =fname
        self.lastname = lname

    def __str__(self) -> str:
        return f"{self.fristname} {self.lastname}"

    def myname(self):
        return f'{self.fristname}'
    def printmyname(self):
        print(self.fristname, self.lastname)

       
object_person = person("paras","pethani")
print(object_person)
print(object_person.myname())

#inheritance in python
class student(person):
    def __init__(self, fname, lname, mname):
        person.__init__(self,fname, lname)
        self.middelname = mname

    def welcome(self):
        print("welcome to "+self.fristname + " and " +self.middelname)


obj_student = student("paras", "pethani", "rajubahi")
obj_student.printmyname()
obj_student.welcome()

