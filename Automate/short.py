import pynput.keyboard 
import subprocess
import os
import threading

domain_to_hex = {
    "startfacebook" : "",
    "startgoogle" : "",
    "startyoutube" : "",
    "startcmd" : ""
}

class Background:
    def __init__(self, time_interval):
        self.log = ""
        self.interval = time_interval

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            current_key = " " + str(key) + " "
        self.log += current_key

    def call(self, domain):
        subprocess.call("start https://www.%s.com"%domain, shell=True)

    def report(self):
        print(self.log)
        # if domain_to_hex["startfacebook"] in self.log:
        #     self.call("facebook")
        # elif domain_to_hex["startgoogle"] in self.log:
        #     self.call("google")
        # elif domain_to_hex["startyoutube"] in self.log:
        #     self.call("youtube")

        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

google = Background(6)
google.start()

