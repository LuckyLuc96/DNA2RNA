def conversion(input):
    array = []
    for unit in input:
        for char in unit:
            if char == "A":
                char = "U"
            elif char == "U":
                char = "A"

            elif char == "C":
                char = "G"
            elif char == "G":
                char = "C"

            elif char == "T":
                char = "A"
            else:
                char = " "
            array.append(char)
    return ''.join(array)


def main():
    userinput = input("Enter a strand of DNA to convert it to RNA:\n").upper()
    result= conversion(userinput)
    print(result)
if __name__ == "__main__":
    main()
