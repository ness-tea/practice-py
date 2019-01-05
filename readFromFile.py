def readFromFile(txtFile):
    names = {}
    with open(txtFile,'r') as open_file:
        all_text = open_file.read().split('\n')
        for name in all_text:
            if name not in names:
                names[name] = 1
            elif name in names:
                names[name] += 1
        print(names)

if __name__ == "__main__":
    txtFile = str(input("Please enter the name of the text file: "))
    readFromFile(txtFile)
