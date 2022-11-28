# Programme 01 === Array Traversing

list = ["Computer", "Civil", "Electrical", "Power"]
length = len(list)
for i in range (0, length):
    print(list[i])
    i = i + 1


# Programme 02 === Insert an Item in an Array with Position
list = ["Computer", "Civil", "Electrical", "Power", ""]
temp_length = len(list)
position = int(input("Please Enter a position: "))
item = str(input("Please Enter a value: "))
length = temp_length

while position <= temp_length:
    list[temp_length - 1] = list[temp_length - 2]
    temp_length -=1
list[position - 1]=item
print(list)