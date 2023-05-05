num1=b'4' #bytes
num2=u'4' #unicode,python3中无需加u就是unicode
num3='壹' #中文数字
num4='Ⅳ' #罗马数字
print(num1.isdigit())
print(num2.isdigit())
print(num3.isdigit())
print(num4.isdigit())

print(num2.isdecimal())
print(num3.isdecimal())
print(num4.isdecimal())

print(num2.isnumeric())
print(num3.isnumeric())
print(num4.isnumeric())