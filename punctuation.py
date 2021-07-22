def specialCharacter(string):
	schar = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

	for x in string.lower():
		if x in schar:
			string = string.replace(x, "")
	print(string)
	
	
string = "welcome! hello,world$"
specialCharacter(string)
