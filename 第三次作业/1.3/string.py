#spacelist存空格的位置
#遍历字符串 找到所有空格的位置，然后反转两个空格之间的内容
def reverse(str):
    str1=list(str)
    length = len(str)
    spacelist=[length]*100
    #这里spacelist[0]赋值成-1是因为后面检索的逻辑，需要赋值第一个空格位置为-1，才能让循环正确的指向第一个元素
    spacelist[0]=-1

    idx2=1
    for idx in range(length):
        if str1[idx]==' ':
            spacelist[idx2]=idx
            idx2+=1
    for i in range(idx2+1):
        '''for j in range(spacelist[i]+1,spacelist[i+1]):
            swap=spacelist[i+1]-1-j-1
            temp=str1[j+1]
            str1[j+1]=str1[swap]
            str1[swap]=temp
            '''
        # 这里被jetbrain的ai误导了 迭代的时候一直没转过弯来。。。
        space=spacelist[i+1]-spacelist[i]-1
        for j in range(space//2):
            a=spacelist[i]+1+j
            b=spacelist[i+1]-1-j
            swap=b-a-1
            temp=str1[a]
            str1[a]=str1[b]
            str1[b]=temp

    str2="".join(str1)
    print(str2)
str="a konomama bokutachi koe ga"
#reverse("a konomama bokutachi koe ga")
reverse("abcdefg hijklmn opq rst uvw")




