file = open("test.txt")  # the full path to file is needed if the file locates in different place
# Read all the content of file
#print(file.read())

# Read only 2 first characters of file
#print(file.read(2))

# Read 2 lines in that case)
#print(file.readline())
#print(file.readline())

# Print line by line using 'readLine' method
'''line = file.readline()
while line != "":
    print(line)
    line = file.readline()'''

# Print line by line using 'readLines' method
for line in file.readlines():
    print(line)

file.close()