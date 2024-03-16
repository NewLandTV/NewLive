# Imports
import json
import os
import sys

from Utils.AI import Request
from Utils.Subtitle import *
from Utils.TTS import *

# Variables
data = {}

# Read data from file
with open(f"{os.getcwd()}\\Character\\Configurations\\{sys.argv[1]}\\Data.json", "r", encoding = "utf-8") as file:
    data = json.load(file)

# Functions
def Main():
    while True:
        message = input("JkhTV : ")
        response = Request(message)

        print(f"{data['name']} : {response}")
        Subtitle(response)
        Speak(response)
        ClearSubtitle()

if __name__ == "__main__":
    try:
        Main()
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)