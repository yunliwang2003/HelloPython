num=eval(input('请输入一个4位整数：'))
ge=num%10
shi=(num%100)//10
bai=(num%1000)//100
qian=(num%10000)//1000
print('个位：',ge)
print('十位：',shi)
print('百位：',bai)
print('千位：',qian)