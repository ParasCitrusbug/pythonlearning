#variable
x = 5
y = "string" + 'python'
z = 21.25
print(x,y,z)
#VARIABLE TYPE
print(type(x),type(y),type(z))

#VARIABLE NAMEING
myname= "paras"
my_name= "paras"
_my_name= "paras"
My_name= "paras"
MyName= "paras"
MYNAME= "paras"
my_name3342= "paras"

#assign type of variable
x,y, z =5,"paras", 25.112
list_variable =[4,"milan",2504.25]
a,b,c =list_variable

#output variable
print(a,b,c)
print(a+c)

#global and local variable
global_var = "global variable"

def local_var():
    local_variable= "local variable"
    print(local_variable)

#using globale

def globalvariable():
    global global_variable 
    global_variable= "local variable"
    print(global_variable)