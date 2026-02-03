import re

def check_validity(password):
    """
    Checks the validity of a user's password.
    Returns error messages or a success confirmation.
    """
    errors = []
    checks = {
        f'Password length must be between 6 and 16 characters. The length of your password is {len(password)}.': lambda p: 6 <= len(p) <= 16,
        'Password must contain at least one uppercase letter': lambda p: re.search(r'[A-Z]', p),
        'Password must contain at least one lowercase letter': lambda p: re.search( r'[a-z]', p),
        'Password must contain at least one number between 0 and 9': lambda p: re.search(r'[0-9]', p),
        'Password must contain at least one of the following characters: $, #, @': lambda p: re.search(r'[$#@]', p)
    }

    for  message, fun in checks.items():
        if not fun(password):
            errors.append(message)

    if errors:
        return f'Error!\n{"\n".join(errors)}'
    return 'Success! Your password is valid and saved!'

password = input('Please enter your password: ')

print(check_validity(password))