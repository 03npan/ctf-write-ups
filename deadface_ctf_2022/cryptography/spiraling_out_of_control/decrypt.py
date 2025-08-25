ct = "fmbi~i{v1d`t3ygz~vfbn"
shift = [0,1,1,2,3,5,8,13,21,34]
i = 0
pt = ""

for char in ct:
    x = ord(char)
    pt += chr(x - shift[i % 10])
    i += 1
 
print(pt)