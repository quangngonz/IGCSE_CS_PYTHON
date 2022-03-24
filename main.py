string1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
string2 = "ABCDE"

duplicates = []

all_combinations = []

for i in string1:
    for j in i:
        all_combinations.append(i + j)
