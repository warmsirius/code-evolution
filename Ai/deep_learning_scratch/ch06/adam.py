import numpy as np


class Adam:
    """Adam (http://arxiv.org/abs/1412.6980v8)"""

    def __init__(self, lr=0.001, beta1=0.9, beta2=0.999):
        self.lr = lr # 基础学习率，Adam 对学习率不敏感，0.001 是业界通用默认值
        self.beta1 = beta1 # 一阶矩(动量)衰减率：保留 90% 的历史梯度方向（动量），让更新更 “顺滑”，减少震荡
        self.beta2 = beta2 # 二阶矩(梯度平方)估计的指数衰减率，控制历史梯度平方的保留比例；
        self.iter = 0 # 记录参数更新的次数，用于后续 “偏差修正”
        self.m = None # 存储「一阶矩」（梯度的指数移动平均，对应动量）
        self.v = None # 存储「二阶矩」（梯度平方的指数移动平均，对应RMSprop）
    
    def update(self, params, grads):
        if self.m is None:
            self.m, self.v = {}, {}
            for key, val in params.items():
                self.m[key] = np.zeros_like(val)
                self.v[key] = np.zeros_like(val)
        
        self.iter += 1 # 每次更新，迭代次数+1（从1开始）
        lr_t = self.lr * np.sqrt(1.0 - self.beta2**self.iter) / (1.0 - self.beta1**self.iter)

        for key in params.keys():
            # 更新一阶矩估计m和二阶矩估计v
            self.m[key] += (1 - self.beta1) * (grads[key] - self.m[key])
            self.v[key] += (1 - self.beta2) * (grads[key]**2 - self.v[key])
            # 使用修正后的m和v来更新参数
            params[key] -= lr_t * self.m[key] / (np.sqrt(self.v[key]) + 1e-7)