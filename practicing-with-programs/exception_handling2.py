def check_age(age):
    if(age<18):
        raise ValueError("Age must be greater than 18")
    return "Allowed"
try:
    age=int(input("Enter the age: "))
    print(check_age(age))
except ValueError as e:
    print(f"custom exception : {e}")