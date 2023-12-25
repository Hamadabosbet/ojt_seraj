
import string

#q4



def count_dict(text):
    for char in string.punctuation:
        text = text.replace(char,"")
    text=text.split()
    dict={x:text.count(x) for x in text}
    sorted_dic={k: v for k, v in sorted(dict.items(), key=lambda x: x[1],reverse=True)}
    print(sorted_dic)




text="hamd hamd mohamad ? . abo sbet abo sbet"
print(text)
count_dict(text)


#q15

def  clean_anagrams(words):
    words = [list((string.lower())) for string in words]
    [string.sort() for string in words]
    words = ["".join(string) for string in words]
    words=set(words)
    return words


words=["nap", "teachers", "cheaters", "PAN","ear", "era","hectares"]
print(clean_anagrams(words))








####q17


def remove_duplicates(items):
    items=set(items)
    return list(items)

print(remove_duplicates([1,2,2,2,5]))




#q18

def is_prime(number):
    divide=2
    while(number%divide!=0):
        divide+=1

    if divide==number:
        return True
    else:
        return False


def return_prime(n):
    prime_list=[]
    for i in range(2,n):
        if is_prime(i)==True:
            prime_list.append(i)
    return prime_list

def return_mersenne_prime(n):
    prim_list=return_prime(n)
    prim_mersenne_list=[]

    for i in range(2,n):
        number=(2**i)-1
        if (number) in prim_list:
            prim_mersenne_list.append(number)


    return prim_mersenne_list




print(return_mersenne_prime(100))



#q19

def power_set(my_set):
    n=len(my_set)
    for i in range(2**n):
        subset=set()
        for j in range(n):
            if (i & (1 << j)):
                subset.add(my_set[j])
        yield subset


for s in power_set((([1,3,6]))):
    print(s)


