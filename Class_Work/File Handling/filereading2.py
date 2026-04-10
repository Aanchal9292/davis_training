# to open file for read operation
filev = open("firstfile.txt","r")
# to check file is open or not 
if(filev):
    # to read data from file
    data = filev.read()
    if(data):
        print("Content of file : ")
        while(data):
            print(data)
            data = filev.readLine()
    else:
        print("File is empty")
    # closing file
    filev.close()
else:
    print("Unable to open the file")