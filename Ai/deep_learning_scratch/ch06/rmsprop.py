import numpy as np

class RMSprop:

    """RMSprop"""

    def __init__(self, lr=0.01, decay_rate = 0.99):
        self.lr = lr
        self.decay_rate = decay_rate # 衰减率（decay_rate），控制历史梯度的保留比例；
        self.h = None # 存储「梯度平方的指数移动平均」的字典，初始为None
        
    def update(self, params, grads):
        if self.h is None:
            self.h = {}
            for key, val in params.items():
                self.h[key] = np.zeros_like(val) # 为每个参数创建和它形状相同的全0数组，存储该参数的梯度平方移动平均
            
        for key in params.keys():
            # 1. 更新梯度平方的指数移动平均h：h = ρ*h + (1-ρ)*grad²
            self.h[key] *= self.decay_rate 
            self.h[key] += (1 - self.decay_rate) * grads[key] * grads[key]
            # 2. 更新参数：θ = θ - lr * grad / (√h + 1e-7)
            # 1e-7是极小值，防止h趋近于0时分母为0，导致计算错
            params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key]) + 1e-7)