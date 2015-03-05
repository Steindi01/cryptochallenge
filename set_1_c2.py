hexadecimal1 = '1c0111001f010100061a024b53535009181c'
hexadecimal2 = '686974207468652062756c6c277320657965'

string1 = hexadecimal1.decode('hex')
string2 = hexadecimal2.decode('hex')
b1 = bytearray(string1)
b2 = bytearray(string2)

b = bytearray(len(b1))
for i in range(len(b1)):
	b[i] = b1[i] ^ b2[i]

print "Result:", str(b).encode('hex')