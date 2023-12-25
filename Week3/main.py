
from stack import creat_stack,pop,push,is_empty





def shrink_stack(chars_stack):
    stack=creat_stack()

    while not is_empty(chars_stack):
        char = pop(chars_stack)
        print(char)
        maxchar = char
        while char!="@" and not is_empty(chars_stack):
            char2 = pop(chars_stack)
            print(char2)

            if maxchar > char2:
                maxchar=maxchar

            else:
                maxchar=char2

    # print(maxchar)
    push(stack,maxchar)
    push(stack, "@")
    return stack


print(shrink_stack(["b","@","b","z","a"]))