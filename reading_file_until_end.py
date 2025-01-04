with open("sample txt","r") as file:
    while (line := file.readline().strip()):
        print (line)