import os

if os.path.exists("copy.txt"):
   os.remove("copy.txt")

else:

 print("File not found")