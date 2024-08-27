import os

os.chdir("./labels/train")
files = os.listdir()
print(files)
for file in files:
    with open(file,"r") as f:
        line = f.readline()
        print("line:",line[0])
    
    with open(file,"w") as f:
        f.writelines(f"0 {line[1:]}")

    with open(file,"r") as f:
            line = f.readline()
            print("new :",line[0])
    
    print("Done")