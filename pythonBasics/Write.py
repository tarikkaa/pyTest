#file = open('test.txt')
#file.close()

# below is the same as two strings above
#with open('test.txt') as file:

# read the file and store all the lines in list
# reverse the list
# write the list back to the file

with open('test.txt', 'r') as reader:     # 'r' or 'w' read or write mode
    content = reader.readlines()   # [12345, boss, cat, dog, eggs]
    reversed(content)              # [eggs, dog, cat, boss, 12345]
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)


