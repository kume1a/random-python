URL = 'http://www.pythonchallenge.com/pc/def/map.html'

encoded = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
REPLACEABLE = "\"{|0)*+"
REPLACEMENTS = " ab,\'()"

def decode(encoded):
	decoded = "".join([chr(ord(letter) + 2) for letter in encoded])
	return decoded.translate(decoded.maketrans(REPLACEABLE, REPLACEMENTS))

decoded = decode(encoded)
solution_path = decode('map')

print(decoded)
print('\n')
print(solution_path)