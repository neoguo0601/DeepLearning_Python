import numpy as np
#交换矩阵的其中两行
a = np.arange(25).reshape(5,5)
print (a)
a[[0,1]] = a[[1,0]]
print (a)

#找出数组中与给定值最接近的数
z = np.array([[0,1,2,3],[4,5,6,7]])
a = 5.1
print (np.abs(z-a).argmin())

#判断二维矩阵中有没有一整列数为0？
z = np.random.randint(0,3,(2,10))
print (z)
print (z.any(axis=0))

#生成二维的高斯矩阵
#help(np.random.randint)

x,y = np.meshgrid(np.linspace(-1,1,10),np.linspace(-1,1,10))
print (x)
print (y)
D = np.sqrt(x**2+y**2)
print (D)
sigma,mu = 1,0
a = np.exp(-(D-mu)**2/(2*sigma**2))
print (a)


