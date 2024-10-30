def MaxWater(Height:list):

    left=right=0
    length = len(Height)
    right=length-1
    water=0

    while left<right:
        length=right-left-1
        if Height[left]<Height[right]:
            left+=1
            water=big((small(Height[left],Height[right])*length),water)
        #elif Height[left]>Height[right]:
        else:
            right-=1
            water=big((small(Height[left],Height[right])*length),water)
    return water

def small(a,b):
    if a<b:
        return a
    else :
        return b

def big(a,b):
    if a>b:
        return a
    else :
        return b


test=[1,8,6,10,5,1,8,3,7,9]
print(MaxWater(test))