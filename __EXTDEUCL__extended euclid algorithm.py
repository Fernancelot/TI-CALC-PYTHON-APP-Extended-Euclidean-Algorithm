# This program implements the Extended Euclidean Algorithm to find the GCD of two integers and the coefficients x and y such that ax + by = gcd(a, b).
# The program takes two integers as input and returns the GCD and the coefficients x and y.
# The extended_euclid function uses recursion to calculate the GCD and the coefficients x and y.
# The main function takes user input for the two integers and calls the extended_euclid function to display the results.
# The program handles invalid input by catching ValueError exceptions and displaying an error message.
# The main function is called to run the program.
# The program can be run and tested with different input values to verify the correctness of the Extended Euclidean Algorith

def extended_euclid(a, b):
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = extended_euclid(b % a, a)
    
    # Update x and y using results of recursive call
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd, x, y

# Function to display results
def main():
    print("Extended Euclidean Algorithm")
    
    try:
        a = int(input("Enter the first integer: "))
        b = int(input("Enter the second integer: "))
    except ValueError:
        print("Please enter valid integers.")
        return
    
    gcd, x, y = extended_euclid(a, b)
    
    print("GCD:", gcd)
    print("Coefficients x and y are:", x, "and", y)

# Run the main function
main()
