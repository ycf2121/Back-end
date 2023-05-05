#json的序列化1
# import json
# dic={'name':'egon','age':18}
# json_str=json.dumps(dic)
# with open('db.json',mode='wt',encoding='utf-8') as f:
#     f.write(json_str)
# print(json_str)

#json的序列化1
# import json
# dic={'name':'egon','age':18}
# with open('db.json',mode='wt',encoding='utf-8') as f:
#     json.dump(dic,f)

#json的反序列化1
# import json
# with open('db.json',mode='rt',encoding='utf-8') as f:
#     json_str=f.read()
# dic=json.loads(json_str)
# print(dic)

#json的反序列化2
# import json
# with open('db.json',mode='rt',encoding='utf-8') as f:
#     dic=json.load(f)
# print(dic)

