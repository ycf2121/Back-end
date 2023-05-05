nums=[1,3,7,11,22,34,55,78,111,115,137,149,246,371]
def search(search_num,nums):
    print(nums)
    if len(nums) == 0:  #如果为nums长度为0则没找到
        print('notfind it')
        return

    min_index = len(nums) // 2  #将列表nums的长度除2取整
    # print(min_index)
    if search_num > nums[min_index]:    #判断要查询的数字是不是比除2取整后的数字大
        nums=nums[min_index+1:]         #当前索引加一，因为上面已经比较过当前数字了
        search(search_num,nums)         #继续调用search函数查
        # print(nums)

    elif search_num < nums[min_index]:  #判断要查询的数字是不是比除2取整后的数字小
        nums=nums[:min_index]           #不写从最小开始到当前索引
        search(search_num,nums)         #继续调用search函数查
        # print(nums)
    else:
        print('find it')
search(111,nums)    #要查询的数字和列表nums
