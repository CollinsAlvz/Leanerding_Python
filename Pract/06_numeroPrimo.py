# ES un numero primo?#

def print_primes():
    for num in range(2, 101):
        prime = True
        for i in range(2, int(num/2)+1):
            if num % i == 0:
                prime = False
                break
        if prime:
            print(num)


print_primes()
