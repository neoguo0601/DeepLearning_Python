import numpy as np
#1:8*8棋盘矩阵，其中1、3、5、7行&&0、2、4、6列的元素置为1   1 ,3，5，7列&&0,2,4,6行也是1
z = np.zeros((8,8),dtype=int)
z[1::2,::2] = 1
z[::2,1::2] = 1
print (z)


z = np.random.random((10,10))
zmin,zmax = z.min(),z.max()

#归一化，将矩阵规格化到0～1，即最小的变成0，最大的变成1，最小与最大之间的等比缩放
z = 10*np.random.random((5,5))
print (z)
zmin,zmax = z.min(),z.max()
z = (z-zmin)/(zmax-zmin)
print (z)

#矩阵相加
z = np.zeros((5,5))
z += np.arange(5)
print (np.arange(5))
print (z)


#生成0~10之间均匀分布的11个数，包括0和10

z = np.linspace(0,10,11,endpoint=True,retstep=True)
print (z)
