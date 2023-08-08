filename = "russia_lastnames_translite_final.txt"
alphabet = "abcdefghijklmnopqrstuvwxyz"

with open(filename, "r") as file:
    strings = file.readlines()

for string in strings:
    string = string.strip()
    for letter1 in alphabet:
        for letter2 in alphabet:
            combination = letter1 + letter2
            new_string = string + combination
            print(new_string)

