import os
import time

def load_array(in_list):
    in_list = in_list[1:len(in_list)-2]
    in_list = in_list.replace('\'','')
    in_list = in_list.split(', ')
    return in_list

fileName = "gift_exchange_list.txt"
inFile = open(fileName, "r")

caesar_shift = int(inFile.readline()) - 77

people_list = inFile.readline()
people_list = load_array(people_list)

gift_list = inFile.readline()
gift_list = load_array(gift_list)

# print(people_list)
# print(gift_list)

decipher_names = []
for name in people_list:
    new_name = ""
    for i, v in enumerate(name):
        new_char = ord(v) - caesar_shift
        if new_char < ord('a'):
            new_char =  ord('a') - new_char - 1
            new_char = ord('z') - new_char 
        new_name = new_name + chr(new_char)
    decipher_names.append(new_name)

decipher_gift_names = []

for name in gift_list:
    new_name = ""
    for i, v in enumerate(name):
        new_char = ord(v) - caesar_shift
        if new_char < ord('a'):
            new_char =  ord('a') - new_char - 1
            new_char = ord('z') - new_char 
        new_name = new_name + chr(new_char)
    decipher_gift_names.append(new_name)


index_name = -1
while index_name < 0:
    name_to_find = input("Please enter your name: ").lower()
    index_name = decipher_names.index(name_to_find)
    if  index_name < 0:
        print("Name not found please try again")

print("Your secret santa is: " + str(decipher_gift_names[index_name]))

time.sleep(5)
