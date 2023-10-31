import math

def is_prime(num):
   
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

number = 18
result = is_prime(number)
print(result)
