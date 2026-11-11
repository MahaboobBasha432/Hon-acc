import sys
def main():
    if len(sys.argv) != 2:
        print("Usage: python task c.py read|read|append|find")
        return
    option=sys.argv[1].lower()
    if option == "read":
        filename=input("Enter file name to read: ")
        try:
            with open(filename, "r", encoding="utf-8") as f:
                print(f.read())
        except FileNotFoundError:
            print("File not found")
    elif option == "append":
        source=input("Enter source file name: ")
        destination=input("Enter destination file name: ")
        try:
            with open(source, "r",encoding="utf-8") as f:
                data=f.read()
            with open(destination, "a",encoding="utf-8") as f:
                data=f.write(data)
            print("Data appended sucessfully")
        except FileNotFoundError:
            print("Source file not found")
    elif option == "find":
        filename=input("Enter file name to search: ")
        word=input("Enter word to find: ")
        try:
            with open(filename, "r",encoding="utf-8") as f:
                data=f.read()
            print("Word count: ")
        except FileNotFoundError:
            print("File not found")
    else:
        print("Invalid Input")
if __name__== "__main__":
    main()
          
