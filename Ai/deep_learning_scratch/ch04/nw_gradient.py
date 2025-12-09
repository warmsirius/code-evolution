# 神经网络实现求梯度代码
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient


class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3)  # 生成2x3的权重矩阵,用高斯分布初始化
 
    def predict(self, x):
        return np.dot(x, self.W)
 
    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)
        return loss
    
net = simpleNet()
print("初始权重W的值：")
print(net.W)
x = np.array([0.6, 0.9])
p = net.predict(x)
print("预测的类别概率p：")
print(p)

np.argmax(p)  # 取得最大值的索引
t = np.array([0, 0, 1])  # 监督数据(正确解标签)
print("损失函数的值：")
print(net.loss(x, t))

# 求梯度
# 使用numerical_gradient函数求损失函数关于权重的梯度，W应该是一个参数
# numerical_gradient在内部会执行f(x),与之兼容定义了f(W)
# def f(W):
#     return net.loss(x, t)
f = lambda w: net.loss(x, t)

dW = numerical_gradient(f, net.W)
print("损失函数关于权重的梯度dW：")
print(dW)