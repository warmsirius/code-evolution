from common.functions import softmax, cross_entropy_error


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