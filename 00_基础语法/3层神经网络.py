from tensorflow as tf

from tensorflow.keras import layers
model=layers.Sequential([
    layers.Dense(128, activation=tf.nn.relu) , # 创建输入层(隐藏层 1）
    layers.Dense(64, activation=tf.nn.relu) , # 创建隐藏层 2
    layers.Dense(2, activation=None) , # 创建输出层
])

out = model(x) # 前向计算得到输出

# 计算损失，损失函数
# 反向传播，优化器优化

