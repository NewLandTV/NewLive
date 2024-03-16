# Imports
import os

# Functions
def Subtitle(text):
    with open(f"{os.getcwd()}\\Character\\Subtitle.txt", "w", encoding = "utf-8") as file:
        file.write(text)

def ClearSubtitle():
    with open(f"{os.getcwd()}\\Character\\Subtitle.txt", "w", encoding = "utf-8") as file:
        file.truncate()