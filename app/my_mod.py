


# this is the "app/my_mod.py" file

# here is a documented version of the function

def enlarge (n):
    ''' This is a docstring. 
    This function enlarges a number.
    Pass in n as a parameter.
    Returns a larger version of the number.
    '''
    return float(n)* 100


if __name__ == 'main':

    x = input("Please input number")
    result = enlarge(x) # we can't do tests unless the function returns sth
    print(result)

