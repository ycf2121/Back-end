msg_dic={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}
print(msg_dic)
for i in msg_dic:
    print(i)
for i in msg_dic.keys():
    print(i)
for i in msg_dic:
    print(msg_dic[i])
for i in msg_dic.values():
    print(i)
for i,j in msg_dic.items():
    print(i,j)
for i in msg_dic.items():
    print(i)

'''
msg_dic={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}
names=[]
values=[]
for k in msg_dic:
    names.append(k)

for i in msg_dic:
    values.append(msg_dic[i])
print(names,values)


keys=msg_dic.keys()
print(keys)
for i in keys:
    print(i)
l=list(keys)
print(l)
vals=msg_dic.values()
print(vals)
for i in vals:
    print(i)
m=list(vals)
print(m)
print(msg_dic.items())
print(list(msg_dic.items()))
'''