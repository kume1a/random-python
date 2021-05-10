import requests
import time

URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
INITIAL_NOTHING = '12345'

nothing = INITIAL_NOTHING
while True:
	web_content = requests.get(f'{URL}?nothing={nothing}').content.decode('utf-8')
	nothing = web_content.split(" ")[-1]
	print(web_content)
	time.sleep(.2)
	if web_content.endswith('html'):
		break
