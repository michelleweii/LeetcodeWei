def transfer(num): # num：str
    # 分成3个一组
    result1 = []
    rev_num = num[::-1]
    n = len(rev_num)
    # 从低位开始，每3位分成一组
    for i in range(0,n,3):
        tmp = rev_num[i:i+3]
        # print(tmp)
        tmp = "".join(list(reversed(tmp)))
        # print(tmp)
        if len(tmp)!=3:
            tmp = tmp.rjust(3,'0')
        result1.insert(0,tmp)
    result1 = "".join(result1)
    # print("results1:{}".format(result1))

    result2 = []
    # 每一组三位数，转成十位2进制，不足10位则0补，
    # 拼接，去掉前导0
    for i in range(0,len(result1),3):
        tmp = result1[i:i+3]
        # print(tmp)
        bintmp = bin(int("".join(tmp)))
        bintmp = bintmp.replace("0b","")
        # print(bintmp)
        # print(int(bintmp,2))
        bintmpfill = bintmp.zfill(10)
        result2+=bintmpfill
    result2 = "".join(result2)
    result2= result2.lstrip('0')
    # print("len2:{}".format(len(result2)))
    # print("result2:{}".format(result2))
    # 对二进制，从低位开始，每5位分成一组
    result2 = result2[::-1]
    result3 = []
    for i in range(0,len(result2),5):
        tmp = result2[i:i+5]
        tmp = "".join(list(reversed(tmp)))
        if len(tmp)!=5:
            tmp = tmp.rjust(5,'0')
        result3.insert(0,tmp)
    result3 = "".join(result3)
    # print("len3:{}".format(len(result3)))
    # print("result3:{}".format(result3))

    dictNUM = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',
    10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:"G",17:"H",18:'I',
               19:'J',20:'K',21:'L',22:'M',23:'N',24:'O',
               25:'P',26:'Q',27:'R',28:'S',29:'T',30:'U',31:'V'}
    result = ""
    for i in range(0,len(result3),5):
        tmp = result3[i:i+5]
        x = "".join(tmp)
        # print(int(x,2))
        result += dictNUM[int(x,2)]
    print(result)

if __name__ == '__main__':
    T = int(input())
    while T:
        num = input()
        transfer(num)
        T -= 1
    # num = "1000"
    # # 55 IN
    # # 5555 5hb
    # transfer(num)