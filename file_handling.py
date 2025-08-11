file_name = input("Please input the name of the file you wish to read: ")
try:
    with open(file_name, "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found. Please check the filename.")
    file_name = input("Please input the name of the file you wish to read: ")
    try:
       with open(file_name, "r") as file:
           data = file.read() 
    except FileNotFoundError:
        print("File still not found. Pleaase start again.")

words = data.split()
word_count = len (words)
upper_case = data.upper()

with open("output.txt", "w") as file2:
    file2.write(upper_case)
    file2.write(str(word_count))
    print ("The output file has been successfully created and it contains ", word_count, "words")


