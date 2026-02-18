class MyError(Exception):
    def __init__(self, number):
        super().__init__(f'You input negative number: {number}. Try again.')

def check_positive(number):
    try:
        number = float(number)
    except ValueError:
        return 'Error type: ValueError!'
    
    if number > 0:
        return f'You input positive number: {number}'
    else:
        return MyError(number)

    
print(check_positive(8.9))
print(check_positive(-19))
print(check_positive("abs"))
print(isinstance(check_positive("-235"), MyError))