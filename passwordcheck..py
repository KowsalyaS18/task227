import re
def patterncheck():
	passwd = input("enter your password")
	reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
	pas = re.compile(reg)
	match = re.search(pas, passwd)
	if match:
		print("Password is valid.")
	else:
		print("Make sure your Password has a number,a upper case and a lower case letter,a special character and of 6-20 digits long !!")
if __name__ == '__main__':
	patterncheck()
