# Define a function to check Prime number
def check_prime(n):
    divisor = []
    for i in range(1,n+1):
        if n%i == 0:
            divisor.append(i)
    if len(divisor) == 2:
        print('This is a prime number')
    else:
        print('This is not a prime number')


print('Please type a number.')
num = int(input())
check_prime(num)
