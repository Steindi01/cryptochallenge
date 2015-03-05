import string as pystring

hexadecimal = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

string = hexadecimal.decode('hex')
b = bytearray(string)

for character in pystring.printable:
	result = bytearray(len(b))
	for i in range(len(b)):
		result[i] = b[i] ^ bytearray(character)[0]

	print "Result:", str(result), "Character:", character