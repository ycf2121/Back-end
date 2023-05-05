l=[item **2 for item in range(1,5) if item > 2]
print(l)

names=['egon','alex_sb','wupeiqi','yuanhao']
names=[name.upper() for name in names]
print(names)

res = print('x') if 5 > 3 else print('y')
