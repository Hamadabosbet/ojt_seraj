from functools import reduce


def sum_digit(num):
    sum = 0
    while (num != 0):
        sum = sum + num % 10
        num = num // 10
    return sum




# #q20
# sentence=input("Please enter a sentence:")
# sentence=sentence.split()
# sentence.reverse()
# print(" ".join(sentence))



# #q22
# login_name=input("Please enter a login name:")
#
# if login_name=="Admin":
#     password=input("Please enter your password:")
#     if password=="TheMaster":
#         print("Welcom!!")
#     elif password=="":
#         print("Canceled")
#     else:
#         print("Wrong password")
#
#
#
# elif login_name=="":
#
#     print("Canceled")
#
# else:
#     print("I do not Know you")


# #q23
# year=int(input("Please enter a year:"))
#
#
# if year%4==0 and year%100!=0:
#         print("year is a leap year")
# elif year%100==0 and year%400==0:
#         print("year is a leap year")
# else:
#     print("year is not a  leap year")
#


#24
#
# num=int(input("Please enter a number:"))
# sum=0
# while(num!=0):
#     sum=sum+num%10
#     num=num//10
# print(sum)


# #25
# num=int(input("Please enter a number:"))
#
# a1,a2=1,1
# print(a1,a2,sep="\n")
# while((a1+a2)<num):
#     a3=a1+a2
#     a1=a2
#     a2=a3
#     print(a3)

#
# #ex
# print("Number   | Square")
# print("-"*19)
# for i in range(1,21):
#     print(str(i),str(i**2),sep="        |")
#
#
#

##q26

# low_number=int(input("Please enter a low number:\n"))
# high_mumber=int(input("Please enter a high  number:"))
#
# for i in range(low_number,high_mumber):
#     if i%2==0:
#         print(i)














#q28

#
# number=int(input("Please enter a number:"))
#
# for i in range(number):
#     print("",end="\n")
#     for k in range(number):
#         print("*",end="")
#


# #q27
#
# import math
# pi=0
# for i in range(20):
#     pi=pi+((-3)**-i)/((2*i)+1)
#
# pi=math.sqrt(12)*pi
#
# print(pi)




#q29



# str='4799 2739 8713 6272'
#
# #Reverse the number
#
# str = ''.join(str.split()[::-1])
# array=[]
# for i in range(len(str)):
#     digit=int(str[i])
#     if(i%2!=0):
#         digit=int(str[i])*2
#         if(digit>10):
#             array.append(sum_digit(digit))
#         else:
#             array.append(digit)
#     else:
#         array.append(digit)
#
#
# print(array )
# sum_arr=sum(array)
#
# if sum_arr%10==0:
#     print(" the credit card number is valid")
# else:
#     print(" the credit card number is  not valid!!!")



#q34
# def trace(M):
#
#     return sum([M[i][i] for i in range(len(M))])
#
# M=[[1,2,3],[4,5,6],[7,8,9]]
#
# print(trace(M))

##################################

#q35
#
#
# def rot13_word(word):
#     return ''.join([chr((ord(c) - 97 + 13) % 26 + 97) for c in word])
#
#
#

##################################
# def rot13_sentence(sentence):
#     sentence = sentence.split()
#     encoded_words = [rot13_word(word) for word in sentence]
#     return ' '.join(encoded_words)
#
#
# print(rot13_sentence("hello world"))
#
##################################
#q31

#
# list1 = ["Jan", "Feb", "March", "Apr", "May", "Jun", "Jul", "Agu", "Sep", "Oct", "Nov", "Dec"]
# list2 = [44.7, 55.2, 66, 87.4, 97.4, 43.5, 75.4, 87.3, 45.3, 64.3, 73.3, 62.3]
#
# data = (sorted(zip(list2, list1)))
# list2,list1=zip(*data)
# print(list2,list1)


##################################
# # q3
#
#
# p=[4,5,0,2]
#
# dpdx=[]
# for i,c in enumerate(p[1:],1):
#     dpdx.append(i*c)
#
# print(dpdx)
##################################

# def get_gcd(a,b):
#     '''
#
#     Return the greatest commmon divisor of two numbers.
#
#     args:
#           a(int):A decimal integer
#           b(int:Another decimal integer
#
#
#     Return: int number of  gcd of   a and b
#     '''
#
#     r = a % b
#     while r!=0:
#         a = b
#         b = r
#         r = a % b
#     return b



# print(get_gcd(1071,462))


##################################
#
#
# def rank(list):
#     rank_list=[1]
#     rank=1
#     rank_index=0
#     for i,num in enumerate(list[1:],1):
#         rank+=1
#         if num==list[i-1]:
#             rank_list.append(rank_list[rank_index])
#             rank_index+=1
#         else:
#             rank_list.append(rank)
#             rank_index += 1
#     return rank_list
#
# scores=[50,75,75,87,32,32]
# scores.sort()
# scores.reverse()
# print(rank(scores))


