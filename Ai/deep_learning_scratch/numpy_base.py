import numpy as np


x = np.array([1, 2, 3])
# shape: 获取数组的形状
print(x.shape) 

# ndim: 获取数组的维度
print(x.ndim)  

# flatten: 将多维数组展平为一维数组
x.flatten()

# reshape: 改变数组的形状
y = x.reshape((3, 1))
print(y.shape)
print(y)