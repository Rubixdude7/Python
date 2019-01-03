import io

# 'r' :: Read only
# 'r+' :: Read & Write
# 'w' :: Write only
# 'w+' :: Write & Read, Creates new file if one didn't exist
# 'a' :: Append only
# 'a+' :: Append & Read
test = open("tester.txt","w+")
str = input("Enter text to Write: ")
test.write(str)
test.close()

funny = open("funny.txt","r")
for i in range(100):
    print(funny.read(1))
