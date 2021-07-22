def substring(st, dch):
	string = ""
	num = 0
	st += dch
	l = len(st)
	substr = []
	for i in range(l):
		if (st[i] != dch):
			string += st[i]
		else:
			if (len(string) != 0):
				substr.append(string)
			string = ""
	return substr
if __name__ == '__main__':
	str = input("enter your String")
	dch = ','
	res = substring(str, dch)
	for x in range(len(res)):
		print(res[x])
