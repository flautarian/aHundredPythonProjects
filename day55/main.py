# Create the logging_decorator() function 👇

def logging_decorator(function, *args):
    def wrapper_function(*args):
        print(f"You called a {str(function.__name__)}")
        result = function(args[0], args[1], args[2])
        print(f"It returned {str(result)}")
    return wrapper_function

# Use the decorator 👇

@logging_decorator
def a_function(a, b, c):
    return a * b * c

a_function(1 ,2 ,3)