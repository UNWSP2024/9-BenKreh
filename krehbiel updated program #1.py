#ben Krehbiel
#3/26/2025
#coun


def count():
    total = 0


    while True:
        try:
            search = str(input("Input the name of the desired file and the extension (names.txt): "))

            if search == "stop":
                break

            with open(search, "r") as file:

                for line in file:
                    line = line.strip()
                    if line:
                        total += 1

            print(f"total lines so far: {total}")

        except FileNotFoundError:(
            print("File not found. Please enter a valid file name."))

        except Exception as e:(
            print(f"An error occurred: {e}"))

count()
