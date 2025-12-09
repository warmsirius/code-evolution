import numpy as np


def step_func(x):
    """阶跃激活函数"""
    return  np.array(x > 0, dtype=int)


def sigmoid(x):
    """Sigmoid激活函数"""
    # x为numpy数组也能计算
    return 1 / (1 + np.exp(-x))

def relu(x):
    """ReLU激活函数"""
    return np.maximum(0, x)

# 3层神经网络实现
def init_network():
    """权重和偏执的初始化"""
    # 只把权重记为大小字母W，其余都用小写
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])
    return network


def forward(network, x):
    """将输入信号转换为输出信号的过程"""
    # 后面有backward传播，这里是向前forward传播
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = a3  # 输出层不使用激活函数
    return y


network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y) # [0.31682708 0.69627909]


# SOFTMAX函数
def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

# 改进后的SOFTMAX函数，防止溢出
def softmax_improve(a):
    c = np.max(a)
    exp_a = np.exp(a - c)  # 防止溢出
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y