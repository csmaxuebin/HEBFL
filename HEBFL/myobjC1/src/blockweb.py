from web3 import Web3, HTTPProvider
import json

class ethereumHandler():
    def __init__(self):
        self.web3 = Web3(HTTPProvider("http://localhost:8585"))
        # 检查是否连接成功
        if self.web3.eth.getBlock(0) is None:
            print("Failed to connect!")
        elif self.web3.isConnected():
            # read the abi
            # r"D:\pycharm_code\contract\myContract_sol_baseContract.abi", 'r'
            with open(r"C:\Users\baihuizhong\Desktop\MyobjClient\contract\new.abi", 'r') as fo:
                preabi = fo.read()
                # print(self.preabi)
                myabi = json.loads(preabi)
                self.myContractAddr = Web3.toChecksumAddress('0xc104c964c87d95f36ae3b38f7f0f9a527cf4cf3c')
                self.myContract = self.web3.eth.contract(address=self.myContractAddr, abi=myabi)
                self.web3.eth.defaultAccount = self.web3.eth.accounts[0]
                print("Successfully connected")
            print(self.myContract.all_functions())

    """检查传入地址是否正确，不正确则转换为正确地址并返回"""

    def CheckAddress(self, _address):
        if self.web3.isChecksumAddress(_address):
            return _address
        else:
            return self.web3.toChecksumAddress(_address)

    def Register(self, layer, isVerifier, number):
        tx_hash = self.myContract.functions.Regist(layer,isVerifier,number).transact()
        self.web3.toHex(tx_hash)

    def OverSubmit(self, IPFS, number):
        tx_hash = self.myContract.functions.OverSubmit(IPFS,number).transact()
        return self.web3.toHex(tx_hash)

    def fetchFedAvg(self, number):
        #self.unlockAccount(_addr)
        quanju = self.myContract.functions.fetchFedAvg(number).call()
        print(quanju)

    def ViewLayerIPFS(self):
        q = self.myContract.functions.ViewLayerIPFS().call()
        print(q)

    def ViewFed(self,number):
        p = self.myContract.functions.ViewFed().call()
        print(p)

    def ViewNode(self,number):
        #self.unlockAccount('0x7296a9c8bfed91b5ebc319592d533f8d3cfd8790')
        qq = self.myContract.functions.ViewNode(number).call()
        print(qq)

    def send_transaction(w3):
        transaction = {
            'to': w3.eth.accounts[1],
            'from': w3.eth.accounts[0],
            'value': w3.toWei('3', 'ether'),
            'gas': 4000000,
            'gasPrice': w3.toWei('40', 'gwei'),
            'chainId': 33,
            'nonce': w3.eth.getTransactionCount(w3.eth.accounts[0])
        }

e1 = ethereumHandler()
#e1.Register(1,False,5)
#e1.Register(1,True)
msg = 'sigmoid'.encode('utf-8')
msg_hex = msg.hex()

# generate message's hash to sign

e1.ViewLayerIPFS()
signed_result = e1.eth.account.signHash()
recovered1_addr = e1.eth.account.recoverHash(signed_result.messageHash, signature=signed_result.signature)
print("from Web3:" + recovered1_addr)

recovered2_addr = e1.functions.get_signer(signed_result.messageHash, signed_result.v,
                                                signed_result.r.to_bytes(32, 'big'),
                                                signed_result.s.to_bytes(32, 'big')).call()
print("from local:" + recovered2_addr)

tx_hash = e1.functions.get_signer(signed_result.messageHash, signed_result.v, signed_result.r.to_bytes(32, 'big'),
                                        signed_result.s.to_bytes(32, 'big')).transact(
    {'from': e1.eth.accounts[0], 'gas': 700000})

tx_receipt = e1.eth.waitForTransactionReceipt(tx_hash)
result = e1.events.ReturnSigner().processReceipt(tx_receipt)

print("from remote: " + result[0].args.signer)


#e1.fetchQuanju(3)
# 这里仅调用两个，剩余可以自己测试
#
#     def SendModelSet(self, _model_array,_addr):#给合约地址发送模型参数
#         self.unlockAccount(_addr)
#         tx_hash = self.myContract.functions.setmodelSet(_model_array).transact()
#         return self.web3.toHex(tx_hash)

#     def PrintHelloWorld(self):
#         mystr = self.myContract.functions.say().call()
#         print("调用合约函数printHelloWorld结果:", mystr)