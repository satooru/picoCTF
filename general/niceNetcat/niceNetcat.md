Nice netcat...
===

### - General Skills
### - 15 Points

### Description
There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 35652, but it doesn't speak English...

### Hints
1. You can practice using netcat with this picoGym problem: what's a netcat?
2. You can practice reading and writing ASCII with this picoGym problem: Let's Warm Up

### Approach
Using the given command
```bash
nc mercury.picoctf.net 35652
```
Gave me this *edited output
```
112 105 99 111 67 84 70 123 103 48 48 100 95 107 49 116 116 121 33 95 110 49 99 51 95 107 49 116 116 121 33 95 57 98 51 98 55 51 57 50 125 10
```

the hints makes a reference to ascii standard, so I'm gonna use the following python code to convert those ascii chars to human readable chars
```Python
import string

chars = [112, 105, 99, 111, 67, 84, 70, 123, 103, 48, 48, 100, 95, 107, 49, 116, 116, 121, 33, 95, 110, 49, 99, 51, 95, 107, 49, 116, 116, 121, 33, 95, 57, 98, 51, 98, 55, 51, 57, 50, 125, 10]

flag = ""

for number in chars:
    flag += chr(number)

print(flag)
```

It printed the flag
```
picoCTF{g00d_k1tty!_n1c3_k1tty!_9b3b7392}
```
