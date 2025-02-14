 #funtion to reverse the string 
'''
def reverse_string(s):
    return s[::-1]

# Example usage
string = "Python"
reversed_string = reverse_string(string)
print("Reversed String:", reversed_string)  # Output: "nohtyP"

'''



#fucntion to check whether the given number is prime or not
'''
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Loop from 2 to sqrt(n)
        if n % i == 0:
            return False
    return True

# Example usage
number = 29
print(f"Is {number} prime?", is_prime(number))  # Output: True
'''
