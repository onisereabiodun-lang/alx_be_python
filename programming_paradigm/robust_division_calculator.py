def safe_divide(numerator, denominator):
    try:
        # Try to convert both inputs to float
        num = float(numerator)
        denom = float(denominator)
        
        # Perform division
        result = num / denom
        return f"The result of the division is {result}"
        
    except ValueError:
        return "Error: Please enter numeric values only."
        
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
        
    except Exception as e:
        # Catch any other unexpected errors (good practice)
        return f"Error: An unexpected error occurred: {str(e)}"