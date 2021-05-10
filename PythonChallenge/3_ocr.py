URL = 'http://www.pythonchallenge.com/pc/def/ocr.html'

encoded_file = open("3_ocr_data.txt")
encoded = encoded_file.read()
encoded_file.close()

unique = [letter for letter in list(dict.fromkeys(encoded))]
filtered = filter(lambda letter: letter.isalpha(), unique)
decoded = "".join(list(filtered))

print(decoded)
