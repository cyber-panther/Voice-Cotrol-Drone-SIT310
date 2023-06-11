from FileModificationHandler import FileModified
import json

import socket
import threading
import time

from word2number import w2n

import pyttsx3

responses = ""

class Controller:
    def __init__(self):
        print("test")
        self.local_ip = ''
        self.local_port = 8889
        self.socket = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM)  # socket for sending cmd
        self.socket.bind((self.local_ip, self.local_port))

        # thread for receiving cmd ack
        self.receive_thread = threading.Thread(target=self._receive_thread)
        self.receive_thread.daemon = True
        self.receive_thread.start()

        self.tello_ip = '192.168.10.1'
        self.tello_port = 8889
        self.tello_address = (self.tello_ip, self.tello_port)
        self.MAX_TIME_OUT = 15.0

    def send_command(self, command):
        self.socket.sendto(command.encode('utf-8'), self.tello_address)
        print('sending command: %s to %s' % (command, self.tello_ip))

        start = time.time()
        now = time.time()
        diff = now - start
        if diff > self.MAX_TIME_OUT:
            print('Max timeout exceeded... command %s' % command)
            return
        print('Done!!! sent command: %s to %s' % (command, self.tello_ip))

    def _receive_thread(self):
        # Listen to responses from the Tello.
        global responses
        while True:
            try:
                self.response, ip = self.socket.recvfrom(1024)
                print('from %s: %s' % (ip, self.response))
                responses = self.response.decode("utf-8")

            except (socket.error, exc):
                print("Caught exception socket.error : %s" % exc)


tello = Controller()

movement = ["move", "go"]
stunt = ["flip"]
turn = ["turn", "rotate", "spin", "degree", "angle"]
lift = ["take", "off"]

def command(txt):

    if any([x in txt for x in lift]):
        tello.send_command("takeoff")
        
    elif "land" in txt:
        tello.send_command("land")
        
    elif "time" in txt:
        tello.send_command("time?")
        engine = pyttsx3.init()
        engine.say("The flight time is " + responses + "Seconds")
        engine.runAndWait()
        
    elif "battery" in txt:
        tello.send_command("battery?")
        engine = pyttsx3.init()
        engine.say("The battery is at " + responses + "percent")
        engine.runAndWait()

    elif any([x in txt for x in movement]):

        if "up" in txt:
            try:
                distance = w2n.word_to_num(txt)
            except ValueError:
                distance = 50
            tello.send_command("up " + str(distance))

        elif "down" in txt:
            try:
                distance = w2n.word_to_num(txt)
            except ValueError:
                distance = 50
            tello.send_command("down " + str(distance))

        elif "left" in txt:
            try:
                distance = w2n.word_to_num(txt)
            except ValueError:
                distance = 50
            tello.send_command("left " + str(distance))

        elif "right" in txt:
            try:
                distance = w2n.word_to_num(txt)
            except ValueError:
                distance = 50
            tello.send_command("right " + str(distance))

        elif "forward" in txt:
            try:
                distance = w2n.word_to_num(txt)
            except ValueError:
                distance = 50
            tello.send_command("forward " + str(distance))

        elif "back" in txt:
            try:
                distance = w2n.word_to_num(txt)
            except ValueError:
                distance = 50
            tello.send_command("back " + str(distance))

    # Check if the word in stunt group is in the text
    elif any([x in txt for x in stunt]):
        if "left" in txt:
            tello.send_command("flip l")
        elif "right" in txt:
            tello.send_command("flip r")
        elif "forward" in txt:
            tello.send_command("flip f")
        elif "back" in txt:
            tello.send_command("flip b")
        else:
            tello.send_command("flip f")

    elif any([x in txt for x in turn]):
        if "left" in txt:
            try:
                angle = w2n.word_to_num(txt)
            except ValueError:
                angle = 90
            tello.send_command("ccw " + str(angle))
        elif "right" in txt:
            try:
                angle = w2n.word_to_num(txt)
            except ValueError:
                angle = 90
            tello.send_command("cw " + str(angle))
        else:
            tello.send_command("cw 90")

    elif txt == "":
        print("nothing")
        tello.send_command("command")
        
def file_modified():
    print("File Modified!")
    # take the text from the file output.txt in varible text
    f = open("output.txt", "r")
    text = f.read()
    f.close()
    # convert the text to json
    json_text = json.loads(text)

    command(json_text["text"])

    return False

fileModifiedHandler = FileModified("output.txt", file_modified)
fileModifiedHandler.start()
