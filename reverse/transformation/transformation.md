Transformation
===

### - Reverse Engineering
### - 20 Points

### Description
I wonder what this really is... enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
enc:
```
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰摤捤㤷慽
```

### Hints
1. You may find some decoders online

### Approach
I used this command to inspect the file
```bash
> file enc
enc: UTF-8 Unicode text, with no line terminators
```

I know that utf are hexadecimal used to express pretty much any character out of ascii. So I tried to see what happened if I did this
```bash
> xxd -p enc | tr -d '\n'
e781a9e68dafe48d94e499bbe384b6e5bda2e6a5b4e78d9fe6a5aee78db4e38cb4e6919fe6bda6e5bcb8e5bcb0e691a4e68da4e3a4b7e685bd%
```
* I have no idea why there is a % at the end of output

for now it looks good, let's put that aside and analyze the task once more

this thing looks like python code to me
```python
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

sorting this code it becomes this:
```python
for i in range(0, len(flag), 2)]):
    ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1]))
```
