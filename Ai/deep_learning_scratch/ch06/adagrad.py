import numpy as np


class AdaGrad:
    def __init__(self, lr=0.01, epsilon=1e-7):
        self.lr = lr
        self.epsilon = epsilon # 防止除以零
        self.h = None  # 用于保存梯度的平方和，初始化时，h中什么都不保存，当第一次调用update时，h以字典保存与参数结构相同的数据

    def update(self, params, grads):
        if self.h is None:
            self.h = {}
            for key, val in params.items():
                self.h[key] = np.zeros_like(val)  # 初始化梯度平方和为0，结构相同

        for key in params.keys():
            self.h[key] += grads[key] * grads[key]  # 累积梯度的平方
            adjusted_lr = self.lr / (np.sqrt(self.h[key]) + self.epsilon)  # 计算调整后的学习率
            params[key] -= adjusted_lr * grads[key]  # 更新参数