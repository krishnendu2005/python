f=open("new12.txt","a")
f.write("Welcome\n")

f.close()

f=open("new12.txt","r")
print(f.read())

f.close()

fr=open("new12.txt","r")

fw=open("copy.txt","w")

for line in fr:

  fw.write(line)
fr.close()
fw.close()