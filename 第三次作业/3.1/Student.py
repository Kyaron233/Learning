class student:
    def __init__(self,name,age,score1,score2,score3):
        self.name=name
        self.age=age
        self.score1=score1
        self.score2=score2
        self.score3=score3

    def avgScore(self):
        print ("平均分：%d" %((self.score1+self.score2+self.score3)/3))
    def display(self):
        print("姓名：%s " %(self.name)+"年龄：%s" %(self.age))
        print("第一科分数：%d" %(self.score1))
        print("第二科分数：%d" %(self.score2))
        print("第三科分数：%d" %(self.score3))

kobe=student("kobe",23,54,55,56)
bryant=student("bryant",24,100,98,85)

kobe.display()
kobe.avgScore()
bryant.display()
bryant.avgScore()