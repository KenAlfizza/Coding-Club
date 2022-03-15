"""
Activity:
You are given a "raw-email.txt" file containing a list of emails, 1 email per line
Some emails end in @gmail.com, while others have @yahoo.com, @hotmail.com, etc

Instructions:
    Create a script to first read the .txt file
    Find all the emails ending in @gmail.com
    Write these emails ending in @gmail.com to a separate file, called "clean-email.txt"
    Write one email per line in this "clean-email.txt" file
    Bonus point:
        Write all the other emails, not ending in @gmail.com, to another file
        Name this file "legacy-email.txt"

Important tip:
    Make sure you run the script from the directory where the files are located

Resources:
    https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

"""
import os

if os.path.exists("clean-email.txt"):
    os.remove("clean-email.txt")
    
if os.path.exists("legacy-email.txt"):
    os.remove("legacy-email.txt")


clean_address = "gmail.com"
with open("raw-email.txt", "r") as file:
    all = file.readlines()
    for item in all:
        item = str(item)
        if clean_address in item:            
            with open("clean-email.txt", "a") as file:
                file.write(item)
        else:
            with open("legacy-email.txt", "a") as file:
                file.write(item)
                
                
                
                
                
