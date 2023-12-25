
##################################
#q8
# def apply(func, list):
#     for i in range(len(list)):
#         list[i] = func(list[i])
#
# list=[2,4,8,4]
# apply(lambda x:x*5,list)
# list_string=["abc","gbd"]
# apply(lambda x:x.capitalize(),list_string)
#
# print(list_string)


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
# fruits = ['app', 'banana', 'che']
# sorted_fruits = bubble_sort(numbers, order=lambda x:x)
# print(sorted_fruits)




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



# q10

def triangular_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
        yield sum

n = 15
triangular = triangular_numbers(n)

for i in (triangular):
    print(i)

#############################



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
# def extract_codons(sequence, frame):
#     codon_list = []
#     for i in range(frame, len(sequence) - 2, 3):
#         codon = sequence[i:i + 3]
#         codon_list.append(codon)
#
#     return codon_list
#
#
# dna_sequence = "AGTCTTATATCT"
# codons = extract_codons(dna_sequence, 0)
# print(codons)


###########################
# c =0
# def calc():
#     c=0
#     def f1(x):
#         nonlocal c
#         c+=x
#         return c
#
#     def f2(x):
#         nonlocal c
#         c=c-x
#         return c
#
#
#     def f3(x):
#         nonlocal c
#         c = c * x
#         return c
#
#     def f4(x):
#         nonlocal c
#         c = c / x
#         return c
#
#
#     def f5():
#         return c
#     return [f1,f2,f3,f4,f5]
#
#
# sony = calc()
# sony[0](14)
# # print(sony[4]())
# # sony[1](4)
# # val = sony[4]()
# # print(val)
# # sony[3](val)
# # print(sony[4]())
# # sony[2](17)
# # print(sony[4]())
#






# ####B
# c =0
# def calc():
#     def f1(x):
#         global c
#         c+=x
#         return c
#
#     def f2(x):
#         global c
#         c=c-x
#         return c
#
#
#     def f3(x):
#         global c
#         c = c * x
#         return c
#
#     def f4(x):
#         global c
#         c = c / x
#         return c
#
#
#     def f5():
#         return c
#     return [f1,f2,f3,f4,f5]
#
#
#
# add=calc()[0]
# add(14)
# equal=calc()[4]
# print(equal())


#Output for the above values:
#14
#10
#1.0
#####################cccc
# import calc
# calc.add(3)
# print(calc.equal())
#
#
