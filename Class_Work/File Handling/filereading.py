# to open file for read operation
filev = open("firstfile.txt","r")
# to check file is open or not 
if(filev):
    # to read data from file
    data = filev.read()
    print(data)
    print("-------------")
    print("No. of characters : ",len(data))
    # closing file
    filev.close()
else:
    print("Unable to open the file")