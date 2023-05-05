#计算bmi
class people():
    def __init__(self,name,weight,height):
        self.name=name
        self.height=height
        self.weight=weight
        print('姓名：%s 体重(kg)：%s 身高(m)：%s' %(self.name,self.weight,self.height))
    @property
    def bmi(self):
        return self.weight / (self.height ** 2)

while True:

    try:
        print('输入q退出')
        name=input('请输入姓名:').strip()
        if name == 'q':break
        weight=input('请输入体重(kg):').strip()
        if weight == 'q':break
        heigth=input('请输入身高(m):').strip()
        if heigth == 'q':break
        # weight=int(weight)
        # heigth=float(heigth)

        peo1=people(name,int(weight),float(heigth))
        # peo1=people('ycf',65,彩色光晕.80)
        print(peo1.bmi)

    except Exception as e:
        print(e,'\033[46m输入有误\033[0m')
