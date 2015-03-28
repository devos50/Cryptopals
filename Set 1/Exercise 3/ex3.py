import string

def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

s1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736".decode('hex')
for l in range(0, 255):
	s2 = chr(l) * 36
	print xor_strings(s1, s2)