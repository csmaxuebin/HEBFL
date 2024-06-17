# This code is the source code implementation for the paper "HEBFL: Privacy-Preserving Blockchain-Based Federated Learning via Homomorphic Encryption"！
![输入图片说明](https://github.com/csmaxuebin/HEBFL/blob/main/picture/10.png)    
# Abstract
Federated learning is a decentralized machine learning method, which can effectively protect the privacy of participants. There are many security problems in traditional federated learning. For example, the intermediate gradients uploaded by participants may cause serious privacy leakage. Attackers can damage the accuracy of the global model by uploading malicious models. Besides, stragglers may reduce the accuracy of the global model because of their stale model. To solve these problems, this paper proposes a blockchain-based privacy preserving framework HEBFL. We use the model weights encryption mechanism based on partitioning aggregation strategy to protect each participant's privacy, propose the malicious-lazy node detecting and disposing mechanism to identify and dispose of malicious nodes and lazy nodes, and design the optimized asynchronous mechanism to mitigate the negative impact on the global model from stragglers. Finally, we implement a prototype of HEBFL and conduct some experiments on several real datasets. The privacy analysis and the results of the experiments show that our proposed framework can achieve better performance in terms of accuracy, robustness, and privacy.

# Reference

使用导航栏左边的文件夹图标可以访问文件资源管理器。您可以通过单击文件资源管理器中的 **创建文件** 图标来创建新文件。您还可以通过单击 **创建文件夹** 图标来创建文件夹。

# Experimental Environment

```
- Python 3.9.6 
- PyTorch 1.11.0
- Geth 1.8.26
- Remix
- web3 5.29.1
- json 4.5.1
- binascii 1.147
- bitcoin 1.1.42
- sha3 1.0.2
- ipfshttpclient 0.8.0a2
- phe 1.5.0
- gmpy2 2.1.5
- py_ecc 6.0.0
- tqdm 4.64.0
- torchvision 1.12.0
```

## Datasets

```
- X-ray、CIFAR-10、Flowers、FashionMNIST、MNIST
```

## Experimental Setup

### Hyperparameters
In two classes classification task
 - the local epoch E = 2
 - learning rate η = 0.01
 - momentum = 0.8
 - batch size = 16
 
In ten classes classification task
 - local epoch E = 3
 - learning rate η = 0.005
 - momentum = 0.9
 - batch size = 16.
 ### Node settings
 ![输入图片说明](https://github.com/csmaxuebin/HEBFL/blob/main/picture/9.png)
## Python Files
-   **blockweb.py**: 
    - def CheckAddress(self, _address): 检查传入地址是否正确
    -   def Register(self, layer, isVerifier, number): 注册函数
    - def OverSubmit(self, IPFS, number):提交训练结果
    - def fetchFedAvg(self, number):取回聚合结果
    - def ViewFed(self,number):检测验证者是否聚合完毕
-   **ecdsa.py**: 
    -    def pack_signature(v, r, s):打包签名
    - def unpack_signature(r, sv):还原打包签名
    - def pubkey_to_ethaddr(pubkey):将公钥转化为以太坊地址
    - def sign(messageHash, seckey):签名
-   **paillier.py**: 
    -    def encodemodel(difef):加密模型
    - def seperate(df):切分模型函数
    - def bianli1(lists):遍历模型中的每个参数
    - def decoded(onedict):解密模型
    - def set_t0_zero(lists):权重更新频率矩阵置零
## Experimental Results
Fig. 4 shows that the accuracy changes of the global model in this paper and IoT mechanism on the X-ray, Flowers, CIFAR-10, and FashionMNIST dataset under the 2 malicious nodes and 1 lazy node.![输入图片说明](https://github.com/csmaxuebin/HEBFL/blob/main/picture/1.png))
![输入图片说明](https://github.com/csmaxuebin/HEBFL/blob/main/picture/2.png)Table 2 shows the test accuracy of the final model of our paper and the IoT mechanism on the X-ray, Flowers, CIFAR-10, and FashionMNIST dataset under 2 malicious nodes and 1 lazy node. 
![输入图片说明](https://github.com/csmaxuebin/HEBFL/blob/main/picture/3.png)![输入图片说明](https://github.com/csmaxuebin/HEBFL/blob/main/picture/4.png)Fig. 5 shows the accuracy changes of the global model of this paper and IoT mechanism on the X-ray, Flowers, CIFAR-10, and FashionMNIST datasets under 4 malicious nodes. 
![输入图片说明](https://github.com/csmaxuebin/HEBFL/blob/main/picture/6.png)Table 3 shows the test accuracy of the final model of our paper and the IoT mechanism on the X-ray, Flowers, CIFAR-10, and FashionMNIST datasets under 4 malicious nodes.
![输入图片说明](https://github.com/csmaxuebin/HEBFL/blob/main/picture/7.png)Fig. 6 shows the accuracy changes of the global model of this paper and FedAT on the X-ray, Flowers, CIFAR-10, and FashionMNIST datasets.
![输入图片说明](/imgs/2024-06-16/UT2FvEom0l9ZbSrR.png)Table 4 shows the accuracy of the final model of our paper and FedAT in this experiment. 

## Updata log

```
- {24.06.13} Uplode overall framwork code and readme file
```

