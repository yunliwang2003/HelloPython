def calc(a,b):
    print(a+b)

calc(10,20)
print(calc(1,2))# None
print('-'*50)

def calc2(a,b):
    s=a+b
    return s

get_s=calc2(10,20)
print(get_s)

get_s2=calc2(calc2(1,2),3)
print(get_s2)
print('-'*50)

def get_sum(num):
    s=0
    odd_sum=0
    even_sum=0
    for i in range(1,num+1):
        if i%2!=0:
            odd_sum+=i
        else:
            even_sum+=i
        s+=i
    return odd_sum,even_sum,s

result=get_sum(10)
print(type(result))
print(result)
# 解包赋值
a,b,c=get_sum(10)
print(a,b,c)
print('-'*50)





