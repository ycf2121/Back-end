#实现打印商品详细信息，用户输入商品名和购买个数，则将商品名，价格，购买个数加入购物列表，如果输入为空或其他非法输入则要求用户重新输入
msg_dic={
    'apple':10,
    'tesla':100000,
    'mac':3000,
    'lenovo':30000,
    'chicken':10,
}
shopping_cart=[]
while True:
    for i in msg_dic:
        info='商品名称:%s 商品价格:%s' % (i, msg_dic[i])
        print(info.center(50,' '))
    name=input('请输入商品名称:').strip()
    if name not in msg_dic:
        print('输入的商品名称名称不正确，请重新输入：')
        continue

    while True:
        count = input('请输入购买个数:').strip()
        if count.isdigit():
            count=int(count)
            break
        else:
            print('商品的个数必须为整数')

    for item in shopping_cart:
        if name == item['name']:
            item['count']+=count
        break
    else:
        print(name,count)
        price=msg_dic[name]
        info={'name':name,'count':count,'price':price}
        shopping_cart.append(info)
    print(shopping_cart)