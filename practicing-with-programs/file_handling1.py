import json
import os

data={"name": "Hemant", "age": 21, "language": "Python"}

#writing json data to a file
with open("data.json","w") as file:
    json.dump(data,file)
    
print("Json files created successully!")

#lets read it now
with open("data.json","r")as file:
    print(json.load(file))

#now lets try to delete the file
if os.path.exists("data.json"):
    os.remove("data.json")
    print("successfully deleted")
else:
    print("file not found")