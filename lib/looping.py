#!/usr/bin/env python3

def happy_new_year():
    num = 10
    while num >= 1:
        print(num)
        num -= 1
        
    print("Happy New Year!")
        
# print(happy_new_year())
    

def square_integers(int_list):
    square_list = [num ** 2 for num in int_list]
    return square_list
  
# print(square_integers([2, 4, 6, 8]))

def fizzbuzz():
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
        
        
print(fizzbuzz())
