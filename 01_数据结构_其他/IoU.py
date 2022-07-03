def Inter(bbox1,bbox2):
    """
    边框以左上为原点
    box:[top, left, bottom, right]
    """
    in_w = min(bbox1[2],bbox2[2])-max(bbox1[0],bbox2[0])
    # print(in_w)
    in_h = min(bbox1[3],bbox2[3])-max(bbox1[1],bbox2[1])
    # print(in_h)
    inter = 0 if in_h<0 or in_w<0 else in_h*in_w
    return inter

if __name__ == '__main__':
    bbox1=[1,1,2,3] # 数字有误
    bbox2=[1,1,3,2]
    print(Inter(bbox1,bbox2))

    print(sum(bbox1))
