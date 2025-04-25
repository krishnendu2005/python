try:
    fp=open("file.txt","w")
    fp.write("python")
except:
    print("something wrong")
finally:
    fp.close        