def is_prime(number):   # We created a function to make it easier for us
    """ Return True if number is prime otherwise False """
    counter = 0 # Variable to keep track of the factors of each number
    if number > 1:  # Because 1 is not a prime number
        for i in range(1, number + 1): # Loop through the number + 1, so that the number can be included.
            if number % i == 0: # Divide the number by i each time the loop execuetes
                counter += 1    # Increase counter by 1
    
    if counter == 2:    # After the loop, If counter is 2 (because prime numbers have only two factors)
        return True # Return True
    return False    # Otherwisw, Return False

print(is_prime(5))  # That should be True
print(is_prime(4))  # This should be False
print(is_prime(1))  # This should be False
