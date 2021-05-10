import os

loc = "C:\\Users\\PC\\Desktop\\Python"
tree = os.walk(loc)

a,b,c = 0,0,0
for e in tree:
    _,dirs,files = e
    a += len(dirs)
    b += len(files)
    for file in files:
        if(file.endswith(".py")):
            c+=1

print(a,b,c)
