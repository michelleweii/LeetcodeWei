# 20230111
# auc: 遍历正负样本对
# https://blog.csdn.net/weixin_31866177/article/details/88394966
"""
1、正的概率大于负的，auc加1
2、正的概率等于负的，auc加0.5
3、正的概率小于负的，auc加0

计算原理：

遍历正负样本对
正样本的概率大于负样本，auc += 1
正样本的概率等于负样本，auc += 0.5
正样本的概率小于负样本，auc += 0
遍历完毕，auc = auc / 正负样本对数
举个例子：

label = [1, 0, 0,]
pre = [0.9, 0.8, 0.3]

第一个是正样本，后面两个是负样本。

正负样本对有：（label[0],label[1]），（label[0],label[2]）。
因为pre[0]>pre[1]，因为正样本的概率大于负样本，所以auc += 1，
因为pre[0]>pre[2]，因为正样本的概率大于负样本，所以auc += 1，
总对数为2:
所以auc = (1 + 1)/2 = 1。
————————————————
版权声明：本文为CSDN博主「littlemichelle」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_31866177/article/details/88394966
"""

def AUC(label, pre):
    pos = []
    neg = []
    auc = 0
    for index, l in enumerate(label):
        if l == 0:
            neg.append(index)
        else:
            pos.append(index)
    for i in pos:
        for j in neg:
            # 遍历预测分数，所以是pre
            if pre[i] > pre[j]:
                auc += 1
            elif pre[i] == pre[j]:
                auc += 0.5
    return auc * 1.0 / (len(pos)*len(neg))

if __name__ == '__main__':
    label = [1, 0, 0, 0, 1, 0, 1, 0]
    pre = [0.9, 0.8, 0.3, 0.1, 0.4, 0.9, 0.66, 0.7]
    print(AUC(label, pre))

    from sklearn import metrics
    auc = metrics.roc_auc_score(label, pre)
    print('sklearn' ,auc)
    # 0.5666666666666667
    # sklearn 0.5666666666666667