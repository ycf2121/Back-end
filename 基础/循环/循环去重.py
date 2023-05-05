stu_info=[
    {'name':'isetan','age':18,'sex':'male'},
    {'name':'isetan','age':18,'sex':'male'},
    {'name':'isetan','age':18,'sex':'male'},
    {'name':'axxxx','age':73,'sex':'male'},
    {'name':'oldboy','age':84,'sex':'female'},
]
new_info=[]
for i in stu_info:
    if i not in new_info:
        new_info.append(i)
print(new_info)