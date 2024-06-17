import operator
import pickle
from fedavg import fedavg

f = open('D:\iotFlower\layer2\dicFed2-10.txt', 'rb')
#client.get("QmZdmLc9xgzDSCDx2QfoRQaEirSW6x95YVbj4Agy7hfEWA")#把别人的训练结果接回来
#f=open('QmZdmLc9xgzDSCDx2QfoRQaEirSW6x95YVbj4Agy7hfEWA', 'rb')
First=pickle.load(f)
f.close()

f = open('D:\iotFlower\layer2\dic4-12.txt', 'rb')
#client.get("QmZdmLc9xgzDSCDx2QfoRQaEirSW6x95YVbj4Agy7hfEWA")#把别人的训练结果接回来
#f=open('QmZdmLc9xgzDSCDx2QfoRQaEirSW6x95YVbj4Agy7hfEWA', 'rb')
Second=pickle.load(f)
f.close()
#
#
            # f = open('D:\SecondExp\layer1\dic3-2.txt', 'rb')
            # #client.get("QmZdmLc9xgzDSCDx2QfoRQaEirSW6x95YVbj4Agy7hfEWA")#把别人的训练结果接回来
f=open('D:\iotFlower\layer2\dic4-12.txt', 'rb')
Third=pickle.load(f)
f.close()
# f = open('D:\SecondExp\layer1\dicFedmid.txt', 'wb')
# pickle.dump(fedavg(First,Second), f)
# f.close()
fedavg(First,Second)
fedavg(Third,Second)
f = open('D:\iotFlower\layer2\dicFed2-11.txt', 'wb')
pickle.dump(Second, f)
f.close()
# f = open('D:\SecondExp\layer1\dicFedmid.txt', 'rb')
# #client.get("QmZdmLc9xgzDSCDx2QfoRQaEirSW6x95YVbj4Agy7hfEWA")#把别人的训练结果接回来
# #f=open('QmZdmLc9xgzDSCDx2QfoRQaEirSW6x95YVbj4Agy7hfEWA', 'rb')
# mid=pickle.load(f)
# f.close()
# f = open('D:\SecondExp\layer1\dicFed1-1.txt', 'rb')
# #client.get("QmZdmLc9xgzDSCDx2QfoRQaEirSW6x95YVbj4Agy7hfEWA")#把别人的训练结果接回来
# #f=open('QmZdmLc9xgzDSCDx2QfoRQaEirSW6x95YVbj4Agy7hfEWA', 'rb')
# fin=pickle.load(f)
# f.close()
# print(operator.eq(mid,fin))
# decoded(Second)
# covermodel(Second)
#
# acc= test_inference(model.load_state_dict(Second),testdataset)#测算它的精度是否是中毒精度
# print("聚合后的全局模型Test Accuracy: {:.2f}%".format(100*acc))
#QuanJu = decoded(QuanJu)
#acc= test_inference(covermodel(decoded(First),model), testdataset)#测算它的精度是否是中毒精度
#print("Test Accuracy: {:.2f}%".format(100*acc))
# covermodel(QuanJu,model)
#quanjudict = client.get_json("QmZdmLc9xgzDSCDx2QfoRQaEirSW6x95YVbj4Agy7hfEWA")#把上一轮聚合的的全局模型接回来
#newdict = decoded(newdict)#解码训练结点的模型，得到的是非tensor的字典
#quanjudict = decoded(quanjudict)#解码上次的全局模型，得到的是非tensor的字典


# if test_same(newdict, quanjudict):#operator看看是否一样，一样则返回true
#     #上传一致信息到区块链
#     print("一致")
#print(decoded(fedavg(newdict,quanjudict)))

#nosecretmodel = covermodel(), model)#把字典cover进去



