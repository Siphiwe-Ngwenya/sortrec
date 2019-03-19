def sum_array(array):
    a=sum(array) #assigning 'a' to a sum of all the elements in the array
    return a

def fibonacci(n):
    """Recursive function that adds the sum of the precceding integers to n"""
    if n<=1:
        return n
    else :
        return fibonacci(n-1)+fibonacci(n-2) #Adding n to the numbers that precedes it in the series

def factorial(n):
    """This is a function that calls itself to perfom
    a mathematical calculation called factorial"""
    if n <=1:
        return 1
    else:
        return n * factorial(n-1) #multiplying n by every number the preceeds it

def reverse(word):
    """Recursive function that takes a string and prints it out in reverse"""
    if word == "": #testing if the string is empty or has contents
        return word
    else:
        return reverse(word[1:]) + word[0] #iterating through a string and returning it in reverse
