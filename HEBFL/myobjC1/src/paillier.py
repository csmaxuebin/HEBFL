import math
import pickle
from torch import nn
import torch#张量操作
from phe import paillier, EncryptedNumber
#多秘钥加密
f = open('d:\privatekey.txt', 'rb')#密钥1
ListKey=pickle.load(f)
f.close()
# f = open('d:\privatekey.txt', 'rb')#密钥2
# ListKey2=pickle.load(f)//
# f.close()
# f = open('d:\privatekey.txt', 'rb')#密钥3
# ListKey3=pickle.load(f)//
# f.close()
sikey = paillier.PaillierPrivateKey(ListKey[0], ListKey[1], ListKey[2])#私钥1
# sikey2 = paillier.PaillierPrivateKey(ListKey2[0], ListKey2[1], ListKey2[2])//#私钥2
# sikey3 = paillier.PaillierPrivateKey(ListKey3[0], ListKey3[1], ListKey3[2])//#私钥3

def encodemodel(difef):#加密模型
    print("调用了encoding")
    for key in difef:
        # diff[name] = (data)
        print(key)
        c = difef[key].tolist()
        # print(c)
        if type(c) == list:
            bianli1(c)
            #print("输出b")
            #print(b)
        #
        #c = torch.tensor(c)
        print("包裹成功")
        difef[key] = c
        #print("输出c")
    f = open('D:\dic1-3.txt', 'wb')
    pickle.dump(difef, f)
    f.close()
    #print(diff)
#将模型切分为3部分，每部分用一个独立的字典存储
p1 = dict()
p2 = dict()
p3 = dict()
def seperate(df):#切分模型函数
    for key in df:
        if key == 'conv1.weight'  or key == 'conv2.weight'  or key == 'conv3.weight':#conv1.weight，conv1.bias，conv2.weight，conv2.bias，conv3.weight，conv3.bias，fc1.weight，fc1.bias，fc2.weight，fc2.bias，fc3.weight，fc3.bias
            print('进了p1')
            global p1
            p1[key] = df[key]
        else:
            if key == 'conv1.bias' or key == 'conv2.bias' or key == 'conv3.bias':  # conv1.weight，conv1.bias，conv2.weight，conv2.bias，conv3.weight，conv3.bias，fc1.weight，fc1.bias，fc2.weight，fc2.bias，fc3.weight，fc3.bias
                global p2
                print('进了p2')
                p2[key] = df[key]
            else:
                global p3
                print('进了p3')
                p3[key] = df[key]
    print(p1.keys(),p2.keys(),p3.keys())




def bianli1(lists):
    for i in range(len(lists)):
        if type(lists[i]) != list:
            #print("进入了不是list")
            #print(lists[i])
            lists[i] = lists[i]#ListKey[0].encrypt(lists[i])
            #lists[i] =lists[i].ciphertext()
            #lists[i] = sikey.raw_decrypt(lists[i])
            #print(lists[i])
        else:
            print("进入了list")
            bianli1(lists[i])
    #print(lists)

def covermodel(zidian):
    # for name, data in global_model.state_dict().items():
        for key in zidian:
            # if key == name:
                print(key)
                zidian[key] = torch.tensor(zidian[key])

def decoded(onedict):
    for key in onedict:
        if type(onedict[key]) == list:
            bianli2(onedict[key])
        else:
            print("进了else，小心了")
            #onedict[key] = sikey.decrypt(onedict[key])
            onedict[key] = ((onedict[key])/3)
    return onedict

def bianli2(lists):
    for i in range(len(lists)):
        if type(lists[i]) != list:
            #lists[i] = sikey.decrypt(lists[i])
            lists[i] = (lists[i]/3)
        else:
            bianli2(lists[i])

def set_t0_zero(lists):#权重更新频率矩阵置零
    for i in range(len(lists)):
         if type(lists[i]) != list:
            lists[i] = 0
         else:
             set_t0_zero(lists[i])
