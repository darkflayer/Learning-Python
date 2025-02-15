#in this we are trying to open a file
try:
    file= open("sample.txt","r")
    content=file.read()

except FileNotFoundError:
    print("file not found ")
else:
    print("file read successfully!")
    print(content)
finally:
    print("closing the file...")
    file.close()