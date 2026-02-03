import re

def check_validity(password):
    """
    Checks the validity of a user's password.
    Returns error messages or a success confirmation.
    """
    errors = []

    if len(password) < 6 or len(password) > 16:
        errors.append(f'Password length must be between 6 and 16 characters. The length of your password is {len(password)}.')

    if not re.search(r'[A-Z]', password):
        errors.append('Password must contain at least one uppercase letter')

    if not re.search(r'[a-z]', password):
        errors.append('Password must contain at least one lowercase letter')

    if not re.search(r'[0-9]', password):
        errors.append('Password must contain at least one number between 0 and 9')

    if not re.search(r'[$#@]', password):
        errors.append('Password must contain at least one of the following characters: $, #, @')
    
    if errors:
        return f'Error!\n{"\n".join(errors)}'
    return 'Success! Your password is valid and saved!'

password = input('Please enter your password: ')

print(check_validity(password))
