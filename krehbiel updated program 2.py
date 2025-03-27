#ben krehbiel
#3/26/2025
#write that down write that down

import random as rn

def write():
    loops = int(input("input the amount of numbers you would like to write to the file: "))
    search = str(input("Input the name of the desired file and the extension (numbers.txt): "))
    with open(search, "w") as file:
        for i in range(loops):
            file.write(str(rn.randint(1,500)))
            file.write("\n")
            
write()

