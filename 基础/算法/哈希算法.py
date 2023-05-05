
#算法
import hashlib
m=hashlib.md5()
m.update('123'.encode('utf-8'))
print(m.hexdigest())

n=hashlib.md5()
m.update('1234'.encode('utf-8'))
print(n.hexdigest())
print(len(m.hexdigest()))
print(len(n.hexdigest()))

import hmac
m=hmac.new('哈哈哈'.encode('utf-8'))
m.update('123'.encode('utf-8'))
print(m.hexdigest())
print(len(m.hexdigest()))

n=hmac.new('哈哈哈'.encode('utf-8'))
n.update('1234'.encode('utf-8'))
print(n.hexdigest())
print(len(n.hexdigest()))
