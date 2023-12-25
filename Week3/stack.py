



def creat_stack():
    return []


def push(stack,item):
    stack.append(item)

def is_empty(stack):

    return len(stack)==0

def top(stack):
    if not is_empty(stack):
        return stack[-1]


def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        print("the stack is empty")

