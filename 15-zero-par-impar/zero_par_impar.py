def get_number():
    number = int(input("Type a number: "))

    return number


def even_odd_zero():
    results = get_number()

    if results % 2 == 0 and results != 0:
        return "Even"
    
    elif results % 2 != 0:
        return "Odd"
    
    else:
        return "Zero"
    


print(even_odd_zero())
    
    
