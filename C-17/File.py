# open(filename, mode)

# f = open("demofile.txt", "w")

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the file, returns an error if the file exists

# f  = open("demofile.txt", "r")
# # print(f.read(6))
# print(f.readline())
# f.close()

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
