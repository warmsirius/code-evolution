from common.functions import softmax, cross_entropy_error
import numpy as np


class Relu:
    def __init__(self):
        # mask 由True/False 构成的Numpy数组,
        self.mask = None
    
    def forward(self, x):
        # 会把正向传播时输入的x元素<=0的位置设为True,其他地方保存为False
        # 将输入所有小于等于0的元素置0
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0
        return out
    
    def backward(self, dout):
        # 将反向传播时传递进来的梯度dout,在mask为True的位置上也置0
        dout[self.mask] = 0
        dx = dout
        return dx


class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None # 损失
        self.y = None  # softmax的输出
        self.t = None  # 教师标签,监督数据(one-hot vector)

    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y, self.t)
        return self.loss

    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size #反向传播时，将要传播的值除以批的大小 batch_size 后，传递给前面的层的是单个数据的误差
        return dx


class Affine:
    def __init__(self, W, b):
        self.W = W
        self.b = b
        self.x = None
        self.dW = None
        self.db = None

    def forward(self, x):
        self.x = x
        out = np.dot(self.x, self.W) + self.b
        return out

    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)
        return dx
