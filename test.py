#!python3
# -*- coding: utf-8 -*-
import os
import tempfile
import requests
import pyautogui
import time
import json

body = {
	"name": "test_name"
}

headers = {
	"Content-Type": "application/json"
}

res = requests.post("http://localhost:8080/api/v1/test", data=body)
print(res.content.decode('ascii'))