test=(1,2.0,"three",True)
print(test)
for i in test:
    print(i)
    print(type(i))

'''
# test[1]=2
Traceback (most recent call last):
  File "G:\Documents\Python-Learning\第三次作业\tuple.py", line 7, in <module>
    test[1]=2
TypeError: 'tuple' object does not support item assignment
'''