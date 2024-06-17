import pickle
import time

from tqdm import tqdm #能更好展现程序运行过程的提示进度条

import torch#张量操作
from torch.utils.data import DataLoader#只要是用PyTorch来训练模型基本都会用到该接口，该接口主要用来将自定义的数据读取接口的输出
# 或者PyTorch已有的数据读取接口的输入按照batch size封装成Tensor，后续只需要再包装成Variable即可作为模型的输入
from src.paillier import covermodel, encodemodel, decoded, set_t0_zero
from src.testacc import test_inference
from utils import get_dataset
from options import args_parser#命令行选项、参数和子命令解析器
from models import CNNCifar
from torchvision import models

def train_start():
    args = args_parser()
    if args.gpu:
        torch.cuda.set_device(args.gpu)  # 指定需要使用的GPU
    device = 'cuda' if args.gpu else 'cpu'
    train_dataset,testdata = get_dataset(args)
    #all_range = list(range(len(train_dataset)))
    #data_len = int(len(train_dataset) / 6)
    #train_indices = all_range[0 * data_len: (17 + 3) * data_len]

    trainloader = torch.utils.data.DataLoader(train_dataset, batch_size=args.local_bs,shuffle=True )
    global_model = models.squeezenet1_0(pretrained=True)
    #loaded_stated = torch.load('d:\optimizer2.txt')
    optimizer = torch.optim.SGD(global_model.parameters(), lr=args.lr,
                                momentum=args.momentum)
    #optimizer.load_state_dict(loaded_stated)
    acc = test_inference(global_model, testdata)
    print("初始化全局模型Test Accuracy: {:.2f}%".format(100 * acc))
    #print(optimizer.state_dict())
    #torch.save(global_model.module.state_dict(),'checkpoint.pth.tar')

    #f = open('D:\dic1-3.txt', 'rb')
    #table1 = pickle.load(f)
    #f.close()


    # f = open('d:\oneepoch\layer1\ded_ecode.txt', 'wb')
    # pickle.dump(decoded(table1), f)
    # f.close()
    # exit()
    # exit()

    #decoded(table1)
    #covermodel(table1)
   # global_model.load_state_dict(table1, strict=False)
   # acc = test_inference(global_model, testdata)
    #print("最终全局模型Test Accuracy: {:.2f}%".format(100 * acc))


    # Training
    # Set optimizer and criterion


    # optimizer = torch.optim.SGD(global_model.parameters(), lr=args.lr,
    #                             momentum=args.momentum)  # 随机梯度下降算法
    # 本质上是带有动量项的RMSprop，它利用梯度的一阶矩估计
    # 和二阶矩估计动态调整每一个参数的学习率。它的优势主要在于通过偏置校订后，每一次迭代学习率都有个肯定范围，使得
    # 参数比较平稳。
    global_model.to(device)
    global_model.train()
        #trainloader = DataLoader(train_dataset, batch_size=args.local_bs, shuffle=True)
    criterion = torch.nn.NLLLoss().to(device)  # 交叉熵我们就能够确定预测数据与真是数据之间的相近程度。交叉熵越小
    cacheFrequenMX = dict()#权重频率
    FrequenMX = dict()#权重频率更新矩阵
    for name,data in global_model.state_dict().items():
        if name == 'classifier.1.weight':
            print('找到了')
            global FrequenMX
            FrequenMX = data.tolist()
            set_t0_zero(FrequenMX)
            #print(FrequenMX)
        # ，表示数据越接近真实样本
    for epoch in tqdm(range(args.epochs)):
        batch_loss = []
        for batch_idx, (images, labels) in enumerate(trainloader):  # 遍历的数据对象
            images, labels = images.to(device), labels.to(device)

            optimizer.zero_grad()  # 意思是把梯度置零，也就是把loss关于weight的导数变成0.
            outputs = global_model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            if batch_idx % 100 == 0:
                print('Train Epoch: {} [{}/{} ({:.0f}%)]'.format(
                    epoch + 1, batch_idx * len(images), len(trainloader.dataset),
                    100. * batch_idx / len(trainloader)))
            batch_loss.append(loss.item())
            #time.sleep(1500)
        acc = test_inference(global_model,testdata)
        print("Test Accuracy: {:.2f}%".format(100*acc))
        for name, data in global_model.state_dict().items():
            if name == 'classifier.1.weight':
                print('找到了')
                global FrequenMX#权重频率更新矩阵
                global cacheFrequenMX#权重频率
                cachecacheFrequenMX = data.tolist()
                for i in range(len(cachecacheFrequenMX)):
                    if cachecacheFrequenMX[i] != cacheFrequenMX:#如果上一次该权重与本次权重不同
                        FrequenMX[i] = FrequenMX[i] + 1#权重频率更新加1
                cacheFrequenMX = cachecacheFrequenMX
        #total = sum([param.nelement() for param in global_model.parameters()])
        #print(total)
        # if(epoch == 4):
        #     print("第四个epoch")
        #     ds = dict()
        #     ds = global_model.state_dict()
        #     encodemodel(ds)

    #torch.save(optimizer.state_dict(), 'd:\optimizer2.txt')
    #diff = dict()
    #diff = global_model.state_dict()
    #encodemodel(diff)
