# La sucesión de fibonacci #

def sucesion_fibonacci():
    prev = 0
    next = 1

    for i in range(51):
        print(prev)
        fib = prev + next
        prev = next
        next = fib


sucesion_fibonacci()
