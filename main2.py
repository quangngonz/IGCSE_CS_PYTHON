input_string = "LDD 23 ADD 1 STO 23 LDD 24 SUB 5 ADD 23 OUT"

operand = {
    "OUT": 10010101,
    "SUB": 10010110,
    "ADD": 10010111,
    "STO": 10011000,
    "LDD": 10011001
}

processing = input_string.split(" ")
print(processing)

def convert_denery_to_binary(denery):
    return bin(int(denery))[2:].zfill(8)

for i in processing:
    if i in operand:
        print(operand[i], end=" ")
    else:
        print(convert_denery_to_binary(int(i)))

print()
