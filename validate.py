def validate_num(inp):
    response = ['Input validated successfully', 'Validation failed! Input is not a number.']
    if type(inp) == int or type(inp) == float:
        print(response[0])
        return True
    else:
        print(response[1])
        return False

def validate_str(inp):
    response = ['Input validated successfully', 'Validation failed! Input is not a string.']
    if type(inp) == str:
        print(response[0])
        return True
    else:
        print(response[1])
        return False

def validate_email(inp):
    response = ['email validated successfully', 'Validation failed! email does not contain "@".', 'Validation failed! Check the positions of "@" and ".".']
    indices_of_at = [i for i, a in enumerate(inp) if a == '@']

    # checks for the presence of @
    if len(indices_of_at) > 0:
        indices_of_dot = [i for i, a in enumerate(inp) if a == '.']
        for i in indices_of_dot:
            for k in indices_of_at:
                # checks if there is a "." after "@" example@somewhere.com
                if i>k:
                    print(response[0])
                    return True
        print(response[2])
        return False
    print(response[1])
    return False