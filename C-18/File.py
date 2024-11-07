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

# f = open("demofile3.txt", "a")
# f.write("Now the file has more content!")
# f.close()
# f = open("demofile3.txt", "r")
# print(f.read())
# f.close()

# f = open("demofile3.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

# Delete the file
# import os
# os.remove("demofile3.txt")

# File path exists
# import os
# if os.path.exists("demofile3.txt"):
#     os.remove("demofile3.txt")
# else:
#     print("The file does not exist")

# Delete folder
import os
os.rmdir("myfolder")
