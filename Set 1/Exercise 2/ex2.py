def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

s1 = "1c0111001f010100061a024b53535009181c".decode('hex')
s2 = "686974207468652062756c6c277320657965".decode('hex')
s3 = xor_strings(s1, s2)

print s3.encode('hex')