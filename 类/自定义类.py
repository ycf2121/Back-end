#自定义类
class Mymeta(type):
    def __init__(self,class_name,class_bases,class_dic):

        super(Mymeta,self).__init__(class_name,class_bases,class_dic)

    def __call__(self, *args, **kwargs):
        obj=self.__new__(self)
        self.__init__(obj,*args,**kwargs)
        obj.__dict__={'_%s__%s' %(self.__name__,k):v for k,v in obj.__dict__.items()}
        return obj

class Foo(object,metaclass=Mymeta):

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

obj=Foo('xxx',18,'male')
print(Foo.__dict__)
print(obj.__dict__)
