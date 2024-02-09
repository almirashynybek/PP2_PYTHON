def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

mylist = [2, 3, 6, 8, 13, 46]
prime_numbers = filter_prime(mylist)
print(prime_numbers)