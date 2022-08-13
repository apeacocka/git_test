# from operator import mod


# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# #you need to close the file when done with it.
# file.close()


# #you can open the file with the 'with' keyword, this way you don't have to remember to close your file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# #to write to a file, you need to change the mode, w writes over the file, a appends to it
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

#if the file doesn't exist, a new one will be created.
with open("./Day-024/my_file.txt", mode="a") as dog:
    dog.write("\nSame text.")

file = open("./Day-024/my_file2.txt")
contents = file.read()
print(contents)
#you need to close the file when done with it.
file.close()

#files and folders
#files can live in folders
#file paths /work/project/talk.ppt
#relative file paths are the directory you are working from ./talk.ppt
#to go upwards in the directory tree ../report.doc
# .. takes you up one step
#