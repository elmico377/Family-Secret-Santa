import os
import random

if not os.path.exists('output'):
    os.makedirs('output')

names = ["Michael", "Sabrina", "Benjamin", "Tiffany", "Ricardo", "Jennifer", "Miguel", "Diana", "Walter", "Armando", "Yolanda"]
lower_names = []
for name in names:
    lower_names.append(name.lower())
names = lower_names

#print(names)

caesar_shift = random.randint(1,15)

#print (caesar_shift)
cipher_names = []
for name in names:
    new_name = ""
    for i, v in enumerate(name):
        new_char = ord(v) + caesar_shift
        if new_char > ord('z'):
            new_char = new_char - ord('z') - 1
            new_char = ord('a') + new_char 
        new_name = new_name + chr(new_char)
    cipher_names.append(new_name)

#print(new_names)
gift_names = []
for name in cipher_names:
    gift_names.append(name)
random.shuffle(gift_names)

i = 0
while i < len(gift_names):
    if gift_names[i] == cipher_names[i]:
        temp = gift_names[i]
        gift_names[i] = gift_names[(i+1)%len(gift_names)]
        gift_names[(i+1)%len(gift_names)] = temp
    i = i + 1
    

# print(cipher_names)
# print(gift_names)

weird_number = (caesar_shift + 77)

fileName = "output/gift_exchange_list.txt"
outFile = open(fileName, "w")
outFile.write(str(weird_number) + "\n")
outFile.write(str(cipher_names))
outFile.write('\n')
outFile.write(str(gift_names))
outFile.close()

print("Names have been generated in \'gift_exchange_list.txt\' in the output directory")

            