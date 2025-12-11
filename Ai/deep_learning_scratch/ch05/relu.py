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
