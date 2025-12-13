from os import listdir
from os.path import isfile, join

mypath = "."
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith(".txt")]

for file in onlyfiles:
    with open(mypath+"/"+file, "r", encoding="utf-8") as f:
        data = f.readlines()

    write_arr = []
    for line in data:
        if line.startswith("#"):
            write_arr.append(line)
        else:
            char = line.strip("\r\n")
            write_arr.append(char+"\t"+str(hex(ord(char[0])))[2:].upper()+"\n")

    
    with open(mypath+"/"+file, 'w', encoding="utf-8") as f:
        f.writelines(write_arr)

            
