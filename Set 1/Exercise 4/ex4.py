import re

def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

f = open("4.txt", "r")
contents = f.readlines()

for line in contents:
	line = line.rstrip('\n').decode('hex')
	for l in range(0, 255):
		s2 = chr(l) * 120
		res = xor_strings(line, s2)
		match = re.match("^[a-zA-Z., ]*$", res)
		if match is not None:
			print res