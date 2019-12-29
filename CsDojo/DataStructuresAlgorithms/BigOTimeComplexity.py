# O(n):T=a*n+b
def find_sum(given_array):
    total=0
    for i in given_array:
        total+=i
    return total

# O(1):T=c
def stupid_function(given_array):
    total=0
    return total

# O(n**2):T=a*n**2 + b*n + c
def find_sun_2d(array_2d):
    total=0
    for row in array_2d:
        for i in row:
            total+=i
    return total

    
