#!/usr/bin/env python3

input = open('eaxy', 'rb')
data = input.read()
input.close()

for val in range(0, 256):
    decoded_array = []
    for idx in range(0, len(data)):
        decoded_array.append(data[idx] ^ val)

    output = open('output/' + hex(val), 'wb')
    output.write(bytes(decoded_array))
    output.close()

