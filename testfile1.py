string1 = "Bonnie"
string2 = "runnin' down the hill"
string3 = string1 + " is " + string2
print(string3)

if 3 == 2:
	print("3 is equal to 2")
elif 3 <= 2:
	print("3 is less than or euqal to 2")
else:
	print("3 is greater than 2")

def myfunc(Name):
	print("In myfunc")
	print("Hi" + " " + Name)
#myfunc()

myfunc("Bonnie")
