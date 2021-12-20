str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str2 = "RahulShetty"

print(str[1]) #a

print(str[0:5]) # Rahul

print(str + " " + str1)  # concatenation

print(str2 in str)  # substring check

var = str.split(".")  # it divides the string where is a "." on separate values in list that can be reached by index
print(var)
print(var[0])

str4 = " great "  # removes whitespaces at the beginning and the end of the string
print(str4.strip())

# removes whitespaces only at the beginning of the string (left side of the string)
print(str4.lstrip())

# removes whitespaces only at the end of the string (right side of the string)
print(str4.rstrip())
