import re

URL = 'http://www.pythonchallenge.com/pc/def/equality.html'

encoded_file = open("4_equality_data.txt")
encoded = encoded_file.read()
encoded_file.close()


res = re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", encoded)
print("".join(res))

