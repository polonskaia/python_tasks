def divide(numerator, denominator):
    try:
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise ValueError
        
        if denominator == 0:
            return f'Oops, {numerator}/{denominator}, division by zero is error!!!'
        else:
            return f'Result is {numerator / denominator}'
    except ValueError:
        return 'Value Error! You did not enter a number!'


print(divide(4, 8))
print(divide(8, 0))
print(divide("9", 3))