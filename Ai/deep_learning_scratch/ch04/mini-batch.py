import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from dataset.mnist import load_mnist


(x_train, t_train), (x_test, t_test) = \
load_mnist(normalize=True, one_hot_label=True)
print(x_train.shape) # (60000, 784)
print(t_train.shape) # (60000, 10)


# 使用numpy的 np.random.choice() 随机抽取数据
tran_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(tran_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]


# mini-batch交叉熵误差函数的实现(支持一维和多维)
def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    
    batch_size = y.shape[0]
    return -np.sum(t * np.log(y + 1e-7)) / batch_size


# 当监督数据是标签形式，非one-hot，直接2,7这种
def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    
    batch_size = y.shape[0]
    # 监督数据是标签形式
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size
