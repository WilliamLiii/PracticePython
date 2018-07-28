# define a function to create Fibonnaci numbers which is a sequence of number where the next number in the sequence
# is the sum of previous two
def Fibonnaci(n):
    if n == 0:
        result = None
    elif n == 1:
        result = [1]
    elif n == 2:
        result = [1,1]
    elif n > 2:
        result = [1,1]
        count_number = 2
        while n > 2:
            result.append(result[-1]+result[-2])
            count_number += 1
            if count_number == n:
                break
    print(result)

num = int(input('Please type a number: '))
Fibonnaci(num)
