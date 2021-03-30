#!/usr/bin/env python3

key = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '{', '}']

flag = ["-"]*38
for keys in key:
    b = bytearray(open('eaxy', 'rb').read())
    for i in range(len(b)):
        b[i] ^= int(hex(ord(keys)),16)
    if "The XOR key you used" in str(b):
        for i in str(b).split("this is the ")[1:]:
            flag[int(i[0:2])] = str(keys)
print("".join(flag))
