def age(n):
    if n == 1:
        return 20
    return age(n-1)+2
print(age(5))