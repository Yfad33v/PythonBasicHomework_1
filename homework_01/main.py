

def power_numbers(*args: int):
   return [i**2 for i in args if isinstance(i, int)]

def is_prime(k):
    if k > 1:
        for i in range(2, int(k / 2) + 1):
            if (k % i) == 0:
                return False
        else:
            return True
    else:
        return False

# filter types
ODD = "odd" #нечетный
EVEN = "even"  # четный
PRIME = "prime" # простое число


def filter_numbers(args,check):
    if check == EVEN:
        return list(filter(lambda x: x % 2 == 0, args))
    if check == ODD:
        return list(filter(lambda x: x % 2 != 0, args))
    if check == PRIME:
        return list(filter(is_prime, args))
