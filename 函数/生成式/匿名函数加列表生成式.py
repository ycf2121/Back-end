names=['张明言','刘华强','苍井空','alex']
aaa=map(lambda x:x+"_SB",names) #匿名函数
print(aaa)
print(list(aaa))    #打印

print([name+"_SB" for name in names])   #列表生成式

names=['alexSB','egon','wxxSB','OLDBOYSB']
print([name for name in names if name.endswith('SB')])  #列表生成式
aaa=filter(lambda x:x.endswith('SB'),names) #匿名函数
print(aaa)
print(list(aaa))
print(list(aaa))