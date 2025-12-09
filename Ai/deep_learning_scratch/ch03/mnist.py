import sys, os

# sys.path.append(os.pardir) # 为了导入父目录中的文件而进行的设定
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dataset.mnist import load_mnist
import numpy as np
from PIL import Image


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img)) # 将保存为numpy数组的图像数据转换为PIL用的数据对象
    pil_img.show()


# 第一次调用会花费几分钟 ……
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)
# flatten=True,读入按照一维读入

# 输出各个数据的形状
print(x_train.shape) # (60000, 784)
print(t_train.shape) # (60000,)
print(x_test.shape) # (10000, 784)
print(t_test.shape) # (10000,)

img = x_train[0]
label = t_train[0]
print(label) # 5

print(img.shape) # (784,)
img = img.reshape(28, 28) # 显示时,需要把图像的形状变成原来的尺寸,28x28像素
print(img.shape) # (28, 28)
img_show(img)