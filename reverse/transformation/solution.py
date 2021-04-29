flag = "e781a9e68dafe48d94e499bbe384b6e5bda2e6a5b4e78d9fe6a5aee78db4e38cb4e6919fe6bda6e5bcb8e5bcb0e691a4e68da4e3a4b7e685bd"
submit = ""
#''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
for i in range(0, len(flag), 2):
    flag1 = (ord(flag[i]) << 8)
    flag2 = ord(flag[i + 1])
    print("flag1 " + str(flag1))
    print("flag2 " + str(flag2))
    print("char " + chr(flag1 + flag2))
    submit += chr(flag1 + flag2)
print(submit)
