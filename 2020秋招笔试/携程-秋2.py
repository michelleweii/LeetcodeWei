def auc_cal(y,pred):
    n = len(y)
    posNum,negNum = 0,0
    total_case = list(zip(pred,y))
    # print(total_case)
    sortlist = [valj for vali,valj in sorted(total_case,key=lambda x:x[0])]
    # print(sortlist) # [0, 1, 0, 0, 1, 0, 1, 1, 0, 1]
    # print(type(sortlist[1]))
    # print("n",n)
    # for i in range(n):
    #     print(i)
    #     if sortlist[i]==1:
    #         print("yes")
    postive_len = [i+1 for i in range(n) if sortlist[i]==1]
    # print(postive_len)
    for i in range(n):
        if(y[i]==1):posNum+=1
        else:negNum+=1
    auc = (sum(postive_len) - (posNum*(posNum+1))*0.5)/(posNum*negNum)
    return auc

if __name__ == '__main__':
    n = int(input())
    y,pred = [],[]
    for i in range(n):
        tmp = input().strip().split(' ')
        n = int(tmp[0].strip())
        m = float(tmp[1].strip())
        y.append(n)
        pred.append(m)


    # n = 10
    # y = [1,0,1,1,0,1,0,0,1,0]
    # pred =[0.9,0.7,0.6,0.55,0.52,0.4,0.38,0.35,0.31,0.1]

    res = auc_cal(y,pred)
    print(res)
