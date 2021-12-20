

ItemsInCart = 0
#2 items will be added to the cart


'''if ItemsInCart != 2:
    raise Exception("Products Cart count not matching")'''

if ItemsInCart != 2:
    pass

assert(ItemsInCart == 0)  # or you can use 'assert' to invoke an error when it is "false"

# try, catch
try:
    with open("test.txt", "r") as reader:
        reader.read()

except:
    print("Some how I reached this block because there is failure in try block")

try:
    with open("test.txt", "r") as reader:
        reader.read()

except Exception as e:
        print(e)

finally:
    print("Success")