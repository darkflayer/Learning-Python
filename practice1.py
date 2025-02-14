# task 1 Below function calculates the factorial 
def factorial(num):
    if num==0 or num==1:
        return 1
    return num*(num-1)
number=int(input("Enter a number: "))
print(f"Factorial of {number} :",factorial(number))