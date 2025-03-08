try:
    num=int(input("enter a number: "))
    result=10/num #where the error could be caused
    print("Result:",result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter a number.")
#for all kind of exception we use exception ehre we store the object in a variable that creates exception
except Exception as e:
    print(f"Unexpected error: {e}")

#for multiple exception 
except(ZeroDivisionError,ValueError) as e:
    print(f"Error:{e}")