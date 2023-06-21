#FizzBuzz
#Write a program that prints the numbers from 1 to 100.
#But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.  
#For numbers which are multiples of both three and five print “FizzBuzz”
def fizzbuzz(number):
    if number % 15 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return str(number)  # convert number to string

def main():
    """
    test the fizzbuzz function with 200,1000,10000
    """
    for i in [200, 1000,10000]:
        print(fizzbuzz(i))
        
#求0-1的随机数   
import random
def random_number():
    return random.random()

#随机数的测试
def test_random_number():
    for i in range(10):
        print(random_number())  





#run
main()
