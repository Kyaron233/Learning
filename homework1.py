
def oushu(m,num1):
    return (num1[int(m/2-1)]+num1[int(m/2)])/2

def jishu(m,num1):
    return num1[int(m/2)]

def homework(m,num):
    if m%2==0:
       return oushu(m,num)
    else:
        return jishu(m,num)

num1=[1,2,3,4,5,6,7,8,9]
num2=[1,2,3,4]

mid1=homework(len(num1),num1)
mid2=homework(len(num2),num2)

print(mid1,mid2)