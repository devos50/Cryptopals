def encrypt(str, key):
	curchar = 0
	res = ""
	for c in str:
		res += chr(ord(c) ^ ord(key[curchar]))
		curchar = curchar + 1
		if curchar == 3:
			curchar = 0
	return res.encode('hex')

s1 = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
print encrypt(s1, "ICE")