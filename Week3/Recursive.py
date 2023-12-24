

#q1

def sum_digit(num):
    if num==0:
        return 0
    else:
        return num%10+sum_digit(num//10)




#q2

def count_digit(num):
    if num==0:
        return 0
    else:
        return 1+count_digit(num//10)



#q3

def count_odd_digit(num):
    if num==0:
        return 0
    if (num%10)%2==0:
        num=num//10
    return 1+count_odd_digit(num//10)


#q4
def print_reverse_str(str):
    if  len(str)==0:
        return
    print(str[-1], end='')
    print_reverse_str(str[:-1])

#q5
def sum_list(numbers):
    if  len(numbers)==0:
        return 0
    return numbers[0] + sum_list(numbers[1:])

#q6

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

#q7
def division(num1, num2):
    if num1 < num2:
        return 0
    return 1 + division(num1 - num2, num2)

#18

def is_palindrome(str):
    if len(str) <= 1:
        return True
    else:
        return  str[0] == str[-1] and is_palindrome(str[1:-1])


print(is_palindrome("llo"))