##################################
# def outer_func():
#     def inner_func():
#         a = 9
#         print("inside inner_func, a is {} (id={})".format(a, id(a)))
#         print("inside inner_func, b is {} (id={})".format(b, id(b)))
#         print("inside inner_func, len is {} (id={})".format(len, id(len)))
#     len = 2
#     print("inside outer_func, a is {} (id={})".format(a, id(a)))
#     print("inside outer_func, b is {} (id={})".format(b, id(b)))
#     print("inside outer_func, len is {} (id={})".format(len, id(len)))
#     inner_func()
#
#
# a, b = 6, 7
# outer_func()
# print("in global scope, a is {} (id={})".format(a, id(a)))
# print("in global scope, b is {} (id={})".format(b, id(b)))
# print("in global scope, len is {} (id={})".format(len,id(len)))

##################################
# Make this code work:
#
# //... your code


# def what():
#     strList=[]
#
#     def ma(n):
#         nonlocal strList
#         strList.append(n)
#         return "".join(strList[::-1])
#
#     return ma
#
#
#
# ma = what()
# print(ma('a'))
# print(ma('b'))
# print(ma('c'))
# # print(ma('a')) //'a'
# # print(ma('b')) //'ba'
# # print(ma('c'))//'cba'


###########
# def fromStr(str):
#     def subsets(leng=None):
#         nonlocal str
#         if leng is None:
#             leng = len(str)
#             subsets = [str[i:i + j] for i in range(len(str)) for j in range(1, leng + 1) if i + j <= len(str)]
#         else:
#             subsets = [str[i:i + j] for i in range(leng,len(str)) for j in range(1, leng + 2) if i + j <= len(str)]
#         return subsets
#
#
#     return subsets


# subsets = fromStr("Lala")
# # print(subsets())
# # ['L', 'La', 'Lal', 'Lala', 'a', 'al', 'ala', 'l', 'la', 'a' ]
#
# print(subsets(1))
# # # # ['a', 'al', 'ala', 'l','la','a']


# print(sorted("Nobdy expects the Spanish Inquisition".split(),key=lambda x:x.lower()))

#
# list2=["a","b","c","d"]
#
# def my_join(str):
#         return lambda list:(reduce(lambda x, y: f'{x}{str}{y}', list2))
#
# x=my_join(",")
# print(x(list2))
#


##################################
# #q8
# def apply(func, list):
#     for i in range(len(list)):
#         list[i] = func(list[i])
#
# list=[2,4,8,4]
# apply(lambda x:x*5,list)
# print(list)
#
#
# def func1(f):
#     return lambda x: f(x +2)
#
# func2 = func1(lambda x:x*x)
# print(func2(2))

##################################




#q9
#
# def bubble_sort(items, order):
#     n = len(items)
#     for i in range(n - 1):
#         print(i)
#         for j in range(n - i - 1):
#             print(j)
#             if order(items[j]) >order(items[j + 1]):
#                 items[j], items[j + 1] = items[j + 1], items[j]
#
#     return items
#
# numbers = [6, 4, 5, 2]
# fruits = ['apple', 'banana', 'cherry']
# sorted_fruits = bubble_sort(numbers, order=lambda x:x)
# print(sorted_fruits)
#
#



##################################

# what = lambda x: lambda y: y-1 < x+1
#
# f=what(4)
# print(f(9))
#




##################################
#q11
# s = ["There","are", "no", "miracles","in","this","world"]
# list_word=list(filter(lambda x:"a" in x,s))
# list_word=list(map(len,list_word))
# print(list_word)
#
# list_word=[word for word in s if "a" in word]
# print(list_word)
# list_word=[len(word) for word in list_word]
# print(list_word)

##################################



#q10
# def triangular_numbers(n):
#     sum = 0
#     for i in range(1, n + 1):
#         sum += i
#         yield sum
#
# n = 15
# triangular = triangular_numbers(n)
#
# for i in (triangular):
#     print(i)

##############################



#q4

# def dot_product(a, b):
#     dot = sum(ai * bi for ai, bi in zip(a, b))
#     return dot
#
# def cross_product(a,b):
#
#     a1=a[1]*b[2]-a[2]*b[1]
#     a2=a[2]*b[0]-a[0]*b[2]
#     a3=a[0]*b[1]-a[1]*b[0]
#
#     return [a1,a2,a3]
#
#
# a = [4, 5, 3]
# b = [4, 2, 6]
# c=zip(a,b)
# for i in c:
#     print(i)
# print(cross_product(a,b))
####################################

##q5
def extract_codons(sequence, frame):
    codon_list = []
    for i in range(frame, len(sequence) - 2, 3):
        codon = sequence[i:i + 3]
        codon_list.append(codon)

    return codon_list


dna_sequence = "AGTCTTATATCT"
codons = extract_codons(dna_sequence, 0)
print(codons)
