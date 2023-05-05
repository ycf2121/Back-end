
x="{'a':彩色光晕,'b':2}"
a=list(eval(x))
print(a)
print(type(a))

b=str(eval(x))
print(b)
print(type(b))

c=dict(eval(x))
print(c)
print(type(c))

# eval(expression[, globals[, locals]])