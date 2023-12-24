





#q1:
def max(items):
    if len(items)==1:
        return items[0]
    else:
        return max(items[1:]) if  max(items[1:])>items[0] else items[0]



def min(items):
    if len(items)==1:
        return items[0]
    else:
        return max(items[1:]) if  max(items[1:])<items[0] else items[0]






#q3
def sum_even(numbers):
    if  len(numbers)==0:
        return 0

    if numbers[0]%2==0:
        return numbers[0]+sum_even(numbers[1:])
    else:
        return sum_even(numbers[1:])

#q4
def mul(items):
    if  len(items)==0:
        return 0
    return items[0] * sum_even(items[1:])






#q5
def average_items(items):
    if len(items) == 1:
         return items[0]

    return (items[0] + (len(items)-1)*average_items(items[1:]))/len(items)
