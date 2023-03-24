class ArthimeticClass:
    def add(x, y):
        # adding two numbers
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("inputs should be integers or floats")
        return x + y
    
    def subtract(x, y):
        # subtracting two numbers
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("inputs should be integers or floats")
        return x - y
    
    def multiply(x, y):
        # multiplying two numbers
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("inputs should be integers or floats")
        return x * y
    
    def divide(x, y):
        # dividing two numbers also make sure the denominator is not zero
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("inputs should be integers or floats")
        return x / y