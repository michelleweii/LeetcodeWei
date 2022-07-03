import numpy as np

def softmax(y):
    print('ymax',np.max(y, axis=1, keepdims=True))
    y_shift = y - np.max(y, axis=1, keepdims=True)
    print('y_shift',y_shift)
    y_exp = np.exp(y_shift)
    print('y_exp',y_exp)
    y_exp_sum = np.sum(y_exp, axis=1, keepdims=True)
    print('y_exp_sum',y_exp_sum)
    return y_exp / y_exp_sum

if __name__ == "__main__":
    # y = np.array([1, 0, 0, 1]).reshape(-1, 1)
    # y_hat = np.array([1, 0.4, 0.5, 0.1]).reshape(-1, 1)
    # print(cross_entropy(y, y_hat))
    y = np.array([[1,2,3,4],[1,3,4,5],[3,4,5,6]])
    print('y',y)
    print('softmax',softmax(y))