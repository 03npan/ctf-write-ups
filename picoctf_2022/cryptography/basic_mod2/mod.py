output = ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "_"]
flag = ""

with open('D:/GitHub/ctf-write-ups/picoctf-2022/cryptography/basic_mod2/message.txt','r') as file:
    for line in file:
        for num in line.split():
            char = pow(int(num), -1, 41)
            flag += output[char]

print("picoCTF{" + flag + "}")