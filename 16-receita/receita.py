EXPECTED_BAKE_TIME = (int(40))

def bake_time_remaining(elapsed_time):

    return EXPECTED_BAKE_TIME - elapsed_time

print(bake_time_remaining(30))

def preparation_time_in_minutes(number_of_layers):

    return number_of_layers * 2

print(preparation_time_in_minutes(2))

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):

    return number_of_layers + elapsed_bake_time
        
print(elapsed_time_in_minutes(2, 30))



