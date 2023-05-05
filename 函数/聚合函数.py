salaries={
    'egon':3000,
    'alex':100000000,
    'wupeiqi':10000,
    'yuanhao':2000
}

def func(k):
    return salaries[k]
print(func(k='egon'))
print(max(salaries,key=func)) #next(iter_s)
print(min(salaries,key=func)) #next(iter_s)

print(sorted(salaries,key=lambda k:salaries[k],reverse=True))
