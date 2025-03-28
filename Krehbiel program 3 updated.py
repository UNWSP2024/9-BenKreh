#Ben Krehbiel
#3/28/2025
#search and smush

def smush():

    search = str(input("Input the name of the desired file and the extension (numbers.txt): "))
    with open(search, "r") as file:
        total = count = 0
        for line in file:
            try:
                num = float(line.strip())
                total += num
                count += 1
            except ValueError:
                pass

        if count > 0:
            average = total / count
            print(f"average: {average}")
        else:
            print("no valid numbers")



smush()
