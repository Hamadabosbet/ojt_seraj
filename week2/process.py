
def process(items, filter_func, manipulate_func,action_func):


    items=list(filter(filter_func,items))
    items=list(map(manipulate_func,items))
    print(items)

    for item in items:
        action_func(item)

print("********process2*********")
numbers = [-100, 330, 11, 121, 215, 99]
process(numbers,lambda x:x%2!=0 and -400<x<100 and x!=7,lambda x:x*1.17,lambda x:print("the tax is :"+str(x)))



print("\n","********process2*********")
students=[("hamda","python",80),("shishi","python",60),("mohmad","java",80)]
action_func=lambda x:print("you have student named  " +x[0]+" learning Python with grade "+str(x[2])+": "+x[0]+"'s grade ("+str(x[2])+") is now ")
process(students,lambda x: x[1]=="python" and x[2]>70,lambda x:(x[0],x[1],(x[2]+5)),action_func)


