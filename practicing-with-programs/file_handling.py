
# #creating a file with some text
# with open("hello.txt","w") as file:
#     file.write("Hello this is a file handling tutorial.\n")
#     file.write("and i am trying this first time .\n")

# #now its tiem to read this file
# with open("hello.txt","r") as file:
#  content = file.read()
#  print("File Content :\n",content)


# #now writing 
# with open("hello1.txt","w") as file:
#     file.write("This is a new file.\n")
#     file.write("All the previous content is deleted\n")

# #reading to check the content
# with open("hello1.txt","r") as file:
#     print(file.read())

# #okay now here we going to do append 
# with open("hello.txt",'a') as file:
#     file.write("This is an append line.\n")

# with open("hello.txt","r") as file:
#     file.readline()
#     print(file.readline().strip())


#here now i will try the r+ mode 

# with open("hello.txt","r+") as file:
#     content=file.readlines()
#     content[0]="So this is the updated first line\n"
#     file.seek(0)
#     file.writelines(content)

# #checking 
# with open("hello.txt","r") as file:
#     print(file.read())